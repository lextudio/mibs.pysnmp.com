# SNMP MIB module (RADLAN-CDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-CDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:41:53 2024
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

(cdpCacheDeviceIndex,
 cdpCacheEntry,
 cdpCacheIfIndex) = mibBuilder.importSymbols(
    "CISCO-CDP-MIB",
    "cdpCacheDeviceIndex",
    "cdpCacheEntry",
    "cdpCacheIfIndex")

(CiscoNetworkAddress,
 CiscoNetworkProtocol) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoNetworkAddress",
    "CiscoNetworkProtocol")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId")

(rndErrorDesc,
 rndErrorSeverity) = mibBuilder.importSymbols(
    "RADLAN-DEVICEPARAMS-MIB",
    "rndErrorDesc",
    "rndErrorSeverity")

(rnd,
 rndNotifications) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd",
    "rndNotifications")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlCdp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 137)
)
rlCdp.setRevisions(
        ("2008-09-14 00:00",
         "2010-08-11 00:00",
         "2010-10-25 00:00",
         "2010-11-10 00:00",
         "2010-11-14 00:00",
         "2011-01-09 00:00",
         "2011-02-15 00:00",
         "2012-02-14 00:00",
         "2015-03-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlCdpVersionTypes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version-v1", 1),
          ("version-v2", 2))
    )



class RlCdpCounterTypes(Integer32, TextualConvention):
    status = "current"
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
        *(("errorPackets", 8),
          ("illegalChksum", 7),
          ("maxNeighborsExceededInMainCache", 9),
          ("maxNeighborsExceededInSecondaryCache", 10),
          ("totalInputPackets", 1),
          ("totalOutputPackets", 4),
          ("v1InputPackets", 2),
          ("v1OutputPackets", 5),
          ("v2InputPackets", 3),
          ("v2OutputPackets", 6))
    )



class RlCdpPduActionTypes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bridging", 2),
          ("filtering", 1),
          ("flooding", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RlCdpVersionAdvertised_Type = RlCdpVersionTypes
_RlCdpVersionAdvertised_Object = MibScalar
rlCdpVersionAdvertised = _RlCdpVersionAdvertised_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 1),
    _RlCdpVersionAdvertised_Type()
)
rlCdpVersionAdvertised.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCdpVersionAdvertised.setStatus("current")


class _RlCdpSourceInterface_Type(InterfaceIndexOrZero):
    """Custom type rlCdpSourceInterface based on InterfaceIndexOrZero"""
    defaultValue = 0


_RlCdpSourceInterface_Object = MibScalar
rlCdpSourceInterface = _RlCdpSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 2),
    _RlCdpSourceInterface_Type()
)
rlCdpSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCdpSourceInterface.setStatus("current")
_RlCdpLogMismatchDuplexEnable_Type = PortList
_RlCdpLogMismatchDuplexEnable_Object = MibScalar
rlCdpLogMismatchDuplexEnable = _RlCdpLogMismatchDuplexEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 3),
    _RlCdpLogMismatchDuplexEnable_Type()
)
rlCdpLogMismatchDuplexEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCdpLogMismatchDuplexEnable.setStatus("current")
_RlCdpCountersTable_Object = MibTable
rlCdpCountersTable = _RlCdpCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 4)
)
if mibBuilder.loadTexts:
    rlCdpCountersTable.setStatus("current")
_RlCdpCountersEntry_Object = MibTableRow
rlCdpCountersEntry = _RlCdpCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 4, 1)
)
rlCdpCountersEntry.setIndexNames(
    (0, "RADLAN-CDP-MIB", "rlCdpCountersName"),
)
if mibBuilder.loadTexts:
    rlCdpCountersEntry.setStatus("current")
_RlCdpCountersName_Type = RlCdpCounterTypes
_RlCdpCountersName_Object = MibTableColumn
rlCdpCountersName = _RlCdpCountersName_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 4, 1, 1),
    _RlCdpCountersName_Type()
)
rlCdpCountersName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlCdpCountersName.setStatus("current")
_RlCdpCountersValue_Type = Counter32
_RlCdpCountersValue_Object = MibTableColumn
rlCdpCountersValue = _RlCdpCountersValue_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 4, 1, 2),
    _RlCdpCountersValue_Type()
)
rlCdpCountersValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpCountersValue.setStatus("current")
_RlCdpCountersClear_Type = TruthValue
_RlCdpCountersClear_Object = MibScalar
rlCdpCountersClear = _RlCdpCountersClear_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 5),
    _RlCdpCountersClear_Type()
)
rlCdpCountersClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCdpCountersClear.setStatus("current")
_RlCdpCacheClear_Type = TruthValue
_RlCdpCacheClear_Object = MibScalar
rlCdpCacheClear = _RlCdpCacheClear_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 6),
    _RlCdpCacheClear_Type()
)
rlCdpCacheClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCdpCacheClear.setStatus("current")


class _RlCdpVoiceVlanId_Type(Integer32):
    """Custom type rlCdpVoiceVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_RlCdpVoiceVlanId_Type.__name__ = "Integer32"
_RlCdpVoiceVlanId_Object = MibScalar
rlCdpVoiceVlanId = _RlCdpVoiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 7),
    _RlCdpVoiceVlanId_Type()
)
rlCdpVoiceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCdpVoiceVlanId.setStatus("obsolete")
_RlCdpCacheTable_Object = MibTable
rlCdpCacheTable = _RlCdpCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 8)
)
if mibBuilder.loadTexts:
    rlCdpCacheTable.setStatus("current")
_RlCdpCacheEntry_Object = MibTableRow
rlCdpCacheEntry = _RlCdpCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 8, 1)
)
if mibBuilder.loadTexts:
    rlCdpCacheEntry.setStatus("current")
_RlCdpCacheVersionExt_Type = DisplayString
_RlCdpCacheVersionExt_Object = MibTableColumn
rlCdpCacheVersionExt = _RlCdpCacheVersionExt_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 8, 1, 1),
    _RlCdpCacheVersionExt_Type()
)
rlCdpCacheVersionExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpCacheVersionExt.setStatus("current")
_RlCdpCacheTimeToLive_Type = Integer32
_RlCdpCacheTimeToLive_Object = MibTableColumn
rlCdpCacheTimeToLive = _RlCdpCacheTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 8, 1, 2),
    _RlCdpCacheTimeToLive_Type()
)
rlCdpCacheTimeToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpCacheTimeToLive.setStatus("current")
_RlCdpCacheCdpVersion_Type = RlCdpVersionTypes
_RlCdpCacheCdpVersion_Object = MibTableColumn
rlCdpCacheCdpVersion = _RlCdpCacheCdpVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 8, 1, 3),
    _RlCdpCacheCdpVersion_Type()
)
rlCdpCacheCdpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpCacheCdpVersion.setStatus("current")


class _RlCdpPduAction_Type(RlCdpPduActionTypes):
    """Custom type rlCdpPduAction based on RlCdpPduActionTypes"""


_RlCdpPduAction_Object = MibScalar
rlCdpPduAction = _RlCdpPduAction_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 9),
    _RlCdpPduAction_Type()
)
rlCdpPduAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCdpPduAction.setStatus("current")
_RlCdpLogMismatchVoiceVlanEnable_Type = PortList
_RlCdpLogMismatchVoiceVlanEnable_Object = MibScalar
rlCdpLogMismatchVoiceVlanEnable = _RlCdpLogMismatchVoiceVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 10),
    _RlCdpLogMismatchVoiceVlanEnable_Type()
)
rlCdpLogMismatchVoiceVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCdpLogMismatchVoiceVlanEnable.setStatus("current")
_RlCdpLogMismatchNativeVlanEnable_Type = PortList
_RlCdpLogMismatchNativeVlanEnable_Object = MibScalar
rlCdpLogMismatchNativeVlanEnable = _RlCdpLogMismatchNativeVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 11),
    _RlCdpLogMismatchNativeVlanEnable_Type()
)
rlCdpLogMismatchNativeVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCdpLogMismatchNativeVlanEnable.setStatus("current")
_RlCdpSecondaryCacheTable_Object = MibTable
rlCdpSecondaryCacheTable = _RlCdpSecondaryCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 12)
)
if mibBuilder.loadTexts:
    rlCdpSecondaryCacheTable.setStatus("current")
_RlCdpSecondaryCacheEntry_Object = MibTableRow
rlCdpSecondaryCacheEntry = _RlCdpSecondaryCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 12, 1)
)
rlCdpSecondaryCacheEntry.setIndexNames(
    (0, "CISCO-CDP-MIB", "cdpCacheIfIndex"),
    (0, "CISCO-CDP-MIB", "cdpCacheDeviceIndex"),
)
if mibBuilder.loadTexts:
    rlCdpSecondaryCacheEntry.setStatus("current")
_RlCdpSecondaryCacheMacAddress_Type = MacAddress
_RlCdpSecondaryCacheMacAddress_Object = MibTableColumn
rlCdpSecondaryCacheMacAddress = _RlCdpSecondaryCacheMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 12, 1, 3),
    _RlCdpSecondaryCacheMacAddress_Type()
)
rlCdpSecondaryCacheMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpSecondaryCacheMacAddress.setStatus("current")
_RlCdpSecondaryCachePlatform_Type = DisplayString
_RlCdpSecondaryCachePlatform_Object = MibTableColumn
rlCdpSecondaryCachePlatform = _RlCdpSecondaryCachePlatform_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 12, 1, 4),
    _RlCdpSecondaryCachePlatform_Type()
)
rlCdpSecondaryCachePlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpSecondaryCachePlatform.setStatus("current")


class _RlCdpSecondaryCacheCapabilities_Type(OctetString):
    """Custom type rlCdpSecondaryCacheCapabilities based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_RlCdpSecondaryCacheCapabilities_Type.__name__ = "OctetString"
_RlCdpSecondaryCacheCapabilities_Object = MibTableColumn
rlCdpSecondaryCacheCapabilities = _RlCdpSecondaryCacheCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 12, 1, 5),
    _RlCdpSecondaryCacheCapabilities_Type()
)
rlCdpSecondaryCacheCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpSecondaryCacheCapabilities.setStatus("current")


class _RlCdpSecondaryCacheVoiceVlanID_Type(Unsigned32):
    """Custom type rlCdpSecondaryCacheVoiceVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RlCdpSecondaryCacheVoiceVlanID_Type.__name__ = "Unsigned32"
_RlCdpSecondaryCacheVoiceVlanID_Object = MibTableColumn
rlCdpSecondaryCacheVoiceVlanID = _RlCdpSecondaryCacheVoiceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 12, 1, 6),
    _RlCdpSecondaryCacheVoiceVlanID_Type()
)
rlCdpSecondaryCacheVoiceVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpSecondaryCacheVoiceVlanID.setStatus("current")
_RlCdpSecondaryCacheTimeToLive_Type = Integer32
_RlCdpSecondaryCacheTimeToLive_Object = MibTableColumn
rlCdpSecondaryCacheTimeToLive = _RlCdpSecondaryCacheTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 12, 1, 7),
    _RlCdpSecondaryCacheTimeToLive_Type()
)
rlCdpSecondaryCacheTimeToLive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpSecondaryCacheTimeToLive.setStatus("current")
_RlCdpSecondaryCachePowerAvailable_Type = Unsigned32
_RlCdpSecondaryCachePowerAvailable_Object = MibTableColumn
rlCdpSecondaryCachePowerAvailable = _RlCdpSecondaryCachePowerAvailable_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 12, 1, 8),
    _RlCdpSecondaryCachePowerAvailable_Type()
)
rlCdpSecondaryCachePowerAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpSecondaryCachePowerAvailable.setStatus("current")
_RlCdpSecondaryCachePowerConsumption_Type = Unsigned32
_RlCdpSecondaryCachePowerConsumption_Object = MibTableColumn
rlCdpSecondaryCachePowerConsumption = _RlCdpSecondaryCachePowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 12, 1, 9),
    _RlCdpSecondaryCachePowerConsumption_Type()
)
rlCdpSecondaryCachePowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpSecondaryCachePowerConsumption.setStatus("current")


class _RlCdpSecondaryCacheSparePairPoECapabilities_Type(Bits):
    """Custom type rlCdpSecondaryCacheSparePairPoECapabilities based on Bits"""
    namedValues = NamedValues(
        *(("desiredState", 2),
          ("detectionClassificationRequired", 1),
          ("operationalState", 3),
          ("supported", 0))
    )

_RlCdpSecondaryCacheSparePairPoECapabilities_Type.__name__ = "Bits"
_RlCdpSecondaryCacheSparePairPoECapabilities_Object = MibTableColumn
rlCdpSecondaryCacheSparePairPoECapabilities = _RlCdpSecondaryCacheSparePairPoECapabilities_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 12, 1, 10),
    _RlCdpSecondaryCacheSparePairPoECapabilities_Type()
)
rlCdpSecondaryCacheSparePairPoECapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpSecondaryCacheSparePairPoECapabilities.setStatus("current")
_RlCdpSecondaryCacheDeviceId_Type = DisplayString
_RlCdpSecondaryCacheDeviceId_Object = MibTableColumn
rlCdpSecondaryCacheDeviceId = _RlCdpSecondaryCacheDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 12, 1, 11),
    _RlCdpSecondaryCacheDeviceId_Type()
)
rlCdpSecondaryCacheDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpSecondaryCacheDeviceId.setStatus("current")
_RlCdpSecondaryCachePortId_Type = DisplayString
_RlCdpSecondaryCachePortId_Object = MibTableColumn
rlCdpSecondaryCachePortId = _RlCdpSecondaryCachePortId_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 12, 1, 12),
    _RlCdpSecondaryCachePortId_Type()
)
rlCdpSecondaryCachePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpSecondaryCachePortId.setStatus("current")


class _RlCdpGlobalLogMismatchDuplexEnable_Type(TruthValue):
    """Custom type rlCdpGlobalLogMismatchDuplexEnable based on TruthValue"""


_RlCdpGlobalLogMismatchDuplexEnable_Object = MibScalar
rlCdpGlobalLogMismatchDuplexEnable = _RlCdpGlobalLogMismatchDuplexEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 13),
    _RlCdpGlobalLogMismatchDuplexEnable_Type()
)
rlCdpGlobalLogMismatchDuplexEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCdpGlobalLogMismatchDuplexEnable.setStatus("current")


class _RlCdpGlobalLogMismatchVoiceVlanEnable_Type(TruthValue):
    """Custom type rlCdpGlobalLogMismatchVoiceVlanEnable based on TruthValue"""


_RlCdpGlobalLogMismatchVoiceVlanEnable_Object = MibScalar
rlCdpGlobalLogMismatchVoiceVlanEnable = _RlCdpGlobalLogMismatchVoiceVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 14),
    _RlCdpGlobalLogMismatchVoiceVlanEnable_Type()
)
rlCdpGlobalLogMismatchVoiceVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCdpGlobalLogMismatchVoiceVlanEnable.setStatus("current")


class _RlCdpGlobalLogMismatchNativeVlanEnable_Type(TruthValue):
    """Custom type rlCdpGlobalLogMismatchNativeVlanEnable based on TruthValue"""


_RlCdpGlobalLogMismatchNativeVlanEnable_Object = MibScalar
rlCdpGlobalLogMismatchNativeVlanEnable = _RlCdpGlobalLogMismatchNativeVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 15),
    _RlCdpGlobalLogMismatchNativeVlanEnable_Type()
)
rlCdpGlobalLogMismatchNativeVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCdpGlobalLogMismatchNativeVlanEnable.setStatus("current")
_RlCdpTlvTable_Object = MibTable
rlCdpTlvTable = _RlCdpTlvTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16)
)
if mibBuilder.loadTexts:
    rlCdpTlvTable.setStatus("current")
_RlCdpTlvEntry_Object = MibTableRow
rlCdpTlvEntry = _RlCdpTlvEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1)
)
rlCdpTlvEntry.setIndexNames(
    (0, "RADLAN-CDP-MIB", "rlCdpTlvIfIndex"),
)
if mibBuilder.loadTexts:
    rlCdpTlvEntry.setStatus("current")


class _RlCdpTlvIfIndex_Type(Unsigned32):
    """Custom type rlCdpTlvIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlCdpTlvIfIndex_Type.__name__ = "Unsigned32"
_RlCdpTlvIfIndex_Object = MibTableColumn
rlCdpTlvIfIndex = _RlCdpTlvIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 1),
    _RlCdpTlvIfIndex_Type()
)
rlCdpTlvIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlCdpTlvIfIndex.setStatus("current")


class _RlCdpTlvDeviceIdFormat_Type(Integer32):
    """Custom type rlCdpTlvDeviceIdFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("macAddress", 2),
          ("other", 3),
          ("serialNumber", 1))
    )


_RlCdpTlvDeviceIdFormat_Type.__name__ = "Integer32"
_RlCdpTlvDeviceIdFormat_Object = MibTableColumn
rlCdpTlvDeviceIdFormat = _RlCdpTlvDeviceIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 2),
    _RlCdpTlvDeviceIdFormat_Type()
)
rlCdpTlvDeviceIdFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvDeviceIdFormat.setStatus("current")
_RlCdpTlvDeviceId_Type = DisplayString
_RlCdpTlvDeviceId_Object = MibTableColumn
rlCdpTlvDeviceId = _RlCdpTlvDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 3),
    _RlCdpTlvDeviceId_Type()
)
rlCdpTlvDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvDeviceId.setStatus("current")
_RlCdpTlvAddress1Type_Type = InetAddressType
_RlCdpTlvAddress1Type_Object = MibTableColumn
rlCdpTlvAddress1Type = _RlCdpTlvAddress1Type_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 4),
    _RlCdpTlvAddress1Type_Type()
)
rlCdpTlvAddress1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvAddress1Type.setStatus("current")
_RlCdpTlvAddress1_Type = InetAddress
_RlCdpTlvAddress1_Object = MibTableColumn
rlCdpTlvAddress1 = _RlCdpTlvAddress1_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 5),
    _RlCdpTlvAddress1_Type()
)
rlCdpTlvAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvAddress1.setStatus("current")
_RlCdpTlvAddress2Type_Type = InetAddressType
_RlCdpTlvAddress2Type_Object = MibTableColumn
rlCdpTlvAddress2Type = _RlCdpTlvAddress2Type_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 6),
    _RlCdpTlvAddress2Type_Type()
)
rlCdpTlvAddress2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvAddress2Type.setStatus("current")
_RlCdpTlvAddress2_Type = InetAddress
_RlCdpTlvAddress2_Object = MibTableColumn
rlCdpTlvAddress2 = _RlCdpTlvAddress2_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 7),
    _RlCdpTlvAddress2_Type()
)
rlCdpTlvAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvAddress2.setStatus("current")
_RlCdpTlvAddress3Type_Type = InetAddressType
_RlCdpTlvAddress3Type_Object = MibTableColumn
rlCdpTlvAddress3Type = _RlCdpTlvAddress3Type_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 8),
    _RlCdpTlvAddress3Type_Type()
)
rlCdpTlvAddress3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvAddress3Type.setStatus("current")
_RlCdpTlvAddress3_Type = InetAddress
_RlCdpTlvAddress3_Object = MibTableColumn
rlCdpTlvAddress3 = _RlCdpTlvAddress3_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 9),
    _RlCdpTlvAddress3_Type()
)
rlCdpTlvAddress3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvAddress3.setStatus("current")
_RlCdpTlvPortId_Type = DisplayString
_RlCdpTlvPortId_Object = MibTableColumn
rlCdpTlvPortId = _RlCdpTlvPortId_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 10),
    _RlCdpTlvPortId_Type()
)
rlCdpTlvPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvPortId.setStatus("current")


class _RlCdpTlvCapabilities_Type(OctetString):
    """Custom type rlCdpTlvCapabilities based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_RlCdpTlvCapabilities_Type.__name__ = "OctetString"
_RlCdpTlvCapabilities_Object = MibTableColumn
rlCdpTlvCapabilities = _RlCdpTlvCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 11),
    _RlCdpTlvCapabilities_Type()
)
rlCdpTlvCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvCapabilities.setStatus("current")
_RlCdpTlvVersion_Type = DisplayString
_RlCdpTlvVersion_Object = MibTableColumn
rlCdpTlvVersion = _RlCdpTlvVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 12),
    _RlCdpTlvVersion_Type()
)
rlCdpTlvVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvVersion.setStatus("current")
_RlCdpTlvPlatform_Type = DisplayString
_RlCdpTlvPlatform_Object = MibTableColumn
rlCdpTlvPlatform = _RlCdpTlvPlatform_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 13),
    _RlCdpTlvPlatform_Type()
)
rlCdpTlvPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvPlatform.setStatus("current")


class _RlCdpTlvNativeVLAN_Type(Unsigned32):
    """Custom type rlCdpTlvNativeVLAN based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RlCdpTlvNativeVLAN_Type.__name__ = "Unsigned32"
_RlCdpTlvNativeVLAN_Object = MibTableColumn
rlCdpTlvNativeVLAN = _RlCdpTlvNativeVLAN_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 14),
    _RlCdpTlvNativeVLAN_Type()
)
rlCdpTlvNativeVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvNativeVLAN.setStatus("current")


class _RlCdpTlvDuplex_Type(Integer32):
    """Custom type rlCdpTlvDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullduplex", 3),
          ("halfduplex", 2),
          ("unknown", 1))
    )


_RlCdpTlvDuplex_Type.__name__ = "Integer32"
_RlCdpTlvDuplex_Object = MibTableColumn
rlCdpTlvDuplex = _RlCdpTlvDuplex_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 15),
    _RlCdpTlvDuplex_Type()
)
rlCdpTlvDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvDuplex.setStatus("current")


class _RlCdpTlvApplianceID_Type(Unsigned32):
    """Custom type rlCdpTlvApplianceID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlCdpTlvApplianceID_Type.__name__ = "Unsigned32"
_RlCdpTlvApplianceID_Object = MibTableColumn
rlCdpTlvApplianceID = _RlCdpTlvApplianceID_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 16),
    _RlCdpTlvApplianceID_Type()
)
rlCdpTlvApplianceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvApplianceID.setStatus("current")


class _RlCdpTlvApplianceVlanID_Type(Unsigned32):
    """Custom type rlCdpTlvApplianceVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_RlCdpTlvApplianceVlanID_Type.__name__ = "Unsigned32"
_RlCdpTlvApplianceVlanID_Object = MibTableColumn
rlCdpTlvApplianceVlanID = _RlCdpTlvApplianceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 17),
    _RlCdpTlvApplianceVlanID_Type()
)
rlCdpTlvApplianceVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvApplianceVlanID.setStatus("current")


class _RlCdpTlvExtendedTrust_Type(Integer32):
    """Custom type rlCdpTlvExtendedTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("untrusted", 0))
    )


_RlCdpTlvExtendedTrust_Type.__name__ = "Integer32"
_RlCdpTlvExtendedTrust_Object = MibTableColumn
rlCdpTlvExtendedTrust = _RlCdpTlvExtendedTrust_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 18),
    _RlCdpTlvExtendedTrust_Type()
)
rlCdpTlvExtendedTrust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvExtendedTrust.setStatus("current")


class _RlCdpTlvCosForUntrustedPorts_Type(Unsigned32):
    """Custom type rlCdpTlvCosForUntrustedPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlCdpTlvCosForUntrustedPorts_Type.__name__ = "Unsigned32"
_RlCdpTlvCosForUntrustedPorts_Object = MibTableColumn
rlCdpTlvCosForUntrustedPorts = _RlCdpTlvCosForUntrustedPorts_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 19),
    _RlCdpTlvCosForUntrustedPorts_Type()
)
rlCdpTlvCosForUntrustedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvCosForUntrustedPorts.setStatus("current")


class _RlCdpTlvPowerAvailableRequestId_Type(Unsigned32):
    """Custom type rlCdpTlvPowerAvailableRequestId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RlCdpTlvPowerAvailableRequestId_Type.__name__ = "Unsigned32"
_RlCdpTlvPowerAvailableRequestId_Object = MibTableColumn
rlCdpTlvPowerAvailableRequestId = _RlCdpTlvPowerAvailableRequestId_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 20),
    _RlCdpTlvPowerAvailableRequestId_Type()
)
rlCdpTlvPowerAvailableRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvPowerAvailableRequestId.setStatus("current")


class _RlCdpTlvPowerAvailablePowerManagementId_Type(Unsigned32):
    """Custom type rlCdpTlvPowerAvailablePowerManagementId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RlCdpTlvPowerAvailablePowerManagementId_Type.__name__ = "Unsigned32"
_RlCdpTlvPowerAvailablePowerManagementId_Object = MibTableColumn
rlCdpTlvPowerAvailablePowerManagementId = _RlCdpTlvPowerAvailablePowerManagementId_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 21),
    _RlCdpTlvPowerAvailablePowerManagementId_Type()
)
rlCdpTlvPowerAvailablePowerManagementId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvPowerAvailablePowerManagementId.setStatus("current")
_RlCdpTlvPowerAvailable_Type = Unsigned32
_RlCdpTlvPowerAvailable_Object = MibTableColumn
rlCdpTlvPowerAvailable = _RlCdpTlvPowerAvailable_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 22),
    _RlCdpTlvPowerAvailable_Type()
)
rlCdpTlvPowerAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvPowerAvailable.setStatus("current")
_RlCdpTlvPowerAvailableManagementPowerLevel_Type = Unsigned32
_RlCdpTlvPowerAvailableManagementPowerLevel_Object = MibTableColumn
rlCdpTlvPowerAvailableManagementPowerLevel = _RlCdpTlvPowerAvailableManagementPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 23),
    _RlCdpTlvPowerAvailableManagementPowerLevel_Type()
)
rlCdpTlvPowerAvailableManagementPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvPowerAvailableManagementPowerLevel.setStatus("current")
_RlCdpTlvSysName_Type = DisplayString
_RlCdpTlvSysName_Object = MibTableColumn
rlCdpTlvSysName = _RlCdpTlvSysName_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 24),
    _RlCdpTlvSysName_Type()
)
rlCdpTlvSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvSysName.setStatus("current")
_RlCdpTlvPowerConsumption_Type = Unsigned32
_RlCdpTlvPowerConsumption_Object = MibTableColumn
rlCdpTlvPowerConsumption = _RlCdpTlvPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 25),
    _RlCdpTlvPowerConsumption_Type()
)
rlCdpTlvPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvPowerConsumption.setStatus("current")
_RlCdpTlvPowerRequestedRequestId_Type = Unsigned32
_RlCdpTlvPowerRequestedRequestId_Object = MibTableColumn
rlCdpTlvPowerRequestedRequestId = _RlCdpTlvPowerRequestedRequestId_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 26),
    _RlCdpTlvPowerRequestedRequestId_Type()
)
rlCdpTlvPowerRequestedRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvPowerRequestedRequestId.setStatus("current")
_RlCdpTlvPowerRequestedPowerManagementId_Type = Unsigned32
_RlCdpTlvPowerRequestedPowerManagementId_Object = MibTableColumn
rlCdpTlvPowerRequestedPowerManagementId = _RlCdpTlvPowerRequestedPowerManagementId_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 27),
    _RlCdpTlvPowerRequestedPowerManagementId_Type()
)
rlCdpTlvPowerRequestedPowerManagementId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvPowerRequestedPowerManagementId.setStatus("current")


class _RlCdpTlvSparePairPoECapabilities_Type(Bits):
    """Custom type rlCdpTlvSparePairPoECapabilities based on Bits"""
    namedValues = NamedValues(
        *(("desiredState", 2),
          ("detectionClassificationRequired", 1),
          ("operationalState", 3),
          ("supported", 0))
    )

_RlCdpTlvSparePairPoECapabilities_Type.__name__ = "Bits"
_RlCdpTlvSparePairPoECapabilities_Object = MibTableColumn
rlCdpTlvSparePairPoECapabilities = _RlCdpTlvSparePairPoECapabilities_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 16, 1, 28),
    _RlCdpTlvSparePairPoECapabilities_Type()
)
rlCdpTlvSparePairPoECapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvSparePairPoECapabilities.setStatus("current")


class _RlCdpAdvertiseApplianceTlv_Type(TruthValue):
    """Custom type rlCdpAdvertiseApplianceTlv based on TruthValue"""


_RlCdpAdvertiseApplianceTlv_Object = MibScalar
rlCdpAdvertiseApplianceTlv = _RlCdpAdvertiseApplianceTlv_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 17),
    _RlCdpAdvertiseApplianceTlv_Type()
)
rlCdpAdvertiseApplianceTlv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCdpAdvertiseApplianceTlv.setStatus("current")


class _RlCdpValidateMandatoryTlvs_Type(TruthValue):
    """Custom type rlCdpValidateMandatoryTlvs based on TruthValue"""


_RlCdpValidateMandatoryTlvs_Object = MibScalar
rlCdpValidateMandatoryTlvs = _RlCdpValidateMandatoryTlvs_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 18),
    _RlCdpValidateMandatoryTlvs_Type()
)
rlCdpValidateMandatoryTlvs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCdpValidateMandatoryTlvs.setStatus("current")
_RlCdpInterfaceCountersTable_Object = MibTable
rlCdpInterfaceCountersTable = _RlCdpInterfaceCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 19)
)
if mibBuilder.loadTexts:
    rlCdpInterfaceCountersTable.setStatus("current")
_RlCdpInterfaceCountersEntry_Object = MibTableRow
rlCdpInterfaceCountersEntry = _RlCdpInterfaceCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 19, 1)
)
rlCdpInterfaceCountersEntry.setIndexNames(
    (0, "RADLAN-CDP-MIB", "rlCdpInterfaceId"),
)
if mibBuilder.loadTexts:
    rlCdpInterfaceCountersEntry.setStatus("current")
_RlCdpInterfaceId_Type = InterfaceIndex
_RlCdpInterfaceId_Object = MibTableColumn
rlCdpInterfaceId = _RlCdpInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 19, 1, 1),
    _RlCdpInterfaceId_Type()
)
rlCdpInterfaceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlCdpInterfaceId.setStatus("current")
_RlCdpInterfaceTotalInputPackets_Type = Counter32
_RlCdpInterfaceTotalInputPackets_Object = MibTableColumn
rlCdpInterfaceTotalInputPackets = _RlCdpInterfaceTotalInputPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 19, 1, 2),
    _RlCdpInterfaceTotalInputPackets_Type()
)
rlCdpInterfaceTotalInputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpInterfaceTotalInputPackets.setStatus("current")
_RlCdpInterfaceV1InputPackets_Type = Counter32
_RlCdpInterfaceV1InputPackets_Object = MibTableColumn
rlCdpInterfaceV1InputPackets = _RlCdpInterfaceV1InputPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 19, 1, 3),
    _RlCdpInterfaceV1InputPackets_Type()
)
rlCdpInterfaceV1InputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpInterfaceV1InputPackets.setStatus("current")
_RlCdpInterfaceV2InputPackets_Type = Counter32
_RlCdpInterfaceV2InputPackets_Object = MibTableColumn
rlCdpInterfaceV2InputPackets = _RlCdpInterfaceV2InputPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 19, 1, 4),
    _RlCdpInterfaceV2InputPackets_Type()
)
rlCdpInterfaceV2InputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpInterfaceV2InputPackets.setStatus("current")
_RlCdpInterfaceTotalOutputPackets_Type = Counter32
_RlCdpInterfaceTotalOutputPackets_Object = MibTableColumn
rlCdpInterfaceTotalOutputPackets = _RlCdpInterfaceTotalOutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 19, 1, 5),
    _RlCdpInterfaceTotalOutputPackets_Type()
)
rlCdpInterfaceTotalOutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpInterfaceTotalOutputPackets.setStatus("current")
_RlCdpInterfaceV1OutputPackets_Type = Counter32
_RlCdpInterfaceV1OutputPackets_Object = MibTableColumn
rlCdpInterfaceV1OutputPackets = _RlCdpInterfaceV1OutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 19, 1, 6),
    _RlCdpInterfaceV1OutputPackets_Type()
)
rlCdpInterfaceV1OutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpInterfaceV1OutputPackets.setStatus("current")
_RlCdpInterfaceV2OutputPackets_Type = Counter32
_RlCdpInterfaceV2OutputPackets_Object = MibTableColumn
rlCdpInterfaceV2OutputPackets = _RlCdpInterfaceV2OutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 19, 1, 7),
    _RlCdpInterfaceV2OutputPackets_Type()
)
rlCdpInterfaceV2OutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpInterfaceV2OutputPackets.setStatus("current")
_RlCdpInterfaceIllegalChksum_Type = Counter32
_RlCdpInterfaceIllegalChksum_Object = MibTableColumn
rlCdpInterfaceIllegalChksum = _RlCdpInterfaceIllegalChksum_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 19, 1, 8),
    _RlCdpInterfaceIllegalChksum_Type()
)
rlCdpInterfaceIllegalChksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpInterfaceIllegalChksum.setStatus("current")
_RlCdpInterfaceErrorPackets_Type = Counter32
_RlCdpInterfaceErrorPackets_Object = MibTableColumn
rlCdpInterfaceErrorPackets = _RlCdpInterfaceErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 19, 1, 9),
    _RlCdpInterfaceErrorPackets_Type()
)
rlCdpInterfaceErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpInterfaceErrorPackets.setStatus("current")
_RlCdpInterfaceMaxNeighborsExceededInMainCache_Type = Counter32
_RlCdpInterfaceMaxNeighborsExceededInMainCache_Object = MibTableColumn
rlCdpInterfaceMaxNeighborsExceededInMainCache = _RlCdpInterfaceMaxNeighborsExceededInMainCache_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 19, 1, 10),
    _RlCdpInterfaceMaxNeighborsExceededInMainCache_Type()
)
rlCdpInterfaceMaxNeighborsExceededInMainCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpInterfaceMaxNeighborsExceededInMainCache.setStatus("current")
_RlCdpInterfaceMaxNeighborsExceededInSecondaryCache_Type = Counter32
_RlCdpInterfaceMaxNeighborsExceededInSecondaryCache_Object = MibTableColumn
rlCdpInterfaceMaxNeighborsExceededInSecondaryCache = _RlCdpInterfaceMaxNeighborsExceededInSecondaryCache_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 19, 1, 11),
    _RlCdpInterfaceMaxNeighborsExceededInSecondaryCache_Type()
)
rlCdpInterfaceMaxNeighborsExceededInSecondaryCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpInterfaceMaxNeighborsExceededInSecondaryCache.setStatus("current")
_RlCdpInterfaceCountersClear_Type = InterfaceIndexOrZero
_RlCdpInterfaceCountersClear_Object = MibScalar
rlCdpInterfaceCountersClear = _RlCdpInterfaceCountersClear_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 20),
    _RlCdpInterfaceCountersClear_Type()
)
rlCdpInterfaceCountersClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlCdpInterfaceCountersClear.setStatus("current")
_RlCdpTlvPowerRequestTable_Object = MibTable
rlCdpTlvPowerRequestTable = _RlCdpTlvPowerRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 21)
)
if mibBuilder.loadTexts:
    rlCdpTlvPowerRequestTable.setStatus("current")
_RlCdpTlvPowerRequestEntry_Object = MibTableRow
rlCdpTlvPowerRequestEntry = _RlCdpTlvPowerRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 21, 1)
)
rlCdpTlvPowerRequestEntry.setIndexNames(
    (0, "RADLAN-CDP-MIB", "rlCdpTlvIfIndex"),
    (0, "RADLAN-CDP-MIB", "rlCdpTlvPowerRequestPowerLevelIndex"),
)
if mibBuilder.loadTexts:
    rlCdpTlvPowerRequestEntry.setStatus("current")


class _RlCdpTlvPowerRequestPowerLevelIndex_Type(Unsigned32):
    """Custom type rlCdpTlvPowerRequestPowerLevelIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlCdpTlvPowerRequestPowerLevelIndex_Type.__name__ = "Unsigned32"
_RlCdpTlvPowerRequestPowerLevelIndex_Object = MibTableColumn
rlCdpTlvPowerRequestPowerLevelIndex = _RlCdpTlvPowerRequestPowerLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 21, 1, 2),
    _RlCdpTlvPowerRequestPowerLevelIndex_Type()
)
rlCdpTlvPowerRequestPowerLevelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlCdpTlvPowerRequestPowerLevelIndex.setStatus("current")


class _RlCdpTlvPowerRequestPowerLevel_Type(Unsigned32):
    """Custom type rlCdpTlvPowerRequestPowerLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlCdpTlvPowerRequestPowerLevel_Type.__name__ = "Unsigned32"
_RlCdpTlvPowerRequestPowerLevel_Object = MibTableColumn
rlCdpTlvPowerRequestPowerLevel = _RlCdpTlvPowerRequestPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 21, 1, 3),
    _RlCdpTlvPowerRequestPowerLevel_Type()
)
rlCdpTlvPowerRequestPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpTlvPowerRequestPowerLevel.setStatus("current")
_RlCdpSecondaryCacheAddressTable_Object = MibTable
rlCdpSecondaryCacheAddressTable = _RlCdpSecondaryCacheAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 22)
)
if mibBuilder.loadTexts:
    rlCdpSecondaryCacheAddressTable.setStatus("current")
_RlCdpSecondaryCacheAddressEntry_Object = MibTableRow
rlCdpSecondaryCacheAddressEntry = _RlCdpSecondaryCacheAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 22, 1)
)
rlCdpSecondaryCacheAddressEntry.setIndexNames(
    (0, "CISCO-CDP-MIB", "cdpCacheIfIndex"),
    (0, "CISCO-CDP-MIB", "cdpCacheDeviceIndex"),
    (0, "RADLAN-CDP-MIB", "rlCdpSecondaryCacheAddressIndex"),
)
if mibBuilder.loadTexts:
    rlCdpSecondaryCacheAddressEntry.setStatus("current")


class _RlCdpSecondaryCacheAddressIndex_Type(Integer32):
    """Custom type rlCdpSecondaryCacheAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlCdpSecondaryCacheAddressIndex_Type.__name__ = "Integer32"
_RlCdpSecondaryCacheAddressIndex_Object = MibTableColumn
rlCdpSecondaryCacheAddressIndex = _RlCdpSecondaryCacheAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 22, 1, 3),
    _RlCdpSecondaryCacheAddressIndex_Type()
)
rlCdpSecondaryCacheAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlCdpSecondaryCacheAddressIndex.setStatus("current")
_RlCdpSecondaryCacheAddressType_Type = CiscoNetworkProtocol
_RlCdpSecondaryCacheAddressType_Object = MibTableColumn
rlCdpSecondaryCacheAddressType = _RlCdpSecondaryCacheAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 22, 1, 4),
    _RlCdpSecondaryCacheAddressType_Type()
)
rlCdpSecondaryCacheAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpSecondaryCacheAddressType.setStatus("current")
_RlCdpSecondaryCacheAddress_Type = CiscoNetworkAddress
_RlCdpSecondaryCacheAddress_Object = MibTableColumn
rlCdpSecondaryCacheAddress = _RlCdpSecondaryCacheAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 22, 1, 5),
    _RlCdpSecondaryCacheAddress_Type()
)
rlCdpSecondaryCacheAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpSecondaryCacheAddress.setStatus("current")
_RlCdpSecondaryCacheRequestedPowerTable_Object = MibTable
rlCdpSecondaryCacheRequestedPowerTable = _RlCdpSecondaryCacheRequestedPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 23)
)
if mibBuilder.loadTexts:
    rlCdpSecondaryCacheRequestedPowerTable.setStatus("current")
_RlCdpSecondaryCacheRequestedPowerEntry_Object = MibTableRow
rlCdpSecondaryCacheRequestedPowerEntry = _RlCdpSecondaryCacheRequestedPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 23, 1)
)
rlCdpSecondaryCacheRequestedPowerEntry.setIndexNames(
    (0, "CISCO-CDP-MIB", "cdpCacheIfIndex"),
    (0, "CISCO-CDP-MIB", "cdpCacheDeviceIndex"),
    (0, "RADLAN-CDP-MIB", "rlCdpSecondaryCacheRequestedPowerIndex"),
)
if mibBuilder.loadTexts:
    rlCdpSecondaryCacheRequestedPowerEntry.setStatus("current")


class _RlCdpSecondaryCacheRequestedPowerIndex_Type(Integer32):
    """Custom type rlCdpSecondaryCacheRequestedPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlCdpSecondaryCacheRequestedPowerIndex_Type.__name__ = "Integer32"
_RlCdpSecondaryCacheRequestedPowerIndex_Object = MibTableColumn
rlCdpSecondaryCacheRequestedPowerIndex = _RlCdpSecondaryCacheRequestedPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 23, 1, 3),
    _RlCdpSecondaryCacheRequestedPowerIndex_Type()
)
rlCdpSecondaryCacheRequestedPowerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlCdpSecondaryCacheRequestedPowerIndex.setStatus("current")


class _RlCdpSecondaryCacheRequestedPowerLevel_Type(Unsigned32):
    """Custom type rlCdpSecondaryCacheRequestedPowerLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlCdpSecondaryCacheRequestedPowerLevel_Type.__name__ = "Unsigned32"
_RlCdpSecondaryCacheRequestedPowerLevel_Object = MibTableColumn
rlCdpSecondaryCacheRequestedPowerLevel = _RlCdpSecondaryCacheRequestedPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 89, 137, 23, 1, 4),
    _RlCdpSecondaryCacheRequestedPowerLevel_Type()
)
rlCdpSecondaryCacheRequestedPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlCdpSecondaryCacheRequestedPowerLevel.setStatus("current")
cdpCacheEntry.registerAugmentions(
    ("RADLAN-CDP-MIB",
     "rlCdpCacheEntry")
)
rlCdpCacheEntry.setIndexNames(*cdpCacheEntry.getIndexNames())

# Managed Objects groups


# Notification objects

rlCdpLogMismatchDuplexTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 224)
)
rlCdpLogMismatchDuplexTrap.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlCdpLogMismatchDuplexTrap.setStatus(
        "current"
    )

rlCdpLogMismatchVoiceVlanTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 225)
)
rlCdpLogMismatchVoiceVlanTrap.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlCdpLogMismatchVoiceVlanTrap.setStatus(
        "current"
    )

rlCdpLogMismatchNativeVlanTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 226)
)
rlCdpLogMismatchNativeVlanTrap.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlCdpLogMismatchNativeVlanTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-CDP-MIB",
    **{"RlCdpVersionTypes": RlCdpVersionTypes,
       "RlCdpCounterTypes": RlCdpCounterTypes,
       "RlCdpPduActionTypes": RlCdpPduActionTypes,
       "rlCdpLogMismatchDuplexTrap": rlCdpLogMismatchDuplexTrap,
       "rlCdpLogMismatchVoiceVlanTrap": rlCdpLogMismatchVoiceVlanTrap,
       "rlCdpLogMismatchNativeVlanTrap": rlCdpLogMismatchNativeVlanTrap,
       "rlCdp": rlCdp,
       "rlCdpVersionAdvertised": rlCdpVersionAdvertised,
       "rlCdpSourceInterface": rlCdpSourceInterface,
       "rlCdpLogMismatchDuplexEnable": rlCdpLogMismatchDuplexEnable,
       "rlCdpCountersTable": rlCdpCountersTable,
       "rlCdpCountersEntry": rlCdpCountersEntry,
       "rlCdpCountersName": rlCdpCountersName,
       "rlCdpCountersValue": rlCdpCountersValue,
       "rlCdpCountersClear": rlCdpCountersClear,
       "rlCdpCacheClear": rlCdpCacheClear,
       "rlCdpVoiceVlanId": rlCdpVoiceVlanId,
       "rlCdpCacheTable": rlCdpCacheTable,
       "rlCdpCacheEntry": rlCdpCacheEntry,
       "rlCdpCacheVersionExt": rlCdpCacheVersionExt,
       "rlCdpCacheTimeToLive": rlCdpCacheTimeToLive,
       "rlCdpCacheCdpVersion": rlCdpCacheCdpVersion,
       "rlCdpPduAction": rlCdpPduAction,
       "rlCdpLogMismatchVoiceVlanEnable": rlCdpLogMismatchVoiceVlanEnable,
       "rlCdpLogMismatchNativeVlanEnable": rlCdpLogMismatchNativeVlanEnable,
       "rlCdpSecondaryCacheTable": rlCdpSecondaryCacheTable,
       "rlCdpSecondaryCacheEntry": rlCdpSecondaryCacheEntry,
       "rlCdpSecondaryCacheMacAddress": rlCdpSecondaryCacheMacAddress,
       "rlCdpSecondaryCachePlatform": rlCdpSecondaryCachePlatform,
       "rlCdpSecondaryCacheCapabilities": rlCdpSecondaryCacheCapabilities,
       "rlCdpSecondaryCacheVoiceVlanID": rlCdpSecondaryCacheVoiceVlanID,
       "rlCdpSecondaryCacheTimeToLive": rlCdpSecondaryCacheTimeToLive,
       "rlCdpSecondaryCachePowerAvailable": rlCdpSecondaryCachePowerAvailable,
       "rlCdpSecondaryCachePowerConsumption": rlCdpSecondaryCachePowerConsumption,
       "rlCdpSecondaryCacheSparePairPoECapabilities": rlCdpSecondaryCacheSparePairPoECapabilities,
       "rlCdpSecondaryCacheDeviceId": rlCdpSecondaryCacheDeviceId,
       "rlCdpSecondaryCachePortId": rlCdpSecondaryCachePortId,
       "rlCdpGlobalLogMismatchDuplexEnable": rlCdpGlobalLogMismatchDuplexEnable,
       "rlCdpGlobalLogMismatchVoiceVlanEnable": rlCdpGlobalLogMismatchVoiceVlanEnable,
       "rlCdpGlobalLogMismatchNativeVlanEnable": rlCdpGlobalLogMismatchNativeVlanEnable,
       "rlCdpTlvTable": rlCdpTlvTable,
       "rlCdpTlvEntry": rlCdpTlvEntry,
       "rlCdpTlvIfIndex": rlCdpTlvIfIndex,
       "rlCdpTlvDeviceIdFormat": rlCdpTlvDeviceIdFormat,
       "rlCdpTlvDeviceId": rlCdpTlvDeviceId,
       "rlCdpTlvAddress1Type": rlCdpTlvAddress1Type,
       "rlCdpTlvAddress1": rlCdpTlvAddress1,
       "rlCdpTlvAddress2Type": rlCdpTlvAddress2Type,
       "rlCdpTlvAddress2": rlCdpTlvAddress2,
       "rlCdpTlvAddress3Type": rlCdpTlvAddress3Type,
       "rlCdpTlvAddress3": rlCdpTlvAddress3,
       "rlCdpTlvPortId": rlCdpTlvPortId,
       "rlCdpTlvCapabilities": rlCdpTlvCapabilities,
       "rlCdpTlvVersion": rlCdpTlvVersion,
       "rlCdpTlvPlatform": rlCdpTlvPlatform,
       "rlCdpTlvNativeVLAN": rlCdpTlvNativeVLAN,
       "rlCdpTlvDuplex": rlCdpTlvDuplex,
       "rlCdpTlvApplianceID": rlCdpTlvApplianceID,
       "rlCdpTlvApplianceVlanID": rlCdpTlvApplianceVlanID,
       "rlCdpTlvExtendedTrust": rlCdpTlvExtendedTrust,
       "rlCdpTlvCosForUntrustedPorts": rlCdpTlvCosForUntrustedPorts,
       "rlCdpTlvPowerAvailableRequestId": rlCdpTlvPowerAvailableRequestId,
       "rlCdpTlvPowerAvailablePowerManagementId": rlCdpTlvPowerAvailablePowerManagementId,
       "rlCdpTlvPowerAvailable": rlCdpTlvPowerAvailable,
       "rlCdpTlvPowerAvailableManagementPowerLevel": rlCdpTlvPowerAvailableManagementPowerLevel,
       "rlCdpTlvSysName": rlCdpTlvSysName,
       "rlCdpTlvPowerConsumption": rlCdpTlvPowerConsumption,
       "rlCdpTlvPowerRequestedRequestId": rlCdpTlvPowerRequestedRequestId,
       "rlCdpTlvPowerRequestedPowerManagementId": rlCdpTlvPowerRequestedPowerManagementId,
       "rlCdpTlvSparePairPoECapabilities": rlCdpTlvSparePairPoECapabilities,
       "rlCdpAdvertiseApplianceTlv": rlCdpAdvertiseApplianceTlv,
       "rlCdpValidateMandatoryTlvs": rlCdpValidateMandatoryTlvs,
       "rlCdpInterfaceCountersTable": rlCdpInterfaceCountersTable,
       "rlCdpInterfaceCountersEntry": rlCdpInterfaceCountersEntry,
       "rlCdpInterfaceId": rlCdpInterfaceId,
       "rlCdpInterfaceTotalInputPackets": rlCdpInterfaceTotalInputPackets,
       "rlCdpInterfaceV1InputPackets": rlCdpInterfaceV1InputPackets,
       "rlCdpInterfaceV2InputPackets": rlCdpInterfaceV2InputPackets,
       "rlCdpInterfaceTotalOutputPackets": rlCdpInterfaceTotalOutputPackets,
       "rlCdpInterfaceV1OutputPackets": rlCdpInterfaceV1OutputPackets,
       "rlCdpInterfaceV2OutputPackets": rlCdpInterfaceV2OutputPackets,
       "rlCdpInterfaceIllegalChksum": rlCdpInterfaceIllegalChksum,
       "rlCdpInterfaceErrorPackets": rlCdpInterfaceErrorPackets,
       "rlCdpInterfaceMaxNeighborsExceededInMainCache": rlCdpInterfaceMaxNeighborsExceededInMainCache,
       "rlCdpInterfaceMaxNeighborsExceededInSecondaryCache": rlCdpInterfaceMaxNeighborsExceededInSecondaryCache,
       "rlCdpInterfaceCountersClear": rlCdpInterfaceCountersClear,
       "rlCdpTlvPowerRequestTable": rlCdpTlvPowerRequestTable,
       "rlCdpTlvPowerRequestEntry": rlCdpTlvPowerRequestEntry,
       "rlCdpTlvPowerRequestPowerLevelIndex": rlCdpTlvPowerRequestPowerLevelIndex,
       "rlCdpTlvPowerRequestPowerLevel": rlCdpTlvPowerRequestPowerLevel,
       "rlCdpSecondaryCacheAddressTable": rlCdpSecondaryCacheAddressTable,
       "rlCdpSecondaryCacheAddressEntry": rlCdpSecondaryCacheAddressEntry,
       "rlCdpSecondaryCacheAddressIndex": rlCdpSecondaryCacheAddressIndex,
       "rlCdpSecondaryCacheAddressType": rlCdpSecondaryCacheAddressType,
       "rlCdpSecondaryCacheAddress": rlCdpSecondaryCacheAddress,
       "rlCdpSecondaryCacheRequestedPowerTable": rlCdpSecondaryCacheRequestedPowerTable,
       "rlCdpSecondaryCacheRequestedPowerEntry": rlCdpSecondaryCacheRequestedPowerEntry,
       "rlCdpSecondaryCacheRequestedPowerIndex": rlCdpSecondaryCacheRequestedPowerIndex,
       "rlCdpSecondaryCacheRequestedPowerLevel": rlCdpSecondaryCacheRequestedPowerLevel}
)
