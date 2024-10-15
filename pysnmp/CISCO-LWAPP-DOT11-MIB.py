# SNMP MIB module (CISCO-LWAPP-DOT11-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-DOT11-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:11 2024
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

(CLDot11Band,
 CLDot11ChannelBandwidth) = mibBuilder.importSymbols(
    "CISCO-LWAPP-TC-MIB",
    "CLDot11Band",
    "CLDot11ChannelBandwidth")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappDot11MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612)
)
ciscoLwappDot11MIB.setRevisions(
        ("2010-05-06 00:00",
         "2007-01-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappDot11MIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappDot11MIBNotifs = _CiscoLwappDot11MIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 0)
)
_CiscoLwappDot11MIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappDot11MIBObjects = _CiscoLwappDot11MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1)
)
_CldConfig_ObjectIdentity = ObjectIdentity
cldConfig = _CldConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1)
)
_CldHtMacOperationsTable_Object = MibTable
cldHtMacOperationsTable = _CldHtMacOperationsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cldHtMacOperationsTable.setStatus("current")
_CldHtMacOperationsEntry_Object = MibTableRow
cldHtMacOperationsEntry = _CldHtMacOperationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 1, 1)
)
cldHtMacOperationsEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-MIB", "cldHtDot11nBand"),
)
if mibBuilder.loadTexts:
    cldHtMacOperationsEntry.setStatus("current")
_CldHtDot11nBand_Type = CLDot11Band
_CldHtDot11nBand_Object = MibTableColumn
cldHtDot11nBand = _CldHtDot11nBand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 1, 1, 1),
    _CldHtDot11nBand_Type()
)
cldHtDot11nBand.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldHtDot11nBand.setStatus("current")


class _CldHtDot11nChannelBandwidth_Type(CLDot11ChannelBandwidth):
    """Custom type cldHtDot11nChannelBandwidth based on CLDot11ChannelBandwidth"""


_CldHtDot11nChannelBandwidth_Object = MibTableColumn
cldHtDot11nChannelBandwidth = _CldHtDot11nChannelBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 1, 1, 2),
    _CldHtDot11nChannelBandwidth_Type()
)
cldHtDot11nChannelBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldHtDot11nChannelBandwidth.setStatus("current")


class _CldHtDot11nRifsEnable_Type(TruthValue):
    """Custom type cldHtDot11nRifsEnable based on TruthValue"""


_CldHtDot11nRifsEnable_Object = MibTableColumn
cldHtDot11nRifsEnable = _CldHtDot11nRifsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 1, 1, 3),
    _CldHtDot11nRifsEnable_Type()
)
cldHtDot11nRifsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldHtDot11nRifsEnable.setStatus("current")


class _CldHtDot11nAmsduEnable_Type(TruthValue):
    """Custom type cldHtDot11nAmsduEnable based on TruthValue"""


_CldHtDot11nAmsduEnable_Object = MibTableColumn
cldHtDot11nAmsduEnable = _CldHtDot11nAmsduEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 1, 1, 4),
    _CldHtDot11nAmsduEnable_Type()
)
cldHtDot11nAmsduEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldHtDot11nAmsduEnable.setStatus("current")


class _CldHtDot11nAmpduEnable_Type(TruthValue):
    """Custom type cldHtDot11nAmpduEnable based on TruthValue"""


_CldHtDot11nAmpduEnable_Object = MibTableColumn
cldHtDot11nAmpduEnable = _CldHtDot11nAmpduEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 1, 1, 5),
    _CldHtDot11nAmpduEnable_Type()
)
cldHtDot11nAmpduEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldHtDot11nAmpduEnable.setStatus("current")


class _CldHtDot11nGuardIntervalEnable_Type(TruthValue):
    """Custom type cldHtDot11nGuardIntervalEnable based on TruthValue"""


_CldHtDot11nGuardIntervalEnable_Object = MibTableColumn
cldHtDot11nGuardIntervalEnable = _CldHtDot11nGuardIntervalEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 1, 1, 6),
    _CldHtDot11nGuardIntervalEnable_Type()
)
cldHtDot11nGuardIntervalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldHtDot11nGuardIntervalEnable.setStatus("current")


class _CldHtDot11nEnable_Type(TruthValue):
    """Custom type cldHtDot11nEnable based on TruthValue"""


_CldHtDot11nEnable_Object = MibTableColumn
cldHtDot11nEnable = _CldHtDot11nEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 1, 1, 7),
    _CldHtDot11nEnable_Type()
)
cldHtDot11nEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldHtDot11nEnable.setStatus("current")


class _CldMultipleCountryCode_Type(SnmpAdminString):
    """Custom type cldMultipleCountryCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CldMultipleCountryCode_Type.__name__ = "SnmpAdminString"
_CldMultipleCountryCode_Object = MibScalar
cldMultipleCountryCode = _CldMultipleCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 2),
    _CldMultipleCountryCode_Type()
)
cldMultipleCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldMultipleCountryCode.setStatus("current")


class _CldRegulatoryDomain_Type(SnmpAdminString):
    """Custom type cldRegulatoryDomain based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CldRegulatoryDomain_Type.__name__ = "SnmpAdminString"
_CldRegulatoryDomain_Object = MibScalar
cldRegulatoryDomain = _CldRegulatoryDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 3),
    _CldRegulatoryDomain_Type()
)
cldRegulatoryDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldRegulatoryDomain.setStatus("current")
_Cld11nMcsTable_Object = MibTable
cld11nMcsTable = _Cld11nMcsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cld11nMcsTable.setStatus("current")
_Cld11nMcsEntry_Object = MibTableRow
cld11nMcsEntry = _Cld11nMcsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 4, 1)
)
cld11nMcsEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-MIB", "cld11nMcsBand"),
    (0, "CISCO-LWAPP-DOT11-MIB", "cld11nMcsDataRateIndex"),
)
if mibBuilder.loadTexts:
    cld11nMcsEntry.setStatus("current")
_Cld11nMcsBand_Type = CLDot11Band
_Cld11nMcsBand_Object = MibTableColumn
cld11nMcsBand = _Cld11nMcsBand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 4, 1, 1),
    _Cld11nMcsBand_Type()
)
cld11nMcsBand.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cld11nMcsBand.setStatus("current")
_Cld11nMcsDataRateIndex_Type = Unsigned32
_Cld11nMcsDataRateIndex_Object = MibTableColumn
cld11nMcsDataRateIndex = _Cld11nMcsDataRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 4, 1, 2),
    _Cld11nMcsDataRateIndex_Type()
)
cld11nMcsDataRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cld11nMcsDataRateIndex.setStatus("current")
_Cld11nMcsDataRate_Type = Unsigned32
_Cld11nMcsDataRate_Object = MibTableColumn
cld11nMcsDataRate = _Cld11nMcsDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 4, 1, 3),
    _Cld11nMcsDataRate_Type()
)
cld11nMcsDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cld11nMcsDataRate.setStatus("current")


class _Cld11nMcsSupportEnable_Type(TruthValue):
    """Custom type cld11nMcsSupportEnable based on TruthValue"""


_Cld11nMcsSupportEnable_Object = MibTableColumn
cld11nMcsSupportEnable = _Cld11nMcsSupportEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 4, 1, 4),
    _Cld11nMcsSupportEnable_Type()
)
cld11nMcsSupportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cld11nMcsSupportEnable.setStatus("current")
_Cld11nMcsChannelWidth_Type = Unsigned32
_Cld11nMcsChannelWidth_Object = MibTableColumn
cld11nMcsChannelWidth = _Cld11nMcsChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 4, 1, 5),
    _Cld11nMcsChannelWidth_Type()
)
cld11nMcsChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cld11nMcsChannelWidth.setStatus("current")
if mibBuilder.loadTexts:
    cld11nMcsChannelWidth.setUnits("MHz")
_Cld11nMcsGuardInterval_Type = Unsigned32
_Cld11nMcsGuardInterval_Object = MibTableColumn
cld11nMcsGuardInterval = _Cld11nMcsGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 4, 1, 6),
    _Cld11nMcsGuardInterval_Type()
)
cld11nMcsGuardInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cld11nMcsGuardInterval.setStatus("current")
if mibBuilder.loadTexts:
    cld11nMcsGuardInterval.setUnits("ns")


class _Cld11nMcsModulation_Type(OctetString):
    """Custom type cld11nMcsModulation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_Cld11nMcsModulation_Type.__name__ = "OctetString"
_Cld11nMcsModulation_Object = MibTableColumn
cld11nMcsModulation = _Cld11nMcsModulation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 4, 1, 7),
    _Cld11nMcsModulation_Type()
)
cld11nMcsModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cld11nMcsModulation.setStatus("current")
_Cld11acConfig_ObjectIdentity = ObjectIdentity
cld11acConfig = _Cld11acConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 5)
)


class _CldVhtDot11acEnable_Type(TruthValue):
    """Custom type cldVhtDot11acEnable based on TruthValue"""


_CldVhtDot11acEnable_Object = MibScalar
cldVhtDot11acEnable = _CldVhtDot11acEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 5, 1),
    _CldVhtDot11acEnable_Type()
)
cldVhtDot11acEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldVhtDot11acEnable.setStatus("current")
_Cld11acMcsTable_Object = MibTable
cld11acMcsTable = _Cld11acMcsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cld11acMcsTable.setStatus("current")
_Cld11acMcsEntry_Object = MibTableRow
cld11acMcsEntry = _Cld11acMcsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 6, 1)
)
cld11acMcsEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-MIB", "cld11acMcsSpatialStreamIndex"),
    (0, "CISCO-LWAPP-DOT11-MIB", "cld11acMcsDataRateIndex"),
)
if mibBuilder.loadTexts:
    cld11acMcsEntry.setStatus("current")
_Cld11acMcsSpatialStreamIndex_Type = Unsigned32
_Cld11acMcsSpatialStreamIndex_Object = MibTableColumn
cld11acMcsSpatialStreamIndex = _Cld11acMcsSpatialStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 6, 1, 1),
    _Cld11acMcsSpatialStreamIndex_Type()
)
cld11acMcsSpatialStreamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cld11acMcsSpatialStreamIndex.setStatus("current")
_Cld11acMcsDataRateIndex_Type = Unsigned32
_Cld11acMcsDataRateIndex_Object = MibTableColumn
cld11acMcsDataRateIndex = _Cld11acMcsDataRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 6, 1, 2),
    _Cld11acMcsDataRateIndex_Type()
)
cld11acMcsDataRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cld11acMcsDataRateIndex.setStatus("current")


class _Cld11acMcsSupportEnable_Type(TruthValue):
    """Custom type cld11acMcsSupportEnable based on TruthValue"""


_Cld11acMcsSupportEnable_Object = MibTableColumn
cld11acMcsSupportEnable = _Cld11acMcsSupportEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 6, 1, 3),
    _Cld11acMcsSupportEnable_Type()
)
cld11acMcsSupportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cld11acMcsSupportEnable.setStatus("current")


class _CldCountryChangeNotifEnable_Type(TruthValue):
    """Custom type cldCountryChangeNotifEnable based on TruthValue"""


_CldCountryChangeNotifEnable_Object = MibScalar
cldCountryChangeNotifEnable = _CldCountryChangeNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 7),
    _CldCountryChangeNotifEnable_Type()
)
cldCountryChangeNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldCountryChangeNotifEnable.setStatus("current")
_CldLoadBalancing_ObjectIdentity = ObjectIdentity
cldLoadBalancing = _CldLoadBalancing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 8)
)


class _CldLoadBalancingEnable_Type(Integer32):
    """Custom type cldLoadBalancingEnable based on Integer32"""
    defaultValue = 1

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


_CldLoadBalancingEnable_Type.__name__ = "Integer32"
_CldLoadBalancingEnable_Object = MibScalar
cldLoadBalancingEnable = _CldLoadBalancingEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 8, 1),
    _CldLoadBalancingEnable_Type()
)
cldLoadBalancingEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldLoadBalancingEnable.setStatus("current")


class _CldLoadBalancingWindowSize_Type(Integer32):
    """Custom type cldLoadBalancingWindowSize based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_CldLoadBalancingWindowSize_Type.__name__ = "Integer32"
_CldLoadBalancingWindowSize_Object = MibScalar
cldLoadBalancingWindowSize = _CldLoadBalancingWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 8, 2),
    _CldLoadBalancingWindowSize_Type()
)
cldLoadBalancingWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldLoadBalancingWindowSize.setStatus("current")


class _CldLoadBalancingDenialCount_Type(Integer32):
    """Custom type cldLoadBalancingDenialCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CldLoadBalancingDenialCount_Type.__name__ = "Integer32"
_CldLoadBalancingDenialCount_Object = MibScalar
cldLoadBalancingDenialCount = _CldLoadBalancingDenialCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 8, 3),
    _CldLoadBalancingDenialCount_Type()
)
cldLoadBalancingDenialCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldLoadBalancingDenialCount.setStatus("current")


class _CldLoadBalancingTrafficThreshold_Type(Unsigned32):
    """Custom type cldLoadBalancingTrafficThreshold based on Unsigned32"""
    defaultValue = 50


_CldLoadBalancingTrafficThreshold_Object = MibScalar
cldLoadBalancingTrafficThreshold = _CldLoadBalancingTrafficThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 8, 4),
    _CldLoadBalancingTrafficThreshold_Type()
)
cldLoadBalancingTrafficThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldLoadBalancingTrafficThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cldLoadBalancingTrafficThreshold.setUnits("Percent")
_CldBandSelect_ObjectIdentity = ObjectIdentity
cldBandSelect = _CldBandSelect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 9)
)


class _CldBandSelectEnable_Type(Integer32):
    """Custom type cldBandSelectEnable based on Integer32"""
    defaultValue = 1

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


_CldBandSelectEnable_Type.__name__ = "Integer32"
_CldBandSelectEnable_Object = MibScalar
cldBandSelectEnable = _CldBandSelectEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 9, 1),
    _CldBandSelectEnable_Type()
)
cldBandSelectEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldBandSelectEnable.setStatus("current")


class _CldBandSelectCycleCount_Type(Integer32):
    """Custom type cldBandSelectCycleCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CldBandSelectCycleCount_Type.__name__ = "Integer32"
_CldBandSelectCycleCount_Object = MibScalar
cldBandSelectCycleCount = _CldBandSelectCycleCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 9, 2),
    _CldBandSelectCycleCount_Type()
)
cldBandSelectCycleCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldBandSelectCycleCount.setStatus("current")


class _CldBandSelectCycleThreshold_Type(Integer32):
    """Custom type cldBandSelectCycleThreshold based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CldBandSelectCycleThreshold_Type.__name__ = "Integer32"
_CldBandSelectCycleThreshold_Object = MibScalar
cldBandSelectCycleThreshold = _CldBandSelectCycleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 9, 3),
    _CldBandSelectCycleThreshold_Type()
)
cldBandSelectCycleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldBandSelectCycleThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cldBandSelectCycleThreshold.setUnits("milliseconds")


class _CldBandSelectAgeOutSuppression_Type(Integer32):
    """Custom type cldBandSelectAgeOutSuppression based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 200),
    )


_CldBandSelectAgeOutSuppression_Type.__name__ = "Integer32"
_CldBandSelectAgeOutSuppression_Object = MibScalar
cldBandSelectAgeOutSuppression = _CldBandSelectAgeOutSuppression_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 9, 4),
    _CldBandSelectAgeOutSuppression_Type()
)
cldBandSelectAgeOutSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldBandSelectAgeOutSuppression.setStatus("current")
if mibBuilder.loadTexts:
    cldBandSelectAgeOutSuppression.setUnits("seconds")


class _CldBandSelectAgeOutDualBand_Type(Integer32):
    """Custom type cldBandSelectAgeOutDualBand based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_CldBandSelectAgeOutDualBand_Type.__name__ = "Integer32"
_CldBandSelectAgeOutDualBand_Object = MibScalar
cldBandSelectAgeOutDualBand = _CldBandSelectAgeOutDualBand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 9, 5),
    _CldBandSelectAgeOutDualBand_Type()
)
cldBandSelectAgeOutDualBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldBandSelectAgeOutDualBand.setStatus("current")
if mibBuilder.loadTexts:
    cldBandSelectAgeOutDualBand.setUnits("seconds")


class _CldBandSelectClientRssi_Type(Integer32):
    """Custom type cldBandSelectClientRssi based on Integer32"""
    defaultValue = -80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -20),
    )


_CldBandSelectClientRssi_Type.__name__ = "Integer32"
_CldBandSelectClientRssi_Object = MibScalar
cldBandSelectClientRssi = _CldBandSelectClientRssi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 1, 9, 6),
    _CldBandSelectClientRssi_Type()
)
cldBandSelectClientRssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cldBandSelectClientRssi.setStatus("current")
if mibBuilder.loadTexts:
    cldBandSelectClientRssi.setUnits("dBm")
_CldStatus_ObjectIdentity = ObjectIdentity
cldStatus = _CldStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 2)
)
_CldCountryTable_Object = MibTable
cldCountryTable = _CldCountryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cldCountryTable.setStatus("current")
_CldCountryEntry_Object = MibTableRow
cldCountryEntry = _CldCountryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 2, 1, 1)
)
cldCountryEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-MIB", "cldCountryCode"),
)
if mibBuilder.loadTexts:
    cldCountryEntry.setStatus("current")


class _CldCountryCode_Type(SnmpAdminString):
    """Custom type cldCountryCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CldCountryCode_Type.__name__ = "SnmpAdminString"
_CldCountryCode_Object = MibTableColumn
cldCountryCode = _CldCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 2, 1, 1, 1),
    _CldCountryCode_Type()
)
cldCountryCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cldCountryCode.setStatus("current")
_CldCountryName_Type = SnmpAdminString
_CldCountryName_Object = MibTableColumn
cldCountryName = _CldCountryName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 2, 1, 1, 2),
    _CldCountryName_Type()
)
cldCountryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldCountryName.setStatus("current")
_CldCountryDot11aChannels_Type = SnmpAdminString
_CldCountryDot11aChannels_Object = MibTableColumn
cldCountryDot11aChannels = _CldCountryDot11aChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 2, 1, 1, 3),
    _CldCountryDot11aChannels_Type()
)
cldCountryDot11aChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldCountryDot11aChannels.setStatus("current")
_CldCountryDot11bChannels_Type = SnmpAdminString
_CldCountryDot11bChannels_Object = MibTableColumn
cldCountryDot11bChannels = _CldCountryDot11bChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 2, 1, 1, 4),
    _CldCountryDot11bChannels_Type()
)
cldCountryDot11bChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldCountryDot11bChannels.setStatus("current")
_CldCountryDot11aDcaChannels_Type = SnmpAdminString
_CldCountryDot11aDcaChannels_Object = MibTableColumn
cldCountryDot11aDcaChannels = _CldCountryDot11aDcaChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 2, 1, 1, 5),
    _CldCountryDot11aDcaChannels_Type()
)
cldCountryDot11aDcaChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldCountryDot11aDcaChannels.setStatus("current")
_CldCountryDot11bDcaChannels_Type = SnmpAdminString
_CldCountryDot11bDcaChannels_Object = MibTableColumn
cldCountryDot11bDcaChannels = _CldCountryDot11bDcaChannels_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 1, 2, 1, 1, 6),
    _CldCountryDot11bDcaChannels_Type()
)
cldCountryDot11bDcaChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cldCountryDot11bDcaChannels.setStatus("current")
_CiscoLwappDot11MIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappDot11MIBConform = _CiscoLwappDot11MIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 2)
)
_CiscoLwappDot11MIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappDot11MIBCompliances = _CiscoLwappDot11MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 2, 1)
)
_CiscoLwappDot11MIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappDot11MIBGroups = _CiscoLwappDot11MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 2, 2)
)

# Managed Objects groups

ciscoLwappDot11MIBMacOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 2, 2, 1)
)
ciscoLwappDot11MIBMacOperGroup.setObjects(
      *(("CISCO-LWAPP-DOT11-MIB", "cldHtDot11nChannelBandwidth"),
        ("CISCO-LWAPP-DOT11-MIB", "cldHtDot11nRifsEnable"),
        ("CISCO-LWAPP-DOT11-MIB", "cldHtDot11nAmsduEnable"),
        ("CISCO-LWAPP-DOT11-MIB", "cldHtDot11nAmpduEnable"),
        ("CISCO-LWAPP-DOT11-MIB", "cldHtDot11nGuardIntervalEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11MIBMacOperGroup.setStatus("current")

ciscoLwappDot11MIBConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 2, 2, 2)
)
ciscoLwappDot11MIBConfigGroup.setObjects(
      *(("CISCO-LWAPP-DOT11-MIB", "cldHtDot11nEnable"),
        ("CISCO-LWAPP-DOT11-MIB", "cldMultipleCountryCode"),
        ("CISCO-LWAPP-DOT11-MIB", "cldRegulatoryDomain"),
        ("CISCO-LWAPP-DOT11-MIB", "cld11nMcsDataRate"),
        ("CISCO-LWAPP-DOT11-MIB", "cld11nMcsSupportEnable"),
        ("CISCO-LWAPP-DOT11-MIB", "cldCountryChangeNotifEnable"),
        ("CISCO-LWAPP-DOT11-MIB", "cldLoadBalancingEnable"),
        ("CISCO-LWAPP-DOT11-MIB", "cldLoadBalancingWindowSize"),
        ("CISCO-LWAPP-DOT11-MIB", "cldLoadBalancingDenialCount"),
        ("CISCO-LWAPP-DOT11-MIB", "cldBandSelectEnable"),
        ("CISCO-LWAPP-DOT11-MIB", "cldBandSelectCycleCount"),
        ("CISCO-LWAPP-DOT11-MIB", "cldBandSelectCycleThreshold"),
        ("CISCO-LWAPP-DOT11-MIB", "cldBandSelectAgeOutSuppression"),
        ("CISCO-LWAPP-DOT11-MIB", "cldBandSelectAgeOutDualBand"),
        ("CISCO-LWAPP-DOT11-MIB", "cldBandSelectClientRssi"),
        ("CISCO-LWAPP-DOT11-MIB", "cld11nMcsChannelWidth"),
        ("CISCO-LWAPP-DOT11-MIB", "cld11nMcsGuardInterval"),
        ("CISCO-LWAPP-DOT11-MIB", "cld11nMcsModulation"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11MIBConfigGroup.setStatus("current")

ciscoLwappDot11MIBStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 2, 2, 4)
)
ciscoLwappDot11MIBStatusGroup.setObjects(
      *(("CISCO-LWAPP-DOT11-MIB", "cldCountryName"),
        ("CISCO-LWAPP-DOT11-MIB", "cldCountryDot11aChannels"),
        ("CISCO-LWAPP-DOT11-MIB", "cldCountryDot11bChannels"),
        ("CISCO-LWAPP-DOT11-MIB", "cldCountryDot11aDcaChannels"),
        ("CISCO-LWAPP-DOT11-MIB", "cldCountryDot11bDcaChannels"))
)
if mibBuilder.loadTexts:
    ciscoLwappDot11MIBStatusGroup.setStatus("current")


# Notification objects

ciscoLwappDot11CountryChangeNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 0, 1)
)
ciscoLwappDot11CountryChangeNotif.setObjects(
    ("CISCO-LWAPP-DOT11-MIB", "cldMultipleCountryCode")
)
if mibBuilder.loadTexts:
    ciscoLwappDot11CountryChangeNotif.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappDot11MIBNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 2, 2, 3)
)
ciscoLwappDot11MIBNotifsGroup.setObjects(
    ("CISCO-LWAPP-DOT11-MIB", "ciscoLwappDot11CountryChangeNotif")
)
if mibBuilder.loadTexts:
    ciscoLwappDot11MIBNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappDot11MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappDot11MIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappDot11MIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 612, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappDot11MIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-DOT11-MIB",
    **{"ciscoLwappDot11MIB": ciscoLwappDot11MIB,
       "ciscoLwappDot11MIBNotifs": ciscoLwappDot11MIBNotifs,
       "ciscoLwappDot11CountryChangeNotif": ciscoLwappDot11CountryChangeNotif,
       "ciscoLwappDot11MIBObjects": ciscoLwappDot11MIBObjects,
       "cldConfig": cldConfig,
       "cldHtMacOperationsTable": cldHtMacOperationsTable,
       "cldHtMacOperationsEntry": cldHtMacOperationsEntry,
       "cldHtDot11nBand": cldHtDot11nBand,
       "cldHtDot11nChannelBandwidth": cldHtDot11nChannelBandwidth,
       "cldHtDot11nRifsEnable": cldHtDot11nRifsEnable,
       "cldHtDot11nAmsduEnable": cldHtDot11nAmsduEnable,
       "cldHtDot11nAmpduEnable": cldHtDot11nAmpduEnable,
       "cldHtDot11nGuardIntervalEnable": cldHtDot11nGuardIntervalEnable,
       "cldHtDot11nEnable": cldHtDot11nEnable,
       "cldMultipleCountryCode": cldMultipleCountryCode,
       "cldRegulatoryDomain": cldRegulatoryDomain,
       "cld11nMcsTable": cld11nMcsTable,
       "cld11nMcsEntry": cld11nMcsEntry,
       "cld11nMcsBand": cld11nMcsBand,
       "cld11nMcsDataRateIndex": cld11nMcsDataRateIndex,
       "cld11nMcsDataRate": cld11nMcsDataRate,
       "cld11nMcsSupportEnable": cld11nMcsSupportEnable,
       "cld11nMcsChannelWidth": cld11nMcsChannelWidth,
       "cld11nMcsGuardInterval": cld11nMcsGuardInterval,
       "cld11nMcsModulation": cld11nMcsModulation,
       "cld11acConfig": cld11acConfig,
       "cldVhtDot11acEnable": cldVhtDot11acEnable,
       "cld11acMcsTable": cld11acMcsTable,
       "cld11acMcsEntry": cld11acMcsEntry,
       "cld11acMcsSpatialStreamIndex": cld11acMcsSpatialStreamIndex,
       "cld11acMcsDataRateIndex": cld11acMcsDataRateIndex,
       "cld11acMcsSupportEnable": cld11acMcsSupportEnable,
       "cldCountryChangeNotifEnable": cldCountryChangeNotifEnable,
       "cldLoadBalancing": cldLoadBalancing,
       "cldLoadBalancingEnable": cldLoadBalancingEnable,
       "cldLoadBalancingWindowSize": cldLoadBalancingWindowSize,
       "cldLoadBalancingDenialCount": cldLoadBalancingDenialCount,
       "cldLoadBalancingTrafficThreshold": cldLoadBalancingTrafficThreshold,
       "cldBandSelect": cldBandSelect,
       "cldBandSelectEnable": cldBandSelectEnable,
       "cldBandSelectCycleCount": cldBandSelectCycleCount,
       "cldBandSelectCycleThreshold": cldBandSelectCycleThreshold,
       "cldBandSelectAgeOutSuppression": cldBandSelectAgeOutSuppression,
       "cldBandSelectAgeOutDualBand": cldBandSelectAgeOutDualBand,
       "cldBandSelectClientRssi": cldBandSelectClientRssi,
       "cldStatus": cldStatus,
       "cldCountryTable": cldCountryTable,
       "cldCountryEntry": cldCountryEntry,
       "cldCountryCode": cldCountryCode,
       "cldCountryName": cldCountryName,
       "cldCountryDot11aChannels": cldCountryDot11aChannels,
       "cldCountryDot11bChannels": cldCountryDot11bChannels,
       "cldCountryDot11aDcaChannels": cldCountryDot11aDcaChannels,
       "cldCountryDot11bDcaChannels": cldCountryDot11bDcaChannels,
       "ciscoLwappDot11MIBConform": ciscoLwappDot11MIBConform,
       "ciscoLwappDot11MIBCompliances": ciscoLwappDot11MIBCompliances,
       "ciscoLwappDot11MIBCompliance": ciscoLwappDot11MIBCompliance,
       "ciscoLwappDot11MIBComplianceRev1": ciscoLwappDot11MIBComplianceRev1,
       "ciscoLwappDot11MIBGroups": ciscoLwappDot11MIBGroups,
       "ciscoLwappDot11MIBMacOperGroup": ciscoLwappDot11MIBMacOperGroup,
       "ciscoLwappDot11MIBConfigGroup": ciscoLwappDot11MIBConfigGroup,
       "ciscoLwappDot11MIBNotifsGroup": ciscoLwappDot11MIBNotifsGroup,
       "ciscoLwappDot11MIBStatusGroup": ciscoLwappDot11MIBStatusGroup}
)
