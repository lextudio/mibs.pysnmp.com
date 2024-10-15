# SNMP MIB module (F5-3DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/F5-3DNS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:33 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F5_ObjectIdentity = ObjectIdentity
f5 = _F5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375)
)
_F5systems_ObjectIdentity = ObjectIdentity
f5systems = _F5systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1)
)
_F53dns_ObjectIdentity = ObjectIdentity
f53dns = _F53dns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2)
)
_F53dnsMIB_ObjectIdentity = ObjectIdentity
f53dnsMIB = _F53dnsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1)
)
_F53dnsMIBObjects_ObjectIdentity = ObjectIdentity
f53dnsMIBObjects = _F53dnsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1)
)
_Globals_ObjectIdentity = ObjectIdentity
globals = _Globals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1)
)


class _GlobalCheckStaticDepends_Type(Integer32):
    """Custom type globalCheckStaticDepends based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_GlobalCheckStaticDepends_Type.__name__ = "Integer32"
_GlobalCheckStaticDepends_Object = MibScalar
globalCheckStaticDepends = _GlobalCheckStaticDepends_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 1),
    _GlobalCheckStaticDepends_Type()
)
globalCheckStaticDepends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalCheckStaticDepends.setStatus("mandatory")


class _GlobalDefaultAlternate_Type(Integer32):
    """Custom type globalDefaultAlternate based on Integer32"""
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
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("connections", 11),
          ("cpu", 16),
          ("diskSpace", 17),
          ("globalAvailability", 9),
          ("hitRatio", 18),
          ("hops", 13),
          ("mem", 15),
          ("none", 2),
          ("packetRate", 14),
          ("qos", 19),
          ("random", 6),
          ("ratio", 5),
          ("returnDNS", 1),
          ("returnVS", 3),
          ("roundRobin", 4),
          ("roundTripTime", 12),
          ("servers", 10),
          ("staticPersist", 8),
          ("topology", 7))
    )


_GlobalDefaultAlternate_Type.__name__ = "Integer32"
_GlobalDefaultAlternate_Object = MibScalar
globalDefaultAlternate = _GlobalDefaultAlternate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 2),
    _GlobalDefaultAlternate_Type()
)
globalDefaultAlternate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalDefaultAlternate.setStatus("mandatory")


class _GlobalTimerGetLBRouterData_Type(Integer32):
    """Custom type globalTimerGetLBRouterData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GlobalTimerGetLBRouterData_Type.__name__ = "Integer32"
_GlobalTimerGetLBRouterData_Object = MibScalar
globalTimerGetLBRouterData = _GlobalTimerGetLBRouterData_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 3),
    _GlobalTimerGetLBRouterData_Type()
)
globalTimerGetLBRouterData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalTimerGetLBRouterData.setStatus("mandatory")


class _GlobalTimerGetVServData_Type(Integer32):
    """Custom type globalTimerGetVServData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GlobalTimerGetVServData_Type.__name__ = "Integer32"
_GlobalTimerGetVServData_Object = MibScalar
globalTimerGetVServData = _GlobalTimerGetVServData_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 4),
    _GlobalTimerGetVServData_Type()
)
globalTimerGetVServData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalTimerGetVServData.setStatus("mandatory")


class _GlobalTimerGetPathData_Type(Integer32):
    """Custom type globalTimerGetPathData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GlobalTimerGetPathData_Type.__name__ = "Integer32"
_GlobalTimerGetPathData_Object = MibScalar
globalTimerGetPathData = _GlobalTimerGetPathData_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 5),
    _GlobalTimerGetPathData_Type()
)
globalTimerGetPathData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalTimerGetPathData.setStatus("mandatory")


class _GlobalLBRouterTTL_Type(Integer32):
    """Custom type globalLBRouterTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_GlobalLBRouterTTL_Type.__name__ = "Integer32"
_GlobalLBRouterTTL_Object = MibScalar
globalLBRouterTTL = _GlobalLBRouterTTL_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 6),
    _GlobalLBRouterTTL_Type()
)
globalLBRouterTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalLBRouterTTL.setStatus("mandatory")


class _GlobalVSTTL_Type(Integer32):
    """Custom type globalVSTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_GlobalVSTTL_Type.__name__ = "Integer32"
_GlobalVSTTL_Object = MibScalar
globalVSTTL = _GlobalVSTTL_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 7),
    _GlobalVSTTL_Type()
)
globalVSTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalVSTTL.setStatus("mandatory")


class _GlobalPathTTL_Type(Integer32):
    """Custom type globalPathTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_GlobalPathTTL_Type.__name__ = "Integer32"
_GlobalPathTTL_Object = MibScalar
globalPathTTL = _GlobalPathTTL_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 8),
    _GlobalPathTTL_Type()
)
globalPathTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalPathTTL.setStatus("mandatory")


class _GlobalRTTTimeout_Type(Integer32):
    """Custom type globalRTTTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_GlobalRTTTimeout_Type.__name__ = "Integer32"
_GlobalRTTTimeout_Object = MibScalar
globalRTTTimeout = _GlobalRTTTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 9),
    _GlobalRTTTimeout_Type()
)
globalRTTTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRTTTimeout.setStatus("mandatory")


class _GlobalRTTSampleCount_Type(Integer32):
    """Custom type globalRTTSampleCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_GlobalRTTSampleCount_Type.__name__ = "Integer32"
_GlobalRTTSampleCount_Object = MibScalar
globalRTTSampleCount = _GlobalRTTSampleCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 10),
    _GlobalRTTSampleCount_Type()
)
globalRTTSampleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRTTSampleCount.setStatus("mandatory")


class _GlobalRTTPacketLength_Type(Integer32):
    """Custom type globalRTTPacketLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 500),
    )


_GlobalRTTPacketLength_Type.__name__ = "Integer32"
_GlobalRTTPacketLength_Object = MibScalar
globalRTTPacketLength = _GlobalRTTPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 11),
    _GlobalRTTPacketLength_Type()
)
globalRTTPacketLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRTTPacketLength.setStatus("mandatory")


class _GlobalRTTProbeProtocol_Type(Integer32):
    """Custom type globalRTTProbeProtocol based on Integer32"""
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
        *(("dnsRetrieveBindVers", 5),
          ("dnsnslookupDot", 4),
          ("icmp", 1),
          ("none", 7),
          ("numberItems", 6),
          ("tcp", 2),
          ("udp", 3))
    )


_GlobalRTTProbeProtocol_Type.__name__ = "Integer32"
_GlobalRTTProbeProtocol_Object = MibScalar
globalRTTProbeProtocol = _GlobalRTTProbeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 12),
    _GlobalRTTProbeProtocol_Type()
)
globalRTTProbeProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRTTProbeProtocol.setStatus("mandatory")


class _GlobalEncryption_Type(Integer32):
    """Custom type globalEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_GlobalEncryption_Type.__name__ = "Integer32"
_GlobalEncryption_Object = MibScalar
globalEncryption = _GlobalEncryption_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 13),
    _GlobalEncryption_Type()
)
globalEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalEncryption.setStatus("mandatory")


class _GlobalEncryptionKeyFile_Type(OctetString):
    """Custom type globalEncryptionKeyFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GlobalEncryptionKeyFile_Type.__name__ = "OctetString"
_GlobalEncryptionKeyFile_Object = MibScalar
globalEncryptionKeyFile = _GlobalEncryptionKeyFile_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 14),
    _GlobalEncryptionKeyFile_Type()
)
globalEncryptionKeyFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalEncryptionKeyFile.setStatus("mandatory")


class _GlobalPathHiWater_Type(Integer32):
    """Custom type globalPathHiWater based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_GlobalPathHiWater_Type.__name__ = "Integer32"
_GlobalPathHiWater_Object = MibScalar
globalPathHiWater = _GlobalPathHiWater_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 15),
    _GlobalPathHiWater_Type()
)
globalPathHiWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalPathHiWater.setStatus("mandatory")


class _GlobalPathLoWater_Type(Integer32):
    """Custom type globalPathLoWater based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_GlobalPathLoWater_Type.__name__ = "Integer32"
_GlobalPathLoWater_Object = MibScalar
globalPathLoWater = _GlobalPathLoWater_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 16),
    _GlobalPathLoWater_Type()
)
globalPathLoWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalPathLoWater.setStatus("mandatory")


class _GlobalPathDuration_Type(Integer32):
    """Custom type globalPathDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3600, 2419200),
    )


_GlobalPathDuration_Type.__name__ = "Integer32"
_GlobalPathDuration_Object = MibScalar
globalPathDuration = _GlobalPathDuration_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 17),
    _GlobalPathDuration_Type()
)
globalPathDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalPathDuration.setStatus("mandatory")


class _GlobalPathReapAlg_Type(Integer32):
    """Custom type globalPathReapAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fewestHits", 2),
          ("lru", 1),
          ("numberItems", 3))
    )


_GlobalPathReapAlg_Type.__name__ = "Integer32"
_GlobalPathReapAlg_Object = MibScalar
globalPathReapAlg = _GlobalPathReapAlg_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 18),
    _GlobalPathReapAlg_Type()
)
globalPathReapAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalPathReapAlg.setStatus("mandatory")


class _GlobalTimerKeepAlive_Type(Integer32):
    """Custom type globalTimerKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GlobalTimerKeepAlive_Type.__name__ = "Integer32"
_GlobalTimerKeepAlive_Object = MibScalar
globalTimerKeepAlive = _GlobalTimerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 19),
    _GlobalTimerKeepAlive_Type()
)
globalTimerKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalTimerKeepAlive.setStatus("mandatory")


class _GlobalRxBufSize_Type(Integer32):
    """Custom type globalRxBufSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8192, 4294967295),
    )


_GlobalRxBufSize_Type.__name__ = "Integer32"
_GlobalRxBufSize_Object = MibScalar
globalRxBufSize = _GlobalRxBufSize_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 20),
    _GlobalRxBufSize_Type()
)
globalRxBufSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRxBufSize.setStatus("mandatory")


class _GlobalTxBufSize_Type(Integer32):
    """Custom type globalTxBufSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8192, 4294967295),
    )


_GlobalTxBufSize_Type.__name__ = "Integer32"
_GlobalTxBufSize_Object = MibScalar
globalTxBufSize = _GlobalTxBufSize_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 21),
    _GlobalTxBufSize_Type()
)
globalTxBufSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalTxBufSize.setStatus("mandatory")


class _GlobalQosCoeffRTT_Type(Integer32):
    """Custom type globalQosCoeffRTT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GlobalQosCoeffRTT_Type.__name__ = "Integer32"
_GlobalQosCoeffRTT_Object = MibScalar
globalQosCoeffRTT = _GlobalQosCoeffRTT_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 22),
    _GlobalQosCoeffRTT_Type()
)
globalQosCoeffRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalQosCoeffRTT.setStatus("mandatory")


class _GlobalQosCoeffCompletionRate_Type(Integer32):
    """Custom type globalQosCoeffCompletionRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GlobalQosCoeffCompletionRate_Type.__name__ = "Integer32"
_GlobalQosCoeffCompletionRate_Object = MibScalar
globalQosCoeffCompletionRate = _GlobalQosCoeffCompletionRate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 23),
    _GlobalQosCoeffCompletionRate_Type()
)
globalQosCoeffCompletionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalQosCoeffCompletionRate.setStatus("mandatory")


class _GlobalQosCoeffHops_Type(Integer32):
    """Custom type globalQosCoeffHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GlobalQosCoeffHops_Type.__name__ = "Integer32"
_GlobalQosCoeffHops_Object = MibScalar
globalQosCoeffHops = _GlobalQosCoeffHops_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 24),
    _GlobalQosCoeffHops_Type()
)
globalQosCoeffHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalQosCoeffHops.setStatus("mandatory")


class _GlobalQosCoeffPacketRate_Type(Integer32):
    """Custom type globalQosCoeffPacketRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GlobalQosCoeffPacketRate_Type.__name__ = "Integer32"
_GlobalQosCoeffPacketRate_Object = MibScalar
globalQosCoeffPacketRate = _GlobalQosCoeffPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 25),
    _GlobalQosCoeffPacketRate_Type()
)
globalQosCoeffPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalQosCoeffPacketRate.setStatus("mandatory")


class _GlobalPathsNoClobber_Type(Integer32):
    """Custom type globalPathsNoClobber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_GlobalPathsNoClobber_Type.__name__ = "Integer32"
_GlobalPathsNoClobber_Object = MibScalar
globalPathsNoClobber = _GlobalPathsNoClobber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 26),
    _GlobalPathsNoClobber_Type()
)
globalPathsNoClobber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalPathsNoClobber.setStatus("mandatory")


class _GlobalPathsNeverDie_Type(Integer32):
    """Custom type globalPathsNeverDie based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_GlobalPathsNeverDie_Type.__name__ = "Integer32"
_GlobalPathsNeverDie_Object = MibScalar
globalPathsNeverDie = _GlobalPathsNeverDie_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 27),
    _GlobalPathsNeverDie_Type()
)
globalPathsNeverDie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalPathsNeverDie.setStatus("mandatory")


class _GlobalRegulateInit_Type(Integer32):
    """Custom type globalRegulateInit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GlobalRegulateInit_Type.__name__ = "Integer32"
_GlobalRegulateInit_Object = MibScalar
globalRegulateInit = _GlobalRegulateInit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 28),
    _GlobalRegulateInit_Type()
)
globalRegulateInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRegulateInit.setStatus("mandatory")


class _GlobalRegulatePaths_Type(Integer32):
    """Custom type globalRegulatePaths based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GlobalRegulatePaths_Type.__name__ = "Integer32"
_GlobalRegulatePaths_Object = MibScalar
globalRegulatePaths = _GlobalRegulatePaths_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 29),
    _GlobalRegulatePaths_Type()
)
globalRegulatePaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRegulatePaths.setStatus("mandatory")
_GlobalProberAddr_Type = IpAddress
_GlobalProberAddr_Object = MibScalar
globalProberAddr = _GlobalProberAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 30),
    _GlobalProberAddr_Type()
)
globalProberAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalProberAddr.setStatus("mandatory")


class _GlobalCheckDynamicDepends_Type(Integer32):
    """Custom type globalCheckDynamicDepends based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_GlobalCheckDynamicDepends_Type.__name__ = "Integer32"
_GlobalCheckDynamicDepends_Object = MibScalar
globalCheckDynamicDepends = _GlobalCheckDynamicDepends_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 31),
    _GlobalCheckDynamicDepends_Type()
)
globalCheckDynamicDepends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalCheckDynamicDepends.setStatus("mandatory")


class _GlobalDefaultFallback_Type(Integer32):
    """Custom type globalDefaultFallback based on Integer32"""
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
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("connections", 11),
          ("cpu", 16),
          ("diskSpace", 17),
          ("globalAvailability", 9),
          ("hitRatio", 18),
          ("hops", 13),
          ("mem", 15),
          ("none", 2),
          ("packetRate", 14),
          ("qos", 19),
          ("random", 6),
          ("ratio", 5),
          ("returnDNS", 1),
          ("returnVS", 3),
          ("roundRobin", 4),
          ("roundTripTime", 12),
          ("servers", 10),
          ("staticPersist", 8),
          ("topology", 7))
    )


_GlobalDefaultFallback_Type.__name__ = "Integer32"
_GlobalDefaultFallback_Object = MibScalar
globalDefaultFallback = _GlobalDefaultFallback_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 32),
    _GlobalDefaultFallback_Type()
)
globalDefaultFallback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalDefaultFallback.setStatus("mandatory")


class _GlobalDefaultTTL_Type(Integer32):
    """Custom type globalDefaultTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GlobalDefaultTTL_Type.__name__ = "Integer32"
_GlobalDefaultTTL_Object = MibScalar
globalDefaultTTL = _GlobalDefaultTTL_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 33),
    _GlobalDefaultTTL_Type()
)
globalDefaultTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalDefaultTTL.setStatus("mandatory")


class _GlobalPersistLDns_Type(Integer32):
    """Custom type globalPersistLDns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_GlobalPersistLDns_Type.__name__ = "Integer32"
_GlobalPersistLDns_Object = MibScalar
globalPersistLDns = _GlobalPersistLDns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 34),
    _GlobalPersistLDns_Type()
)
globalPersistLDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalPersistLDns.setStatus("mandatory")


class _GlobalFbRespectAcl_Type(Integer32):
    """Custom type globalFbRespectAcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_GlobalFbRespectAcl_Type.__name__ = "Integer32"
_GlobalFbRespectAcl_Object = MibScalar
globalFbRespectAcl = _GlobalFbRespectAcl_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 35),
    _GlobalFbRespectAcl_Type()
)
globalFbRespectAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFbRespectAcl.setStatus("mandatory")


class _GlobalFbRespectDepends_Type(Integer32):
    """Custom type globalFbRespectDepends based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_GlobalFbRespectDepends_Type.__name__ = "Integer32"
_GlobalFbRespectDepends_Object = MibScalar
globalFbRespectDepends = _GlobalFbRespectDepends_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 36),
    _GlobalFbRespectDepends_Type()
)
globalFbRespectDepends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalFbRespectDepends.setStatus("mandatory")


class _GlobalHostTTL_Type(Integer32):
    """Custom type globalHostTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_GlobalHostTTL_Type.__name__ = "Integer32"
_GlobalHostTTL_Object = MibScalar
globalHostTTL = _GlobalHostTTL_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 37),
    _GlobalHostTTL_Type()
)
globalHostTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalHostTTL.setStatus("mandatory")


class _GlobalTimerGetHostData_Type(Integer32):
    """Custom type globalTimerGetHostData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GlobalTimerGetHostData_Type.__name__ = "Integer32"
_GlobalTimerGetHostData_Object = MibScalar
globalTimerGetHostData = _GlobalTimerGetHostData_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 38),
    _GlobalTimerGetHostData_Type()
)
globalTimerGetHostData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalTimerGetHostData.setStatus("mandatory")


class _GlobalRTTRetireZero_Type(Integer32):
    """Custom type globalRTTRetireZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_GlobalRTTRetireZero_Type.__name__ = "Integer32"
_GlobalRTTRetireZero_Object = MibScalar
globalRTTRetireZero = _GlobalRTTRetireZero_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 39),
    _GlobalRTTRetireZero_Type()
)
globalRTTRetireZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRTTRetireZero.setStatus("mandatory")


class _GlobalRTTPortDiscovery_Type(Integer32):
    """Custom type globalRTTPortDiscovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_GlobalRTTPortDiscovery_Type.__name__ = "Integer32"
_GlobalRTTPortDiscovery_Object = MibScalar
globalRTTPortDiscovery = _GlobalRTTPortDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 40),
    _GlobalRTTPortDiscovery_Type()
)
globalRTTPortDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRTTPortDiscovery.setStatus("mandatory")


class _GlobalRTTDiscoveryMethod_Type(Integer32):
    """Custom type globalRTTDiscoveryMethod based on Integer32"""
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
        *(("all", 4),
          ("full", 3),
          ("short", 1),
          ("wks", 2))
    )


_GlobalRTTDiscoveryMethod_Type.__name__ = "Integer32"
_GlobalRTTDiscoveryMethod_Object = MibScalar
globalRTTDiscoveryMethod = _GlobalRTTDiscoveryMethod_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 41),
    _GlobalRTTDiscoveryMethod_Type()
)
globalRTTDiscoveryMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRTTDiscoveryMethod.setStatus("mandatory")


class _GlobalRTTProbeDynamic_Type(Integer32):
    """Custom type globalRTTProbeDynamic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_GlobalRTTProbeDynamic_Type.__name__ = "Integer32"
_GlobalRTTProbeDynamic_Object = MibScalar
globalRTTProbeDynamic = _GlobalRTTProbeDynamic_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 42),
    _GlobalRTTProbeDynamic_Type()
)
globalRTTProbeDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRTTProbeDynamic.setStatus("mandatory")


class _GlobalResolverRXBufSize_Type(Integer32):
    """Custom type globalResolverRXBufSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8192, 131072),
    )


_GlobalResolverRXBufSize_Type.__name__ = "Integer32"
_GlobalResolverRXBufSize_Object = MibScalar
globalResolverRXBufSize = _GlobalResolverRXBufSize_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 43),
    _GlobalResolverRXBufSize_Type()
)
globalResolverRXBufSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalResolverRXBufSize.setStatus("mandatory")


class _GlobalResolverTXBufSize_Type(Integer32):
    """Custom type globalResolverTXBufSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8192, 32768),
    )


_GlobalResolverTXBufSize_Type.__name__ = "Integer32"
_GlobalResolverTXBufSize_Object = MibScalar
globalResolverTXBufSize = _GlobalResolverTXBufSize_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 44),
    _GlobalResolverTXBufSize_Type()
)
globalResolverTXBufSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalResolverTXBufSize.setStatus("mandatory")


class _GlobalCoeffLastAccess_Type(Integer32):
    """Custom type globalCoeffLastAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 424967295),
    )


_GlobalCoeffLastAccess_Type.__name__ = "Integer32"
_GlobalCoeffLastAccess_Object = MibScalar
globalCoeffLastAccess = _GlobalCoeffLastAccess_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 45),
    _GlobalCoeffLastAccess_Type()
)
globalCoeffLastAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalCoeffLastAccess.setStatus("mandatory")


class _GlobalCoeffFreshRemain_Type(Integer32):
    """Custom type globalCoeffFreshRemain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 424967295),
    )


_GlobalCoeffFreshRemain_Type.__name__ = "Integer32"
_GlobalCoeffFreshRemain_Object = MibScalar
globalCoeffFreshRemain = _GlobalCoeffFreshRemain_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 46),
    _GlobalCoeffFreshRemain_Type()
)
globalCoeffFreshRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalCoeffFreshRemain.setStatus("mandatory")


class _GlobalCoeffAccessRefresh_Type(Integer32):
    """Custom type globalCoeffAccessRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 424967295),
    )


_GlobalCoeffAccessRefresh_Type.__name__ = "Integer32"
_GlobalCoeffAccessRefresh_Object = MibScalar
globalCoeffAccessRefresh = _GlobalCoeffAccessRefresh_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 47),
    _GlobalCoeffAccessRefresh_Type()
)
globalCoeffAccessRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalCoeffAccessRefresh.setStatus("mandatory")


class _GlobalCoeffAccessTotal_Type(Integer32):
    """Custom type globalCoeffAccessTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 424967295),
    )


_GlobalCoeffAccessTotal_Type.__name__ = "Integer32"
_GlobalCoeffAccessTotal_Object = MibScalar
globalCoeffAccessTotal = _GlobalCoeffAccessTotal_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 48),
    _GlobalCoeffAccessTotal_Type()
)
globalCoeffAccessTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalCoeffAccessTotal.setStatus("mandatory")


class _GlobalCoeffDRTT_Type(Integer32):
    """Custom type globalCoeffDRTT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 424967295),
    )


_GlobalCoeffDRTT_Type.__name__ = "Integer32"
_GlobalCoeffDRTT_Object = MibScalar
globalCoeffDRTT = _GlobalCoeffDRTT_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 49),
    _GlobalCoeffDRTT_Type()
)
globalCoeffDRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalCoeffDRTT.setStatus("mandatory")


class _GlobalCoeffDCompletionRate_Type(Integer32):
    """Custom type globalCoeffDCompletionRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 424967295),
    )


_GlobalCoeffDCompletionRate_Type.__name__ = "Integer32"
_GlobalCoeffDCompletionRate_Object = MibScalar
globalCoeffDCompletionRate = _GlobalCoeffDCompletionRate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 50),
    _GlobalCoeffDCompletionRate_Type()
)
globalCoeffDCompletionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalCoeffDCompletionRate.setStatus("mandatory")


class _GlobalQosCoeffTopology_Type(Integer32):
    """Custom type globalQosCoeffTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_GlobalQosCoeffTopology_Type.__name__ = "Integer32"
_GlobalQosCoeffTopology_Object = MibScalar
globalQosCoeffTopology = _GlobalQosCoeffTopology_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 51),
    _GlobalQosCoeffTopology_Type()
)
globalQosCoeffTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalQosCoeffTopology.setStatus("mandatory")


class _GlobalQosFactorRTT_Type(Integer32):
    """Custom type globalQosFactorRTT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 424967295),
    )


_GlobalQosFactorRTT_Type.__name__ = "Integer32"
_GlobalQosFactorRTT_Object = MibScalar
globalQosFactorRTT = _GlobalQosFactorRTT_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 52),
    _GlobalQosFactorRTT_Type()
)
globalQosFactorRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalQosFactorRTT.setStatus("mandatory")


class _GlobalQosFactorHops_Type(Integer32):
    """Custom type globalQosFactorHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 424967295),
    )


_GlobalQosFactorHops_Type.__name__ = "Integer32"
_GlobalQosFactorHops_Object = MibScalar
globalQosFactorHops = _GlobalQosFactorHops_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 53),
    _GlobalQosFactorHops_Type()
)
globalQosFactorHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalQosFactorHops.setStatus("mandatory")


class _GlobalQosFactorCompletionRate_Type(Integer32):
    """Custom type globalQosFactorCompletionRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 424967295),
    )


_GlobalQosFactorCompletionRate_Type.__name__ = "Integer32"
_GlobalQosFactorCompletionRate_Object = MibScalar
globalQosFactorCompletionRate = _GlobalQosFactorCompletionRate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 54),
    _GlobalQosFactorCompletionRate_Type()
)
globalQosFactorCompletionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalQosFactorCompletionRate.setStatus("mandatory")


class _GlobalQosFactorPacketRate_Type(Integer32):
    """Custom type globalQosFactorPacketRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 424967295),
    )


_GlobalQosFactorPacketRate_Type.__name__ = "Integer32"
_GlobalQosFactorPacketRate_Object = MibScalar
globalQosFactorPacketRate = _GlobalQosFactorPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 55),
    _GlobalQosFactorPacketRate_Type()
)
globalQosFactorPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalQosFactorPacketRate.setStatus("mandatory")


class _GlobalQosFactorTopology_Type(Integer32):
    """Custom type globalQosFactorTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 424967295),
    )


_GlobalQosFactorTopology_Type.__name__ = "Integer32"
_GlobalQosFactorTopology_Object = MibScalar
globalQosFactorTopology = _GlobalQosFactorTopology_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 56),
    _GlobalQosFactorTopology_Type()
)
globalQosFactorTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalQosFactorTopology.setStatus("mandatory")


class _GlobalLDnsHiWater_Type(Integer32):
    """Custom type globalLDnsHiWater based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 424967295),
    )


_GlobalLDnsHiWater_Type.__name__ = "Integer32"
_GlobalLDnsHiWater_Object = MibScalar
globalLDnsHiWater = _GlobalLDnsHiWater_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 57),
    _GlobalLDnsHiWater_Type()
)
globalLDnsHiWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalLDnsHiWater.setStatus("mandatory")


class _GlobalLDnsLoWater_Type(Integer32):
    """Custom type globalLDnsLoWater based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 424967295),
    )


_GlobalLDnsLoWater_Type.__name__ = "Integer32"
_GlobalLDnsLoWater_Object = MibScalar
globalLDnsLoWater = _GlobalLDnsLoWater_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 58),
    _GlobalLDnsLoWater_Type()
)
globalLDnsLoWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalLDnsLoWater.setStatus("mandatory")


class _GlobalLDnsDuration_Type(Integer32):
    """Custom type globalLDnsDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3600, 424967295),
    )


_GlobalLDnsDuration_Type.__name__ = "Integer32"
_GlobalLDnsDuration_Object = MibScalar
globalLDnsDuration = _GlobalLDnsDuration_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 59),
    _GlobalLDnsDuration_Type()
)
globalLDnsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalLDnsDuration.setStatus("mandatory")


class _GlobalLDnsReapAlg_Type(Integer32):
    """Custom type globalLDnsReapAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fewestHits", 2),
          ("lru", 1),
          ("numberItems", 3))
    )


_GlobalLDnsReapAlg_Type.__name__ = "Integer32"
_GlobalLDnsReapAlg_Object = MibScalar
globalLDnsReapAlg = _GlobalLDnsReapAlg_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 60),
    _GlobalLDnsReapAlg_Type()
)
globalLDnsReapAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalLDnsReapAlg.setStatus("mandatory")


class _GlobalUseAltIqPort_Type(Integer32):
    """Custom type globalUseAltIqPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_GlobalUseAltIqPort_Type.__name__ = "Integer32"
_GlobalUseAltIqPort_Object = MibScalar
globalUseAltIqPort = _GlobalUseAltIqPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 61),
    _GlobalUseAltIqPort_Type()
)
globalUseAltIqPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalUseAltIqPort.setStatus("mandatory")


class _GlobalMultiplexIq_Type(Integer32):
    """Custom type globalMultiplexIq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_GlobalMultiplexIq_Type.__name__ = "Integer32"
_GlobalMultiplexIq_Object = MibScalar
globalMultiplexIq = _GlobalMultiplexIq_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 62),
    _GlobalMultiplexIq_Type()
)
globalMultiplexIq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalMultiplexIq.setStatus("mandatory")


class _GlobalRTTProbeProtocolList_Type(OctetString):
    """Custom type globalRTTProbeProtocolList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GlobalRTTProbeProtocolList_Type.__name__ = "OctetString"
_GlobalRTTProbeProtocolList_Object = MibScalar
globalRTTProbeProtocolList = _GlobalRTTProbeProtocolList_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 63),
    _GlobalRTTProbeProtocolList_Type()
)
globalRTTProbeProtocolList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRTTProbeProtocolList.setStatus("mandatory")


class _GlobalRTTProbeProtocolState_Type(OctetString):
    """Custom type globalRTTProbeProtocolState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GlobalRTTProbeProtocolState_Type.__name__ = "OctetString"
_GlobalRTTProbeProtocolState_Object = MibScalar
globalRTTProbeProtocolState = _GlobalRTTProbeProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 64),
    _GlobalRTTProbeProtocolState_Type()
)
globalRTTProbeProtocolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalRTTProbeProtocolState.setStatus("mandatory")


class _GlobalResetCounters_Type(Integer32):
    """Custom type globalResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("unreset", 2))
    )


_GlobalResetCounters_Type.__name__ = "Integer32"
_GlobalResetCounters_Object = MibScalar
globalResetCounters = _GlobalResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 65),
    _GlobalResetCounters_Type()
)
globalResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    globalResetCounters.setStatus("mandatory")
_GlobalResetCounterTime_Type = DateAndTime
_GlobalResetCounterTime_Object = MibScalar
globalResetCounterTime = _GlobalResetCounterTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 1, 66),
    _GlobalResetCounterTime_Type()
)
globalResetCounterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalResetCounterTime.setStatus("mandatory")
_DataCenters_ObjectIdentity = ObjectIdentity
dataCenters = _DataCenters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 2)
)
_DataCenterTable_Object = MibTable
dataCenterTable = _DataCenterTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dataCenterTable.setStatus("mandatory")
_DataCenterEntry_Object = MibTableRow
dataCenterEntry = _DataCenterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 2, 1, 1)
)
dataCenterEntry.setIndexNames(
    (0, "F5-3DNS-MIB", "dataCenterName"),
)
if mibBuilder.loadTexts:
    dataCenterEntry.setStatus("mandatory")


class _DataCenterName_Type(OctetString):
    """Custom type dataCenterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DataCenterName_Type.__name__ = "OctetString"
_DataCenterName_Object = MibTableColumn
dataCenterName = _DataCenterName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 2, 1, 1, 1),
    _DataCenterName_Type()
)
dataCenterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataCenterName.setStatus("mandatory")


class _DataCenterContact_Type(OctetString):
    """Custom type dataCenterContact based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DataCenterContact_Type.__name__ = "OctetString"
_DataCenterContact_Object = MibTableColumn
dataCenterContact = _DataCenterContact_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 2, 1, 1, 2),
    _DataCenterContact_Type()
)
dataCenterContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataCenterContact.setStatus("mandatory")


class _DataCenterLocation_Type(OctetString):
    """Custom type dataCenterLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DataCenterLocation_Type.__name__ = "OctetString"
_DataCenterLocation_Object = MibTableColumn
dataCenterLocation = _DataCenterLocation_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 2, 1, 1, 3),
    _DataCenterLocation_Type()
)
dataCenterLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataCenterLocation.setStatus("mandatory")
_DataCenterPathCount_Type = Integer32
_DataCenterPathCount_Object = MibTableColumn
dataCenterPathCount = _DataCenterPathCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 2, 1, 1, 4),
    _DataCenterPathCount_Type()
)
dataCenterPathCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataCenterPathCount.setStatus("mandatory")


class _DataCenterDisabled_Type(Integer32):
    """Custom type dataCenterDisabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_DataCenterDisabled_Type.__name__ = "Integer32"
_DataCenterDisabled_Object = MibTableColumn
dataCenterDisabled = _DataCenterDisabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 2, 1, 1, 5),
    _DataCenterDisabled_Type()
)
dataCenterDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataCenterDisabled.setStatus("mandatory")
_DataCenterDisableDuration_Type = TimeTicks
_DataCenterDisableDuration_Object = MibTableColumn
dataCenterDisableDuration = _DataCenterDisableDuration_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 2, 1, 1, 6),
    _DataCenterDisableDuration_Type()
)
dataCenterDisableDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataCenterDisableDuration.setStatus("mandatory")
_DataCenterServTable_Object = MibTable
dataCenterServTable = _DataCenterServTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dataCenterServTable.setStatus("mandatory")
_DataCenterServEntry_Object = MibTableRow
dataCenterServEntry = _DataCenterServEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 2, 2, 1)
)
dataCenterServEntry.setIndexNames(
    (0, "F5-3DNS-MIB", "dataCenterName"),
    (0, "F5-3DNS-MIB", "dataCenterServAddr"),
)
if mibBuilder.loadTexts:
    dataCenterServEntry.setStatus("mandatory")
_DataCenterServAddr_Type = IpAddress
_DataCenterServAddr_Object = MibTableColumn
dataCenterServAddr = _DataCenterServAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 2, 2, 1, 1),
    _DataCenterServAddr_Type()
)
dataCenterServAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataCenterServAddr.setStatus("mandatory")


class _DataCenterServType_Type(Integer32):
    """Custom type dataCenterServType based on Integer32"""
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
        *(("host", 4),
          ("lDns", 5),
          ("lbDnsServ", 3),
          ("lbRouter", 2),
          ("prober", 6),
          ("unknown", 1))
    )


_DataCenterServType_Type.__name__ = "Integer32"
_DataCenterServType_Object = MibTableColumn
dataCenterServType = _DataCenterServType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 2, 2, 1, 2),
    _DataCenterServType_Type()
)
dataCenterServType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataCenterServType.setStatus("mandatory")
_LbRouters_ObjectIdentity = ObjectIdentity
lbRouters = _LbRouters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3)
)
_LbRouterTable_Object = MibTable
lbRouterTable = _LbRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lbRouterTable.setStatus("mandatory")
_LbRouterEntry_Object = MibTableRow
lbRouterEntry = _LbRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 1, 1)
)
lbRouterEntry.setIndexNames(
    (0, "F5-3DNS-MIB", "lbRouterAddr"),
)
if mibBuilder.loadTexts:
    lbRouterEntry.setStatus("mandatory")
_LbRouterAddr_Type = IpAddress
_LbRouterAddr_Object = MibTableColumn
lbRouterAddr = _LbRouterAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 1, 1, 1),
    _LbRouterAddr_Type()
)
lbRouterAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterAddr.setStatus("mandatory")


class _LbRouterName_Type(OctetString):
    """Custom type lbRouterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LbRouterName_Type.__name__ = "OctetString"
_LbRouterName_Object = MibTableColumn
lbRouterName = _LbRouterName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 1, 1, 2),
    _LbRouterName_Type()
)
lbRouterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterName.setStatus("mandatory")
_LbRouterVServCount_Type = Integer32
_LbRouterVServCount_Object = MibTableColumn
lbRouterVServCount = _LbRouterVServCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 1, 1, 3),
    _LbRouterVServCount_Type()
)
lbRouterVServCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterVServCount.setStatus("mandatory")
_LbRouterPicks_Type = Counter32
_LbRouterPicks_Object = MibTableColumn
lbRouterPicks = _LbRouterPicks_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 1, 1, 4),
    _LbRouterPicks_Type()
)
lbRouterPicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterPicks.setStatus("mandatory")
_LbRouterRefreshes_Type = Counter32
_LbRouterRefreshes_Object = MibTableColumn
lbRouterRefreshes = _LbRouterRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 1, 1, 5),
    _LbRouterRefreshes_Type()
)
lbRouterRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterRefreshes.setStatus("mandatory")


class _LbRouterDisabled_Type(Integer32):
    """Custom type lbRouterDisabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_LbRouterDisabled_Type.__name__ = "Integer32"
_LbRouterDisabled_Object = MibTableColumn
lbRouterDisabled = _LbRouterDisabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 1, 1, 6),
    _LbRouterDisabled_Type()
)
lbRouterDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterDisabled.setStatus("mandatory")
_LbRouterDisableDuration_Type = TimeTicks
_LbRouterDisableDuration_Object = MibTableColumn
lbRouterDisableDuration = _LbRouterDisableDuration_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 1, 1, 7),
    _LbRouterDisableDuration_Type()
)
lbRouterDisableDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterDisableDuration.setStatus("mandatory")


class _LbRouterIQProto_Type(Integer32):
    """Custom type lbRouterIQProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_LbRouterIQProto_Type.__name__ = "Integer32"
_LbRouterIQProto_Object = MibTableColumn
lbRouterIQProto = _LbRouterIQProto_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 1, 1, 8),
    _LbRouterIQProto_Type()
)
lbRouterIQProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterIQProto.setStatus("mandatory")
_LbRouterIfTable_Object = MibTable
lbRouterIfTable = _LbRouterIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    lbRouterIfTable.setStatus("mandatory")
_LbRouterIfEntry_Object = MibTableRow
lbRouterIfEntry = _LbRouterIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 2, 1)
)
lbRouterIfEntry.setIndexNames(
    (0, "F5-3DNS-MIB", "lbRouterAddr"),
    (0, "F5-3DNS-MIB", "lbRouterIfAddr"),
)
if mibBuilder.loadTexts:
    lbRouterIfEntry.setStatus("mandatory")
_LbRouterIfAddr_Type = IpAddress
_LbRouterIfAddr_Object = MibTableColumn
lbRouterIfAddr = _LbRouterIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 2, 1, 1),
    _LbRouterIfAddr_Type()
)
lbRouterIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterIfAddr.setStatus("mandatory")


class _LbRouterIfShared_Type(Integer32):
    """Custom type lbRouterIfShared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_LbRouterIfShared_Type.__name__ = "Integer32"
_LbRouterIfShared_Object = MibTableColumn
lbRouterIfShared = _LbRouterIfShared_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 2, 1, 2),
    _LbRouterIfShared_Type()
)
lbRouterIfShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterIfShared.setStatus("mandatory")


class _LbRouterIfStatus_Type(Integer32):
    """Custom type lbRouterIfStatus based on Integer32"""
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
        *(("alert", 5),
          ("down", 3),
          ("panic", 6),
          ("unknown", 1),
          ("up", 2),
          ("waiting", 4))
    )


_LbRouterIfStatus_Type.__name__ = "Integer32"
_LbRouterIfStatus_Object = MibTableColumn
lbRouterIfStatus = _LbRouterIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 2, 1, 3),
    _LbRouterIfStatus_Type()
)
lbRouterIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterIfStatus.setStatus("mandatory")
_LbRouterIfTXPackets_Type = Counter32
_LbRouterIfTXPackets_Object = MibTableColumn
lbRouterIfTXPackets = _LbRouterIfTXPackets_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 2, 1, 4),
    _LbRouterIfTXPackets_Type()
)
lbRouterIfTXPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterIfTXPackets.setStatus("mandatory")
_LbRouterIfRXPackets_Type = Counter32
_LbRouterIfRXPackets_Object = MibTableColumn
lbRouterIfRXPackets = _LbRouterIfRXPackets_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 2, 1, 5),
    _LbRouterIfRXPackets_Type()
)
lbRouterIfRXPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterIfRXPackets.setStatus("mandatory")
_LbRouterIfPacketRate_Type = Integer32
_LbRouterIfPacketRate_Object = MibTableColumn
lbRouterIfPacketRate = _LbRouterIfPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 2, 1, 6),
    _LbRouterIfPacketRate_Type()
)
lbRouterIfPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterIfPacketRate.setStatus("mandatory")
_LbRouterIfUpTime_Type = TimeTicks
_LbRouterIfUpTime_Object = MibTableColumn
lbRouterIfUpTime = _LbRouterIfUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 2, 1, 7),
    _LbRouterIfUpTime_Type()
)
lbRouterIfUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterIfUpTime.setStatus("mandatory")
_LbRouterIfAliveTime_Type = DateAndTime
_LbRouterIfAliveTime_Object = MibTableColumn
lbRouterIfAliveTime = _LbRouterIfAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 2, 1, 8),
    _LbRouterIfAliveTime_Type()
)
lbRouterIfAliveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterIfAliveTime.setStatus("mandatory")
_LbRouterIfDataTime_Type = DateAndTime
_LbRouterIfDataTime_Object = MibTableColumn
lbRouterIfDataTime = _LbRouterIfDataTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 2, 1, 9),
    _LbRouterIfDataTime_Type()
)
lbRouterIfDataTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterIfDataTime.setStatus("mandatory")
_LbRouterIfPathSentTime_Type = DateAndTime
_LbRouterIfPathSentTime_Object = MibTableColumn
lbRouterIfPathSentTime = _LbRouterIfPathSentTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 2, 1, 10),
    _LbRouterIfPathSentTime_Type()
)
lbRouterIfPathSentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterIfPathSentTime.setStatus("mandatory")
_LbRouterIfPathsSent_Type = Integer32
_LbRouterIfPathsSent_Object = MibTableColumn
lbRouterIfPathsSent = _LbRouterIfPathsSent_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 2, 1, 11),
    _LbRouterIfPathsSent_Type()
)
lbRouterIfPathsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterIfPathsSent.setStatus("mandatory")
_LbRouterIfPathsRcvd_Type = Integer32
_LbRouterIfPathsRcvd_Object = MibTableColumn
lbRouterIfPathsRcvd = _LbRouterIfPathsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 2, 1, 12),
    _LbRouterIfPathsRcvd_Type()
)
lbRouterIfPathsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterIfPathsRcvd.setStatus("mandatory")
_LbRouterIfPathSends_Type = Counter32
_LbRouterIfPathSends_Object = MibTableColumn
lbRouterIfPathSends = _LbRouterIfPathSends_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 2, 1, 13),
    _LbRouterIfPathSends_Type()
)
lbRouterIfPathSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterIfPathSends.setStatus("mandatory")
_LbRouterIfPathRcvs_Type = Counter32
_LbRouterIfPathRcvs_Object = MibTableColumn
lbRouterIfPathRcvs = _LbRouterIfPathRcvs_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 2, 1, 14),
    _LbRouterIfPathRcvs_Type()
)
lbRouterIfPathRcvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterIfPathRcvs.setStatus("mandatory")
_LbRouterIfAvgPathsSentX1000_Type = Integer32
_LbRouterIfAvgPathsSentX1000_Object = MibTableColumn
lbRouterIfAvgPathsSentX1000 = _LbRouterIfAvgPathsSentX1000_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 2, 1, 15),
    _LbRouterIfAvgPathsSentX1000_Type()
)
lbRouterIfAvgPathsSentX1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterIfAvgPathsSentX1000.setStatus("mandatory")
_LbRouterIfAvgPathsRcvdX1000_Type = Integer32
_LbRouterIfAvgPathsRcvdX1000_Object = MibTableColumn
lbRouterIfAvgPathsRcvdX1000 = _LbRouterIfAvgPathsRcvdX1000_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 2, 1, 16),
    _LbRouterIfAvgPathsRcvdX1000_Type()
)
lbRouterIfAvgPathsRcvdX1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterIfAvgPathsRcvdX1000.setStatus("mandatory")
_LbRouterIfFctryTable_Object = MibTable
lbRouterIfFctryTable = _LbRouterIfFctryTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    lbRouterIfFctryTable.setStatus("mandatory")
_LbRouterIfFctryEntry_Object = MibTableRow
lbRouterIfFctryEntry = _LbRouterIfFctryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 3, 1)
)
lbRouterIfFctryEntry.setIndexNames(
    (0, "F5-3DNS-MIB", "lbRouterAddr"),
    (0, "F5-3DNS-MIB", "lbRouterIfAddr"),
    (0, "F5-3DNS-MIB", "lbRouterIfFctryType"),
)
if mibBuilder.loadTexts:
    lbRouterIfFctryEntry.setStatus("mandatory")


class _LbRouterIfFctryType_Type(Integer32):
    """Custom type lbRouterIfFctryType based on Integer32"""
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
        *(("discovery", 3),
          ("hops", 5),
          ("lbRouter", 1),
          ("prober", 2),
          ("server", 6),
          ("snmp", 4))
    )


_LbRouterIfFctryType_Type.__name__ = "Integer32"
_LbRouterIfFctryType_Object = MibTableColumn
lbRouterIfFctryType = _LbRouterIfFctryType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 3, 1, 1),
    _LbRouterIfFctryType_Type()
)
lbRouterIfFctryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterIfFctryType.setStatus("mandatory")
_LbRouterIfFctryCount_Type = Integer32
_LbRouterIfFctryCount_Object = MibTableColumn
lbRouterIfFctryCount = _LbRouterIfFctryCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 3, 1, 2),
    _LbRouterIfFctryCount_Type()
)
lbRouterIfFctryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterIfFctryCount.setStatus("mandatory")
_LbRouterVServTable_Object = MibTable
lbRouterVServTable = _LbRouterVServTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    lbRouterVServTable.setStatus("mandatory")
_LbRouterVServEntry_Object = MibTableRow
lbRouterVServEntry = _LbRouterVServEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 4, 1)
)
lbRouterVServEntry.setIndexNames(
    (0, "F5-3DNS-MIB", "lbRouterAddr"),
    (0, "F5-3DNS-MIB", "lbRouterVServAddr"),
    (0, "F5-3DNS-MIB", "lbRouterVServPort"),
)
if mibBuilder.loadTexts:
    lbRouterVServEntry.setStatus("mandatory")
_LbRouterVServAddr_Type = IpAddress
_LbRouterVServAddr_Object = MibTableColumn
lbRouterVServAddr = _LbRouterVServAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 4, 1, 1),
    _LbRouterVServAddr_Type()
)
lbRouterVServAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterVServAddr.setStatus("mandatory")


class _LbRouterVServPort_Type(Integer32):
    """Custom type lbRouterVServPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LbRouterVServPort_Type.__name__ = "Integer32"
_LbRouterVServPort_Object = MibTableColumn
lbRouterVServPort = _LbRouterVServPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 4, 1, 2),
    _LbRouterVServPort_Type()
)
lbRouterVServPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterVServPort.setStatus("mandatory")
_LbRouterVServXlatedAddr_Type = IpAddress
_LbRouterVServXlatedAddr_Object = MibTableColumn
lbRouterVServXlatedAddr = _LbRouterVServXlatedAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 4, 1, 3),
    _LbRouterVServXlatedAddr_Type()
)
lbRouterVServXlatedAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterVServXlatedAddr.setStatus("mandatory")
_LbRouterVServXlatedPort_Type = Integer32
_LbRouterVServXlatedPort_Object = MibTableColumn
lbRouterVServXlatedPort = _LbRouterVServXlatedPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 4, 1, 4),
    _LbRouterVServXlatedPort_Type()
)
lbRouterVServXlatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterVServXlatedPort.setStatus("mandatory")


class _LbRouterVServProbeProtocol_Type(Integer32):
    """Custom type lbRouterVServProbeProtocol based on Integer32"""
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
        *(("dnsRetrieveBindVers", 5),
          ("dnsnslookupDot", 4),
          ("icmp", 1),
          ("none", 7),
          ("numberItems", 6),
          ("tcp", 2),
          ("udp", 3))
    )


_LbRouterVServProbeProtocol_Type.__name__ = "Integer32"
_LbRouterVServProbeProtocol_Object = MibTableColumn
lbRouterVServProbeProtocol = _LbRouterVServProbeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 4, 1, 5),
    _LbRouterVServProbeProtocol_Type()
)
lbRouterVServProbeProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterVServProbeProtocol.setStatus("mandatory")
_LbRouterVServPicks_Type = Counter32
_LbRouterVServPicks_Object = MibTableColumn
lbRouterVServPicks = _LbRouterVServPicks_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 4, 1, 6),
    _LbRouterVServPicks_Type()
)
lbRouterVServPicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterVServPicks.setStatus("mandatory")
_LbRouterVServRefreshes_Type = Counter32
_LbRouterVServRefreshes_Object = MibTableColumn
lbRouterVServRefreshes = _LbRouterVServRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 4, 1, 7),
    _LbRouterVServRefreshes_Type()
)
lbRouterVServRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterVServRefreshes.setStatus("mandatory")
_LbRouterVServAliveTime_Type = DateAndTime
_LbRouterVServAliveTime_Object = MibTableColumn
lbRouterVServAliveTime = _LbRouterVServAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 4, 1, 8),
    _LbRouterVServAliveTime_Type()
)
lbRouterVServAliveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterVServAliveTime.setStatus("mandatory")
_LbRouterVServDataTime_Type = DateAndTime
_LbRouterVServDataTime_Object = MibTableColumn
lbRouterVServDataTime = _LbRouterVServDataTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 4, 1, 9),
    _LbRouterVServDataTime_Type()
)
lbRouterVServDataTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterVServDataTime.setStatus("mandatory")
_LbRouterVServCurConns_Type = Integer32
_LbRouterVServCurConns_Object = MibTableColumn
lbRouterVServCurConns = _LbRouterVServCurConns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 4, 1, 10),
    _LbRouterVServCurConns_Type()
)
lbRouterVServCurConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterVServCurConns.setStatus("mandatory")
_LbRouterVServCurConnLimit_Type = Integer32
_LbRouterVServCurConnLimit_Object = MibTableColumn
lbRouterVServCurConnLimit = _LbRouterVServCurConnLimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 4, 1, 11),
    _LbRouterVServCurConnLimit_Type()
)
lbRouterVServCurConnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterVServCurConnLimit.setStatus("mandatory")
_LbRouterVServCurNodesUp_Type = Integer32
_LbRouterVServCurNodesUp_Object = MibTableColumn
lbRouterVServCurNodesUp = _LbRouterVServCurNodesUp_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 4, 1, 12),
    _LbRouterVServCurNodesUp_Type()
)
lbRouterVServCurNodesUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterVServCurNodesUp.setStatus("mandatory")


class _LbRouterVServCurEnabled_Type(Integer32):
    """Custom type lbRouterVServCurEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_LbRouterVServCurEnabled_Type.__name__ = "Integer32"
_LbRouterVServCurEnabled_Object = MibTableColumn
lbRouterVServCurEnabled = _LbRouterVServCurEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 4, 1, 13),
    _LbRouterVServCurEnabled_Type()
)
lbRouterVServCurEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterVServCurEnabled.setStatus("mandatory")


class _LbRouterVServDnsServDisabled_Type(Integer32):
    """Custom type lbRouterVServDnsServDisabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_LbRouterVServDnsServDisabled_Type.__name__ = "Integer32"
_LbRouterVServDnsServDisabled_Object = MibTableColumn
lbRouterVServDnsServDisabled = _LbRouterVServDnsServDisabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 4, 1, 14),
    _LbRouterVServDnsServDisabled_Type()
)
lbRouterVServDnsServDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterVServDnsServDisabled.setStatus("mandatory")
_LbRouterVServDisableDuration_Type = TimeTicks
_LbRouterVServDisableDuration_Object = MibTableColumn
lbRouterVServDisableDuration = _LbRouterVServDisableDuration_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 3, 4, 1, 15),
    _LbRouterVServDisableDuration_Type()
)
lbRouterVServDisableDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbRouterVServDisableDuration.setStatus("mandatory")
_Hosts_ObjectIdentity = ObjectIdentity
hosts = _Hosts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4)
)
_HostTable_Object = MibTable
hostTable = _HostTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hostTable.setStatus("mandatory")
_HostEntry_Object = MibTableRow
hostEntry = _HostEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1)
)
hostEntry.setIndexNames(
    (0, "F5-3DNS-MIB", "hostAddr"),
)
if mibBuilder.loadTexts:
    hostEntry.setStatus("mandatory")
_HostAddr_Type = IpAddress
_HostAddr_Object = MibTableColumn
hostAddr = _HostAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1, 1),
    _HostAddr_Type()
)
hostAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostAddr.setStatus("mandatory")


class _HostName_Type(OctetString):
    """Custom type hostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HostName_Type.__name__ = "OctetString"
_HostName_Object = MibTableColumn
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1, 2),
    _HostName_Type()
)
hostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostName.setStatus("mandatory")
_HostProber_Type = IpAddress
_HostProber_Object = MibTableColumn
hostProber = _HostProber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1, 3),
    _HostProber_Type()
)
hostProber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostProber.setStatus("mandatory")


class _HostProbeProtocol_Type(Integer32):
    """Custom type hostProbeProtocol based on Integer32"""
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
        *(("dnsRetrieveBindVers", 5),
          ("dnsnslookupDot", 4),
          ("icmp", 1),
          ("none", 7),
          ("numberItems", 6),
          ("tcp", 2),
          ("udp", 3))
    )


_HostProbeProtocol_Type.__name__ = "Integer32"
_HostProbeProtocol_Object = MibTableColumn
hostProbeProtocol = _HostProbeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1, 4),
    _HostProbeProtocol_Type()
)
hostProbeProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostProbeProtocol.setStatus("mandatory")
_HostProbePort_Type = Integer32
_HostProbePort_Object = MibTableColumn
hostProbePort = _HostProbePort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1, 5),
    _HostProbePort_Type()
)
hostProbePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostProbePort.setStatus("mandatory")
_HostVServCount_Type = Integer32
_HostVServCount_Object = MibTableColumn
hostVServCount = _HostVServCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1, 6),
    _HostVServCount_Type()
)
hostVServCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostVServCount.setStatus("mandatory")


class _HostStatus_Type(Integer32):
    """Custom type hostStatus based on Integer32"""
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
        *(("alert", 5),
          ("down", 3),
          ("panic", 6),
          ("unknown", 1),
          ("up", 2),
          ("waiting", 4))
    )


_HostStatus_Type.__name__ = "Integer32"
_HostStatus_Object = MibTableColumn
hostStatus = _HostStatus_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1, 7),
    _HostStatus_Type()
)
hostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostStatus.setStatus("mandatory")
_HostPicks_Type = Counter32
_HostPicks_Object = MibTableColumn
hostPicks = _HostPicks_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1, 8),
    _HostPicks_Type()
)
hostPicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostPicks.setStatus("mandatory")
_HostRefreshes_Type = Counter32
_HostRefreshes_Object = MibTableColumn
hostRefreshes = _HostRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1, 9),
    _HostRefreshes_Type()
)
hostRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostRefreshes.setStatus("mandatory")


class _HostDisabled_Type(Integer32):
    """Custom type hostDisabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HostDisabled_Type.__name__ = "Integer32"
_HostDisabled_Object = MibTableColumn
hostDisabled = _HostDisabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1, 10),
    _HostDisabled_Type()
)
hostDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostDisabled.setStatus("mandatory")
_HostDisableDuration_Type = TimeTicks
_HostDisableDuration_Object = MibTableColumn
hostDisableDuration = _HostDisableDuration_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1, 11),
    _HostDisableDuration_Type()
)
hostDisableDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostDisableDuration.setStatus("mandatory")


class _HostMetrics_Type(Integer32):
    """Custom type hostMetrics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 3),
          ("unkown", 1),
          ("yes", 2))
    )


_HostMetrics_Type.__name__ = "Integer32"
_HostMetrics_Object = MibTableColumn
hostMetrics = _HostMetrics_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1, 12),
    _HostMetrics_Type()
)
hostMetrics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostMetrics.setStatus("mandatory")
_HostMemory_Type = Integer32
_HostMemory_Object = MibTableColumn
hostMemory = _HostMemory_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1, 13),
    _HostMemory_Type()
)
hostMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostMemory.setStatus("mandatory")
_HostCPU_Type = Integer32
_HostCPU_Object = MibTableColumn
hostCPU = _HostCPU_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1, 14),
    _HostCPU_Type()
)
hostCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostCPU.setStatus("mandatory")
_HostDiskSpace_Type = Integer32
_HostDiskSpace_Object = MibTableColumn
hostDiskSpace = _HostDiskSpace_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1, 15),
    _HostDiskSpace_Type()
)
hostDiskSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostDiskSpace.setStatus("mandatory")
_HostSNMPConfigured_Type = Integer32
_HostSNMPConfigured_Object = MibTableColumn
hostSNMPConfigured = _HostSNMPConfigured_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1, 16),
    _HostSNMPConfigured_Type()
)
hostSNMPConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostSNMPConfigured.setStatus("mandatory")


class _HostSNMPAgentType_Type(Integer32):
    """Custom type hostSNMPAgentType based on Integer32"""
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
        *(("ciscold", 1),
          ("ciscold2", 2),
          ("ciscold3", 3),
          ("ntserv", 6),
          ("solstice", 5),
          ("ucd", 4))
    )


_HostSNMPAgentType_Type.__name__ = "Integer32"
_HostSNMPAgentType_Object = MibTableColumn
hostSNMPAgentType = _HostSNMPAgentType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1, 17),
    _HostSNMPAgentType_Type()
)
hostSNMPAgentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostSNMPAgentType.setStatus("mandatory")
_HostSNMPAddress_Type = IpAddress
_HostSNMPAddress_Object = MibTableColumn
hostSNMPAddress = _HostSNMPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1, 18),
    _HostSNMPAddress_Type()
)
hostSNMPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostSNMPAddress.setStatus("mandatory")
_HostSNMPPort_Type = Integer32
_HostSNMPPort_Object = MibTableColumn
hostSNMPPort = _HostSNMPPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1, 19),
    _HostSNMPPort_Type()
)
hostSNMPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostSNMPPort.setStatus("mandatory")
_HostSNMPRetries_Type = Integer32
_HostSNMPRetries_Object = MibTableColumn
hostSNMPRetries = _HostSNMPRetries_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1, 20),
    _HostSNMPRetries_Type()
)
hostSNMPRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostSNMPRetries.setStatus("mandatory")
_HostSNMPTimeout_Type = Integer32
_HostSNMPTimeout_Object = MibTableColumn
hostSNMPTimeout = _HostSNMPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1, 21),
    _HostSNMPTimeout_Type()
)
hostSNMPTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostSNMPTimeout.setStatus("mandatory")


class _HostSNMPVersion_Type(Integer32):
    """Custom type hostSNMPVersion based on Integer32"""
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
        *(("notset", 4),
          ("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_HostSNMPVersion_Type.__name__ = "Integer32"
_HostSNMPVersion_Object = MibTableColumn
hostSNMPVersion = _HostSNMPVersion_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1, 22),
    _HostSNMPVersion_Type()
)
hostSNMPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostSNMPVersion.setStatus("mandatory")


class _HostSNMPCommunity_Type(OctetString):
    """Custom type hostSNMPCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HostSNMPCommunity_Type.__name__ = "OctetString"
_HostSNMPCommunity_Object = MibTableColumn
hostSNMPCommunity = _HostSNMPCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 1, 1, 23),
    _HostSNMPCommunity_Type()
)
hostSNMPCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostSNMPCommunity.setStatus("mandatory")
_HostIfTable_Object = MibTable
hostIfTable = _HostIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hostIfTable.setStatus("mandatory")
_HostIfEntry_Object = MibTableRow
hostIfEntry = _HostIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 2, 1)
)
hostIfEntry.setIndexNames(
    (0, "F5-3DNS-MIB", "hostAddr"),
    (0, "F5-3DNS-MIB", "hostIfAddr"),
)
if mibBuilder.loadTexts:
    hostIfEntry.setStatus("mandatory")
_HostIfAddr_Type = IpAddress
_HostIfAddr_Object = MibTableColumn
hostIfAddr = _HostIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 2, 1, 1),
    _HostIfAddr_Type()
)
hostIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIfAddr.setStatus("mandatory")


class _HostIfShared_Type(Integer32):
    """Custom type hostIfShared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HostIfShared_Type.__name__ = "Integer32"
_HostIfShared_Object = MibTableColumn
hostIfShared = _HostIfShared_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 2, 1, 2),
    _HostIfShared_Type()
)
hostIfShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIfShared.setStatus("mandatory")


class _HostIfStatus_Type(Integer32):
    """Custom type hostIfStatus based on Integer32"""
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
        *(("alert", 5),
          ("down", 3),
          ("panic", 6),
          ("unknown", 1),
          ("up", 2),
          ("waiting", 4))
    )


_HostIfStatus_Type.__name__ = "Integer32"
_HostIfStatus_Object = MibTableColumn
hostIfStatus = _HostIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 2, 1, 3),
    _HostIfStatus_Type()
)
hostIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIfStatus.setStatus("mandatory")
_HostIfTXPackets_Type = Counter32
_HostIfTXPackets_Object = MibTableColumn
hostIfTXPackets = _HostIfTXPackets_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 2, 1, 4),
    _HostIfTXPackets_Type()
)
hostIfTXPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIfTXPackets.setStatus("mandatory")
_HostIfRXPackets_Type = Counter32
_HostIfRXPackets_Object = MibTableColumn
hostIfRXPackets = _HostIfRXPackets_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 2, 1, 5),
    _HostIfRXPackets_Type()
)
hostIfRXPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIfRXPackets.setStatus("mandatory")
_HostIfUpTime_Type = TimeTicks
_HostIfUpTime_Object = MibTableColumn
hostIfUpTime = _HostIfUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 2, 1, 6),
    _HostIfUpTime_Type()
)
hostIfUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIfUpTime.setStatus("mandatory")
_HostIfAliveTime_Type = DateAndTime
_HostIfAliveTime_Object = MibTableColumn
hostIfAliveTime = _HostIfAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 2, 1, 7),
    _HostIfAliveTime_Type()
)
hostIfAliveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIfAliveTime.setStatus("mandatory")
_HostIfDataTime_Type = DateAndTime
_HostIfDataTime_Object = MibTableColumn
hostIfDataTime = _HostIfDataTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 2, 1, 8),
    _HostIfDataTime_Type()
)
hostIfDataTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIfDataTime.setStatus("mandatory")
_HostIfPathSentTime_Type = DateAndTime
_HostIfPathSentTime_Object = MibTableColumn
hostIfPathSentTime = _HostIfPathSentTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 2, 1, 9),
    _HostIfPathSentTime_Type()
)
hostIfPathSentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIfPathSentTime.setStatus("mandatory")
_HostIfPathsSent_Type = Integer32
_HostIfPathsSent_Object = MibTableColumn
hostIfPathsSent = _HostIfPathsSent_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 2, 1, 10),
    _HostIfPathsSent_Type()
)
hostIfPathsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIfPathsSent.setStatus("mandatory")
_HostIfPathsRcvd_Type = Integer32
_HostIfPathsRcvd_Object = MibTableColumn
hostIfPathsRcvd = _HostIfPathsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 2, 1, 11),
    _HostIfPathsRcvd_Type()
)
hostIfPathsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIfPathsRcvd.setStatus("mandatory")
_HostIfPathSends_Type = Counter32
_HostIfPathSends_Object = MibTableColumn
hostIfPathSends = _HostIfPathSends_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 2, 1, 12),
    _HostIfPathSends_Type()
)
hostIfPathSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIfPathSends.setStatus("mandatory")
_HostIfPathRcvs_Type = Counter32
_HostIfPathRcvs_Object = MibTableColumn
hostIfPathRcvs = _HostIfPathRcvs_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 2, 1, 13),
    _HostIfPathRcvs_Type()
)
hostIfPathRcvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIfPathRcvs.setStatus("mandatory")
_HostIfAvgPathsSentX1000_Type = Integer32
_HostIfAvgPathsSentX1000_Object = MibTableColumn
hostIfAvgPathsSentX1000 = _HostIfAvgPathsSentX1000_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 2, 1, 14),
    _HostIfAvgPathsSentX1000_Type()
)
hostIfAvgPathsSentX1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIfAvgPathsSentX1000.setStatus("mandatory")
_HostIfAvgPathsRcvdX1000_Type = Integer32
_HostIfAvgPathsRcvdX1000_Object = MibTableColumn
hostIfAvgPathsRcvdX1000 = _HostIfAvgPathsRcvdX1000_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 2, 1, 15),
    _HostIfAvgPathsRcvdX1000_Type()
)
hostIfAvgPathsRcvdX1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIfAvgPathsRcvdX1000.setStatus("mandatory")
_HostIfFctryTable_Object = MibTable
hostIfFctryTable = _HostIfFctryTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    hostIfFctryTable.setStatus("mandatory")
_HostIfFctryEntry_Object = MibTableRow
hostIfFctryEntry = _HostIfFctryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 3, 1)
)
hostIfFctryEntry.setIndexNames(
    (0, "F5-3DNS-MIB", "hostAddr"),
    (0, "F5-3DNS-MIB", "hostIfAddr"),
    (0, "F5-3DNS-MIB", "hostIfFctryType"),
)
if mibBuilder.loadTexts:
    hostIfFctryEntry.setStatus("mandatory")


class _HostIfFctryType_Type(Integer32):
    """Custom type hostIfFctryType based on Integer32"""
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
        *(("discovery", 3),
          ("hops", 5),
          ("lbRouter", 1),
          ("prober", 2),
          ("server", 6),
          ("snmp", 4))
    )


_HostIfFctryType_Type.__name__ = "Integer32"
_HostIfFctryType_Object = MibTableColumn
hostIfFctryType = _HostIfFctryType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 3, 1, 1),
    _HostIfFctryType_Type()
)
hostIfFctryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIfFctryType.setStatus("mandatory")
_HostIfFctryCount_Type = Integer32
_HostIfFctryCount_Object = MibTableColumn
hostIfFctryCount = _HostIfFctryCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 3, 1, 2),
    _HostIfFctryCount_Type()
)
hostIfFctryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIfFctryCount.setStatus("mandatory")
_HostVServTable_Object = MibTable
hostVServTable = _HostVServTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    hostVServTable.setStatus("mandatory")
_HostVServEntry_Object = MibTableRow
hostVServEntry = _HostVServEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 4, 1)
)
hostVServEntry.setIndexNames(
    (0, "F5-3DNS-MIB", "hostAddr"),
    (0, "F5-3DNS-MIB", "hostVServAddr"),
    (0, "F5-3DNS-MIB", "hostVServPort"),
)
if mibBuilder.loadTexts:
    hostVServEntry.setStatus("mandatory")
_HostVServAddr_Type = IpAddress
_HostVServAddr_Object = MibTableColumn
hostVServAddr = _HostVServAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 4, 1, 1),
    _HostVServAddr_Type()
)
hostVServAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostVServAddr.setStatus("mandatory")


class _HostVServPort_Type(Integer32):
    """Custom type hostVServPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HostVServPort_Type.__name__ = "Integer32"
_HostVServPort_Object = MibTableColumn
hostVServPort = _HostVServPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 4, 1, 2),
    _HostVServPort_Type()
)
hostVServPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostVServPort.setStatus("mandatory")
_HostVServXlatedAddr_Type = IpAddress
_HostVServXlatedAddr_Object = MibTableColumn
hostVServXlatedAddr = _HostVServXlatedAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 4, 1, 3),
    _HostVServXlatedAddr_Type()
)
hostVServXlatedAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostVServXlatedAddr.setStatus("mandatory")
_HostVServXlatedPort_Type = Integer32
_HostVServXlatedPort_Object = MibTableColumn
hostVServXlatedPort = _HostVServXlatedPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 4, 1, 4),
    _HostVServXlatedPort_Type()
)
hostVServXlatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostVServXlatedPort.setStatus("mandatory")


class _HostVServProbeProtocol_Type(Integer32):
    """Custom type hostVServProbeProtocol based on Integer32"""
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
        *(("dnsRetrieveBindVers", 5),
          ("dnsnslookupDot", 4),
          ("icmp", 1),
          ("none", 7),
          ("numberItems", 6),
          ("tcp", 2),
          ("udp", 3))
    )


_HostVServProbeProtocol_Type.__name__ = "Integer32"
_HostVServProbeProtocol_Object = MibTableColumn
hostVServProbeProtocol = _HostVServProbeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 4, 1, 5),
    _HostVServProbeProtocol_Type()
)
hostVServProbeProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostVServProbeProtocol.setStatus("mandatory")
_HostVServPicks_Type = Counter32
_HostVServPicks_Object = MibTableColumn
hostVServPicks = _HostVServPicks_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 4, 1, 6),
    _HostVServPicks_Type()
)
hostVServPicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostVServPicks.setStatus("mandatory")
_HostVServRefreshes_Type = Counter32
_HostVServRefreshes_Object = MibTableColumn
hostVServRefreshes = _HostVServRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 4, 1, 7),
    _HostVServRefreshes_Type()
)
hostVServRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostVServRefreshes.setStatus("mandatory")
_HostVServAliveTime_Type = DateAndTime
_HostVServAliveTime_Object = MibTableColumn
hostVServAliveTime = _HostVServAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 4, 1, 8),
    _HostVServAliveTime_Type()
)
hostVServAliveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostVServAliveTime.setStatus("mandatory")
_HostVServDataTime_Type = DateAndTime
_HostVServDataTime_Object = MibTableColumn
hostVServDataTime = _HostVServDataTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 4, 1, 9),
    _HostVServDataTime_Type()
)
hostVServDataTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostVServDataTime.setStatus("mandatory")


class _HostVServDisabled_Type(Integer32):
    """Custom type hostVServDisabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HostVServDisabled_Type.__name__ = "Integer32"
_HostVServDisabled_Object = MibTableColumn
hostVServDisabled = _HostVServDisabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 4, 1, 10),
    _HostVServDisabled_Type()
)
hostVServDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostVServDisabled.setStatus("mandatory")
_HostVServDisableDuration_Type = TimeTicks
_HostVServDisableDuration_Object = MibTableColumn
hostVServDisableDuration = _HostVServDisableDuration_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 4, 4, 1, 11),
    _HostVServDisableDuration_Type()
)
hostVServDisableDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostVServDisableDuration.setStatus("mandatory")
_LbDnsServs_ObjectIdentity = ObjectIdentity
lbDnsServs = _LbDnsServs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5)
)
_LbDnsServTable_Object = MibTable
lbDnsServTable = _LbDnsServTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    lbDnsServTable.setStatus("mandatory")
_LbDnsServEntry_Object = MibTableRow
lbDnsServEntry = _LbDnsServEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 1, 1)
)
lbDnsServEntry.setIndexNames(
    (0, "F5-3DNS-MIB", "lbDnsServAddr"),
)
if mibBuilder.loadTexts:
    lbDnsServEntry.setStatus("mandatory")
_LbDnsServAddr_Type = IpAddress
_LbDnsServAddr_Object = MibTableColumn
lbDnsServAddr = _LbDnsServAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 1, 1, 1),
    _LbDnsServAddr_Type()
)
lbDnsServAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServAddr.setStatus("mandatory")


class _LbDnsServName_Type(OctetString):
    """Custom type lbDnsServName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LbDnsServName_Type.__name__ = "OctetString"
_LbDnsServName_Object = MibTableColumn
lbDnsServName = _LbDnsServName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 1, 1, 2),
    _LbDnsServName_Type()
)
lbDnsServName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServName.setStatus("mandatory")
_LbDnsServProber_Type = IpAddress
_LbDnsServProber_Object = MibTableColumn
lbDnsServProber = _LbDnsServProber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 1, 1, 3),
    _LbDnsServProber_Type()
)
lbDnsServProber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServProber.setStatus("mandatory")


class _LbDnsServProbeProtocol_Type(Integer32):
    """Custom type lbDnsServProbeProtocol based on Integer32"""
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
        *(("dnsRetrieveBindVers", 5),
          ("dnsnslookupDot", 4),
          ("icmp", 1),
          ("none", 7),
          ("numberItems", 6),
          ("tcp", 2),
          ("udp", 3))
    )


_LbDnsServProbeProtocol_Type.__name__ = "Integer32"
_LbDnsServProbeProtocol_Object = MibTableColumn
lbDnsServProbeProtocol = _LbDnsServProbeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 1, 1, 4),
    _LbDnsServProbeProtocol_Type()
)
lbDnsServProbeProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServProbeProtocol.setStatus("mandatory")
_LbDnsServProbePort_Type = Integer32
_LbDnsServProbePort_Object = MibTableColumn
lbDnsServProbePort = _LbDnsServProbePort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 1, 1, 5),
    _LbDnsServProbePort_Type()
)
lbDnsServProbePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServProbePort.setStatus("mandatory")


class _LbDnsServStatus_Type(Integer32):
    """Custom type lbDnsServStatus based on Integer32"""
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
        *(("alert", 5),
          ("down", 3),
          ("panic", 6),
          ("unknown", 1),
          ("up", 2),
          ("waiting", 4))
    )


_LbDnsServStatus_Type.__name__ = "Integer32"
_LbDnsServStatus_Object = MibTableColumn
lbDnsServStatus = _LbDnsServStatus_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 1, 1, 6),
    _LbDnsServStatus_Type()
)
lbDnsServStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServStatus.setStatus("mandatory")
_LbDnsServPicks_Type = Counter32
_LbDnsServPicks_Object = MibTableColumn
lbDnsServPicks = _LbDnsServPicks_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 1, 1, 7),
    _LbDnsServPicks_Type()
)
lbDnsServPicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServPicks.setStatus("mandatory")
_LbDnsServRefreshes_Type = Counter32
_LbDnsServRefreshes_Object = MibTableColumn
lbDnsServRefreshes = _LbDnsServRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 1, 1, 8),
    _LbDnsServRefreshes_Type()
)
lbDnsServRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServRefreshes.setStatus("mandatory")


class _LbDnsServDisabled_Type(Integer32):
    """Custom type lbDnsServDisabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_LbDnsServDisabled_Type.__name__ = "Integer32"
_LbDnsServDisabled_Object = MibTableColumn
lbDnsServDisabled = _LbDnsServDisabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 1, 1, 9),
    _LbDnsServDisabled_Type()
)
lbDnsServDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServDisabled.setStatus("mandatory")
_LbDnsServDisableDuration_Type = TimeTicks
_LbDnsServDisableDuration_Object = MibTableColumn
lbDnsServDisableDuration = _LbDnsServDisableDuration_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 1, 1, 10),
    _LbDnsServDisableDuration_Type()
)
lbDnsServDisableDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServDisableDuration.setStatus("mandatory")


class _LbDnsServIQProto_Type(Integer32):
    """Custom type lbDnsServIQProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_LbDnsServIQProto_Type.__name__ = "Integer32"
_LbDnsServIQProto_Object = MibTableColumn
lbDnsServIQProto = _LbDnsServIQProto_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 1, 1, 11),
    _LbDnsServIQProto_Type()
)
lbDnsServIQProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServIQProto.setStatus("mandatory")
_LbDnsServIfTable_Object = MibTable
lbDnsServIfTable = _LbDnsServIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    lbDnsServIfTable.setStatus("mandatory")
_LbDnsServIfEntry_Object = MibTableRow
lbDnsServIfEntry = _LbDnsServIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 2, 1)
)
lbDnsServIfEntry.setIndexNames(
    (0, "F5-3DNS-MIB", "lbDnsServAddr"),
    (0, "F5-3DNS-MIB", "lbDnsServIfAddr"),
)
if mibBuilder.loadTexts:
    lbDnsServIfEntry.setStatus("mandatory")
_LbDnsServIfAddr_Type = IpAddress
_LbDnsServIfAddr_Object = MibTableColumn
lbDnsServIfAddr = _LbDnsServIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 2, 1, 1),
    _LbDnsServIfAddr_Type()
)
lbDnsServIfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServIfAddr.setStatus("mandatory")


class _LbDnsServIfShared_Type(Integer32):
    """Custom type lbDnsServIfShared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_LbDnsServIfShared_Type.__name__ = "Integer32"
_LbDnsServIfShared_Object = MibTableColumn
lbDnsServIfShared = _LbDnsServIfShared_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 2, 1, 2),
    _LbDnsServIfShared_Type()
)
lbDnsServIfShared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServIfShared.setStatus("mandatory")


class _LbDnsServIfStatus_Type(Integer32):
    """Custom type lbDnsServIfStatus based on Integer32"""
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
        *(("alert", 5),
          ("down", 3),
          ("panic", 6),
          ("unknown", 1),
          ("up", 2),
          ("waiting", 4))
    )


_LbDnsServIfStatus_Type.__name__ = "Integer32"
_LbDnsServIfStatus_Object = MibTableColumn
lbDnsServIfStatus = _LbDnsServIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 2, 1, 3),
    _LbDnsServIfStatus_Type()
)
lbDnsServIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServIfStatus.setStatus("mandatory")
_LbDnsServIfTXPackets_Type = Counter32
_LbDnsServIfTXPackets_Object = MibTableColumn
lbDnsServIfTXPackets = _LbDnsServIfTXPackets_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 2, 1, 4),
    _LbDnsServIfTXPackets_Type()
)
lbDnsServIfTXPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServIfTXPackets.setStatus("mandatory")
_LbDnsServIfRXPackets_Type = Counter32
_LbDnsServIfRXPackets_Object = MibTableColumn
lbDnsServIfRXPackets = _LbDnsServIfRXPackets_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 2, 1, 5),
    _LbDnsServIfRXPackets_Type()
)
lbDnsServIfRXPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServIfRXPackets.setStatus("mandatory")
_LbDnsServIfUpTime_Type = TimeTicks
_LbDnsServIfUpTime_Object = MibTableColumn
lbDnsServIfUpTime = _LbDnsServIfUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 2, 1, 6),
    _LbDnsServIfUpTime_Type()
)
lbDnsServIfUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServIfUpTime.setStatus("mandatory")
_LbDnsServIfAliveTime_Type = DateAndTime
_LbDnsServIfAliveTime_Object = MibTableColumn
lbDnsServIfAliveTime = _LbDnsServIfAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 2, 1, 7),
    _LbDnsServIfAliveTime_Type()
)
lbDnsServIfAliveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServIfAliveTime.setStatus("mandatory")
_LbDnsServIfDataTime_Type = DateAndTime
_LbDnsServIfDataTime_Object = MibTableColumn
lbDnsServIfDataTime = _LbDnsServIfDataTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 2, 1, 8),
    _LbDnsServIfDataTime_Type()
)
lbDnsServIfDataTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServIfDataTime.setStatus("mandatory")
_LbDnsServIfPathSentTime_Type = DateAndTime
_LbDnsServIfPathSentTime_Object = MibTableColumn
lbDnsServIfPathSentTime = _LbDnsServIfPathSentTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 2, 1, 9),
    _LbDnsServIfPathSentTime_Type()
)
lbDnsServIfPathSentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServIfPathSentTime.setStatus("mandatory")
_LbDnsServIfPathsSent_Type = Integer32
_LbDnsServIfPathsSent_Object = MibTableColumn
lbDnsServIfPathsSent = _LbDnsServIfPathsSent_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 2, 1, 10),
    _LbDnsServIfPathsSent_Type()
)
lbDnsServIfPathsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServIfPathsSent.setStatus("mandatory")
_LbDnsServIfPathsRcvd_Type = Integer32
_LbDnsServIfPathsRcvd_Object = MibTableColumn
lbDnsServIfPathsRcvd = _LbDnsServIfPathsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 2, 1, 11),
    _LbDnsServIfPathsRcvd_Type()
)
lbDnsServIfPathsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServIfPathsRcvd.setStatus("mandatory")
_LbDnsServIfPathSends_Type = Counter32
_LbDnsServIfPathSends_Object = MibTableColumn
lbDnsServIfPathSends = _LbDnsServIfPathSends_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 2, 1, 12),
    _LbDnsServIfPathSends_Type()
)
lbDnsServIfPathSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServIfPathSends.setStatus("mandatory")
_LbDnsServIfPathRcvs_Type = Counter32
_LbDnsServIfPathRcvs_Object = MibTableColumn
lbDnsServIfPathRcvs = _LbDnsServIfPathRcvs_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 2, 1, 13),
    _LbDnsServIfPathRcvs_Type()
)
lbDnsServIfPathRcvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServIfPathRcvs.setStatus("mandatory")
_LbDnsServIfAvgPathsSentX1000_Type = Integer32
_LbDnsServIfAvgPathsSentX1000_Object = MibTableColumn
lbDnsServIfAvgPathsSentX1000 = _LbDnsServIfAvgPathsSentX1000_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 2, 1, 14),
    _LbDnsServIfAvgPathsSentX1000_Type()
)
lbDnsServIfAvgPathsSentX1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServIfAvgPathsSentX1000.setStatus("mandatory")
_LbDnsServIfAvgPathsRcvdX1000_Type = Integer32
_LbDnsServIfAvgPathsRcvdX1000_Object = MibTableColumn
lbDnsServIfAvgPathsRcvdX1000 = _LbDnsServIfAvgPathsRcvdX1000_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 2, 1, 15),
    _LbDnsServIfAvgPathsRcvdX1000_Type()
)
lbDnsServIfAvgPathsRcvdX1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServIfAvgPathsRcvdX1000.setStatus("mandatory")
_LbDnsServIfFctryTable_Object = MibTable
lbDnsServIfFctryTable = _LbDnsServIfFctryTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    lbDnsServIfFctryTable.setStatus("mandatory")
_LbDnsServIfFctryEntry_Object = MibTableRow
lbDnsServIfFctryEntry = _LbDnsServIfFctryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 3, 1)
)
lbDnsServIfFctryEntry.setIndexNames(
    (0, "F5-3DNS-MIB", "lbDnsServAddr"),
    (0, "F5-3DNS-MIB", "lbDnsServIfAddr"),
    (0, "F5-3DNS-MIB", "lbDnsServIfFctryType"),
)
if mibBuilder.loadTexts:
    lbDnsServIfFctryEntry.setStatus("mandatory")


class _LbDnsServIfFctryType_Type(Integer32):
    """Custom type lbDnsServIfFctryType based on Integer32"""
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
        *(("discovery", 3),
          ("hops", 5),
          ("lbRouter", 1),
          ("prober", 2),
          ("server", 6),
          ("snmp", 4))
    )


_LbDnsServIfFctryType_Type.__name__ = "Integer32"
_LbDnsServIfFctryType_Object = MibTableColumn
lbDnsServIfFctryType = _LbDnsServIfFctryType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 3, 1, 1),
    _LbDnsServIfFctryType_Type()
)
lbDnsServIfFctryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServIfFctryType.setStatus("mandatory")
_LbDnsServIfFctryCount_Type = Integer32
_LbDnsServIfFctryCount_Object = MibTableColumn
lbDnsServIfFctryCount = _LbDnsServIfFctryCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 5, 3, 1, 2),
    _LbDnsServIfFctryCount_Type()
)
lbDnsServIfFctryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDnsServIfFctryCount.setStatus("mandatory")
_LbDomains_ObjectIdentity = ObjectIdentity
lbDomains = _LbDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6)
)
_LbDomainTable_Object = MibTable
lbDomainTable = _LbDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    lbDomainTable.setStatus("mandatory")
_LbDomainEntry_Object = MibTableRow
lbDomainEntry = _LbDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 1, 1)
)
lbDomainEntry.setIndexNames(
    (0, "F5-3DNS-MIB", "lbDomainName"),
)
if mibBuilder.loadTexts:
    lbDomainEntry.setStatus("mandatory")


class _LbDomainName_Type(OctetString):
    """Custom type lbDomainName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LbDomainName_Type.__name__ = "OctetString"
_LbDomainName_Object = MibTableColumn
lbDomainName = _LbDomainName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 1, 1, 1),
    _LbDomainName_Type()
)
lbDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainName.setStatus("mandatory")
_LbDomainAddr_Type = IpAddress
_LbDomainAddr_Object = MibTableColumn
lbDomainAddr = _LbDomainAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 1, 1, 2),
    _LbDomainAddr_Type()
)
lbDomainAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainAddr.setStatus("mandatory")


class _LbDomainPort_Type(Integer32):
    """Custom type lbDomainPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LbDomainPort_Type.__name__ = "Integer32"
_LbDomainPort_Object = MibTableColumn
lbDomainPort = _LbDomainPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 1, 1, 3),
    _LbDomainPort_Type()
)
lbDomainPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPort.setStatus("mandatory")


class _LbDomainTTL_Type(Integer32):
    """Custom type lbDomainTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LbDomainTTL_Type.__name__ = "Integer32"
_LbDomainTTL_Object = MibTableColumn
lbDomainTTL = _LbDomainTTL_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 1, 1, 4),
    _LbDomainTTL_Type()
)
lbDomainTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainTTL.setStatus("mandatory")


class _LbDomainLBModePool_Type(Integer32):
    """Custom type lbDomainLBModePool based on Integer32"""
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
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("connections", 11),
          ("cpu", 16),
          ("diskSpace", 17),
          ("globalAvailability", 9),
          ("hitRatio", 18),
          ("hops", 13),
          ("mem", 15),
          ("none", 2),
          ("packetRate", 14),
          ("qos", 19),
          ("random", 6),
          ("ratio", 5),
          ("returnDNS", 1),
          ("returnVS", 3),
          ("roundRobin", 4),
          ("roundTripTime", 12),
          ("servers", 10),
          ("staticPersist", 8),
          ("topology", 7))
    )


_LbDomainLBModePool_Type.__name__ = "Integer32"
_LbDomainLBModePool_Object = MibTableColumn
lbDomainLBModePool = _LbDomainLBModePool_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 1, 1, 5),
    _LbDomainLBModePool_Type()
)
lbDomainLBModePool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainLBModePool.setStatus("mandatory")


class _LbDomainQosCoeffRTT_Type(Integer32):
    """Custom type lbDomainQosCoeffRTT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LbDomainQosCoeffRTT_Type.__name__ = "Integer32"
_LbDomainQosCoeffRTT_Object = MibTableColumn
lbDomainQosCoeffRTT = _LbDomainQosCoeffRTT_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 1, 1, 6),
    _LbDomainQosCoeffRTT_Type()
)
lbDomainQosCoeffRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainQosCoeffRTT.setStatus("mandatory")


class _LbDomainQosCoeffHops_Type(Integer32):
    """Custom type lbDomainQosCoeffHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LbDomainQosCoeffHops_Type.__name__ = "Integer32"
_LbDomainQosCoeffHops_Object = MibTableColumn
lbDomainQosCoeffHops = _LbDomainQosCoeffHops_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 1, 1, 7),
    _LbDomainQosCoeffHops_Type()
)
lbDomainQosCoeffHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainQosCoeffHops.setStatus("mandatory")


class _LbDomainQosCoeffTopology_Type(Integer32):
    """Custom type lbDomainQosCoeffTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LbDomainQosCoeffTopology_Type.__name__ = "Integer32"
_LbDomainQosCoeffTopology_Object = MibTableColumn
lbDomainQosCoeffTopology = _LbDomainQosCoeffTopology_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 1, 1, 8),
    _LbDomainQosCoeffTopology_Type()
)
lbDomainQosCoeffTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainQosCoeffTopology.setStatus("mandatory")


class _LbDomainQosCoeffCompletionRate_Type(Integer32):
    """Custom type lbDomainQosCoeffCompletionRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LbDomainQosCoeffCompletionRate_Type.__name__ = "Integer32"
_LbDomainQosCoeffCompletionRate_Object = MibTableColumn
lbDomainQosCoeffCompletionRate = _LbDomainQosCoeffCompletionRate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 1, 1, 9),
    _LbDomainQosCoeffCompletionRate_Type()
)
lbDomainQosCoeffCompletionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainQosCoeffCompletionRate.setStatus("mandatory")


class _LbDomainQosCoeffPacketRate_Type(Integer32):
    """Custom type lbDomainQosCoeffPacketRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LbDomainQosCoeffPacketRate_Type.__name__ = "Integer32"
_LbDomainQosCoeffPacketRate_Object = MibTableColumn
lbDomainQosCoeffPacketRate = _LbDomainQosCoeffPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 1, 1, 10),
    _LbDomainQosCoeffPacketRate_Type()
)
lbDomainQosCoeffPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainQosCoeffPacketRate.setStatus("mandatory")
_LbDomainRequests_Type = Counter32
_LbDomainRequests_Object = MibTableColumn
lbDomainRequests = _LbDomainRequests_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 1, 1, 11),
    _LbDomainRequests_Type()
)
lbDomainRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainRequests.setStatus("mandatory")
_LbDomainPreferredResolves_Type = Counter32
_LbDomainPreferredResolves_Object = MibTableColumn
lbDomainPreferredResolves = _LbDomainPreferredResolves_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 1, 1, 12),
    _LbDomainPreferredResolves_Type()
)
lbDomainPreferredResolves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPreferredResolves.setStatus("mandatory")
_LbDomainAlternateResolves_Type = Counter32
_LbDomainAlternateResolves_Object = MibTableColumn
lbDomainAlternateResolves = _LbDomainAlternateResolves_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 1, 1, 13),
    _LbDomainAlternateResolves_Type()
)
lbDomainAlternateResolves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainAlternateResolves.setStatus("mandatory")
_LbDomainFallbackResolves_Type = Counter32
_LbDomainFallbackResolves_Object = MibTableColumn
lbDomainFallbackResolves = _LbDomainFallbackResolves_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 1, 1, 14),
    _LbDomainFallbackResolves_Type()
)
lbDomainFallbackResolves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainFallbackResolves.setStatus("mandatory")
_LbDomainReturnsToDns_Type = Counter32
_LbDomainReturnsToDns_Object = MibTableColumn
lbDomainReturnsToDns = _LbDomainReturnsToDns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 1, 1, 15),
    _LbDomainReturnsToDns_Type()
)
lbDomainReturnsToDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainReturnsToDns.setStatus("mandatory")
_LbDomainLastResolve_Type = DateAndTime
_LbDomainLastResolve_Object = MibTableColumn
lbDomainLastResolve = _LbDomainLastResolve_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 1, 1, 16),
    _LbDomainLastResolve_Type()
)
lbDomainLastResolve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainLastResolve.setStatus("mandatory")


class _LbDomainDisabled_Type(Integer32):
    """Custom type lbDomainDisabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_LbDomainDisabled_Type.__name__ = "Integer32"
_LbDomainDisabled_Object = MibTableColumn
lbDomainDisabled = _LbDomainDisabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 1, 1, 17),
    _LbDomainDisabled_Type()
)
lbDomainDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainDisabled.setStatus("mandatory")
_LbDomainDisableDuration_Type = TimeTicks
_LbDomainDisableDuration_Object = MibTableColumn
lbDomainDisableDuration = _LbDomainDisableDuration_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 1, 1, 18),
    _LbDomainDisableDuration_Type()
)
lbDomainDisableDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainDisableDuration.setStatus("mandatory")


class _LbDomainPersist_Type(Integer32):
    """Custom type lbDomainPersist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_LbDomainPersist_Type.__name__ = "Integer32"
_LbDomainPersist_Object = MibTableColumn
lbDomainPersist = _LbDomainPersist_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 1, 1, 19),
    _LbDomainPersist_Type()
)
lbDomainPersist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPersist.setStatus("mandatory")
_LbDomainPersistTTL_Type = TimeTicks
_LbDomainPersistTTL_Object = MibTableColumn
lbDomainPersistTTL = _LbDomainPersistTTL_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 1, 1, 20),
    _LbDomainPersistTTL_Type()
)
lbDomainPersistTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPersistTTL.setStatus("mandatory")
_LbDomainAliasTable_Object = MibTable
lbDomainAliasTable = _LbDomainAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    lbDomainAliasTable.setStatus("mandatory")
_LbDomainAliasEntry_Object = MibTableRow
lbDomainAliasEntry = _LbDomainAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 2, 1)
)
lbDomainAliasEntry.setIndexNames(
    (0, "F5-3DNS-MIB", "lbDomainName"),
    (0, "F5-3DNS-MIB", "lbDomainAliasIndex"),
)
if mibBuilder.loadTexts:
    lbDomainAliasEntry.setStatus("mandatory")


class _LbDomainAliasIndex_Type(Integer32):
    """Custom type lbDomainAliasIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LbDomainAliasIndex_Type.__name__ = "Integer32"
_LbDomainAliasIndex_Object = MibTableColumn
lbDomainAliasIndex = _LbDomainAliasIndex_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 2, 1, 1),
    _LbDomainAliasIndex_Type()
)
lbDomainAliasIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainAliasIndex.setStatus("mandatory")


class _LbDomainAliasName_Type(OctetString):
    """Custom type lbDomainAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LbDomainAliasName_Type.__name__ = "OctetString"
_LbDomainAliasName_Object = MibTableColumn
lbDomainAliasName = _LbDomainAliasName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 2, 1, 2),
    _LbDomainAliasName_Type()
)
lbDomainAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainAliasName.setStatus("mandatory")
_LbDomainAliasRequests_Type = Counter32
_LbDomainAliasRequests_Object = MibTableColumn
lbDomainAliasRequests = _LbDomainAliasRequests_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 2, 1, 3),
    _LbDomainAliasRequests_Type()
)
lbDomainAliasRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainAliasRequests.setStatus("mandatory")
_LbDomainPortTable_Object = MibTable
lbDomainPortTable = _LbDomainPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    lbDomainPortTable.setStatus("mandatory")
_LbDomainPortEntry_Object = MibTableRow
lbDomainPortEntry = _LbDomainPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 3, 1)
)
lbDomainPortEntry.setIndexNames(
    (0, "F5-3DNS-MIB", "lbDomainName"),
    (0, "F5-3DNS-MIB", "lbDomainPortPort"),
)
if mibBuilder.loadTexts:
    lbDomainPortEntry.setStatus("mandatory")


class _LbDomainPortPort_Type(Integer32):
    """Custom type lbDomainPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LbDomainPortPort_Type.__name__ = "Integer32"
_LbDomainPortPort_Object = MibTableColumn
lbDomainPortPort = _LbDomainPortPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 3, 1, 1),
    _LbDomainPortPort_Type()
)
lbDomainPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPortPort.setStatus("mandatory")
_LbDomainPoolTable_Object = MibTable
lbDomainPoolTable = _LbDomainPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 4)
)
if mibBuilder.loadTexts:
    lbDomainPoolTable.setStatus("mandatory")
_LbDomainPoolEntry_Object = MibTableRow
lbDomainPoolEntry = _LbDomainPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 4, 1)
)
lbDomainPoolEntry.setIndexNames(
    (0, "F5-3DNS-MIB", "lbDomainName"),
    (0, "F5-3DNS-MIB", "lbDomainPoolIndex"),
)
if mibBuilder.loadTexts:
    lbDomainPoolEntry.setStatus("mandatory")


class _LbDomainPoolIndex_Type(Integer32):
    """Custom type lbDomainPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LbDomainPoolIndex_Type.__name__ = "Integer32"
_LbDomainPoolIndex_Object = MibTableColumn
lbDomainPoolIndex = _LbDomainPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 4, 1, 1),
    _LbDomainPoolIndex_Type()
)
lbDomainPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPoolIndex.setStatus("mandatory")


class _LbDomainPoolName_Type(OctetString):
    """Custom type lbDomainPoolName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LbDomainPoolName_Type.__name__ = "OctetString"
_LbDomainPoolName_Object = MibTableColumn
lbDomainPoolName = _LbDomainPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 4, 1, 2),
    _LbDomainPoolName_Type()
)
lbDomainPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPoolName.setStatus("mandatory")


class _LbDomainPoolType_Type(Integer32):
    """Custom type lbDomainPoolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("host", 3),
          ("lbRouter", 2),
          ("unknown", 1))
    )


_LbDomainPoolType_Type.__name__ = "Integer32"
_LbDomainPoolType_Object = MibTableColumn
lbDomainPoolType = _LbDomainPoolType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 4, 1, 3),
    _LbDomainPoolType_Type()
)
lbDomainPoolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPoolType.setStatus("mandatory")


class _LbDomainPoolState_Type(Integer32):
    """Custom type lbDomainPoolState based on Integer32"""
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
        *(("alternate", 3),
          ("fallback", 4),
          ("preferred", 2),
          ("unknown", 1))
    )


_LbDomainPoolState_Type.__name__ = "Integer32"
_LbDomainPoolState_Object = MibTableColumn
lbDomainPoolState = _LbDomainPoolState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 4, 1, 4),
    _LbDomainPoolState_Type()
)
lbDomainPoolState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPoolState.setStatus("mandatory")
_LbDomainPoolVSCount_Type = Integer32
_LbDomainPoolVSCount_Object = MibTableColumn
lbDomainPoolVSCount = _LbDomainPoolVSCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 4, 1, 5),
    _LbDomainPoolVSCount_Type()
)
lbDomainPoolVSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPoolVSCount.setStatus("mandatory")


class _LbDomainPoolLBMode_Type(Integer32):
    """Custom type lbDomainPoolLBMode based on Integer32"""
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
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("connections", 11),
          ("cpu", 16),
          ("diskSpace", 17),
          ("globalAvailability", 9),
          ("hitRatio", 18),
          ("hops", 13),
          ("mem", 15),
          ("none", 2),
          ("packetRate", 14),
          ("qos", 19),
          ("random", 6),
          ("ratio", 5),
          ("returnDNS", 1),
          ("returnVS", 3),
          ("roundRobin", 4),
          ("roundTripTime", 12),
          ("servers", 10),
          ("staticPersist", 8),
          ("topology", 7))
    )


_LbDomainPoolLBMode_Type.__name__ = "Integer32"
_LbDomainPoolLBMode_Object = MibTableColumn
lbDomainPoolLBMode = _LbDomainPoolLBMode_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 4, 1, 6),
    _LbDomainPoolLBMode_Type()
)
lbDomainPoolLBMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPoolLBMode.setStatus("mandatory")


class _LbDomainPoolAlternateLBMode_Type(Integer32):
    """Custom type lbDomainPoolAlternateLBMode based on Integer32"""
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
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("connections", 11),
          ("cpu", 16),
          ("diskSpace", 17),
          ("globalAvailability", 9),
          ("hitRatio", 18),
          ("hops", 13),
          ("mem", 15),
          ("none", 2),
          ("packetRate", 14),
          ("qos", 19),
          ("random", 6),
          ("ratio", 5),
          ("returnDNS", 1),
          ("returnVS", 3),
          ("roundRobin", 4),
          ("roundTripTime", 12),
          ("servers", 10),
          ("staticPersist", 8),
          ("topology", 7))
    )


_LbDomainPoolAlternateLBMode_Type.__name__ = "Integer32"
_LbDomainPoolAlternateLBMode_Object = MibTableColumn
lbDomainPoolAlternateLBMode = _LbDomainPoolAlternateLBMode_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 4, 1, 7),
    _LbDomainPoolAlternateLBMode_Type()
)
lbDomainPoolAlternateLBMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPoolAlternateLBMode.setStatus("mandatory")


class _LbDomainPoolFallbackLBMode_Type(Integer32):
    """Custom type lbDomainPoolFallbackLBMode based on Integer32"""
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
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("connections", 11),
          ("cpu", 16),
          ("diskSpace", 17),
          ("globalAvailability", 9),
          ("hitRatio", 18),
          ("hops", 13),
          ("mem", 15),
          ("none", 2),
          ("packetRate", 14),
          ("qos", 19),
          ("random", 6),
          ("ratio", 5),
          ("returnDNS", 1),
          ("returnVS", 3),
          ("roundRobin", 4),
          ("roundTripTime", 12),
          ("servers", 10),
          ("staticPersist", 8),
          ("topology", 7))
    )


_LbDomainPoolFallbackLBMode_Type.__name__ = "Integer32"
_LbDomainPoolFallbackLBMode_Object = MibTableColumn
lbDomainPoolFallbackLBMode = _LbDomainPoolFallbackLBMode_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 4, 1, 8),
    _LbDomainPoolFallbackLBMode_Type()
)
lbDomainPoolFallbackLBMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPoolFallbackLBMode.setStatus("mandatory")


class _LbDomainPoolCheckStaticDepends_Type(Integer32):
    """Custom type lbDomainPoolCheckStaticDepends based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_LbDomainPoolCheckStaticDepends_Type.__name__ = "Integer32"
_LbDomainPoolCheckStaticDepends_Object = MibTableColumn
lbDomainPoolCheckStaticDepends = _LbDomainPoolCheckStaticDepends_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 4, 1, 9),
    _LbDomainPoolCheckStaticDepends_Type()
)
lbDomainPoolCheckStaticDepends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPoolCheckStaticDepends.setStatus("mandatory")


class _LbDomainPoolCheckDynamicDepends_Type(Integer32):
    """Custom type lbDomainPoolCheckDynamicDepends based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_LbDomainPoolCheckDynamicDepends_Type.__name__ = "Integer32"
_LbDomainPoolCheckDynamicDepends_Object = MibTableColumn
lbDomainPoolCheckDynamicDepends = _LbDomainPoolCheckDynamicDepends_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 4, 1, 10),
    _LbDomainPoolCheckDynamicDepends_Type()
)
lbDomainPoolCheckDynamicDepends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPoolCheckDynamicDepends.setStatus("mandatory")
_LbDomainPoolRatio_Type = Integer32
_LbDomainPoolRatio_Object = MibTableColumn
lbDomainPoolRatio = _LbDomainPoolRatio_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 4, 1, 11),
    _LbDomainPoolRatio_Type()
)
lbDomainPoolRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPoolRatio.setStatus("mandatory")
_LbDomainPoolRipeness_Type = Integer32
_LbDomainPoolRipeness_Object = MibTableColumn
lbDomainPoolRipeness = _LbDomainPoolRipeness_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 4, 1, 12),
    _LbDomainPoolRipeness_Type()
)
lbDomainPoolRipeness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPoolRipeness.setStatus("mandatory")
_LbDomainPoolPreferredResolves_Type = Counter32
_LbDomainPoolPreferredResolves_Object = MibTableColumn
lbDomainPoolPreferredResolves = _LbDomainPoolPreferredResolves_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 4, 1, 13),
    _LbDomainPoolPreferredResolves_Type()
)
lbDomainPoolPreferredResolves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPoolPreferredResolves.setStatus("mandatory")
_LbDomainPoolAlternateResolves_Type = Counter32
_LbDomainPoolAlternateResolves_Object = MibTableColumn
lbDomainPoolAlternateResolves = _LbDomainPoolAlternateResolves_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 4, 1, 14),
    _LbDomainPoolAlternateResolves_Type()
)
lbDomainPoolAlternateResolves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPoolAlternateResolves.setStatus("mandatory")
_LbDomainPoolFallbackResolves_Type = Counter32
_LbDomainPoolFallbackResolves_Object = MibTableColumn
lbDomainPoolFallbackResolves = _LbDomainPoolFallbackResolves_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 4, 1, 15),
    _LbDomainPoolFallbackResolves_Type()
)
lbDomainPoolFallbackResolves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPoolFallbackResolves.setStatus("mandatory")
_LbDomainPoolReturnsToDns_Type = Counter32
_LbDomainPoolReturnsToDns_Object = MibTableColumn
lbDomainPoolReturnsToDns = _LbDomainPoolReturnsToDns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 4, 1, 16),
    _LbDomainPoolReturnsToDns_Type()
)
lbDomainPoolReturnsToDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPoolReturnsToDns.setStatus("mandatory")


class _LbDomainPoolRRLdns_Type(Integer32):
    """Custom type lbDomainPoolRRLdns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_LbDomainPoolRRLdns_Type.__name__ = "Integer32"
_LbDomainPoolRRLdns_Object = MibTableColumn
lbDomainPoolRRLdns = _LbDomainPoolRRLdns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 4, 1, 17),
    _LbDomainPoolRRLdns_Type()
)
lbDomainPoolRRLdns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPoolRRLdns.setStatus("mandatory")
_LbDomainPoolRRLdnsLimit_Type = Integer32
_LbDomainPoolRRLdnsLimit_Object = MibTableColumn
lbDomainPoolRRLdnsLimit = _LbDomainPoolRRLdnsLimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 4, 1, 18),
    _LbDomainPoolRRLdnsLimit_Type()
)
lbDomainPoolRRLdnsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPoolRRLdnsLimit.setStatus("mandatory")
_LbDomainPoolVSTable_Object = MibTable
lbDomainPoolVSTable = _LbDomainPoolVSTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 5)
)
if mibBuilder.loadTexts:
    lbDomainPoolVSTable.setStatus("mandatory")
_LbDomainPoolVSEntry_Object = MibTableRow
lbDomainPoolVSEntry = _LbDomainPoolVSEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 5, 1)
)
lbDomainPoolVSEntry.setIndexNames(
    (0, "F5-3DNS-MIB", "lbDomainName"),
    (0, "F5-3DNS-MIB", "lbDomainPoolIndex"),
    (0, "F5-3DNS-MIB", "lbDomainPoolVSAddr"),
    (0, "F5-3DNS-MIB", "lbDomainPoolVSPort"),
)
if mibBuilder.loadTexts:
    lbDomainPoolVSEntry.setStatus("mandatory")
_LbDomainPoolVSAddr_Type = IpAddress
_LbDomainPoolVSAddr_Object = MibTableColumn
lbDomainPoolVSAddr = _LbDomainPoolVSAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 5, 1, 1),
    _LbDomainPoolVSAddr_Type()
)
lbDomainPoolVSAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPoolVSAddr.setStatus("mandatory")


class _LbDomainPoolVSPort_Type(Integer32):
    """Custom type lbDomainPoolVSPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LbDomainPoolVSPort_Type.__name__ = "Integer32"
_LbDomainPoolVSPort_Object = MibTableColumn
lbDomainPoolVSPort = _LbDomainPoolVSPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 5, 1, 2),
    _LbDomainPoolVSPort_Type()
)
lbDomainPoolVSPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPoolVSPort.setStatus("mandatory")
_LbDomainPoolVSRatio_Type = Integer32
_LbDomainPoolVSRatio_Object = MibTableColumn
lbDomainPoolVSRatio = _LbDomainPoolVSRatio_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 5, 1, 3),
    _LbDomainPoolVSRatio_Type()
)
lbDomainPoolVSRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPoolVSRatio.setStatus("mandatory")
_LbDomainPoolVSRipeness_Type = Integer32
_LbDomainPoolVSRipeness_Object = MibTableColumn
lbDomainPoolVSRipeness = _LbDomainPoolVSRipeness_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 6, 5, 1, 4),
    _LbDomainPoolVSRipeness_Type()
)
lbDomainPoolVSRipeness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbDomainPoolVSRipeness.setStatus("mandatory")
_Summary_ObjectIdentity = ObjectIdentity
summary = _Summary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 7)
)


class _SummaryVersion_Type(OctetString):
    """Custom type summaryVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SummaryVersion_Type.__name__ = "OctetString"
_SummaryVersion_Object = MibScalar
summaryVersion = _SummaryVersion_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 7, 1),
    _SummaryVersion_Type()
)
summaryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summaryVersion.setStatus("mandatory")
_SummaryUpTime_Type = TimeTicks
_SummaryUpTime_Object = MibScalar
summaryUpTime = _SummaryUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 7, 2),
    _SummaryUpTime_Type()
)
summaryUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summaryUpTime.setStatus("mandatory")
_SummaryDate_Type = DateAndTime
_SummaryDate_Object = MibScalar
summaryDate = _SummaryDate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 7, 3),
    _SummaryDate_Type()
)
summaryDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summaryDate.setStatus("mandatory")
_SummaryLastReload_Type = TimeTicks
_SummaryLastReload_Object = MibScalar
summaryLastReload = _SummaryLastReload_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 7, 4),
    _SummaryLastReload_Type()
)
summaryLastReload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summaryLastReload.setStatus("mandatory")
_SummaryLastDump_Type = TimeTicks
_SummaryLastDump_Object = MibScalar
summaryLastDump = _SummaryLastDump_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 7, 5),
    _SummaryLastDump_Type()
)
summaryLastDump.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summaryLastDump.setStatus("mandatory")
_SummaryRequests_Type = Counter32
_SummaryRequests_Object = MibScalar
summaryRequests = _SummaryRequests_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 7, 6),
    _SummaryRequests_Type()
)
summaryRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summaryRequests.setStatus("mandatory")


class _SummarySyncMode_Type(Integer32):
    """Custom type summarySyncMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("primary", 1),
          ("secondary", 2))
    )


_SummarySyncMode_Type.__name__ = "Integer32"
_SummarySyncMode_Object = MibScalar
summarySyncMode = _SummarySyncMode_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 7, 7),
    _SummarySyncMode_Type()
)
summarySyncMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summarySyncMode.setStatus("mandatory")


class _SummarySyncFile_Type(OctetString):
    """Custom type summarySyncFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SummarySyncFile_Type.__name__ = "OctetString"
_SummarySyncFile_Object = MibScalar
summarySyncFile = _SummarySyncFile_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 7, 8),
    _SummarySyncFile_Type()
)
summarySyncFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summarySyncFile.setStatus("mandatory")
_SummarySyncIns_Type = Counter32
_SummarySyncIns_Object = MibScalar
summarySyncIns = _SummarySyncIns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 7, 9),
    _SummarySyncIns_Type()
)
summarySyncIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summarySyncIns.setStatus("mandatory")
_SummarySyncInErrors_Type = Counter32
_SummarySyncInErrors_Object = MibScalar
summarySyncInErrors = _SummarySyncInErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 7, 10),
    _SummarySyncInErrors_Type()
)
summarySyncInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summarySyncInErrors.setStatus("mandatory")
_SummaryLastSyncIn_Type = TimeTicks
_SummaryLastSyncIn_Object = MibScalar
summaryLastSyncIn = _SummaryLastSyncIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 7, 11),
    _SummaryLastSyncIn_Type()
)
summaryLastSyncIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summaryLastSyncIn.setStatus("mandatory")
_SummarySyncOuts_Type = Counter32
_SummarySyncOuts_Object = MibScalar
summarySyncOuts = _SummarySyncOuts_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 7, 12),
    _SummarySyncOuts_Type()
)
summarySyncOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summarySyncOuts.setStatus("mandatory")
_SummarySyncOutErrors_Type = Counter32
_SummarySyncOutErrors_Object = MibScalar
summarySyncOutErrors = _SummarySyncOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 7, 13),
    _SummarySyncOutErrors_Type()
)
summarySyncOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summarySyncOutErrors.setStatus("mandatory")
_SummaryLastSyncOut_Type = TimeTicks
_SummaryLastSyncOut_Object = MibScalar
summaryLastSyncOut = _SummaryLastSyncOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 1, 1, 7, 14),
    _SummaryLastSyncOut_Type()
)
summaryLastSyncOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    summaryLastSyncOut.setStatus("mandatory")
_ThreednsTrap_ObjectIdentity = ObjectIdentity
threednsTrap = _ThreednsTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 2)
)
_ThreednsTraps_ObjectIdentity = ObjectIdentity
threednsTraps = _ThreednsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 2, 2)
)

# Managed Objects groups


# Notification objects

threednsTrapVSGreenToRed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 2, 2, 0, 1)
)
if mibBuilder.loadTexts:
    threednsTrapVSGreenToRed.setStatus(
        ""
    )

threednsTrapVSRedToGreen = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 2, 2, 0, 2)
)
if mibBuilder.loadTexts:
    threednsTrapVSRedToGreen.setStatus(
        ""
    )

threednsTrapServerRedToGreen = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 2, 2, 0, 3)
)
if mibBuilder.loadTexts:
    threednsTrapServerRedToGreen.setStatus(
        ""
    )

threednsTrapServerGreenToRed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 2, 2, 0, 4)
)
if mibBuilder.loadTexts:
    threednsTrapServerGreenToRed.setStatus(
        ""
    )

threednsTrapCRCFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 1, 2, 2, 2, 0, 5)
)
if mibBuilder.loadTexts:
    threednsTrapCRCFailure.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F5-3DNS-MIB",
    **{"f5": f5,
       "f5systems": f5systems,
       "f53dns": f53dns,
       "f53dnsMIB": f53dnsMIB,
       "f53dnsMIBObjects": f53dnsMIBObjects,
       "globals": globals,
       "globalCheckStaticDepends": globalCheckStaticDepends,
       "globalDefaultAlternate": globalDefaultAlternate,
       "globalTimerGetLBRouterData": globalTimerGetLBRouterData,
       "globalTimerGetVServData": globalTimerGetVServData,
       "globalTimerGetPathData": globalTimerGetPathData,
       "globalLBRouterTTL": globalLBRouterTTL,
       "globalVSTTL": globalVSTTL,
       "globalPathTTL": globalPathTTL,
       "globalRTTTimeout": globalRTTTimeout,
       "globalRTTSampleCount": globalRTTSampleCount,
       "globalRTTPacketLength": globalRTTPacketLength,
       "globalRTTProbeProtocol": globalRTTProbeProtocol,
       "globalEncryption": globalEncryption,
       "globalEncryptionKeyFile": globalEncryptionKeyFile,
       "globalPathHiWater": globalPathHiWater,
       "globalPathLoWater": globalPathLoWater,
       "globalPathDuration": globalPathDuration,
       "globalPathReapAlg": globalPathReapAlg,
       "globalTimerKeepAlive": globalTimerKeepAlive,
       "globalRxBufSize": globalRxBufSize,
       "globalTxBufSize": globalTxBufSize,
       "globalQosCoeffRTT": globalQosCoeffRTT,
       "globalQosCoeffCompletionRate": globalQosCoeffCompletionRate,
       "globalQosCoeffHops": globalQosCoeffHops,
       "globalQosCoeffPacketRate": globalQosCoeffPacketRate,
       "globalPathsNoClobber": globalPathsNoClobber,
       "globalPathsNeverDie": globalPathsNeverDie,
       "globalRegulateInit": globalRegulateInit,
       "globalRegulatePaths": globalRegulatePaths,
       "globalProberAddr": globalProberAddr,
       "globalCheckDynamicDepends": globalCheckDynamicDepends,
       "globalDefaultFallback": globalDefaultFallback,
       "globalDefaultTTL": globalDefaultTTL,
       "globalPersistLDns": globalPersistLDns,
       "globalFbRespectAcl": globalFbRespectAcl,
       "globalFbRespectDepends": globalFbRespectDepends,
       "globalHostTTL": globalHostTTL,
       "globalTimerGetHostData": globalTimerGetHostData,
       "globalRTTRetireZero": globalRTTRetireZero,
       "globalRTTPortDiscovery": globalRTTPortDiscovery,
       "globalRTTDiscoveryMethod": globalRTTDiscoveryMethod,
       "globalRTTProbeDynamic": globalRTTProbeDynamic,
       "globalResolverRXBufSize": globalResolverRXBufSize,
       "globalResolverTXBufSize": globalResolverTXBufSize,
       "globalCoeffLastAccess": globalCoeffLastAccess,
       "globalCoeffFreshRemain": globalCoeffFreshRemain,
       "globalCoeffAccessRefresh": globalCoeffAccessRefresh,
       "globalCoeffAccessTotal": globalCoeffAccessTotal,
       "globalCoeffDRTT": globalCoeffDRTT,
       "globalCoeffDCompletionRate": globalCoeffDCompletionRate,
       "globalQosCoeffTopology": globalQosCoeffTopology,
       "globalQosFactorRTT": globalQosFactorRTT,
       "globalQosFactorHops": globalQosFactorHops,
       "globalQosFactorCompletionRate": globalQosFactorCompletionRate,
       "globalQosFactorPacketRate": globalQosFactorPacketRate,
       "globalQosFactorTopology": globalQosFactorTopology,
       "globalLDnsHiWater": globalLDnsHiWater,
       "globalLDnsLoWater": globalLDnsLoWater,
       "globalLDnsDuration": globalLDnsDuration,
       "globalLDnsReapAlg": globalLDnsReapAlg,
       "globalUseAltIqPort": globalUseAltIqPort,
       "globalMultiplexIq": globalMultiplexIq,
       "globalRTTProbeProtocolList": globalRTTProbeProtocolList,
       "globalRTTProbeProtocolState": globalRTTProbeProtocolState,
       "globalResetCounters": globalResetCounters,
       "globalResetCounterTime": globalResetCounterTime,
       "dataCenters": dataCenters,
       "dataCenterTable": dataCenterTable,
       "dataCenterEntry": dataCenterEntry,
       "dataCenterName": dataCenterName,
       "dataCenterContact": dataCenterContact,
       "dataCenterLocation": dataCenterLocation,
       "dataCenterPathCount": dataCenterPathCount,
       "dataCenterDisabled": dataCenterDisabled,
       "dataCenterDisableDuration": dataCenterDisableDuration,
       "dataCenterServTable": dataCenterServTable,
       "dataCenterServEntry": dataCenterServEntry,
       "dataCenterServAddr": dataCenterServAddr,
       "dataCenterServType": dataCenterServType,
       "lbRouters": lbRouters,
       "lbRouterTable": lbRouterTable,
       "lbRouterEntry": lbRouterEntry,
       "lbRouterAddr": lbRouterAddr,
       "lbRouterName": lbRouterName,
       "lbRouterVServCount": lbRouterVServCount,
       "lbRouterPicks": lbRouterPicks,
       "lbRouterRefreshes": lbRouterRefreshes,
       "lbRouterDisabled": lbRouterDisabled,
       "lbRouterDisableDuration": lbRouterDisableDuration,
       "lbRouterIQProto": lbRouterIQProto,
       "lbRouterIfTable": lbRouterIfTable,
       "lbRouterIfEntry": lbRouterIfEntry,
       "lbRouterIfAddr": lbRouterIfAddr,
       "lbRouterIfShared": lbRouterIfShared,
       "lbRouterIfStatus": lbRouterIfStatus,
       "lbRouterIfTXPackets": lbRouterIfTXPackets,
       "lbRouterIfRXPackets": lbRouterIfRXPackets,
       "lbRouterIfPacketRate": lbRouterIfPacketRate,
       "lbRouterIfUpTime": lbRouterIfUpTime,
       "lbRouterIfAliveTime": lbRouterIfAliveTime,
       "lbRouterIfDataTime": lbRouterIfDataTime,
       "lbRouterIfPathSentTime": lbRouterIfPathSentTime,
       "lbRouterIfPathsSent": lbRouterIfPathsSent,
       "lbRouterIfPathsRcvd": lbRouterIfPathsRcvd,
       "lbRouterIfPathSends": lbRouterIfPathSends,
       "lbRouterIfPathRcvs": lbRouterIfPathRcvs,
       "lbRouterIfAvgPathsSentX1000": lbRouterIfAvgPathsSentX1000,
       "lbRouterIfAvgPathsRcvdX1000": lbRouterIfAvgPathsRcvdX1000,
       "lbRouterIfFctryTable": lbRouterIfFctryTable,
       "lbRouterIfFctryEntry": lbRouterIfFctryEntry,
       "lbRouterIfFctryType": lbRouterIfFctryType,
       "lbRouterIfFctryCount": lbRouterIfFctryCount,
       "lbRouterVServTable": lbRouterVServTable,
       "lbRouterVServEntry": lbRouterVServEntry,
       "lbRouterVServAddr": lbRouterVServAddr,
       "lbRouterVServPort": lbRouterVServPort,
       "lbRouterVServXlatedAddr": lbRouterVServXlatedAddr,
       "lbRouterVServXlatedPort": lbRouterVServXlatedPort,
       "lbRouterVServProbeProtocol": lbRouterVServProbeProtocol,
       "lbRouterVServPicks": lbRouterVServPicks,
       "lbRouterVServRefreshes": lbRouterVServRefreshes,
       "lbRouterVServAliveTime": lbRouterVServAliveTime,
       "lbRouterVServDataTime": lbRouterVServDataTime,
       "lbRouterVServCurConns": lbRouterVServCurConns,
       "lbRouterVServCurConnLimit": lbRouterVServCurConnLimit,
       "lbRouterVServCurNodesUp": lbRouterVServCurNodesUp,
       "lbRouterVServCurEnabled": lbRouterVServCurEnabled,
       "lbRouterVServDnsServDisabled": lbRouterVServDnsServDisabled,
       "lbRouterVServDisableDuration": lbRouterVServDisableDuration,
       "hosts": hosts,
       "hostTable": hostTable,
       "hostEntry": hostEntry,
       "hostAddr": hostAddr,
       "hostName": hostName,
       "hostProber": hostProber,
       "hostProbeProtocol": hostProbeProtocol,
       "hostProbePort": hostProbePort,
       "hostVServCount": hostVServCount,
       "hostStatus": hostStatus,
       "hostPicks": hostPicks,
       "hostRefreshes": hostRefreshes,
       "hostDisabled": hostDisabled,
       "hostDisableDuration": hostDisableDuration,
       "hostMetrics": hostMetrics,
       "hostMemory": hostMemory,
       "hostCPU": hostCPU,
       "hostDiskSpace": hostDiskSpace,
       "hostSNMPConfigured": hostSNMPConfigured,
       "hostSNMPAgentType": hostSNMPAgentType,
       "hostSNMPAddress": hostSNMPAddress,
       "hostSNMPPort": hostSNMPPort,
       "hostSNMPRetries": hostSNMPRetries,
       "hostSNMPTimeout": hostSNMPTimeout,
       "hostSNMPVersion": hostSNMPVersion,
       "hostSNMPCommunity": hostSNMPCommunity,
       "hostIfTable": hostIfTable,
       "hostIfEntry": hostIfEntry,
       "hostIfAddr": hostIfAddr,
       "hostIfShared": hostIfShared,
       "hostIfStatus": hostIfStatus,
       "hostIfTXPackets": hostIfTXPackets,
       "hostIfRXPackets": hostIfRXPackets,
       "hostIfUpTime": hostIfUpTime,
       "hostIfAliveTime": hostIfAliveTime,
       "hostIfDataTime": hostIfDataTime,
       "hostIfPathSentTime": hostIfPathSentTime,
       "hostIfPathsSent": hostIfPathsSent,
       "hostIfPathsRcvd": hostIfPathsRcvd,
       "hostIfPathSends": hostIfPathSends,
       "hostIfPathRcvs": hostIfPathRcvs,
       "hostIfAvgPathsSentX1000": hostIfAvgPathsSentX1000,
       "hostIfAvgPathsRcvdX1000": hostIfAvgPathsRcvdX1000,
       "hostIfFctryTable": hostIfFctryTable,
       "hostIfFctryEntry": hostIfFctryEntry,
       "hostIfFctryType": hostIfFctryType,
       "hostIfFctryCount": hostIfFctryCount,
       "hostVServTable": hostVServTable,
       "hostVServEntry": hostVServEntry,
       "hostVServAddr": hostVServAddr,
       "hostVServPort": hostVServPort,
       "hostVServXlatedAddr": hostVServXlatedAddr,
       "hostVServXlatedPort": hostVServXlatedPort,
       "hostVServProbeProtocol": hostVServProbeProtocol,
       "hostVServPicks": hostVServPicks,
       "hostVServRefreshes": hostVServRefreshes,
       "hostVServAliveTime": hostVServAliveTime,
       "hostVServDataTime": hostVServDataTime,
       "hostVServDisabled": hostVServDisabled,
       "hostVServDisableDuration": hostVServDisableDuration,
       "lbDnsServs": lbDnsServs,
       "lbDnsServTable": lbDnsServTable,
       "lbDnsServEntry": lbDnsServEntry,
       "lbDnsServAddr": lbDnsServAddr,
       "lbDnsServName": lbDnsServName,
       "lbDnsServProber": lbDnsServProber,
       "lbDnsServProbeProtocol": lbDnsServProbeProtocol,
       "lbDnsServProbePort": lbDnsServProbePort,
       "lbDnsServStatus": lbDnsServStatus,
       "lbDnsServPicks": lbDnsServPicks,
       "lbDnsServRefreshes": lbDnsServRefreshes,
       "lbDnsServDisabled": lbDnsServDisabled,
       "lbDnsServDisableDuration": lbDnsServDisableDuration,
       "lbDnsServIQProto": lbDnsServIQProto,
       "lbDnsServIfTable": lbDnsServIfTable,
       "lbDnsServIfEntry": lbDnsServIfEntry,
       "lbDnsServIfAddr": lbDnsServIfAddr,
       "lbDnsServIfShared": lbDnsServIfShared,
       "lbDnsServIfStatus": lbDnsServIfStatus,
       "lbDnsServIfTXPackets": lbDnsServIfTXPackets,
       "lbDnsServIfRXPackets": lbDnsServIfRXPackets,
       "lbDnsServIfUpTime": lbDnsServIfUpTime,
       "lbDnsServIfAliveTime": lbDnsServIfAliveTime,
       "lbDnsServIfDataTime": lbDnsServIfDataTime,
       "lbDnsServIfPathSentTime": lbDnsServIfPathSentTime,
       "lbDnsServIfPathsSent": lbDnsServIfPathsSent,
       "lbDnsServIfPathsRcvd": lbDnsServIfPathsRcvd,
       "lbDnsServIfPathSends": lbDnsServIfPathSends,
       "lbDnsServIfPathRcvs": lbDnsServIfPathRcvs,
       "lbDnsServIfAvgPathsSentX1000": lbDnsServIfAvgPathsSentX1000,
       "lbDnsServIfAvgPathsRcvdX1000": lbDnsServIfAvgPathsRcvdX1000,
       "lbDnsServIfFctryTable": lbDnsServIfFctryTable,
       "lbDnsServIfFctryEntry": lbDnsServIfFctryEntry,
       "lbDnsServIfFctryType": lbDnsServIfFctryType,
       "lbDnsServIfFctryCount": lbDnsServIfFctryCount,
       "lbDomains": lbDomains,
       "lbDomainTable": lbDomainTable,
       "lbDomainEntry": lbDomainEntry,
       "lbDomainName": lbDomainName,
       "lbDomainAddr": lbDomainAddr,
       "lbDomainPort": lbDomainPort,
       "lbDomainTTL": lbDomainTTL,
       "lbDomainLBModePool": lbDomainLBModePool,
       "lbDomainQosCoeffRTT": lbDomainQosCoeffRTT,
       "lbDomainQosCoeffHops": lbDomainQosCoeffHops,
       "lbDomainQosCoeffTopology": lbDomainQosCoeffTopology,
       "lbDomainQosCoeffCompletionRate": lbDomainQosCoeffCompletionRate,
       "lbDomainQosCoeffPacketRate": lbDomainQosCoeffPacketRate,
       "lbDomainRequests": lbDomainRequests,
       "lbDomainPreferredResolves": lbDomainPreferredResolves,
       "lbDomainAlternateResolves": lbDomainAlternateResolves,
       "lbDomainFallbackResolves": lbDomainFallbackResolves,
       "lbDomainReturnsToDns": lbDomainReturnsToDns,
       "lbDomainLastResolve": lbDomainLastResolve,
       "lbDomainDisabled": lbDomainDisabled,
       "lbDomainDisableDuration": lbDomainDisableDuration,
       "lbDomainPersist": lbDomainPersist,
       "lbDomainPersistTTL": lbDomainPersistTTL,
       "lbDomainAliasTable": lbDomainAliasTable,
       "lbDomainAliasEntry": lbDomainAliasEntry,
       "lbDomainAliasIndex": lbDomainAliasIndex,
       "lbDomainAliasName": lbDomainAliasName,
       "lbDomainAliasRequests": lbDomainAliasRequests,
       "lbDomainPortTable": lbDomainPortTable,
       "lbDomainPortEntry": lbDomainPortEntry,
       "lbDomainPortPort": lbDomainPortPort,
       "lbDomainPoolTable": lbDomainPoolTable,
       "lbDomainPoolEntry": lbDomainPoolEntry,
       "lbDomainPoolIndex": lbDomainPoolIndex,
       "lbDomainPoolName": lbDomainPoolName,
       "lbDomainPoolType": lbDomainPoolType,
       "lbDomainPoolState": lbDomainPoolState,
       "lbDomainPoolVSCount": lbDomainPoolVSCount,
       "lbDomainPoolLBMode": lbDomainPoolLBMode,
       "lbDomainPoolAlternateLBMode": lbDomainPoolAlternateLBMode,
       "lbDomainPoolFallbackLBMode": lbDomainPoolFallbackLBMode,
       "lbDomainPoolCheckStaticDepends": lbDomainPoolCheckStaticDepends,
       "lbDomainPoolCheckDynamicDepends": lbDomainPoolCheckDynamicDepends,
       "lbDomainPoolRatio": lbDomainPoolRatio,
       "lbDomainPoolRipeness": lbDomainPoolRipeness,
       "lbDomainPoolPreferredResolves": lbDomainPoolPreferredResolves,
       "lbDomainPoolAlternateResolves": lbDomainPoolAlternateResolves,
       "lbDomainPoolFallbackResolves": lbDomainPoolFallbackResolves,
       "lbDomainPoolReturnsToDns": lbDomainPoolReturnsToDns,
       "lbDomainPoolRRLdns": lbDomainPoolRRLdns,
       "lbDomainPoolRRLdnsLimit": lbDomainPoolRRLdnsLimit,
       "lbDomainPoolVSTable": lbDomainPoolVSTable,
       "lbDomainPoolVSEntry": lbDomainPoolVSEntry,
       "lbDomainPoolVSAddr": lbDomainPoolVSAddr,
       "lbDomainPoolVSPort": lbDomainPoolVSPort,
       "lbDomainPoolVSRatio": lbDomainPoolVSRatio,
       "lbDomainPoolVSRipeness": lbDomainPoolVSRipeness,
       "summary": summary,
       "summaryVersion": summaryVersion,
       "summaryUpTime": summaryUpTime,
       "summaryDate": summaryDate,
       "summaryLastReload": summaryLastReload,
       "summaryLastDump": summaryLastDump,
       "summaryRequests": summaryRequests,
       "summarySyncMode": summarySyncMode,
       "summarySyncFile": summarySyncFile,
       "summarySyncIns": summarySyncIns,
       "summarySyncInErrors": summarySyncInErrors,
       "summaryLastSyncIn": summaryLastSyncIn,
       "summarySyncOuts": summarySyncOuts,
       "summarySyncOutErrors": summarySyncOutErrors,
       "summaryLastSyncOut": summaryLastSyncOut,
       "threednsTrap": threednsTrap,
       "threednsTraps": threednsTraps,
       "threednsTrapVSGreenToRed": threednsTrapVSGreenToRed,
       "threednsTrapVSRedToGreen": threednsTrapVSRedToGreen,
       "threednsTrapServerRedToGreen": threednsTrapServerRedToGreen,
       "threednsTrapServerGreenToRed": threednsTrapServerGreenToRed,
       "threednsTrapCRCFailure": threednsTrapCRCFailure}
)
