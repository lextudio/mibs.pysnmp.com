# SNMP MIB module (HM2-PLATFORM-SWITCHING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-PLATFORM-SWITCHING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:26 2024
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

(dot1dBasePortEntry,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePortEntry")

(HmEnabledStatus,
 hm2PlatformMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "hm2PlatformMibs")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(dot1dPortGmrpEntry,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "dot1dPortGmrpEntry")

(PortList,
 VlanId,
 VlanIndex,
 dot1qFdbId,
 dot1qPortVlanEntry,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId",
    "VlanIndex",
    "dot1qFdbId",
    "dot1qPortVlanEntry",
    "dot1qVlanIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hm2PlatformSwitching = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1)
)
hm2PlatformSwitching.setRevisions(
        ("2011-04-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hm2AgentPortMask(OctetString, TextualConvention):
    status = "current"


class LagList(OctetString, TextualConvention):
    status = "current"


class VlanList(OctetString, TextualConvention):
    status = "current"


class Ipv6Address(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



class Ipv6AddressPrefix(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



class Ipv6AddressIfIdentifier(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )



class Ipv6IfIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class Ipv6IfIndexOrZero(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_Hm2PlatformSwitchingTraps_ObjectIdentity = ObjectIdentity
hm2PlatformSwitchingTraps = _Hm2PlatformSwitchingTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 0)
)
_Hm2AgentConfigGroup_ObjectIdentity = ObjectIdentity
hm2AgentConfigGroup = _Hm2AgentConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2)
)
_Hm2AgentLagConfigGroup_ObjectIdentity = ObjectIdentity
hm2AgentLagConfigGroup = _Hm2AgentLagConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2)
)


class _Hm2AgentLagConfigCreate_Type(DisplayString):
    """Custom type hm2AgentLagConfigCreate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 15),
    )


_Hm2AgentLagConfigCreate_Type.__name__ = "DisplayString"
_Hm2AgentLagConfigCreate_Object = MibScalar
hm2AgentLagConfigCreate = _Hm2AgentLagConfigCreate_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 1),
    _Hm2AgentLagConfigCreate_Type()
)
hm2AgentLagConfigCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentLagConfigCreate.setStatus("current")
_Hm2AgentLagSummaryConfigTable_Object = MibTable
hm2AgentLagSummaryConfigTable = _Hm2AgentLagSummaryConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hm2AgentLagSummaryConfigTable.setStatus("current")
_Hm2AgentLagSummaryConfigEntry_Object = MibTableRow
hm2AgentLagSummaryConfigEntry = _Hm2AgentLagSummaryConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 2, 1)
)
hm2AgentLagSummaryConfigEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentLagSummaryLagIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentLagSummaryConfigEntry.setStatus("current")


class _Hm2AgentLagSummaryLagIndex_Type(Integer32):
    """Custom type hm2AgentLagSummaryLagIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2AgentLagSummaryLagIndex_Type.__name__ = "Integer32"
_Hm2AgentLagSummaryLagIndex_Object = MibTableColumn
hm2AgentLagSummaryLagIndex = _Hm2AgentLagSummaryLagIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 2, 1, 1),
    _Hm2AgentLagSummaryLagIndex_Type()
)
hm2AgentLagSummaryLagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentLagSummaryLagIndex.setStatus("current")


class _Hm2AgentLagSummaryName_Type(DisplayString):
    """Custom type hm2AgentLagSummaryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Hm2AgentLagSummaryName_Type.__name__ = "DisplayString"
_Hm2AgentLagSummaryName_Object = MibTableColumn
hm2AgentLagSummaryName = _Hm2AgentLagSummaryName_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 2, 1, 2),
    _Hm2AgentLagSummaryName_Type()
)
hm2AgentLagSummaryName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentLagSummaryName.setStatus("current")
_Hm2AgentLagSummaryFlushTimer_Type = Integer32
_Hm2AgentLagSummaryFlushTimer_Object = MibTableColumn
hm2AgentLagSummaryFlushTimer = _Hm2AgentLagSummaryFlushTimer_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 2, 1, 3),
    _Hm2AgentLagSummaryFlushTimer_Type()
)
hm2AgentLagSummaryFlushTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentLagSummaryFlushTimer.setStatus("obsolete")
_Hm2AgentLagSummaryLinkTrap_Type = HmEnabledStatus
_Hm2AgentLagSummaryLinkTrap_Object = MibTableColumn
hm2AgentLagSummaryLinkTrap = _Hm2AgentLagSummaryLinkTrap_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 2, 1, 4),
    _Hm2AgentLagSummaryLinkTrap_Type()
)
hm2AgentLagSummaryLinkTrap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentLagSummaryLinkTrap.setStatus("current")
_Hm2AgentLagSummaryAdminMode_Type = HmEnabledStatus
_Hm2AgentLagSummaryAdminMode_Object = MibTableColumn
hm2AgentLagSummaryAdminMode = _Hm2AgentLagSummaryAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 2, 1, 5),
    _Hm2AgentLagSummaryAdminMode_Type()
)
hm2AgentLagSummaryAdminMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentLagSummaryAdminMode.setStatus("current")
_Hm2AgentLagSummaryStpMode_Type = HmEnabledStatus
_Hm2AgentLagSummaryStpMode_Object = MibTableColumn
hm2AgentLagSummaryStpMode = _Hm2AgentLagSummaryStpMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 2, 1, 6),
    _Hm2AgentLagSummaryStpMode_Type()
)
hm2AgentLagSummaryStpMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentLagSummaryStpMode.setStatus("current")
_Hm2AgentLagSummaryAddPort_Type = Integer32
_Hm2AgentLagSummaryAddPort_Object = MibTableColumn
hm2AgentLagSummaryAddPort = _Hm2AgentLagSummaryAddPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 2, 1, 7),
    _Hm2AgentLagSummaryAddPort_Type()
)
hm2AgentLagSummaryAddPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentLagSummaryAddPort.setStatus("current")
_Hm2AgentLagSummaryDeletePort_Type = Integer32
_Hm2AgentLagSummaryDeletePort_Object = MibTableColumn
hm2AgentLagSummaryDeletePort = _Hm2AgentLagSummaryDeletePort_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 2, 1, 8),
    _Hm2AgentLagSummaryDeletePort_Type()
)
hm2AgentLagSummaryDeletePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentLagSummaryDeletePort.setStatus("current")
_Hm2AgentLagSummaryStatus_Type = RowStatus
_Hm2AgentLagSummaryStatus_Object = MibTableColumn
hm2AgentLagSummaryStatus = _Hm2AgentLagSummaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 2, 1, 9),
    _Hm2AgentLagSummaryStatus_Type()
)
hm2AgentLagSummaryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentLagSummaryStatus.setStatus("current")


class _Hm2AgentLagSummaryType_Type(Integer32):
    """Custom type hm2AgentLagSummaryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_Hm2AgentLagSummaryType_Type.__name__ = "Integer32"
_Hm2AgentLagSummaryType_Object = MibTableColumn
hm2AgentLagSummaryType = _Hm2AgentLagSummaryType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 2, 1, 10),
    _Hm2AgentLagSummaryType_Type()
)
hm2AgentLagSummaryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentLagSummaryType.setStatus("current")


class _Hm2AgentLagSummaryStaticCapability_Type(HmEnabledStatus):
    """Custom type hm2AgentLagSummaryStaticCapability based on HmEnabledStatus"""


_Hm2AgentLagSummaryStaticCapability_Object = MibTableColumn
hm2AgentLagSummaryStaticCapability = _Hm2AgentLagSummaryStaticCapability_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 2, 1, 11),
    _Hm2AgentLagSummaryStaticCapability_Type()
)
hm2AgentLagSummaryStaticCapability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentLagSummaryStaticCapability.setStatus("current")


class _Hm2AgentLagSummaryHashOption_Type(Integer32):
    """Custom type hm2AgentLagSummaryHashOption based on Integer32"""
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
        *(("destIPdestPort", 5),
          ("destMacVlan", 2),
          ("enhanced", 7),
          ("sourceDestIPPort", 6),
          ("sourceDestMacVlan", 3),
          ("sourceIPsourcePort", 4),
          ("sourceMacVlan", 1))
    )


_Hm2AgentLagSummaryHashOption_Type.__name__ = "Integer32"
_Hm2AgentLagSummaryHashOption_Object = MibTableColumn
hm2AgentLagSummaryHashOption = _Hm2AgentLagSummaryHashOption_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 2, 1, 12),
    _Hm2AgentLagSummaryHashOption_Type()
)
hm2AgentLagSummaryHashOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentLagSummaryHashOption.setStatus("current")


class _Hm2AgentLagSummaryMinimumActiveLinks_Type(Integer32):
    """Custom type hm2AgentLagSummaryMinimumActiveLinks based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Hm2AgentLagSummaryMinimumActiveLinks_Type.__name__ = "Integer32"
_Hm2AgentLagSummaryMinimumActiveLinks_Object = MibTableColumn
hm2AgentLagSummaryMinimumActiveLinks = _Hm2AgentLagSummaryMinimumActiveLinks_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 2, 1, 13),
    _Hm2AgentLagSummaryMinimumActiveLinks_Type()
)
hm2AgentLagSummaryMinimumActiveLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentLagSummaryMinimumActiveLinks.setStatus("current")
_Hm2AgentLagSummaryMaxFrameSizeLimit_Type = Integer32
_Hm2AgentLagSummaryMaxFrameSizeLimit_Object = MibTableColumn
hm2AgentLagSummaryMaxFrameSizeLimit = _Hm2AgentLagSummaryMaxFrameSizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 2, 1, 248),
    _Hm2AgentLagSummaryMaxFrameSizeLimit_Type()
)
hm2AgentLagSummaryMaxFrameSizeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentLagSummaryMaxFrameSizeLimit.setStatus("current")
_Hm2AgentLagSummaryMaxFrameSize_Type = Integer32
_Hm2AgentLagSummaryMaxFrameSize_Object = MibTableColumn
hm2AgentLagSummaryMaxFrameSize = _Hm2AgentLagSummaryMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 2, 1, 249),
    _Hm2AgentLagSummaryMaxFrameSize_Type()
)
hm2AgentLagSummaryMaxFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentLagSummaryMaxFrameSize.setStatus("current")
_Hm2AgentLagDetailedConfigTable_Object = MibTable
hm2AgentLagDetailedConfigTable = _Hm2AgentLagDetailedConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hm2AgentLagDetailedConfigTable.setStatus("current")
_Hm2AgentLagDetailedConfigEntry_Object = MibTableRow
hm2AgentLagDetailedConfigEntry = _Hm2AgentLagDetailedConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 3, 1)
)
hm2AgentLagDetailedConfigEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentLagDetailedLagIndex"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentLagDetailedIfIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentLagDetailedConfigEntry.setStatus("current")


class _Hm2AgentLagDetailedLagIndex_Type(Integer32):
    """Custom type hm2AgentLagDetailedLagIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2AgentLagDetailedLagIndex_Type.__name__ = "Integer32"
_Hm2AgentLagDetailedLagIndex_Object = MibTableColumn
hm2AgentLagDetailedLagIndex = _Hm2AgentLagDetailedLagIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 3, 1, 1),
    _Hm2AgentLagDetailedLagIndex_Type()
)
hm2AgentLagDetailedLagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentLagDetailedLagIndex.setStatus("current")


class _Hm2AgentLagDetailedIfIndex_Type(Integer32):
    """Custom type hm2AgentLagDetailedIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2AgentLagDetailedIfIndex_Type.__name__ = "Integer32"
_Hm2AgentLagDetailedIfIndex_Object = MibTableColumn
hm2AgentLagDetailedIfIndex = _Hm2AgentLagDetailedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 3, 1, 2),
    _Hm2AgentLagDetailedIfIndex_Type()
)
hm2AgentLagDetailedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentLagDetailedIfIndex.setStatus("current")
_Hm2AgentLagDetailedPortSpeed_Type = ObjectIdentifier
_Hm2AgentLagDetailedPortSpeed_Object = MibTableColumn
hm2AgentLagDetailedPortSpeed = _Hm2AgentLagDetailedPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 3, 1, 3),
    _Hm2AgentLagDetailedPortSpeed_Type()
)
hm2AgentLagDetailedPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentLagDetailedPortSpeed.setStatus("current")


class _Hm2AgentLagDetailedPortStatus_Type(Integer32):
    """Custom type hm2AgentLagDetailedPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_Hm2AgentLagDetailedPortStatus_Type.__name__ = "Integer32"
_Hm2AgentLagDetailedPortStatus_Object = MibTableColumn
hm2AgentLagDetailedPortStatus = _Hm2AgentLagDetailedPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 3, 1, 4),
    _Hm2AgentLagDetailedPortStatus_Type()
)
hm2AgentLagDetailedPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentLagDetailedPortStatus.setStatus("current")
_Hm2AgentLagConfigStaticCapability_Type = HmEnabledStatus
_Hm2AgentLagConfigStaticCapability_Object = MibScalar
hm2AgentLagConfigStaticCapability = _Hm2AgentLagConfigStaticCapability_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 4),
    _Hm2AgentLagConfigStaticCapability_Type()
)
hm2AgentLagConfigStaticCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentLagConfigStaticCapability.setStatus("obsolete")


class _Hm2AgentLagConfigGroupHashOption_Type(Integer32):
    """Custom type hm2AgentLagConfigGroupHashOption based on Integer32"""
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
        *(("destIPdestPort", 5),
          ("destMacVlan", 2),
          ("enhanced", 7),
          ("sourceDestIPPort", 6),
          ("sourceDestMacVlan", 3),
          ("sourceIPsourcePort", 4),
          ("sourceMacVlan", 1))
    )


_Hm2AgentLagConfigGroupHashOption_Type.__name__ = "Integer32"
_Hm2AgentLagConfigGroupHashOption_Object = MibScalar
hm2AgentLagConfigGroupHashOption = _Hm2AgentLagConfigGroupHashOption_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 5),
    _Hm2AgentLagConfigGroupHashOption_Type()
)
hm2AgentLagConfigGroupHashOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentLagConfigGroupHashOption.setStatus("current")
_Hm2AgentLagConfigGroupMaxNumPortsPerLag_Type = Unsigned32
_Hm2AgentLagConfigGroupMaxNumPortsPerLag_Object = MibScalar
hm2AgentLagConfigGroupMaxNumPortsPerLag = _Hm2AgentLagConfigGroupMaxNumPortsPerLag_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 248),
    _Hm2AgentLagConfigGroupMaxNumPortsPerLag_Type()
)
hm2AgentLagConfigGroupMaxNumPortsPerLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentLagConfigGroupMaxNumPortsPerLag.setStatus("current")
_Hm2AgentLagConfigGroupMaxNumOfLags_Type = Unsigned32
_Hm2AgentLagConfigGroupMaxNumOfLags_Object = MibScalar
hm2AgentLagConfigGroupMaxNumOfLags = _Hm2AgentLagConfigGroupMaxNumOfLags_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 249),
    _Hm2AgentLagConfigGroupMaxNumOfLags_Type()
)
hm2AgentLagConfigGroupMaxNumOfLags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentLagConfigGroupMaxNumOfLags.setStatus("current")
_Hm2AgentLagConfigGroupNumOfLagsConfigured_Type = Unsigned32
_Hm2AgentLagConfigGroupNumOfLagsConfigured_Object = MibScalar
hm2AgentLagConfigGroupNumOfLagsConfigured = _Hm2AgentLagConfigGroupNumOfLagsConfigured_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 250),
    _Hm2AgentLagConfigGroupNumOfLagsConfigured_Type()
)
hm2AgentLagConfigGroupNumOfLagsConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentLagConfigGroupNumOfLagsConfigured.setStatus("current")
_Hm2AgentLagConfigGroupLagsConfigured_Type = LagList
_Hm2AgentLagConfigGroupLagsConfigured_Object = MibScalar
hm2AgentLagConfigGroupLagsConfigured = _Hm2AgentLagConfigGroupLagsConfigured_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 251),
    _Hm2AgentLagConfigGroupLagsConfigured_Type()
)
hm2AgentLagConfigGroupLagsConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentLagConfigGroupLagsConfigured.setStatus("current")
_Hm2AgentLagConfigSNMPExtensionGroup_ObjectIdentity = ObjectIdentity
hm2AgentLagConfigSNMPExtensionGroup = _Hm2AgentLagConfigSNMPExtensionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 260)
)
_Hm2AgentLagConfigGroupPortIsLagMemberErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentLagConfigGroupPortIsLagMemberErrorReturn = _Hm2AgentLagConfigGroupPortIsLagMemberErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 260, 1)
)
if mibBuilder.loadTexts:
    hm2AgentLagConfigGroupPortIsLagMemberErrorReturn.setStatus("current")
_Hm2AgentLagMirrorProbePortLagMemberErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentLagMirrorProbePortLagMemberErrorReturn = _Hm2AgentLagMirrorProbePortLagMemberErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 2, 260, 2)
)
if mibBuilder.loadTexts:
    hm2AgentLagMirrorProbePortLagMemberErrorReturn.setStatus("current")
_Hm2AgentSwitchConfigGroup_ObjectIdentity = ObjectIdentity
hm2AgentSwitchConfigGroup = _Hm2AgentSwitchConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8)
)
_Hm2AgentSwitchAddressAgingTimeoutTable_Object = MibTable
hm2AgentSwitchAddressAgingTimeoutTable = _Hm2AgentSwitchAddressAgingTimeoutTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 4)
)
if mibBuilder.loadTexts:
    hm2AgentSwitchAddressAgingTimeoutTable.setStatus("current")
_Hm2AgentSwitchAddressAgingTimeoutEntry_Object = MibTableRow
hm2AgentSwitchAddressAgingTimeoutEntry = _Hm2AgentSwitchAddressAgingTimeoutEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 4, 1)
)
hm2AgentSwitchAddressAgingTimeoutEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qFdbId"),
)
if mibBuilder.loadTexts:
    hm2AgentSwitchAddressAgingTimeoutEntry.setStatus("current")


class _Hm2AgentSwitchAddressAgingTimeout_Type(Integer32):
    """Custom type hm2AgentSwitchAddressAgingTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 500000),
    )


_Hm2AgentSwitchAddressAgingTimeout_Type.__name__ = "Integer32"
_Hm2AgentSwitchAddressAgingTimeout_Object = MibTableColumn
hm2AgentSwitchAddressAgingTimeout = _Hm2AgentSwitchAddressAgingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 4, 1, 1),
    _Hm2AgentSwitchAddressAgingTimeout_Type()
)
hm2AgentSwitchAddressAgingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchAddressAgingTimeout.setStatus("current")
_Hm2AgentSwitchStaticMacFilteringTable_Object = MibTable
hm2AgentSwitchStaticMacFilteringTable = _Hm2AgentSwitchStaticMacFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 5)
)
if mibBuilder.loadTexts:
    hm2AgentSwitchStaticMacFilteringTable.setStatus("current")
_Hm2AgentSwitchStaticMacFilteringEntry_Object = MibTableRow
hm2AgentSwitchStaticMacFilteringEntry = _Hm2AgentSwitchStaticMacFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 5, 1)
)
hm2AgentSwitchStaticMacFilteringEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentSwitchStaticMacFilteringVlanId"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentSwitchStaticMacFilteringAddress"),
)
if mibBuilder.loadTexts:
    hm2AgentSwitchStaticMacFilteringEntry.setStatus("current")


class _Hm2AgentSwitchStaticMacFilteringVlanId_Type(Integer32):
    """Custom type hm2AgentSwitchStaticMacFilteringVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2AgentSwitchStaticMacFilteringVlanId_Type.__name__ = "Integer32"
_Hm2AgentSwitchStaticMacFilteringVlanId_Object = MibTableColumn
hm2AgentSwitchStaticMacFilteringVlanId = _Hm2AgentSwitchStaticMacFilteringVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 5, 1, 1),
    _Hm2AgentSwitchStaticMacFilteringVlanId_Type()
)
hm2AgentSwitchStaticMacFilteringVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchStaticMacFilteringVlanId.setStatus("current")
_Hm2AgentSwitchStaticMacFilteringAddress_Type = MacAddress
_Hm2AgentSwitchStaticMacFilteringAddress_Object = MibTableColumn
hm2AgentSwitchStaticMacFilteringAddress = _Hm2AgentSwitchStaticMacFilteringAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 5, 1, 2),
    _Hm2AgentSwitchStaticMacFilteringAddress_Type()
)
hm2AgentSwitchStaticMacFilteringAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchStaticMacFilteringAddress.setStatus("current")
_Hm2AgentSwitchStaticMacFilteringSourcePortMask_Type = Hm2AgentPortMask
_Hm2AgentSwitchStaticMacFilteringSourcePortMask_Object = MibTableColumn
hm2AgentSwitchStaticMacFilteringSourcePortMask = _Hm2AgentSwitchStaticMacFilteringSourcePortMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 5, 1, 3),
    _Hm2AgentSwitchStaticMacFilteringSourcePortMask_Type()
)
hm2AgentSwitchStaticMacFilteringSourcePortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchStaticMacFilteringSourcePortMask.setStatus("current")
_Hm2AgentSwitchStaticMacFilteringDestPortMask_Type = Hm2AgentPortMask
_Hm2AgentSwitchStaticMacFilteringDestPortMask_Object = MibTableColumn
hm2AgentSwitchStaticMacFilteringDestPortMask = _Hm2AgentSwitchStaticMacFilteringDestPortMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 5, 1, 4),
    _Hm2AgentSwitchStaticMacFilteringDestPortMask_Type()
)
hm2AgentSwitchStaticMacFilteringDestPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchStaticMacFilteringDestPortMask.setStatus("current")
_Hm2AgentSwitchStaticMacFilteringStatus_Type = RowStatus
_Hm2AgentSwitchStaticMacFilteringStatus_Object = MibTableColumn
hm2AgentSwitchStaticMacFilteringStatus = _Hm2AgentSwitchStaticMacFilteringStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 5, 1, 5),
    _Hm2AgentSwitchStaticMacFilteringStatus_Type()
)
hm2AgentSwitchStaticMacFilteringStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentSwitchStaticMacFilteringStatus.setStatus("current")
_Hm2AgentSwitchSnoopingGroup_ObjectIdentity = ObjectIdentity
hm2AgentSwitchSnoopingGroup = _Hm2AgentSwitchSnoopingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 6)
)
_Hm2AgentSwitchSnoopingCfgTable_Object = MibTable
hm2AgentSwitchSnoopingCfgTable = _Hm2AgentSwitchSnoopingCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 6, 1)
)
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingCfgTable.setStatus("current")
_Hm2AgentSwitchSnoopingCfgEntry_Object = MibTableRow
hm2AgentSwitchSnoopingCfgEntry = _Hm2AgentSwitchSnoopingCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 6, 1, 1)
)
hm2AgentSwitchSnoopingCfgEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentSwitchSnoopingProtocol"),
)
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingCfgEntry.setStatus("current")
_Hm2AgentSwitchSnoopingProtocol_Type = InetAddressType
_Hm2AgentSwitchSnoopingProtocol_Object = MibTableColumn
hm2AgentSwitchSnoopingProtocol = _Hm2AgentSwitchSnoopingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 6, 1, 1, 1),
    _Hm2AgentSwitchSnoopingProtocol_Type()
)
hm2AgentSwitchSnoopingProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingProtocol.setStatus("current")


class _Hm2AgentSwitchSnoopingAdminMode_Type(HmEnabledStatus):
    """Custom type hm2AgentSwitchSnoopingAdminMode based on HmEnabledStatus"""


_Hm2AgentSwitchSnoopingAdminMode_Object = MibTableColumn
hm2AgentSwitchSnoopingAdminMode = _Hm2AgentSwitchSnoopingAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 6, 1, 1, 2),
    _Hm2AgentSwitchSnoopingAdminMode_Type()
)
hm2AgentSwitchSnoopingAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingAdminMode.setStatus("current")


class _Hm2AgentSwitchSnoopingPortMask_Type(Hm2AgentPortMask):
    """Custom type hm2AgentSwitchSnoopingPortMask based on Hm2AgentPortMask"""
    defaultHexValue = "000000000000"


_Hm2AgentSwitchSnoopingPortMask_Object = MibTableColumn
hm2AgentSwitchSnoopingPortMask = _Hm2AgentSwitchSnoopingPortMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 6, 1, 1, 3),
    _Hm2AgentSwitchSnoopingPortMask_Type()
)
hm2AgentSwitchSnoopingPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingPortMask.setStatus("current")
_Hm2AgentSwitchSnoopingMulticastControlFramesProcessed_Type = Counter32
_Hm2AgentSwitchSnoopingMulticastControlFramesProcessed_Object = MibTableColumn
hm2AgentSwitchSnoopingMulticastControlFramesProcessed = _Hm2AgentSwitchSnoopingMulticastControlFramesProcessed_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 6, 1, 1, 4),
    _Hm2AgentSwitchSnoopingMulticastControlFramesProcessed_Type()
)
hm2AgentSwitchSnoopingMulticastControlFramesProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingMulticastControlFramesProcessed.setStatus("current")
_Hm2AgentSwitchSnoopingIntfGroup_ObjectIdentity = ObjectIdentity
hm2AgentSwitchSnoopingIntfGroup = _Hm2AgentSwitchSnoopingIntfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 7)
)
_Hm2AgentSwitchSnoopingIntfTable_Object = MibTable
hm2AgentSwitchSnoopingIntfTable = _Hm2AgentSwitchSnoopingIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 7, 1)
)
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingIntfTable.setStatus("current")
_Hm2AgentSwitchSnoopingIntfEntry_Object = MibTableRow
hm2AgentSwitchSnoopingIntfEntry = _Hm2AgentSwitchSnoopingIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 7, 1, 1)
)
hm2AgentSwitchSnoopingIntfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentSwitchSnoopingProtocol"),
)
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingIntfEntry.setStatus("current")


class _Hm2AgentSwitchSnoopingIntfIndex_Type(Unsigned32):
    """Custom type hm2AgentSwitchSnoopingIntfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hm2AgentSwitchSnoopingIntfIndex_Type.__name__ = "Unsigned32"
_Hm2AgentSwitchSnoopingIntfIndex_Object = MibTableColumn
hm2AgentSwitchSnoopingIntfIndex = _Hm2AgentSwitchSnoopingIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 7, 1, 1, 1),
    _Hm2AgentSwitchSnoopingIntfIndex_Type()
)
hm2AgentSwitchSnoopingIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingIntfIndex.setStatus("current")


class _Hm2AgentSwitchSnoopingIntfAdminMode_Type(HmEnabledStatus):
    """Custom type hm2AgentSwitchSnoopingIntfAdminMode based on HmEnabledStatus"""


_Hm2AgentSwitchSnoopingIntfAdminMode_Object = MibTableColumn
hm2AgentSwitchSnoopingIntfAdminMode = _Hm2AgentSwitchSnoopingIntfAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 7, 1, 1, 2),
    _Hm2AgentSwitchSnoopingIntfAdminMode_Type()
)
hm2AgentSwitchSnoopingIntfAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingIntfAdminMode.setStatus("current")


class _Hm2AgentSwitchSnoopingIntfGroupMembershipInterval_Type(Integer32):
    """Custom type hm2AgentSwitchSnoopingIntfGroupMembershipInterval based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3600),
    )


_Hm2AgentSwitchSnoopingIntfGroupMembershipInterval_Type.__name__ = "Integer32"
_Hm2AgentSwitchSnoopingIntfGroupMembershipInterval_Object = MibTableColumn
hm2AgentSwitchSnoopingIntfGroupMembershipInterval = _Hm2AgentSwitchSnoopingIntfGroupMembershipInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 7, 1, 1, 3),
    _Hm2AgentSwitchSnoopingIntfGroupMembershipInterval_Type()
)
hm2AgentSwitchSnoopingIntfGroupMembershipInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingIntfGroupMembershipInterval.setStatus("current")


class _Hm2AgentSwitchSnoopingIntfMaxResponseTime_Type(Integer32):
    """Custom type hm2AgentSwitchSnoopingIntfMaxResponseTime based on Integer32"""
    defaultValue = 10


_Hm2AgentSwitchSnoopingIntfMaxResponseTime_Object = MibTableColumn
hm2AgentSwitchSnoopingIntfMaxResponseTime = _Hm2AgentSwitchSnoopingIntfMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 7, 1, 1, 4),
    _Hm2AgentSwitchSnoopingIntfMaxResponseTime_Type()
)
hm2AgentSwitchSnoopingIntfMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingIntfMaxResponseTime.setStatus("current")


class _Hm2AgentSwitchSnoopingIntfMRPExpirationTime_Type(Integer32):
    """Custom type hm2AgentSwitchSnoopingIntfMRPExpirationTime based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_Hm2AgentSwitchSnoopingIntfMRPExpirationTime_Type.__name__ = "Integer32"
_Hm2AgentSwitchSnoopingIntfMRPExpirationTime_Object = MibTableColumn
hm2AgentSwitchSnoopingIntfMRPExpirationTime = _Hm2AgentSwitchSnoopingIntfMRPExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 7, 1, 1, 5),
    _Hm2AgentSwitchSnoopingIntfMRPExpirationTime_Type()
)
hm2AgentSwitchSnoopingIntfMRPExpirationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingIntfMRPExpirationTime.setStatus("current")


class _Hm2AgentSwitchSnoopingIntfFastLeaveAdminMode_Type(HmEnabledStatus):
    """Custom type hm2AgentSwitchSnoopingIntfFastLeaveAdminMode based on HmEnabledStatus"""


_Hm2AgentSwitchSnoopingIntfFastLeaveAdminMode_Object = MibTableColumn
hm2AgentSwitchSnoopingIntfFastLeaveAdminMode = _Hm2AgentSwitchSnoopingIntfFastLeaveAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 7, 1, 1, 6),
    _Hm2AgentSwitchSnoopingIntfFastLeaveAdminMode_Type()
)
hm2AgentSwitchSnoopingIntfFastLeaveAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingIntfFastLeaveAdminMode.setStatus("current")


class _Hm2AgentSwitchSnoopingIntfMulticastRouterMode_Type(HmEnabledStatus):
    """Custom type hm2AgentSwitchSnoopingIntfMulticastRouterMode based on HmEnabledStatus"""


_Hm2AgentSwitchSnoopingIntfMulticastRouterMode_Object = MibTableColumn
hm2AgentSwitchSnoopingIntfMulticastRouterMode = _Hm2AgentSwitchSnoopingIntfMulticastRouterMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 7, 1, 1, 7),
    _Hm2AgentSwitchSnoopingIntfMulticastRouterMode_Type()
)
hm2AgentSwitchSnoopingIntfMulticastRouterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingIntfMulticastRouterMode.setStatus("current")
_Hm2AgentSwitchSnoopingIntfVlanIDs_Type = VlanList
_Hm2AgentSwitchSnoopingIntfVlanIDs_Object = MibTableColumn
hm2AgentSwitchSnoopingIntfVlanIDs = _Hm2AgentSwitchSnoopingIntfVlanIDs_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 7, 1, 1, 8),
    _Hm2AgentSwitchSnoopingIntfVlanIDs_Type()
)
hm2AgentSwitchSnoopingIntfVlanIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingIntfVlanIDs.setStatus("current")
_Hm2AgentSwitchSnoopingVlanGroup_ObjectIdentity = ObjectIdentity
hm2AgentSwitchSnoopingVlanGroup = _Hm2AgentSwitchSnoopingVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 8)
)
_Hm2AgentSwitchSnoopingVlanTable_Object = MibTable
hm2AgentSwitchSnoopingVlanTable = _Hm2AgentSwitchSnoopingVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 8, 1)
)
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingVlanTable.setStatus("current")
_Hm2AgentSwitchSnoopingVlanEntry_Object = MibTableRow
hm2AgentSwitchSnoopingVlanEntry = _Hm2AgentSwitchSnoopingVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 8, 1, 1)
)
hm2AgentSwitchSnoopingVlanEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentSwitchSnoopingProtocol"),
)
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingVlanEntry.setStatus("current")


class _Hm2AgentSwitchSnoopingVlanAdminMode_Type(HmEnabledStatus):
    """Custom type hm2AgentSwitchSnoopingVlanAdminMode based on HmEnabledStatus"""


_Hm2AgentSwitchSnoopingVlanAdminMode_Object = MibTableColumn
hm2AgentSwitchSnoopingVlanAdminMode = _Hm2AgentSwitchSnoopingVlanAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 8, 1, 1, 1),
    _Hm2AgentSwitchSnoopingVlanAdminMode_Type()
)
hm2AgentSwitchSnoopingVlanAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingVlanAdminMode.setStatus("current")


class _Hm2AgentSwitchSnoopingVlanGroupMembershipInterval_Type(Integer32):
    """Custom type hm2AgentSwitchSnoopingVlanGroupMembershipInterval based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 3600),
    )


_Hm2AgentSwitchSnoopingVlanGroupMembershipInterval_Type.__name__ = "Integer32"
_Hm2AgentSwitchSnoopingVlanGroupMembershipInterval_Object = MibTableColumn
hm2AgentSwitchSnoopingVlanGroupMembershipInterval = _Hm2AgentSwitchSnoopingVlanGroupMembershipInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 8, 1, 1, 2),
    _Hm2AgentSwitchSnoopingVlanGroupMembershipInterval_Type()
)
hm2AgentSwitchSnoopingVlanGroupMembershipInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingVlanGroupMembershipInterval.setStatus("current")


class _Hm2AgentSwitchSnoopingVlanMaxResponseTime_Type(Integer32):
    """Custom type hm2AgentSwitchSnoopingVlanMaxResponseTime based on Integer32"""
    defaultValue = 10


_Hm2AgentSwitchSnoopingVlanMaxResponseTime_Object = MibTableColumn
hm2AgentSwitchSnoopingVlanMaxResponseTime = _Hm2AgentSwitchSnoopingVlanMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 8, 1, 1, 3),
    _Hm2AgentSwitchSnoopingVlanMaxResponseTime_Type()
)
hm2AgentSwitchSnoopingVlanMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingVlanMaxResponseTime.setStatus("current")


class _Hm2AgentSwitchSnoopingVlanFastLeaveAdminMode_Type(HmEnabledStatus):
    """Custom type hm2AgentSwitchSnoopingVlanFastLeaveAdminMode based on HmEnabledStatus"""


_Hm2AgentSwitchSnoopingVlanFastLeaveAdminMode_Object = MibTableColumn
hm2AgentSwitchSnoopingVlanFastLeaveAdminMode = _Hm2AgentSwitchSnoopingVlanFastLeaveAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 8, 1, 1, 4),
    _Hm2AgentSwitchSnoopingVlanFastLeaveAdminMode_Type()
)
hm2AgentSwitchSnoopingVlanFastLeaveAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingVlanFastLeaveAdminMode.setStatus("current")


class _Hm2AgentSwitchSnoopingVlanMRPExpirationTime_Type(Integer32):
    """Custom type hm2AgentSwitchSnoopingVlanMRPExpirationTime based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_Hm2AgentSwitchSnoopingVlanMRPExpirationTime_Type.__name__ = "Integer32"
_Hm2AgentSwitchSnoopingVlanMRPExpirationTime_Object = MibTableColumn
hm2AgentSwitchSnoopingVlanMRPExpirationTime = _Hm2AgentSwitchSnoopingVlanMRPExpirationTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 8, 1, 1, 5),
    _Hm2AgentSwitchSnoopingVlanMRPExpirationTime_Type()
)
hm2AgentSwitchSnoopingVlanMRPExpirationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingVlanMRPExpirationTime.setStatus("current")


class _Hm2AgentSwitchSnoopingVlanReportSuppMode_Type(HmEnabledStatus):
    """Custom type hm2AgentSwitchSnoopingVlanReportSuppMode based on HmEnabledStatus"""


_Hm2AgentSwitchSnoopingVlanReportSuppMode_Object = MibTableColumn
hm2AgentSwitchSnoopingVlanReportSuppMode = _Hm2AgentSwitchSnoopingVlanReportSuppMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 8, 1, 1, 6),
    _Hm2AgentSwitchSnoopingVlanReportSuppMode_Type()
)
hm2AgentSwitchSnoopingVlanReportSuppMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingVlanReportSuppMode.setStatus("current")
_Hm2AgentSwitchVlanStaticMrouterGroup_ObjectIdentity = ObjectIdentity
hm2AgentSwitchVlanStaticMrouterGroup = _Hm2AgentSwitchVlanStaticMrouterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 9)
)
_Hm2AgentSwitchVlanStaticMrouterTable_Object = MibTable
hm2AgentSwitchVlanStaticMrouterTable = _Hm2AgentSwitchVlanStaticMrouterTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 9, 1)
)
if mibBuilder.loadTexts:
    hm2AgentSwitchVlanStaticMrouterTable.setStatus("current")
_Hm2AgentSwitchVlanStaticMrouterEntry_Object = MibTableRow
hm2AgentSwitchVlanStaticMrouterEntry = _Hm2AgentSwitchVlanStaticMrouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 9, 1, 1)
)
hm2AgentSwitchVlanStaticMrouterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentSwitchSnoopingProtocol"),
)
if mibBuilder.loadTexts:
    hm2AgentSwitchVlanStaticMrouterEntry.setStatus("current")


class _Hm2AgentSwitchVlanStaticMrouterAdminMode_Type(HmEnabledStatus):
    """Custom type hm2AgentSwitchVlanStaticMrouterAdminMode based on HmEnabledStatus"""


_Hm2AgentSwitchVlanStaticMrouterAdminMode_Object = MibTableColumn
hm2AgentSwitchVlanStaticMrouterAdminMode = _Hm2AgentSwitchVlanStaticMrouterAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 9, 1, 1, 1),
    _Hm2AgentSwitchVlanStaticMrouterAdminMode_Type()
)
hm2AgentSwitchVlanStaticMrouterAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchVlanStaticMrouterAdminMode.setStatus("current")
_Hm2AgentSwitchMFDBGroup_ObjectIdentity = ObjectIdentity
hm2AgentSwitchMFDBGroup = _Hm2AgentSwitchMFDBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 10)
)
_Hm2AgentSwitchMFDBTable_Object = MibTable
hm2AgentSwitchMFDBTable = _Hm2AgentSwitchMFDBTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 10, 1)
)
if mibBuilder.loadTexts:
    hm2AgentSwitchMFDBTable.setStatus("current")
_Hm2AgentSwitchMFDBEntry_Object = MibTableRow
hm2AgentSwitchMFDBEntry = _Hm2AgentSwitchMFDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 10, 1, 1)
)
hm2AgentSwitchMFDBEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentSwitchMFDBVlanId"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentSwitchMFDBMacAddress"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentSwitchMFDBProtocolType"),
)
if mibBuilder.loadTexts:
    hm2AgentSwitchMFDBEntry.setStatus("current")
_Hm2AgentSwitchMFDBVlanId_Type = VlanIndex
_Hm2AgentSwitchMFDBVlanId_Object = MibTableColumn
hm2AgentSwitchMFDBVlanId = _Hm2AgentSwitchMFDBVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 10, 1, 1, 1),
    _Hm2AgentSwitchMFDBVlanId_Type()
)
hm2AgentSwitchMFDBVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchMFDBVlanId.setStatus("current")
_Hm2AgentSwitchMFDBMacAddress_Type = MacAddress
_Hm2AgentSwitchMFDBMacAddress_Object = MibTableColumn
hm2AgentSwitchMFDBMacAddress = _Hm2AgentSwitchMFDBMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 10, 1, 1, 2),
    _Hm2AgentSwitchMFDBMacAddress_Type()
)
hm2AgentSwitchMFDBMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchMFDBMacAddress.setStatus("current")


class _Hm2AgentSwitchMFDBProtocolType_Type(Integer32):
    """Custom type hm2AgentSwitchMFDBProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              248)
        )
    )
    namedValues = NamedValues(
        *(("gmrp", 2),
          ("igmp", 3),
          ("mld", 4),
          ("mrp-mmrp", 248),
          ("static", 1))
    )


_Hm2AgentSwitchMFDBProtocolType_Type.__name__ = "Integer32"
_Hm2AgentSwitchMFDBProtocolType_Object = MibTableColumn
hm2AgentSwitchMFDBProtocolType = _Hm2AgentSwitchMFDBProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 10, 1, 1, 3),
    _Hm2AgentSwitchMFDBProtocolType_Type()
)
hm2AgentSwitchMFDBProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchMFDBProtocolType.setStatus("current")


class _Hm2AgentSwitchMFDBType_Type(Integer32):
    """Custom type hm2AgentSwitchMFDBType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_Hm2AgentSwitchMFDBType_Type.__name__ = "Integer32"
_Hm2AgentSwitchMFDBType_Object = MibTableColumn
hm2AgentSwitchMFDBType = _Hm2AgentSwitchMFDBType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 10, 1, 1, 4),
    _Hm2AgentSwitchMFDBType_Type()
)
hm2AgentSwitchMFDBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchMFDBType.setStatus("current")
_Hm2AgentSwitchMFDBDescription_Type = DisplayString
_Hm2AgentSwitchMFDBDescription_Object = MibTableColumn
hm2AgentSwitchMFDBDescription = _Hm2AgentSwitchMFDBDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 10, 1, 1, 5),
    _Hm2AgentSwitchMFDBDescription_Type()
)
hm2AgentSwitchMFDBDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchMFDBDescription.setStatus("current")
_Hm2AgentSwitchMFDBForwardingPortMask_Type = Hm2AgentPortMask
_Hm2AgentSwitchMFDBForwardingPortMask_Object = MibTableColumn
hm2AgentSwitchMFDBForwardingPortMask = _Hm2AgentSwitchMFDBForwardingPortMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 10, 1, 1, 6),
    _Hm2AgentSwitchMFDBForwardingPortMask_Type()
)
hm2AgentSwitchMFDBForwardingPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchMFDBForwardingPortMask.setStatus("current")
_Hm2AgentSwitchMFDBFilteringPortMask_Type = Hm2AgentPortMask
_Hm2AgentSwitchMFDBFilteringPortMask_Object = MibTableColumn
hm2AgentSwitchMFDBFilteringPortMask = _Hm2AgentSwitchMFDBFilteringPortMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 10, 1, 1, 7),
    _Hm2AgentSwitchMFDBFilteringPortMask_Type()
)
hm2AgentSwitchMFDBFilteringPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchMFDBFilteringPortMask.setStatus("current")
_Hm2AgentSwitchMFDBSummaryTable_Object = MibTable
hm2AgentSwitchMFDBSummaryTable = _Hm2AgentSwitchMFDBSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 10, 2)
)
if mibBuilder.loadTexts:
    hm2AgentSwitchMFDBSummaryTable.setStatus("current")
_Hm2AgentSwitchMFDBSummaryEntry_Object = MibTableRow
hm2AgentSwitchMFDBSummaryEntry = _Hm2AgentSwitchMFDBSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 10, 2, 1)
)
hm2AgentSwitchMFDBSummaryEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentSwitchMFDBSummaryVlanId"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentSwitchMFDBSummaryMacAddress"),
)
if mibBuilder.loadTexts:
    hm2AgentSwitchMFDBSummaryEntry.setStatus("current")
_Hm2AgentSwitchMFDBSummaryVlanId_Type = VlanIndex
_Hm2AgentSwitchMFDBSummaryVlanId_Object = MibTableColumn
hm2AgentSwitchMFDBSummaryVlanId = _Hm2AgentSwitchMFDBSummaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 10, 2, 1, 1),
    _Hm2AgentSwitchMFDBSummaryVlanId_Type()
)
hm2AgentSwitchMFDBSummaryVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchMFDBSummaryVlanId.setStatus("current")
_Hm2AgentSwitchMFDBSummaryMacAddress_Type = MacAddress
_Hm2AgentSwitchMFDBSummaryMacAddress_Object = MibTableColumn
hm2AgentSwitchMFDBSummaryMacAddress = _Hm2AgentSwitchMFDBSummaryMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 10, 2, 1, 2),
    _Hm2AgentSwitchMFDBSummaryMacAddress_Type()
)
hm2AgentSwitchMFDBSummaryMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchMFDBSummaryMacAddress.setStatus("current")
_Hm2AgentSwitchMFDBSummaryForwardingPortMask_Type = Hm2AgentPortMask
_Hm2AgentSwitchMFDBSummaryForwardingPortMask_Object = MibTableColumn
hm2AgentSwitchMFDBSummaryForwardingPortMask = _Hm2AgentSwitchMFDBSummaryForwardingPortMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 10, 2, 1, 3),
    _Hm2AgentSwitchMFDBSummaryForwardingPortMask_Type()
)
hm2AgentSwitchMFDBSummaryForwardingPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchMFDBSummaryForwardingPortMask.setStatus("current")
_Hm2AgentSwitchMFDBMaxTableEntries_Type = Gauge32
_Hm2AgentSwitchMFDBMaxTableEntries_Object = MibScalar
hm2AgentSwitchMFDBMaxTableEntries = _Hm2AgentSwitchMFDBMaxTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 10, 3),
    _Hm2AgentSwitchMFDBMaxTableEntries_Type()
)
hm2AgentSwitchMFDBMaxTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchMFDBMaxTableEntries.setStatus("current")
_Hm2AgentSwitchMFDBMostEntriesUsed_Type = Gauge32
_Hm2AgentSwitchMFDBMostEntriesUsed_Object = MibScalar
hm2AgentSwitchMFDBMostEntriesUsed = _Hm2AgentSwitchMFDBMostEntriesUsed_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 10, 4),
    _Hm2AgentSwitchMFDBMostEntriesUsed_Type()
)
hm2AgentSwitchMFDBMostEntriesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchMFDBMostEntriesUsed.setStatus("current")
_Hm2AgentSwitchMFDBCurrentEntries_Type = Gauge32
_Hm2AgentSwitchMFDBCurrentEntries_Object = MibScalar
hm2AgentSwitchMFDBCurrentEntries = _Hm2AgentSwitchMFDBCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 10, 5),
    _Hm2AgentSwitchMFDBCurrentEntries_Type()
)
hm2AgentSwitchMFDBCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchMFDBCurrentEntries.setStatus("current")
_Hm2AgentSwitchVlanMacAssociationGroup_ObjectIdentity = ObjectIdentity
hm2AgentSwitchVlanMacAssociationGroup = _Hm2AgentSwitchVlanMacAssociationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 17)
)
_Hm2AgentSwitchVlanMacAssociationTable_Object = MibTable
hm2AgentSwitchVlanMacAssociationTable = _Hm2AgentSwitchVlanMacAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 17, 1)
)
if mibBuilder.loadTexts:
    hm2AgentSwitchVlanMacAssociationTable.setStatus("current")
_Hm2AgentSwitchVlanMacAssociationEntry_Object = MibTableRow
hm2AgentSwitchVlanMacAssociationEntry = _Hm2AgentSwitchVlanMacAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 17, 1, 1)
)
hm2AgentSwitchVlanMacAssociationEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentSwitchVlanMacAssociationMacAddress"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentSwitchVlanMacAssociationVlanId"),
)
if mibBuilder.loadTexts:
    hm2AgentSwitchVlanMacAssociationEntry.setStatus("current")
_Hm2AgentSwitchVlanMacAssociationMacAddress_Type = MacAddress
_Hm2AgentSwitchVlanMacAssociationMacAddress_Object = MibTableColumn
hm2AgentSwitchVlanMacAssociationMacAddress = _Hm2AgentSwitchVlanMacAssociationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 17, 1, 1, 1),
    _Hm2AgentSwitchVlanMacAssociationMacAddress_Type()
)
hm2AgentSwitchVlanMacAssociationMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentSwitchVlanMacAssociationMacAddress.setStatus("current")
_Hm2AgentSwitchVlanMacAssociationVlanId_Type = VlanIndex
_Hm2AgentSwitchVlanMacAssociationVlanId_Object = MibTableColumn
hm2AgentSwitchVlanMacAssociationVlanId = _Hm2AgentSwitchVlanMacAssociationVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 17, 1, 1, 2),
    _Hm2AgentSwitchVlanMacAssociationVlanId_Type()
)
hm2AgentSwitchVlanMacAssociationVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentSwitchVlanMacAssociationVlanId.setStatus("current")
_Hm2AgentSwitchVlanMacAssociationRowStatus_Type = RowStatus
_Hm2AgentSwitchVlanMacAssociationRowStatus_Object = MibTableColumn
hm2AgentSwitchVlanMacAssociationRowStatus = _Hm2AgentSwitchVlanMacAssociationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 17, 1, 1, 3),
    _Hm2AgentSwitchVlanMacAssociationRowStatus_Type()
)
hm2AgentSwitchVlanMacAssociationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentSwitchVlanMacAssociationRowStatus.setStatus("current")
_Hm2AgentSwitchProtectedPortConfigGroup_ObjectIdentity = ObjectIdentity
hm2AgentSwitchProtectedPortConfigGroup = _Hm2AgentSwitchProtectedPortConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 18)
)
_Hm2AgentSwitchProtectedPortTable_Object = MibTable
hm2AgentSwitchProtectedPortTable = _Hm2AgentSwitchProtectedPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 18, 1)
)
if mibBuilder.loadTexts:
    hm2AgentSwitchProtectedPortTable.setStatus("current")
_Hm2AgentSwitchProtectedPortEntry_Object = MibTableRow
hm2AgentSwitchProtectedPortEntry = _Hm2AgentSwitchProtectedPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 18, 1, 1)
)
hm2AgentSwitchProtectedPortEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentSwitchProtectedPortGroupId"),
)
if mibBuilder.loadTexts:
    hm2AgentSwitchProtectedPortEntry.setStatus("current")


class _Hm2AgentSwitchProtectedPortGroupId_Type(Integer32):
    """Custom type hm2AgentSwitchProtectedPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2AgentSwitchProtectedPortGroupId_Type.__name__ = "Integer32"
_Hm2AgentSwitchProtectedPortGroupId_Object = MibTableColumn
hm2AgentSwitchProtectedPortGroupId = _Hm2AgentSwitchProtectedPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 18, 1, 1, 1),
    _Hm2AgentSwitchProtectedPortGroupId_Type()
)
hm2AgentSwitchProtectedPortGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentSwitchProtectedPortGroupId.setStatus("current")


class _Hm2AgentSwitchProtectedPortGroupName_Type(DisplayString):
    """Custom type hm2AgentSwitchProtectedPortGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2AgentSwitchProtectedPortGroupName_Type.__name__ = "DisplayString"
_Hm2AgentSwitchProtectedPortGroupName_Object = MibTableColumn
hm2AgentSwitchProtectedPortGroupName = _Hm2AgentSwitchProtectedPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 18, 1, 1, 2),
    _Hm2AgentSwitchProtectedPortGroupName_Type()
)
hm2AgentSwitchProtectedPortGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchProtectedPortGroupName.setStatus("current")
_Hm2AgentSwitchProtectedPortPortList_Type = PortList
_Hm2AgentSwitchProtectedPortPortList_Object = MibTableColumn
hm2AgentSwitchProtectedPortPortList = _Hm2AgentSwitchProtectedPortPortList_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 18, 1, 1, 3),
    _Hm2AgentSwitchProtectedPortPortList_Type()
)
hm2AgentSwitchProtectedPortPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchProtectedPortPortList.setStatus("current")
_Hm2AgentSwitchVlanSubnetAssociationGroup_ObjectIdentity = ObjectIdentity
hm2AgentSwitchVlanSubnetAssociationGroup = _Hm2AgentSwitchVlanSubnetAssociationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 19)
)
_Hm2AgentSwitchVlanSubnetAssociationTable_Object = MibTable
hm2AgentSwitchVlanSubnetAssociationTable = _Hm2AgentSwitchVlanSubnetAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 19, 1)
)
if mibBuilder.loadTexts:
    hm2AgentSwitchVlanSubnetAssociationTable.setStatus("current")
_Hm2AgentSwitchVlanSubnetAssociationEntry_Object = MibTableRow
hm2AgentSwitchVlanSubnetAssociationEntry = _Hm2AgentSwitchVlanSubnetAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 19, 1, 1)
)
hm2AgentSwitchVlanSubnetAssociationEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentSwitchVlanSubnetAssociationIPAddress"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentSwitchVlanSubnetAssociationSubnetMask"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentSwitchVlanSubnetAssociationVlanId"),
)
if mibBuilder.loadTexts:
    hm2AgentSwitchVlanSubnetAssociationEntry.setStatus("current")
_Hm2AgentSwitchVlanSubnetAssociationIPAddress_Type = IpAddress
_Hm2AgentSwitchVlanSubnetAssociationIPAddress_Object = MibTableColumn
hm2AgentSwitchVlanSubnetAssociationIPAddress = _Hm2AgentSwitchVlanSubnetAssociationIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 19, 1, 1, 1),
    _Hm2AgentSwitchVlanSubnetAssociationIPAddress_Type()
)
hm2AgentSwitchVlanSubnetAssociationIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentSwitchVlanSubnetAssociationIPAddress.setStatus("current")
_Hm2AgentSwitchVlanSubnetAssociationSubnetMask_Type = IpAddress
_Hm2AgentSwitchVlanSubnetAssociationSubnetMask_Object = MibTableColumn
hm2AgentSwitchVlanSubnetAssociationSubnetMask = _Hm2AgentSwitchVlanSubnetAssociationSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 19, 1, 1, 2),
    _Hm2AgentSwitchVlanSubnetAssociationSubnetMask_Type()
)
hm2AgentSwitchVlanSubnetAssociationSubnetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentSwitchVlanSubnetAssociationSubnetMask.setStatus("current")
_Hm2AgentSwitchVlanSubnetAssociationVlanId_Type = VlanIndex
_Hm2AgentSwitchVlanSubnetAssociationVlanId_Object = MibTableColumn
hm2AgentSwitchVlanSubnetAssociationVlanId = _Hm2AgentSwitchVlanSubnetAssociationVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 19, 1, 1, 3),
    _Hm2AgentSwitchVlanSubnetAssociationVlanId_Type()
)
hm2AgentSwitchVlanSubnetAssociationVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentSwitchVlanSubnetAssociationVlanId.setStatus("current")
_Hm2AgentSwitchVlanSubnetAssociationRowStatus_Type = RowStatus
_Hm2AgentSwitchVlanSubnetAssociationRowStatus_Object = MibTableColumn
hm2AgentSwitchVlanSubnetAssociationRowStatus = _Hm2AgentSwitchVlanSubnetAssociationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 19, 1, 1, 4),
    _Hm2AgentSwitchVlanSubnetAssociationRowStatus_Type()
)
hm2AgentSwitchVlanSubnetAssociationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentSwitchVlanSubnetAssociationRowStatus.setStatus("current")
_Hm2AgentSwitchSnoopingQuerierGroup_ObjectIdentity = ObjectIdentity
hm2AgentSwitchSnoopingQuerierGroup = _Hm2AgentSwitchSnoopingQuerierGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 20)
)
_Hm2AgentSwitchSnoopingQuerierCfgTable_Object = MibTable
hm2AgentSwitchSnoopingQuerierCfgTable = _Hm2AgentSwitchSnoopingQuerierCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 20, 1)
)
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingQuerierCfgTable.setStatus("current")
_Hm2AgentSwitchSnoopingQuerierCfgEntry_Object = MibTableRow
hm2AgentSwitchSnoopingQuerierCfgEntry = _Hm2AgentSwitchSnoopingQuerierCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 20, 1, 1)
)
hm2AgentSwitchSnoopingQuerierCfgEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentSwitchSnoopingProtocol"),
)
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingQuerierCfgEntry.setStatus("current")


class _Hm2AgentSwitchSnoopingQuerierAdminMode_Type(HmEnabledStatus):
    """Custom type hm2AgentSwitchSnoopingQuerierAdminMode based on HmEnabledStatus"""


_Hm2AgentSwitchSnoopingQuerierAdminMode_Object = MibTableColumn
hm2AgentSwitchSnoopingQuerierAdminMode = _Hm2AgentSwitchSnoopingQuerierAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 20, 1, 1, 1),
    _Hm2AgentSwitchSnoopingQuerierAdminMode_Type()
)
hm2AgentSwitchSnoopingQuerierAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingQuerierAdminMode.setStatus("current")


class _Hm2AgentSwitchSnoopingQuerierVersion_Type(Integer32):
    """Custom type hm2AgentSwitchSnoopingQuerierVersion based on Integer32"""
    defaultValue = 2


_Hm2AgentSwitchSnoopingQuerierVersion_Object = MibTableColumn
hm2AgentSwitchSnoopingQuerierVersion = _Hm2AgentSwitchSnoopingQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 20, 1, 1, 2),
    _Hm2AgentSwitchSnoopingQuerierVersion_Type()
)
hm2AgentSwitchSnoopingQuerierVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingQuerierVersion.setStatus("current")


class _Hm2AgentSwitchSnoopingQuerierQueryInterval_Type(Integer32):
    """Custom type hm2AgentSwitchSnoopingQuerierQueryInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_Hm2AgentSwitchSnoopingQuerierQueryInterval_Type.__name__ = "Integer32"
_Hm2AgentSwitchSnoopingQuerierQueryInterval_Object = MibTableColumn
hm2AgentSwitchSnoopingQuerierQueryInterval = _Hm2AgentSwitchSnoopingQuerierQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 20, 1, 1, 4),
    _Hm2AgentSwitchSnoopingQuerierQueryInterval_Type()
)
hm2AgentSwitchSnoopingQuerierQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingQuerierQueryInterval.setStatus("current")


class _Hm2AgentSwitchSnoopingQuerierExpiryInterval_Type(Integer32):
    """Custom type hm2AgentSwitchSnoopingQuerierExpiryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_Hm2AgentSwitchSnoopingQuerierExpiryInterval_Type.__name__ = "Integer32"
_Hm2AgentSwitchSnoopingQuerierExpiryInterval_Object = MibTableColumn
hm2AgentSwitchSnoopingQuerierExpiryInterval = _Hm2AgentSwitchSnoopingQuerierExpiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 20, 1, 1, 5),
    _Hm2AgentSwitchSnoopingQuerierExpiryInterval_Type()
)
hm2AgentSwitchSnoopingQuerierExpiryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingQuerierExpiryInterval.setStatus("current")
_Hm2AgentSwitchSnoopingQuerierVlanTable_Object = MibTable
hm2AgentSwitchSnoopingQuerierVlanTable = _Hm2AgentSwitchSnoopingQuerierVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 20, 2)
)
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingQuerierVlanTable.setStatus("current")
_Hm2AgentSwitchSnoopingQuerierVlanEntry_Object = MibTableRow
hm2AgentSwitchSnoopingQuerierVlanEntry = _Hm2AgentSwitchSnoopingQuerierVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 20, 2, 1)
)
hm2AgentSwitchSnoopingQuerierVlanEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentSwitchSnoopingProtocol"),
)
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingQuerierVlanEntry.setStatus("current")


class _Hm2AgentSwitchSnoopingQuerierVlanAdminMode_Type(HmEnabledStatus):
    """Custom type hm2AgentSwitchSnoopingQuerierVlanAdminMode based on HmEnabledStatus"""


_Hm2AgentSwitchSnoopingQuerierVlanAdminMode_Object = MibTableColumn
hm2AgentSwitchSnoopingQuerierVlanAdminMode = _Hm2AgentSwitchSnoopingQuerierVlanAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 20, 2, 1, 1),
    _Hm2AgentSwitchSnoopingQuerierVlanAdminMode_Type()
)
hm2AgentSwitchSnoopingQuerierVlanAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingQuerierVlanAdminMode.setStatus("current")


class _Hm2AgentSwitchSnoopingQuerierVlanOperMode_Type(Integer32):
    """Custom type hm2AgentSwitchSnoopingQuerierVlanOperMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("non-querier", 2),
          ("querier", 1))
    )


_Hm2AgentSwitchSnoopingQuerierVlanOperMode_Type.__name__ = "Integer32"
_Hm2AgentSwitchSnoopingQuerierVlanOperMode_Object = MibTableColumn
hm2AgentSwitchSnoopingQuerierVlanOperMode = _Hm2AgentSwitchSnoopingQuerierVlanOperMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 20, 2, 1, 2),
    _Hm2AgentSwitchSnoopingQuerierVlanOperMode_Type()
)
hm2AgentSwitchSnoopingQuerierVlanOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingQuerierVlanOperMode.setStatus("current")


class _Hm2AgentSwitchSnoopingQuerierElectionParticipateMode_Type(HmEnabledStatus):
    """Custom type hm2AgentSwitchSnoopingQuerierElectionParticipateMode based on HmEnabledStatus"""


_Hm2AgentSwitchSnoopingQuerierElectionParticipateMode_Object = MibTableColumn
hm2AgentSwitchSnoopingQuerierElectionParticipateMode = _Hm2AgentSwitchSnoopingQuerierElectionParticipateMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 20, 2, 1, 3),
    _Hm2AgentSwitchSnoopingQuerierElectionParticipateMode_Type()
)
hm2AgentSwitchSnoopingQuerierElectionParticipateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingQuerierElectionParticipateMode.setStatus("deprecated")


class _Hm2AgentSwitchSnoopingQuerierVlanAddress_Type(InetAddress):
    """Custom type hm2AgentSwitchSnoopingQuerierVlanAddress based on InetAddress"""
    defaultHexValue = "00000000"


_Hm2AgentSwitchSnoopingQuerierVlanAddress_Object = MibTableColumn
hm2AgentSwitchSnoopingQuerierVlanAddress = _Hm2AgentSwitchSnoopingQuerierVlanAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 20, 2, 1, 4),
    _Hm2AgentSwitchSnoopingQuerierVlanAddress_Type()
)
hm2AgentSwitchSnoopingQuerierVlanAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingQuerierVlanAddress.setStatus("current")
_Hm2AgentSwitchSnoopingQuerierOperVersion_Type = Integer32
_Hm2AgentSwitchSnoopingQuerierOperVersion_Object = MibTableColumn
hm2AgentSwitchSnoopingQuerierOperVersion = _Hm2AgentSwitchSnoopingQuerierOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 20, 2, 1, 5),
    _Hm2AgentSwitchSnoopingQuerierOperVersion_Type()
)
hm2AgentSwitchSnoopingQuerierOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingQuerierOperVersion.setStatus("current")


class _Hm2AgentSwitchSnoopingQuerierOperMaxResponseTime_Type(Integer32):
    """Custom type hm2AgentSwitchSnoopingQuerierOperMaxResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2AgentSwitchSnoopingQuerierOperMaxResponseTime_Type.__name__ = "Integer32"
_Hm2AgentSwitchSnoopingQuerierOperMaxResponseTime_Object = MibTableColumn
hm2AgentSwitchSnoopingQuerierOperMaxResponseTime = _Hm2AgentSwitchSnoopingQuerierOperMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 20, 2, 1, 6),
    _Hm2AgentSwitchSnoopingQuerierOperMaxResponseTime_Type()
)
hm2AgentSwitchSnoopingQuerierOperMaxResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingQuerierOperMaxResponseTime.setStatus("current")
_Hm2AgentSwitchSnoopingQuerierLastQuerierAddress_Type = InetAddress
_Hm2AgentSwitchSnoopingQuerierLastQuerierAddress_Object = MibTableColumn
hm2AgentSwitchSnoopingQuerierLastQuerierAddress = _Hm2AgentSwitchSnoopingQuerierLastQuerierAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 20, 2, 1, 7),
    _Hm2AgentSwitchSnoopingQuerierLastQuerierAddress_Type()
)
hm2AgentSwitchSnoopingQuerierLastQuerierAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingQuerierLastQuerierAddress.setStatus("current")
_Hm2AgentSwitchSnoopingQuerierLastQuerierVersion_Type = Integer32
_Hm2AgentSwitchSnoopingQuerierLastQuerierVersion_Object = MibTableColumn
hm2AgentSwitchSnoopingQuerierLastQuerierVersion = _Hm2AgentSwitchSnoopingQuerierLastQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 20, 2, 1, 8),
    _Hm2AgentSwitchSnoopingQuerierLastQuerierVersion_Type()
)
hm2AgentSwitchSnoopingQuerierLastQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchSnoopingQuerierLastQuerierVersion.setStatus("current")
_Hm2AgentDaiConfigGroup_ObjectIdentity = ObjectIdentity
hm2AgentDaiConfigGroup = _Hm2AgentDaiConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21)
)


class _Hm2AgentDaiSrcMacValidate_Type(TruthValue):
    """Custom type hm2AgentDaiSrcMacValidate based on TruthValue"""


_Hm2AgentDaiSrcMacValidate_Object = MibScalar
hm2AgentDaiSrcMacValidate = _Hm2AgentDaiSrcMacValidate_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 1),
    _Hm2AgentDaiSrcMacValidate_Type()
)
hm2AgentDaiSrcMacValidate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDaiSrcMacValidate.setStatus("current")


class _Hm2AgentDaiDstMacValidate_Type(TruthValue):
    """Custom type hm2AgentDaiDstMacValidate based on TruthValue"""


_Hm2AgentDaiDstMacValidate_Object = MibScalar
hm2AgentDaiDstMacValidate = _Hm2AgentDaiDstMacValidate_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 2),
    _Hm2AgentDaiDstMacValidate_Type()
)
hm2AgentDaiDstMacValidate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDaiDstMacValidate.setStatus("current")


class _Hm2AgentDaiIPValidate_Type(TruthValue):
    """Custom type hm2AgentDaiIPValidate based on TruthValue"""


_Hm2AgentDaiIPValidate_Object = MibScalar
hm2AgentDaiIPValidate = _Hm2AgentDaiIPValidate_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 3),
    _Hm2AgentDaiIPValidate_Type()
)
hm2AgentDaiIPValidate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDaiIPValidate.setStatus("current")
_Hm2AgentDaiVlanConfigTable_Object = MibTable
hm2AgentDaiVlanConfigTable = _Hm2AgentDaiVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 4)
)
if mibBuilder.loadTexts:
    hm2AgentDaiVlanConfigTable.setStatus("current")
_Hm2AgentDaiVlanConfigEntry_Object = MibTableRow
hm2AgentDaiVlanConfigEntry = _Hm2AgentDaiVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 4, 1)
)
hm2AgentDaiVlanConfigEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentDaiVlanIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentDaiVlanConfigEntry.setStatus("current")
_Hm2AgentDaiVlanIndex_Type = VlanIndex
_Hm2AgentDaiVlanIndex_Object = MibTableColumn
hm2AgentDaiVlanIndex = _Hm2AgentDaiVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 4, 1, 1),
    _Hm2AgentDaiVlanIndex_Type()
)
hm2AgentDaiVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDaiVlanIndex.setStatus("current")


class _Hm2AgentDaiVlanDynArpInspEnable_Type(TruthValue):
    """Custom type hm2AgentDaiVlanDynArpInspEnable based on TruthValue"""


_Hm2AgentDaiVlanDynArpInspEnable_Object = MibTableColumn
hm2AgentDaiVlanDynArpInspEnable = _Hm2AgentDaiVlanDynArpInspEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 4, 1, 2),
    _Hm2AgentDaiVlanDynArpInspEnable_Type()
)
hm2AgentDaiVlanDynArpInspEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDaiVlanDynArpInspEnable.setStatus("current")


class _Hm2AgentDaiVlanLoggingEnable_Type(TruthValue):
    """Custom type hm2AgentDaiVlanLoggingEnable based on TruthValue"""


_Hm2AgentDaiVlanLoggingEnable_Object = MibTableColumn
hm2AgentDaiVlanLoggingEnable = _Hm2AgentDaiVlanLoggingEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 4, 1, 3),
    _Hm2AgentDaiVlanLoggingEnable_Type()
)
hm2AgentDaiVlanLoggingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDaiVlanLoggingEnable.setStatus("current")


class _Hm2AgentDaiVlanArpAclName_Type(DisplayString):
    """Custom type hm2AgentDaiVlanArpAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hm2AgentDaiVlanArpAclName_Type.__name__ = "DisplayString"
_Hm2AgentDaiVlanArpAclName_Object = MibTableColumn
hm2AgentDaiVlanArpAclName = _Hm2AgentDaiVlanArpAclName_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 4, 1, 4),
    _Hm2AgentDaiVlanArpAclName_Type()
)
hm2AgentDaiVlanArpAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDaiVlanArpAclName.setStatus("current")


class _Hm2AgentDaiVlanArpAclStaticFlag_Type(TruthValue):
    """Custom type hm2AgentDaiVlanArpAclStaticFlag based on TruthValue"""


_Hm2AgentDaiVlanArpAclStaticFlag_Object = MibTableColumn
hm2AgentDaiVlanArpAclStaticFlag = _Hm2AgentDaiVlanArpAclStaticFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 4, 1, 5),
    _Hm2AgentDaiVlanArpAclStaticFlag_Type()
)
hm2AgentDaiVlanArpAclStaticFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDaiVlanArpAclStaticFlag.setStatus("current")


class _Hm2AgentDaiVlanBindingCheckEnable_Type(TruthValue):
    """Custom type hm2AgentDaiVlanBindingCheckEnable based on TruthValue"""


_Hm2AgentDaiVlanBindingCheckEnable_Object = MibTableColumn
hm2AgentDaiVlanBindingCheckEnable = _Hm2AgentDaiVlanBindingCheckEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 4, 1, 248),
    _Hm2AgentDaiVlanBindingCheckEnable_Type()
)
hm2AgentDaiVlanBindingCheckEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDaiVlanBindingCheckEnable.setStatus("current")


class _Hm2AgentDaiStatsReset_Type(Integer32):
    """Custom type hm2AgentDaiStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_Hm2AgentDaiStatsReset_Type.__name__ = "Integer32"
_Hm2AgentDaiStatsReset_Object = MibScalar
hm2AgentDaiStatsReset = _Hm2AgentDaiStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 5),
    _Hm2AgentDaiStatsReset_Type()
)
hm2AgentDaiStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDaiStatsReset.setStatus("current")
_Hm2AgentDaiVlanStatsTable_Object = MibTable
hm2AgentDaiVlanStatsTable = _Hm2AgentDaiVlanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 6)
)
if mibBuilder.loadTexts:
    hm2AgentDaiVlanStatsTable.setStatus("current")
_Hm2AgentDaiVlanStatsEntry_Object = MibTableRow
hm2AgentDaiVlanStatsEntry = _Hm2AgentDaiVlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 6, 1)
)
hm2AgentDaiVlanStatsEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentDaiVlanStatsIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentDaiVlanStatsEntry.setStatus("current")
_Hm2AgentDaiVlanStatsIndex_Type = VlanIndex
_Hm2AgentDaiVlanStatsIndex_Object = MibTableColumn
hm2AgentDaiVlanStatsIndex = _Hm2AgentDaiVlanStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 6, 1, 1),
    _Hm2AgentDaiVlanStatsIndex_Type()
)
hm2AgentDaiVlanStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDaiVlanStatsIndex.setStatus("current")
_Hm2AgentDaiVlanPktsForwarded_Type = Counter32
_Hm2AgentDaiVlanPktsForwarded_Object = MibTableColumn
hm2AgentDaiVlanPktsForwarded = _Hm2AgentDaiVlanPktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 6, 1, 2),
    _Hm2AgentDaiVlanPktsForwarded_Type()
)
hm2AgentDaiVlanPktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDaiVlanPktsForwarded.setStatus("current")
_Hm2AgentDaiVlanPktsDropped_Type = Counter32
_Hm2AgentDaiVlanPktsDropped_Object = MibTableColumn
hm2AgentDaiVlanPktsDropped = _Hm2AgentDaiVlanPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 6, 1, 3),
    _Hm2AgentDaiVlanPktsDropped_Type()
)
hm2AgentDaiVlanPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDaiVlanPktsDropped.setStatus("current")
_Hm2AgentDaiVlanDhcpDrops_Type = Counter32
_Hm2AgentDaiVlanDhcpDrops_Object = MibTableColumn
hm2AgentDaiVlanDhcpDrops = _Hm2AgentDaiVlanDhcpDrops_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 6, 1, 4),
    _Hm2AgentDaiVlanDhcpDrops_Type()
)
hm2AgentDaiVlanDhcpDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDaiVlanDhcpDrops.setStatus("current")
_Hm2AgentDaiVlanDhcpPermits_Type = Counter32
_Hm2AgentDaiVlanDhcpPermits_Object = MibTableColumn
hm2AgentDaiVlanDhcpPermits = _Hm2AgentDaiVlanDhcpPermits_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 6, 1, 5),
    _Hm2AgentDaiVlanDhcpPermits_Type()
)
hm2AgentDaiVlanDhcpPermits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDaiVlanDhcpPermits.setStatus("current")
_Hm2AgentDaiVlanAclDrops_Type = Counter32
_Hm2AgentDaiVlanAclDrops_Object = MibTableColumn
hm2AgentDaiVlanAclDrops = _Hm2AgentDaiVlanAclDrops_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 6, 1, 6),
    _Hm2AgentDaiVlanAclDrops_Type()
)
hm2AgentDaiVlanAclDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDaiVlanAclDrops.setStatus("current")
_Hm2AgentDaiVlanAclPermits_Type = Counter32
_Hm2AgentDaiVlanAclPermits_Object = MibTableColumn
hm2AgentDaiVlanAclPermits = _Hm2AgentDaiVlanAclPermits_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 6, 1, 7),
    _Hm2AgentDaiVlanAclPermits_Type()
)
hm2AgentDaiVlanAclPermits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDaiVlanAclPermits.setStatus("current")
_Hm2AgentDaiVlanSrcMacFailures_Type = Counter32
_Hm2AgentDaiVlanSrcMacFailures_Object = MibTableColumn
hm2AgentDaiVlanSrcMacFailures = _Hm2AgentDaiVlanSrcMacFailures_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 6, 1, 8),
    _Hm2AgentDaiVlanSrcMacFailures_Type()
)
hm2AgentDaiVlanSrcMacFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDaiVlanSrcMacFailures.setStatus("current")
_Hm2AgentDaiVlanDstMacFailures_Type = Counter32
_Hm2AgentDaiVlanDstMacFailures_Object = MibTableColumn
hm2AgentDaiVlanDstMacFailures = _Hm2AgentDaiVlanDstMacFailures_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 6, 1, 9),
    _Hm2AgentDaiVlanDstMacFailures_Type()
)
hm2AgentDaiVlanDstMacFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDaiVlanDstMacFailures.setStatus("current")
_Hm2AgentDaiVlanIpValidFailures_Type = Counter32
_Hm2AgentDaiVlanIpValidFailures_Object = MibTableColumn
hm2AgentDaiVlanIpValidFailures = _Hm2AgentDaiVlanIpValidFailures_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 6, 1, 10),
    _Hm2AgentDaiVlanIpValidFailures_Type()
)
hm2AgentDaiVlanIpValidFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDaiVlanIpValidFailures.setStatus("current")
_Hm2AgentDaiIfConfigTable_Object = MibTable
hm2AgentDaiIfConfigTable = _Hm2AgentDaiIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 7)
)
if mibBuilder.loadTexts:
    hm2AgentDaiIfConfigTable.setStatus("current")
_Hm2AgentDaiIfConfigEntry_Object = MibTableRow
hm2AgentDaiIfConfigEntry = _Hm2AgentDaiIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 7, 1)
)
hm2AgentDaiIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentDaiIfConfigEntry.setStatus("current")


class _Hm2AgentDaiIfTrustEnable_Type(TruthValue):
    """Custom type hm2AgentDaiIfTrustEnable based on TruthValue"""


_Hm2AgentDaiIfTrustEnable_Object = MibTableColumn
hm2AgentDaiIfTrustEnable = _Hm2AgentDaiIfTrustEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 7, 1, 1),
    _Hm2AgentDaiIfTrustEnable_Type()
)
hm2AgentDaiIfTrustEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDaiIfTrustEnable.setStatus("current")


class _Hm2AgentDaiIfRateLimit_Type(Integer32):
    """Custom type hm2AgentDaiIfRateLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 300),
    )


_Hm2AgentDaiIfRateLimit_Type.__name__ = "Integer32"
_Hm2AgentDaiIfRateLimit_Object = MibTableColumn
hm2AgentDaiIfRateLimit = _Hm2AgentDaiIfRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 7, 1, 2),
    _Hm2AgentDaiIfRateLimit_Type()
)
hm2AgentDaiIfRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDaiIfRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    hm2AgentDaiIfRateLimit.setUnits("packets per second")


class _Hm2AgentDaiIfBurstInterval_Type(Unsigned32):
    """Custom type hm2AgentDaiIfBurstInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Hm2AgentDaiIfBurstInterval_Type.__name__ = "Unsigned32"
_Hm2AgentDaiIfBurstInterval_Object = MibTableColumn
hm2AgentDaiIfBurstInterval = _Hm2AgentDaiIfBurstInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 7, 1, 3),
    _Hm2AgentDaiIfBurstInterval_Type()
)
hm2AgentDaiIfBurstInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDaiIfBurstInterval.setStatus("current")


class _Hm2AgentDaiIfAutoDisable_Type(TruthValue):
    """Custom type hm2AgentDaiIfAutoDisable based on TruthValue"""


_Hm2AgentDaiIfAutoDisable_Object = MibTableColumn
hm2AgentDaiIfAutoDisable = _Hm2AgentDaiIfAutoDisable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 21, 7, 1, 248),
    _Hm2AgentDaiIfAutoDisable_Type()
)
hm2AgentDaiIfAutoDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDaiIfAutoDisable.setStatus("current")
_Hm2AgentArpAclGroup_ObjectIdentity = ObjectIdentity
hm2AgentArpAclGroup = _Hm2AgentArpAclGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 22)
)
_Hm2AgentArpAclTable_Object = MibTable
hm2AgentArpAclTable = _Hm2AgentArpAclTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 22, 1)
)
if mibBuilder.loadTexts:
    hm2AgentArpAclTable.setStatus("current")
_Hm2AgentArpAclEntry_Object = MibTableRow
hm2AgentArpAclEntry = _Hm2AgentArpAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 22, 1, 1)
)
hm2AgentArpAclEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentArpAclName"),
)
if mibBuilder.loadTexts:
    hm2AgentArpAclEntry.setStatus("current")


class _Hm2AgentArpAclName_Type(DisplayString):
    """Custom type hm2AgentArpAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Hm2AgentArpAclName_Type.__name__ = "DisplayString"
_Hm2AgentArpAclName_Object = MibTableColumn
hm2AgentArpAclName = _Hm2AgentArpAclName_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 22, 1, 1, 1),
    _Hm2AgentArpAclName_Type()
)
hm2AgentArpAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentArpAclName.setStatus("current")
_Hm2AgentArpAclRowStatus_Type = RowStatus
_Hm2AgentArpAclRowStatus_Object = MibTableColumn
hm2AgentArpAclRowStatus = _Hm2AgentArpAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 22, 1, 1, 2),
    _Hm2AgentArpAclRowStatus_Type()
)
hm2AgentArpAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentArpAclRowStatus.setStatus("current")
_Hm2AgentArpAclRuleTable_Object = MibTable
hm2AgentArpAclRuleTable = _Hm2AgentArpAclRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 22, 2)
)
if mibBuilder.loadTexts:
    hm2AgentArpAclRuleTable.setStatus("current")
_Hm2AgentArpAclRuleEntry_Object = MibTableRow
hm2AgentArpAclRuleEntry = _Hm2AgentArpAclRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 22, 2, 1)
)
hm2AgentArpAclRuleEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentArpAclName"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentArpAclRuleMatchSenderIpAddr"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentArpAclRuleMatchSenderMacAddr"),
)
if mibBuilder.loadTexts:
    hm2AgentArpAclRuleEntry.setStatus("current")
_Hm2AgentArpAclRuleMatchSenderIpAddr_Type = IpAddress
_Hm2AgentArpAclRuleMatchSenderIpAddr_Object = MibTableColumn
hm2AgentArpAclRuleMatchSenderIpAddr = _Hm2AgentArpAclRuleMatchSenderIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 22, 2, 1, 1),
    _Hm2AgentArpAclRuleMatchSenderIpAddr_Type()
)
hm2AgentArpAclRuleMatchSenderIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentArpAclRuleMatchSenderIpAddr.setStatus("current")
_Hm2AgentArpAclRuleMatchSenderMacAddr_Type = MacAddress
_Hm2AgentArpAclRuleMatchSenderMacAddr_Object = MibTableColumn
hm2AgentArpAclRuleMatchSenderMacAddr = _Hm2AgentArpAclRuleMatchSenderMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 22, 2, 1, 2),
    _Hm2AgentArpAclRuleMatchSenderMacAddr_Type()
)
hm2AgentArpAclRuleMatchSenderMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentArpAclRuleMatchSenderMacAddr.setStatus("current")
_Hm2AgentArpAclRuleRowStatus_Type = RowStatus
_Hm2AgentArpAclRuleRowStatus_Object = MibTableColumn
hm2AgentArpAclRuleRowStatus = _Hm2AgentArpAclRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 22, 2, 1, 3),
    _Hm2AgentArpAclRuleRowStatus_Type()
)
hm2AgentArpAclRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentArpAclRuleRowStatus.setStatus("current")
_Hm2AgentDhcpSnoopingConfigGroup_ObjectIdentity = ObjectIdentity
hm2AgentDhcpSnoopingConfigGroup = _Hm2AgentDhcpSnoopingConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23)
)


class _Hm2AgentDhcpSnoopingAdminMode_Type(TruthValue):
    """Custom type hm2AgentDhcpSnoopingAdminMode based on TruthValue"""


_Hm2AgentDhcpSnoopingAdminMode_Object = MibScalar
hm2AgentDhcpSnoopingAdminMode = _Hm2AgentDhcpSnoopingAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 1),
    _Hm2AgentDhcpSnoopingAdminMode_Type()
)
hm2AgentDhcpSnoopingAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDhcpSnoopingAdminMode.setStatus("current")


class _Hm2AgentDhcpSnoopingVerifyMac_Type(TruthValue):
    """Custom type hm2AgentDhcpSnoopingVerifyMac based on TruthValue"""


_Hm2AgentDhcpSnoopingVerifyMac_Object = MibScalar
hm2AgentDhcpSnoopingVerifyMac = _Hm2AgentDhcpSnoopingVerifyMac_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 2),
    _Hm2AgentDhcpSnoopingVerifyMac_Type()
)
hm2AgentDhcpSnoopingVerifyMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDhcpSnoopingVerifyMac.setStatus("current")
_Hm2AgentDhcpSnoopingVlanConfigTable_Object = MibTable
hm2AgentDhcpSnoopingVlanConfigTable = _Hm2AgentDhcpSnoopingVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 3)
)
if mibBuilder.loadTexts:
    hm2AgentDhcpSnoopingVlanConfigTable.setStatus("current")
_Hm2AgentDhcpSnoopingVlanConfigEntry_Object = MibTableRow
hm2AgentDhcpSnoopingVlanConfigEntry = _Hm2AgentDhcpSnoopingVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 3, 1)
)
hm2AgentDhcpSnoopingVlanConfigEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentDhcpSnoopingVlanIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentDhcpSnoopingVlanConfigEntry.setStatus("current")
_Hm2AgentDhcpSnoopingVlanIndex_Type = VlanIndex
_Hm2AgentDhcpSnoopingVlanIndex_Object = MibTableColumn
hm2AgentDhcpSnoopingVlanIndex = _Hm2AgentDhcpSnoopingVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 3, 1, 1),
    _Hm2AgentDhcpSnoopingVlanIndex_Type()
)
hm2AgentDhcpSnoopingVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDhcpSnoopingVlanIndex.setStatus("current")


class _Hm2AgentDhcpSnoopingVlanEnable_Type(TruthValue):
    """Custom type hm2AgentDhcpSnoopingVlanEnable based on TruthValue"""


_Hm2AgentDhcpSnoopingVlanEnable_Object = MibTableColumn
hm2AgentDhcpSnoopingVlanEnable = _Hm2AgentDhcpSnoopingVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 3, 1, 2),
    _Hm2AgentDhcpSnoopingVlanEnable_Type()
)
hm2AgentDhcpSnoopingVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDhcpSnoopingVlanEnable.setStatus("current")
_Hm2AgentDhcpSnoopingIfConfigTable_Object = MibTable
hm2AgentDhcpSnoopingIfConfigTable = _Hm2AgentDhcpSnoopingIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 4)
)
if mibBuilder.loadTexts:
    hm2AgentDhcpSnoopingIfConfigTable.setStatus("current")
_Hm2AgentDhcpSnoopingIfConfigEntry_Object = MibTableRow
hm2AgentDhcpSnoopingIfConfigEntry = _Hm2AgentDhcpSnoopingIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 4, 1)
)
hm2AgentDhcpSnoopingIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentDhcpSnoopingIfConfigEntry.setStatus("current")


class _Hm2AgentDhcpSnoopingIfTrustEnable_Type(TruthValue):
    """Custom type hm2AgentDhcpSnoopingIfTrustEnable based on TruthValue"""


_Hm2AgentDhcpSnoopingIfTrustEnable_Object = MibTableColumn
hm2AgentDhcpSnoopingIfTrustEnable = _Hm2AgentDhcpSnoopingIfTrustEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 4, 1, 1),
    _Hm2AgentDhcpSnoopingIfTrustEnable_Type()
)
hm2AgentDhcpSnoopingIfTrustEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDhcpSnoopingIfTrustEnable.setStatus("current")


class _Hm2AgentDhcpSnoopingIfLogEnable_Type(TruthValue):
    """Custom type hm2AgentDhcpSnoopingIfLogEnable based on TruthValue"""


_Hm2AgentDhcpSnoopingIfLogEnable_Object = MibTableColumn
hm2AgentDhcpSnoopingIfLogEnable = _Hm2AgentDhcpSnoopingIfLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 4, 1, 2),
    _Hm2AgentDhcpSnoopingIfLogEnable_Type()
)
hm2AgentDhcpSnoopingIfLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDhcpSnoopingIfLogEnable.setStatus("current")


class _Hm2AgentDhcpSnoopingIfRateLimit_Type(Integer32):
    """Custom type hm2AgentDhcpSnoopingIfRateLimit based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 150),
    )


_Hm2AgentDhcpSnoopingIfRateLimit_Type.__name__ = "Integer32"
_Hm2AgentDhcpSnoopingIfRateLimit_Object = MibTableColumn
hm2AgentDhcpSnoopingIfRateLimit = _Hm2AgentDhcpSnoopingIfRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 4, 1, 3),
    _Hm2AgentDhcpSnoopingIfRateLimit_Type()
)
hm2AgentDhcpSnoopingIfRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDhcpSnoopingIfRateLimit.setStatus("current")
if mibBuilder.loadTexts:
    hm2AgentDhcpSnoopingIfRateLimit.setUnits("packets per second")


class _Hm2AgentDhcpSnoopingIfBurstInterval_Type(Integer32):
    """Custom type hm2AgentDhcpSnoopingIfBurstInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Hm2AgentDhcpSnoopingIfBurstInterval_Type.__name__ = "Integer32"
_Hm2AgentDhcpSnoopingIfBurstInterval_Object = MibTableColumn
hm2AgentDhcpSnoopingIfBurstInterval = _Hm2AgentDhcpSnoopingIfBurstInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 4, 1, 4),
    _Hm2AgentDhcpSnoopingIfBurstInterval_Type()
)
hm2AgentDhcpSnoopingIfBurstInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDhcpSnoopingIfBurstInterval.setStatus("current")


class _Hm2AgentDhcpSnoopingIfAutoDisable_Type(TruthValue):
    """Custom type hm2AgentDhcpSnoopingIfAutoDisable based on TruthValue"""


_Hm2AgentDhcpSnoopingIfAutoDisable_Object = MibTableColumn
hm2AgentDhcpSnoopingIfAutoDisable = _Hm2AgentDhcpSnoopingIfAutoDisable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 4, 1, 248),
    _Hm2AgentDhcpSnoopingIfAutoDisable_Type()
)
hm2AgentDhcpSnoopingIfAutoDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDhcpSnoopingIfAutoDisable.setStatus("current")
_Hm2AgentIpsgIfConfigTable_Object = MibTable
hm2AgentIpsgIfConfigTable = _Hm2AgentIpsgIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 5)
)
if mibBuilder.loadTexts:
    hm2AgentIpsgIfConfigTable.setStatus("current")
_Hm2AgentIpsgIfConfigEntry_Object = MibTableRow
hm2AgentIpsgIfConfigEntry = _Hm2AgentIpsgIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 5, 1)
)
hm2AgentIpsgIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentIpsgIfConfigEntry.setStatus("current")


class _Hm2AgentIpsgIfVerifySource_Type(TruthValue):
    """Custom type hm2AgentIpsgIfVerifySource based on TruthValue"""


_Hm2AgentIpsgIfVerifySource_Object = MibTableColumn
hm2AgentIpsgIfVerifySource = _Hm2AgentIpsgIfVerifySource_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 5, 1, 1),
    _Hm2AgentIpsgIfVerifySource_Type()
)
hm2AgentIpsgIfVerifySource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentIpsgIfVerifySource.setStatus("current")


class _Hm2AgentIpsgIfPortSecurity_Type(TruthValue):
    """Custom type hm2AgentIpsgIfPortSecurity based on TruthValue"""


_Hm2AgentIpsgIfPortSecurity_Object = MibTableColumn
hm2AgentIpsgIfPortSecurity = _Hm2AgentIpsgIfPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 5, 1, 2),
    _Hm2AgentIpsgIfPortSecurity_Type()
)
hm2AgentIpsgIfPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentIpsgIfPortSecurity.setStatus("current")


class _Hm2AgentDhcpSnoopingStatsReset_Type(Integer32):
    """Custom type hm2AgentDhcpSnoopingStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_Hm2AgentDhcpSnoopingStatsReset_Type.__name__ = "Integer32"
_Hm2AgentDhcpSnoopingStatsReset_Object = MibScalar
hm2AgentDhcpSnoopingStatsReset = _Hm2AgentDhcpSnoopingStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 6),
    _Hm2AgentDhcpSnoopingStatsReset_Type()
)
hm2AgentDhcpSnoopingStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDhcpSnoopingStatsReset.setStatus("current")
_Hm2AgentDhcpSnoopingStatsTable_Object = MibTable
hm2AgentDhcpSnoopingStatsTable = _Hm2AgentDhcpSnoopingStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 7)
)
if mibBuilder.loadTexts:
    hm2AgentDhcpSnoopingStatsTable.setStatus("current")
_Hm2AgentDhcpSnoopingStatsEntry_Object = MibTableRow
hm2AgentDhcpSnoopingStatsEntry = _Hm2AgentDhcpSnoopingStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 7, 1)
)
hm2AgentDhcpSnoopingStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentDhcpSnoopingStatsEntry.setStatus("current")
_Hm2AgentDhcpSnoopingMacVerifyFailures_Type = Counter32
_Hm2AgentDhcpSnoopingMacVerifyFailures_Object = MibTableColumn
hm2AgentDhcpSnoopingMacVerifyFailures = _Hm2AgentDhcpSnoopingMacVerifyFailures_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 7, 1, 1),
    _Hm2AgentDhcpSnoopingMacVerifyFailures_Type()
)
hm2AgentDhcpSnoopingMacVerifyFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDhcpSnoopingMacVerifyFailures.setStatus("current")
_Hm2AgentDhcpSnoopingInvalidClientMessages_Type = Counter32
_Hm2AgentDhcpSnoopingInvalidClientMessages_Object = MibTableColumn
hm2AgentDhcpSnoopingInvalidClientMessages = _Hm2AgentDhcpSnoopingInvalidClientMessages_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 7, 1, 2),
    _Hm2AgentDhcpSnoopingInvalidClientMessages_Type()
)
hm2AgentDhcpSnoopingInvalidClientMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDhcpSnoopingInvalidClientMessages.setStatus("current")
_Hm2AgentDhcpSnoopingInvalidServerMessages_Type = Counter32
_Hm2AgentDhcpSnoopingInvalidServerMessages_Object = MibTableColumn
hm2AgentDhcpSnoopingInvalidServerMessages = _Hm2AgentDhcpSnoopingInvalidServerMessages_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 7, 1, 3),
    _Hm2AgentDhcpSnoopingInvalidServerMessages_Type()
)
hm2AgentDhcpSnoopingInvalidServerMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDhcpSnoopingInvalidServerMessages.setStatus("current")
_Hm2AgentStaticIpsgBindingTable_Object = MibTable
hm2AgentStaticIpsgBindingTable = _Hm2AgentStaticIpsgBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 8)
)
if mibBuilder.loadTexts:
    hm2AgentStaticIpsgBindingTable.setStatus("current")
_Hm2AgentStaticIpsgBindingEntry_Object = MibTableRow
hm2AgentStaticIpsgBindingEntry = _Hm2AgentStaticIpsgBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 8, 1)
)
hm2AgentStaticIpsgBindingEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentStaticIpsgBindingIfIndex"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentStaticIpsgBindingVlanId"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentStaticIpsgBindingMacAddr"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentStaticIpsgBindingIpAddr"),
)
if mibBuilder.loadTexts:
    hm2AgentStaticIpsgBindingEntry.setStatus("current")
_Hm2AgentStaticIpsgBindingIfIndex_Type = InterfaceIndex
_Hm2AgentStaticIpsgBindingIfIndex_Object = MibTableColumn
hm2AgentStaticIpsgBindingIfIndex = _Hm2AgentStaticIpsgBindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 8, 1, 1),
    _Hm2AgentStaticIpsgBindingIfIndex_Type()
)
hm2AgentStaticIpsgBindingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentStaticIpsgBindingIfIndex.setStatus("current")
_Hm2AgentStaticIpsgBindingVlanId_Type = VlanIndex
_Hm2AgentStaticIpsgBindingVlanId_Object = MibTableColumn
hm2AgentStaticIpsgBindingVlanId = _Hm2AgentStaticIpsgBindingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 8, 1, 2),
    _Hm2AgentStaticIpsgBindingVlanId_Type()
)
hm2AgentStaticIpsgBindingVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentStaticIpsgBindingVlanId.setStatus("current")
_Hm2AgentStaticIpsgBindingMacAddr_Type = MacAddress
_Hm2AgentStaticIpsgBindingMacAddr_Object = MibTableColumn
hm2AgentStaticIpsgBindingMacAddr = _Hm2AgentStaticIpsgBindingMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 8, 1, 3),
    _Hm2AgentStaticIpsgBindingMacAddr_Type()
)
hm2AgentStaticIpsgBindingMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentStaticIpsgBindingMacAddr.setStatus("current")
_Hm2AgentStaticIpsgBindingIpAddr_Type = IpAddress
_Hm2AgentStaticIpsgBindingIpAddr_Object = MibTableColumn
hm2AgentStaticIpsgBindingIpAddr = _Hm2AgentStaticIpsgBindingIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 8, 1, 4),
    _Hm2AgentStaticIpsgBindingIpAddr_Type()
)
hm2AgentStaticIpsgBindingIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentStaticIpsgBindingIpAddr.setStatus("current")
_Hm2AgentStaticIpsgBindingRowStatus_Type = RowStatus
_Hm2AgentStaticIpsgBindingRowStatus_Object = MibTableColumn
hm2AgentStaticIpsgBindingRowStatus = _Hm2AgentStaticIpsgBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 8, 1, 5),
    _Hm2AgentStaticIpsgBindingRowStatus_Type()
)
hm2AgentStaticIpsgBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentStaticIpsgBindingRowStatus.setStatus("current")


class _Hm2AgentStaticIpsgBindingHwStatus_Type(TruthValue):
    """Custom type hm2AgentStaticIpsgBindingHwStatus based on TruthValue"""


_Hm2AgentStaticIpsgBindingHwStatus_Object = MibTableColumn
hm2AgentStaticIpsgBindingHwStatus = _Hm2AgentStaticIpsgBindingHwStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 8, 1, 248),
    _Hm2AgentStaticIpsgBindingHwStatus_Type()
)
hm2AgentStaticIpsgBindingHwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStaticIpsgBindingHwStatus.setStatus("current")
_Hm2AgentDynamicIpsgBindingTable_Object = MibTable
hm2AgentDynamicIpsgBindingTable = _Hm2AgentDynamicIpsgBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 9)
)
if mibBuilder.loadTexts:
    hm2AgentDynamicIpsgBindingTable.setStatus("current")
_Hm2AgentDynamicIpsgBindingEntry_Object = MibTableRow
hm2AgentDynamicIpsgBindingEntry = _Hm2AgentDynamicIpsgBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 9, 1)
)
hm2AgentDynamicIpsgBindingEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentDynamicIpsgBindingIfIndex"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentDynamicIpsgBindingVlanId"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentDynamicIpsgBindingMacAddr"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentDynamicIpsgBindingIpAddr"),
)
if mibBuilder.loadTexts:
    hm2AgentDynamicIpsgBindingEntry.setStatus("current")
_Hm2AgentDynamicIpsgBindingIfIndex_Type = InterfaceIndex
_Hm2AgentDynamicIpsgBindingIfIndex_Object = MibTableColumn
hm2AgentDynamicIpsgBindingIfIndex = _Hm2AgentDynamicIpsgBindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 9, 1, 1),
    _Hm2AgentDynamicIpsgBindingIfIndex_Type()
)
hm2AgentDynamicIpsgBindingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDynamicIpsgBindingIfIndex.setStatus("current")
_Hm2AgentDynamicIpsgBindingVlanId_Type = VlanIndex
_Hm2AgentDynamicIpsgBindingVlanId_Object = MibTableColumn
hm2AgentDynamicIpsgBindingVlanId = _Hm2AgentDynamicIpsgBindingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 9, 1, 2),
    _Hm2AgentDynamicIpsgBindingVlanId_Type()
)
hm2AgentDynamicIpsgBindingVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDynamicIpsgBindingVlanId.setStatus("current")
_Hm2AgentDynamicIpsgBindingMacAddr_Type = MacAddress
_Hm2AgentDynamicIpsgBindingMacAddr_Object = MibTableColumn
hm2AgentDynamicIpsgBindingMacAddr = _Hm2AgentDynamicIpsgBindingMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 9, 1, 3),
    _Hm2AgentDynamicIpsgBindingMacAddr_Type()
)
hm2AgentDynamicIpsgBindingMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDynamicIpsgBindingMacAddr.setStatus("current")
_Hm2AgentDynamicIpsgBindingIpAddr_Type = IpAddress
_Hm2AgentDynamicIpsgBindingIpAddr_Object = MibTableColumn
hm2AgentDynamicIpsgBindingIpAddr = _Hm2AgentDynamicIpsgBindingIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 9, 1, 4),
    _Hm2AgentDynamicIpsgBindingIpAddr_Type()
)
hm2AgentDynamicIpsgBindingIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDynamicIpsgBindingIpAddr.setStatus("current")
_Hm2AgentDynamicIpsgBindingHwStatus_Type = TruthValue
_Hm2AgentDynamicIpsgBindingHwStatus_Object = MibTableColumn
hm2AgentDynamicIpsgBindingHwStatus = _Hm2AgentDynamicIpsgBindingHwStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 9, 1, 248),
    _Hm2AgentDynamicIpsgBindingHwStatus_Type()
)
hm2AgentDynamicIpsgBindingHwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDynamicIpsgBindingHwStatus.setStatus("current")
_Hm2AgentStaticDsBindingTable_Object = MibTable
hm2AgentStaticDsBindingTable = _Hm2AgentStaticDsBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 10)
)
if mibBuilder.loadTexts:
    hm2AgentStaticDsBindingTable.setStatus("current")
_Hm2AgentStaticDsBindingEntry_Object = MibTableRow
hm2AgentStaticDsBindingEntry = _Hm2AgentStaticDsBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 10, 1)
)
hm2AgentStaticDsBindingEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentStaticDsBindingMacAddr"),
)
if mibBuilder.loadTexts:
    hm2AgentStaticDsBindingEntry.setStatus("current")


class _Hm2AgentStaticDsBindingIfIndex_Type(InterfaceIndexOrZero):
    """Custom type hm2AgentStaticDsBindingIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm2AgentStaticDsBindingIfIndex_Object = MibTableColumn
hm2AgentStaticDsBindingIfIndex = _Hm2AgentStaticDsBindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 10, 1, 1),
    _Hm2AgentStaticDsBindingIfIndex_Type()
)
hm2AgentStaticDsBindingIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentStaticDsBindingIfIndex.setStatus("current")


class _Hm2AgentStaticDsBindingVlanId_Type(VlanId):
    """Custom type hm2AgentStaticDsBindingVlanId based on VlanId"""
    defaultValue = 1


_Hm2AgentStaticDsBindingVlanId_Object = MibTableColumn
hm2AgentStaticDsBindingVlanId = _Hm2AgentStaticDsBindingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 10, 1, 2),
    _Hm2AgentStaticDsBindingVlanId_Type()
)
hm2AgentStaticDsBindingVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentStaticDsBindingVlanId.setStatus("current")
_Hm2AgentStaticDsBindingMacAddr_Type = MacAddress
_Hm2AgentStaticDsBindingMacAddr_Object = MibTableColumn
hm2AgentStaticDsBindingMacAddr = _Hm2AgentStaticDsBindingMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 10, 1, 3),
    _Hm2AgentStaticDsBindingMacAddr_Type()
)
hm2AgentStaticDsBindingMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentStaticDsBindingMacAddr.setStatus("current")


class _Hm2AgentStaticDsBindingIpAddr_Type(IpAddress):
    """Custom type hm2AgentStaticDsBindingIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_Hm2AgentStaticDsBindingIpAddr_Object = MibTableColumn
hm2AgentStaticDsBindingIpAddr = _Hm2AgentStaticDsBindingIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 10, 1, 4),
    _Hm2AgentStaticDsBindingIpAddr_Type()
)
hm2AgentStaticDsBindingIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentStaticDsBindingIpAddr.setStatus("current")
_Hm2AgentStaticDsBindingRowStatus_Type = RowStatus
_Hm2AgentStaticDsBindingRowStatus_Object = MibTableColumn
hm2AgentStaticDsBindingRowStatus = _Hm2AgentStaticDsBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 10, 1, 5),
    _Hm2AgentStaticDsBindingRowStatus_Type()
)
hm2AgentStaticDsBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentStaticDsBindingRowStatus.setStatus("current")
_Hm2AgentDynamicDsBindingTable_Object = MibTable
hm2AgentDynamicDsBindingTable = _Hm2AgentDynamicDsBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 11)
)
if mibBuilder.loadTexts:
    hm2AgentDynamicDsBindingTable.setStatus("current")
_Hm2AgentDynamicDsBindingEntry_Object = MibTableRow
hm2AgentDynamicDsBindingEntry = _Hm2AgentDynamicDsBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 11, 1)
)
hm2AgentDynamicDsBindingEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentDynamicDsBindingMacAddr"),
)
if mibBuilder.loadTexts:
    hm2AgentDynamicDsBindingEntry.setStatus("current")
_Hm2AgentDynamicDsBindingIfIndex_Type = InterfaceIndex
_Hm2AgentDynamicDsBindingIfIndex_Object = MibTableColumn
hm2AgentDynamicDsBindingIfIndex = _Hm2AgentDynamicDsBindingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 11, 1, 1),
    _Hm2AgentDynamicDsBindingIfIndex_Type()
)
hm2AgentDynamicDsBindingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDynamicDsBindingIfIndex.setStatus("current")
_Hm2AgentDynamicDsBindingVlanId_Type = VlanIndex
_Hm2AgentDynamicDsBindingVlanId_Object = MibTableColumn
hm2AgentDynamicDsBindingVlanId = _Hm2AgentDynamicDsBindingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 11, 1, 2),
    _Hm2AgentDynamicDsBindingVlanId_Type()
)
hm2AgentDynamicDsBindingVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDynamicDsBindingVlanId.setStatus("current")
_Hm2AgentDynamicDsBindingMacAddr_Type = MacAddress
_Hm2AgentDynamicDsBindingMacAddr_Object = MibTableColumn
hm2AgentDynamicDsBindingMacAddr = _Hm2AgentDynamicDsBindingMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 11, 1, 3),
    _Hm2AgentDynamicDsBindingMacAddr_Type()
)
hm2AgentDynamicDsBindingMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDynamicDsBindingMacAddr.setStatus("current")
_Hm2AgentDynamicDsBindingIpAddr_Type = IpAddress
_Hm2AgentDynamicDsBindingIpAddr_Object = MibTableColumn
hm2AgentDynamicDsBindingIpAddr = _Hm2AgentDynamicDsBindingIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 11, 1, 4),
    _Hm2AgentDynamicDsBindingIpAddr_Type()
)
hm2AgentDynamicDsBindingIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDynamicDsBindingIpAddr.setStatus("current")
_Hm2AgentDynamicDsBindingLeaseRemainingTime_Type = TimeTicks
_Hm2AgentDynamicDsBindingLeaseRemainingTime_Object = MibTableColumn
hm2AgentDynamicDsBindingLeaseRemainingTime = _Hm2AgentDynamicDsBindingLeaseRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 11, 1, 5),
    _Hm2AgentDynamicDsBindingLeaseRemainingTime_Type()
)
hm2AgentDynamicDsBindingLeaseRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDynamicDsBindingLeaseRemainingTime.setStatus("current")


class _Hm2AgentDhcpSnoopingRemoteFileName_Type(DisplayString):
    """Custom type hm2AgentDhcpSnoopingRemoteFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Hm2AgentDhcpSnoopingRemoteFileName_Type.__name__ = "DisplayString"
_Hm2AgentDhcpSnoopingRemoteFileName_Object = MibScalar
hm2AgentDhcpSnoopingRemoteFileName = _Hm2AgentDhcpSnoopingRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 12),
    _Hm2AgentDhcpSnoopingRemoteFileName_Type()
)
hm2AgentDhcpSnoopingRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDhcpSnoopingRemoteFileName.setStatus("current")


class _Hm2AgentDhcpSnoopingRemoteIpAddr_Type(IpAddress):
    """Custom type hm2AgentDhcpSnoopingRemoteIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_Hm2AgentDhcpSnoopingRemoteIpAddr_Object = MibScalar
hm2AgentDhcpSnoopingRemoteIpAddr = _Hm2AgentDhcpSnoopingRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 13),
    _Hm2AgentDhcpSnoopingRemoteIpAddr_Type()
)
hm2AgentDhcpSnoopingRemoteIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDhcpSnoopingRemoteIpAddr.setStatus("current")


class _Hm2AgentDhcpSnoopingStoreInterval_Type(Unsigned32):
    """Custom type hm2AgentDhcpSnoopingStoreInterval based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 86400),
    )


_Hm2AgentDhcpSnoopingStoreInterval_Type.__name__ = "Unsigned32"
_Hm2AgentDhcpSnoopingStoreInterval_Object = MibScalar
hm2AgentDhcpSnoopingStoreInterval = _Hm2AgentDhcpSnoopingStoreInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 23, 14),
    _Hm2AgentDhcpSnoopingStoreInterval_Type()
)
hm2AgentDhcpSnoopingStoreInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDhcpSnoopingStoreInterval.setStatus("current")
_Hm2AgentDhcpL2RelayConfigGroup_ObjectIdentity = ObjectIdentity
hm2AgentDhcpL2RelayConfigGroup = _Hm2AgentDhcpL2RelayConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 24)
)


class _Hm2AgentDhcpL2RelayAdminMode_Type(TruthValue):
    """Custom type hm2AgentDhcpL2RelayAdminMode based on TruthValue"""


_Hm2AgentDhcpL2RelayAdminMode_Object = MibScalar
hm2AgentDhcpL2RelayAdminMode = _Hm2AgentDhcpL2RelayAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 24, 1),
    _Hm2AgentDhcpL2RelayAdminMode_Type()
)
hm2AgentDhcpL2RelayAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDhcpL2RelayAdminMode.setStatus("current")
_Hm2AgentDhcpL2RelayIfConfigTable_Object = MibTable
hm2AgentDhcpL2RelayIfConfigTable = _Hm2AgentDhcpL2RelayIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 24, 2)
)
if mibBuilder.loadTexts:
    hm2AgentDhcpL2RelayIfConfigTable.setStatus("current")
_Hm2AgentDhcpL2RelayIfConfigEntry_Object = MibTableRow
hm2AgentDhcpL2RelayIfConfigEntry = _Hm2AgentDhcpL2RelayIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 24, 2, 1)
)
hm2AgentDhcpL2RelayIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentDhcpL2RelayIfConfigEntry.setStatus("current")


class _Hm2AgentDhcpL2RelayIfEnable_Type(TruthValue):
    """Custom type hm2AgentDhcpL2RelayIfEnable based on TruthValue"""


_Hm2AgentDhcpL2RelayIfEnable_Object = MibTableColumn
hm2AgentDhcpL2RelayIfEnable = _Hm2AgentDhcpL2RelayIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 24, 2, 1, 1),
    _Hm2AgentDhcpL2RelayIfEnable_Type()
)
hm2AgentDhcpL2RelayIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDhcpL2RelayIfEnable.setStatus("current")


class _Hm2AgentDhcpL2RelayIfTrustEnable_Type(TruthValue):
    """Custom type hm2AgentDhcpL2RelayIfTrustEnable based on TruthValue"""


_Hm2AgentDhcpL2RelayIfTrustEnable_Object = MibTableColumn
hm2AgentDhcpL2RelayIfTrustEnable = _Hm2AgentDhcpL2RelayIfTrustEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 24, 2, 1, 2),
    _Hm2AgentDhcpL2RelayIfTrustEnable_Type()
)
hm2AgentDhcpL2RelayIfTrustEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDhcpL2RelayIfTrustEnable.setStatus("current")
_Hm2AgentDhcpL2RelayVlanConfigTable_Object = MibTable
hm2AgentDhcpL2RelayVlanConfigTable = _Hm2AgentDhcpL2RelayVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 24, 3)
)
if mibBuilder.loadTexts:
    hm2AgentDhcpL2RelayVlanConfigTable.setStatus("current")
_Hm2AgentDhcpL2RelayVlanConfigEntry_Object = MibTableRow
hm2AgentDhcpL2RelayVlanConfigEntry = _Hm2AgentDhcpL2RelayVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 24, 3, 1)
)
hm2AgentDhcpL2RelayVlanConfigEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentDhcpL2RelayVlanIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentDhcpL2RelayVlanConfigEntry.setStatus("current")
_Hm2AgentDhcpL2RelayVlanIndex_Type = VlanIndex
_Hm2AgentDhcpL2RelayVlanIndex_Object = MibTableColumn
hm2AgentDhcpL2RelayVlanIndex = _Hm2AgentDhcpL2RelayVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 24, 3, 1, 1),
    _Hm2AgentDhcpL2RelayVlanIndex_Type()
)
hm2AgentDhcpL2RelayVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDhcpL2RelayVlanIndex.setStatus("current")


class _Hm2AgentDhcpL2RelayVlanEnable_Type(TruthValue):
    """Custom type hm2AgentDhcpL2RelayVlanEnable based on TruthValue"""


_Hm2AgentDhcpL2RelayVlanEnable_Object = MibTableColumn
hm2AgentDhcpL2RelayVlanEnable = _Hm2AgentDhcpL2RelayVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 24, 3, 1, 2),
    _Hm2AgentDhcpL2RelayVlanEnable_Type()
)
hm2AgentDhcpL2RelayVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDhcpL2RelayVlanEnable.setStatus("current")


class _Hm2AgentDhcpL2RelayCircuitIdVlanEnable_Type(TruthValue):
    """Custom type hm2AgentDhcpL2RelayCircuitIdVlanEnable based on TruthValue"""


_Hm2AgentDhcpL2RelayCircuitIdVlanEnable_Object = MibTableColumn
hm2AgentDhcpL2RelayCircuitIdVlanEnable = _Hm2AgentDhcpL2RelayCircuitIdVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 24, 3, 1, 3),
    _Hm2AgentDhcpL2RelayCircuitIdVlanEnable_Type()
)
hm2AgentDhcpL2RelayCircuitIdVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDhcpL2RelayCircuitIdVlanEnable.setStatus("current")


class _Hm2AgentDhcpL2RelayRemoteIdVlanEnable_Type(DisplayString):
    """Custom type hm2AgentDhcpL2RelayRemoteIdVlanEnable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hm2AgentDhcpL2RelayRemoteIdVlanEnable_Type.__name__ = "DisplayString"
_Hm2AgentDhcpL2RelayRemoteIdVlanEnable_Object = MibTableColumn
hm2AgentDhcpL2RelayRemoteIdVlanEnable = _Hm2AgentDhcpL2RelayRemoteIdVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 24, 3, 1, 4),
    _Hm2AgentDhcpL2RelayRemoteIdVlanEnable_Type()
)
hm2AgentDhcpL2RelayRemoteIdVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDhcpL2RelayRemoteIdVlanEnable.setStatus("current")


class _Hm2AgentDhcpL2RelayVlanRemoteIdType_Type(Integer32):
    """Custom type hm2AgentDhcpL2RelayVlanRemoteIdType based on Integer32"""
    defaultValue = 2

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
        *(("client-id", 3),
          ("ip", 1),
          ("mac", 2),
          ("other", 4))
    )


_Hm2AgentDhcpL2RelayVlanRemoteIdType_Type.__name__ = "Integer32"
_Hm2AgentDhcpL2RelayVlanRemoteIdType_Object = MibTableColumn
hm2AgentDhcpL2RelayVlanRemoteIdType = _Hm2AgentDhcpL2RelayVlanRemoteIdType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 24, 3, 1, 248),
    _Hm2AgentDhcpL2RelayVlanRemoteIdType_Type()
)
hm2AgentDhcpL2RelayVlanRemoteIdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDhcpL2RelayVlanRemoteIdType.setStatus("current")


class _Hm2AgentDhcpL2RelayStatsReset_Type(Integer32):
    """Custom type hm2AgentDhcpL2RelayStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_Hm2AgentDhcpL2RelayStatsReset_Type.__name__ = "Integer32"
_Hm2AgentDhcpL2RelayStatsReset_Object = MibScalar
hm2AgentDhcpL2RelayStatsReset = _Hm2AgentDhcpL2RelayStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 24, 6),
    _Hm2AgentDhcpL2RelayStatsReset_Type()
)
hm2AgentDhcpL2RelayStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDhcpL2RelayStatsReset.setStatus("current")
_Hm2AgentDhcpL2RelayStatsTable_Object = MibTable
hm2AgentDhcpL2RelayStatsTable = _Hm2AgentDhcpL2RelayStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 24, 7)
)
if mibBuilder.loadTexts:
    hm2AgentDhcpL2RelayStatsTable.setStatus("current")
_Hm2AgentDhcpL2RelayStatsEntry_Object = MibTableRow
hm2AgentDhcpL2RelayStatsEntry = _Hm2AgentDhcpL2RelayStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 24, 7, 1)
)
hm2AgentDhcpL2RelayStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentDhcpL2RelayStatsEntry.setStatus("current")
_Hm2AgentDhcpL2RelayUntrustedSrvrMsgsWithOptn82_Type = Counter32
_Hm2AgentDhcpL2RelayUntrustedSrvrMsgsWithOptn82_Object = MibTableColumn
hm2AgentDhcpL2RelayUntrustedSrvrMsgsWithOptn82 = _Hm2AgentDhcpL2RelayUntrustedSrvrMsgsWithOptn82_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 24, 7, 1, 1),
    _Hm2AgentDhcpL2RelayUntrustedSrvrMsgsWithOptn82_Type()
)
hm2AgentDhcpL2RelayUntrustedSrvrMsgsWithOptn82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDhcpL2RelayUntrustedSrvrMsgsWithOptn82.setStatus("current")
_Hm2AgentDhcpL2RelayUntrustedClntMsgsWithOptn82_Type = Counter32
_Hm2AgentDhcpL2RelayUntrustedClntMsgsWithOptn82_Object = MibTableColumn
hm2AgentDhcpL2RelayUntrustedClntMsgsWithOptn82 = _Hm2AgentDhcpL2RelayUntrustedClntMsgsWithOptn82_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 24, 7, 1, 2),
    _Hm2AgentDhcpL2RelayUntrustedClntMsgsWithOptn82_Type()
)
hm2AgentDhcpL2RelayUntrustedClntMsgsWithOptn82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDhcpL2RelayUntrustedClntMsgsWithOptn82.setStatus("current")
_Hm2AgentDhcpL2RelayTrustedSrvrMsgsWithoutOptn82_Type = Counter32
_Hm2AgentDhcpL2RelayTrustedSrvrMsgsWithoutOptn82_Object = MibTableColumn
hm2AgentDhcpL2RelayTrustedSrvrMsgsWithoutOptn82 = _Hm2AgentDhcpL2RelayTrustedSrvrMsgsWithoutOptn82_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 24, 7, 1, 3),
    _Hm2AgentDhcpL2RelayTrustedSrvrMsgsWithoutOptn82_Type()
)
hm2AgentDhcpL2RelayTrustedSrvrMsgsWithoutOptn82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDhcpL2RelayTrustedSrvrMsgsWithoutOptn82.setStatus("current")
_Hm2AgentDhcpL2RelayTrustedClntMsgsWithoutOptn82_Type = Counter32
_Hm2AgentDhcpL2RelayTrustedClntMsgsWithoutOptn82_Object = MibTableColumn
hm2AgentDhcpL2RelayTrustedClntMsgsWithoutOptn82 = _Hm2AgentDhcpL2RelayTrustedClntMsgsWithoutOptn82_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 24, 7, 1, 4),
    _Hm2AgentDhcpL2RelayTrustedClntMsgsWithoutOptn82_Type()
)
hm2AgentDhcpL2RelayTrustedClntMsgsWithoutOptn82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDhcpL2RelayTrustedClntMsgsWithoutOptn82.setStatus("current")
_Hm2AgentSwitchVoiceVLANGroup_ObjectIdentity = ObjectIdentity
hm2AgentSwitchVoiceVLANGroup = _Hm2AgentSwitchVoiceVLANGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 25)
)


class _Hm2AgentSwitchVoiceVLANAdminMode_Type(HmEnabledStatus):
    """Custom type hm2AgentSwitchVoiceVLANAdminMode based on HmEnabledStatus"""


_Hm2AgentSwitchVoiceVLANAdminMode_Object = MibScalar
hm2AgentSwitchVoiceVLANAdminMode = _Hm2AgentSwitchVoiceVLANAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 25, 1),
    _Hm2AgentSwitchVoiceVLANAdminMode_Type()
)
hm2AgentSwitchVoiceVLANAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchVoiceVLANAdminMode.setStatus("current")
_Hm2AgentSwitchVoiceVlanDeviceTable_Object = MibTable
hm2AgentSwitchVoiceVlanDeviceTable = _Hm2AgentSwitchVoiceVlanDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 25, 2)
)
if mibBuilder.loadTexts:
    hm2AgentSwitchVoiceVlanDeviceTable.setStatus("current")
_Hm2AgentSwitchVoiceVlanDeviceEntry_Object = MibTableRow
hm2AgentSwitchVoiceVlanDeviceEntry = _Hm2AgentSwitchVoiceVlanDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 25, 2, 1)
)
hm2AgentSwitchVoiceVlanDeviceEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentSwitchVoiceVlanInterfaceNum"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentSwitchVoiceVlanDeviceMacAddress"),
)
if mibBuilder.loadTexts:
    hm2AgentSwitchVoiceVlanDeviceEntry.setStatus("current")


class _Hm2AgentSwitchVoiceVlanInterfaceNum_Type(Integer32):
    """Custom type hm2AgentSwitchVoiceVlanInterfaceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hm2AgentSwitchVoiceVlanInterfaceNum_Type.__name__ = "Integer32"
_Hm2AgentSwitchVoiceVlanInterfaceNum_Object = MibTableColumn
hm2AgentSwitchVoiceVlanInterfaceNum = _Hm2AgentSwitchVoiceVlanInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 25, 2, 1, 1),
    _Hm2AgentSwitchVoiceVlanInterfaceNum_Type()
)
hm2AgentSwitchVoiceVlanInterfaceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchVoiceVlanInterfaceNum.setStatus("current")
_Hm2AgentSwitchVoiceVlanDeviceMacAddress_Type = MacAddress
_Hm2AgentSwitchVoiceVlanDeviceMacAddress_Object = MibTableColumn
hm2AgentSwitchVoiceVlanDeviceMacAddress = _Hm2AgentSwitchVoiceVlanDeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 25, 2, 1, 2),
    _Hm2AgentSwitchVoiceVlanDeviceMacAddress_Type()
)
hm2AgentSwitchVoiceVlanDeviceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchVoiceVlanDeviceMacAddress.setStatus("current")
_Hm2AgentSdmPreferConfigGroup_ObjectIdentity = ObjectIdentity
hm2AgentSdmPreferConfigGroup = _Hm2AgentSdmPreferConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 27)
)


class _Hm2AgentSdmPreferCurrentTemplate_Type(Integer32):
    """Custom type hm2AgentSdmPreferCurrentTemplate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("ipv4DataCenter", 3),
          ("ipv4RoutingDefault", 2),
          ("ipv4RoutingMulticast", 11),
          ("ipv4RoutingUnicast", 10))
    )


_Hm2AgentSdmPreferCurrentTemplate_Type.__name__ = "Integer32"
_Hm2AgentSdmPreferCurrentTemplate_Object = MibScalar
hm2AgentSdmPreferCurrentTemplate = _Hm2AgentSdmPreferCurrentTemplate_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 27, 1),
    _Hm2AgentSdmPreferCurrentTemplate_Type()
)
hm2AgentSdmPreferCurrentTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSdmPreferCurrentTemplate.setStatus("current")


class _Hm2AgentSdmPreferNextTemplate_Type(Integer32):
    """Custom type hm2AgentSdmPreferNextTemplate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("ipv4DataCenter", 3),
          ("ipv4RoutingDefault", 2),
          ("ipv4RoutingMulticast", 11),
          ("ipv4RoutingUnicast", 10))
    )


_Hm2AgentSdmPreferNextTemplate_Type.__name__ = "Integer32"
_Hm2AgentSdmPreferNextTemplate_Object = MibScalar
hm2AgentSdmPreferNextTemplate = _Hm2AgentSdmPreferNextTemplate_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 27, 2),
    _Hm2AgentSdmPreferNextTemplate_Type()
)
hm2AgentSdmPreferNextTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSdmPreferNextTemplate.setStatus("current")
_Hm2AgentSdmTemplateSummaryTable_ObjectIdentity = ObjectIdentity
hm2AgentSdmTemplateSummaryTable = _Hm2AgentSdmTemplateSummaryTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 28)
)
_Hm2AgentSdmTemplateTable_Object = MibTable
hm2AgentSdmTemplateTable = _Hm2AgentSdmTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 28, 1)
)
if mibBuilder.loadTexts:
    hm2AgentSdmTemplateTable.setStatus("current")
_Hm2AgentSdmTemplateEntry_Object = MibTableRow
hm2AgentSdmTemplateEntry = _Hm2AgentSdmTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 28, 1, 1)
)
hm2AgentSdmTemplateEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentSdmTemplateId"),
)
if mibBuilder.loadTexts:
    hm2AgentSdmTemplateEntry.setStatus("current")


class _Hm2AgentSdmTemplateId_Type(Integer32):
    """Custom type hm2AgentSdmTemplateId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("ipv4DataCenter", 3),
          ("ipv4RoutingDefault", 2),
          ("ipv4RoutingMulticast", 11),
          ("ipv4RoutingUnicast", 10))
    )


_Hm2AgentSdmTemplateId_Type.__name__ = "Integer32"
_Hm2AgentSdmTemplateId_Object = MibTableColumn
hm2AgentSdmTemplateId = _Hm2AgentSdmTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 28, 1, 1, 1),
    _Hm2AgentSdmTemplateId_Type()
)
hm2AgentSdmTemplateId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentSdmTemplateId.setStatus("current")
_Hm2AgentArpEntries_Type = Integer32
_Hm2AgentArpEntries_Object = MibTableColumn
hm2AgentArpEntries = _Hm2AgentArpEntries_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 28, 1, 1, 2),
    _Hm2AgentArpEntries_Type()
)
hm2AgentArpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentArpEntries.setStatus("current")
_Hm2AgentIPv4UnicastRoutes_Type = Integer32
_Hm2AgentIPv4UnicastRoutes_Object = MibTableColumn
hm2AgentIPv4UnicastRoutes = _Hm2AgentIPv4UnicastRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 28, 1, 1, 3),
    _Hm2AgentIPv4UnicastRoutes_Type()
)
hm2AgentIPv4UnicastRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentIPv4UnicastRoutes.setStatus("current")
_Hm2AgentIPv6NdpEntries_Type = Integer32
_Hm2AgentIPv6NdpEntries_Object = MibTableColumn
hm2AgentIPv6NdpEntries = _Hm2AgentIPv6NdpEntries_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 28, 1, 1, 4),
    _Hm2AgentIPv6NdpEntries_Type()
)
hm2AgentIPv6NdpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentIPv6NdpEntries.setStatus("current")
_Hm2AgentIPv6UnicastRoutes_Type = Integer32
_Hm2AgentIPv6UnicastRoutes_Object = MibTableColumn
hm2AgentIPv6UnicastRoutes = _Hm2AgentIPv6UnicastRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 28, 1, 1, 5),
    _Hm2AgentIPv6UnicastRoutes_Type()
)
hm2AgentIPv6UnicastRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentIPv6UnicastRoutes.setStatus("current")
_Hm2AgentEcmpNextHops_Type = Integer32
_Hm2AgentEcmpNextHops_Object = MibTableColumn
hm2AgentEcmpNextHops = _Hm2AgentEcmpNextHops_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 28, 1, 1, 6),
    _Hm2AgentEcmpNextHops_Type()
)
hm2AgentEcmpNextHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentEcmpNextHops.setStatus("current")
_Hm2AgentIPv4MulticastRoutes_Type = Integer32
_Hm2AgentIPv4MulticastRoutes_Object = MibTableColumn
hm2AgentIPv4MulticastRoutes = _Hm2AgentIPv4MulticastRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 28, 1, 1, 7),
    _Hm2AgentIPv4MulticastRoutes_Type()
)
hm2AgentIPv4MulticastRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentIPv4MulticastRoutes.setStatus("current")
_Hm2AgentIPv6MulticastRoutes_Type = Integer32
_Hm2AgentIPv6MulticastRoutes_Object = MibTableColumn
hm2AgentIPv6MulticastRoutes = _Hm2AgentIPv6MulticastRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 28, 1, 1, 8),
    _Hm2AgentIPv6MulticastRoutes_Type()
)
hm2AgentIPv6MulticastRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentIPv6MulticastRoutes.setStatus("current")
_Hm2AgentSwitchStaticMacStatsGroup_ObjectIdentity = ObjectIdentity
hm2AgentSwitchStaticMacStatsGroup = _Hm2AgentSwitchStaticMacStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 248)
)
_Hm2AgentSwitchStaticMacEntries_Type = Counter32
_Hm2AgentSwitchStaticMacEntries_Object = MibScalar
hm2AgentSwitchStaticMacEntries = _Hm2AgentSwitchStaticMacEntries_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 248, 1),
    _Hm2AgentSwitchStaticMacEntries_Type()
)
hm2AgentSwitchStaticMacEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchStaticMacEntries.setStatus("current")
_Hm2AgentSwitchGARPGroup_ObjectIdentity = ObjectIdentity
hm2AgentSwitchGARPGroup = _Hm2AgentSwitchGARPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 249)
)


class _Hm2AgentSwitchGmrpUnknownMulticastFilterMode_Type(Integer32):
    """Custom type hm2AgentSwitchGmrpUnknownMulticastFilterMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("flood", 1))
    )


_Hm2AgentSwitchGmrpUnknownMulticastFilterMode_Type.__name__ = "Integer32"
_Hm2AgentSwitchGmrpUnknownMulticastFilterMode_Object = MibScalar
hm2AgentSwitchGmrpUnknownMulticastFilterMode = _Hm2AgentSwitchGmrpUnknownMulticastFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 249, 1),
    _Hm2AgentSwitchGmrpUnknownMulticastFilterMode_Type()
)
hm2AgentSwitchGmrpUnknownMulticastFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSwitchGmrpUnknownMulticastFilterMode.setStatus("current")
_Hm2AgentSwitchGmrpPortTable_Object = MibTable
hm2AgentSwitchGmrpPortTable = _Hm2AgentSwitchGmrpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 249, 10)
)
if mibBuilder.loadTexts:
    hm2AgentSwitchGmrpPortTable.setStatus("current")
_Hm2AgentSwitchGmrpPortEntry_Object = MibTableRow
hm2AgentSwitchGmrpPortEntry = _Hm2AgentSwitchGmrpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 249, 10, 1)
)
if mibBuilder.loadTexts:
    hm2AgentSwitchGmrpPortEntry.setStatus("current")
_Hm2AgentSwitchGmrpPortPktRx_Type = Counter32
_Hm2AgentSwitchGmrpPortPktRx_Object = MibTableColumn
hm2AgentSwitchGmrpPortPktRx = _Hm2AgentSwitchGmrpPortPktRx_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 249, 10, 1, 1),
    _Hm2AgentSwitchGmrpPortPktRx_Type()
)
hm2AgentSwitchGmrpPortPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchGmrpPortPktRx.setStatus("current")
_Hm2AgentSwitchGmrpPortPktTx_Type = Counter32
_Hm2AgentSwitchGmrpPortPktTx_Object = MibTableColumn
hm2AgentSwitchGmrpPortPktTx = _Hm2AgentSwitchGmrpPortPktTx_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 249, 10, 1, 2),
    _Hm2AgentSwitchGmrpPortPktTx_Type()
)
hm2AgentSwitchGmrpPortPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchGmrpPortPktTx.setStatus("current")
_Hm2AgentSwitchGvrpPortTable_Object = MibTable
hm2AgentSwitchGvrpPortTable = _Hm2AgentSwitchGvrpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 249, 15)
)
if mibBuilder.loadTexts:
    hm2AgentSwitchGvrpPortTable.setStatus("current")
_Hm2AgentSwitchGvrpPortEntry_Object = MibTableRow
hm2AgentSwitchGvrpPortEntry = _Hm2AgentSwitchGvrpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 249, 15, 1)
)
if mibBuilder.loadTexts:
    hm2AgentSwitchGvrpPortEntry.setStatus("current")
_Hm2AgentSwitchGvrpPortPktRx_Type = Counter32
_Hm2AgentSwitchGvrpPortPktRx_Object = MibTableColumn
hm2AgentSwitchGvrpPortPktRx = _Hm2AgentSwitchGvrpPortPktRx_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 249, 15, 1, 1),
    _Hm2AgentSwitchGvrpPortPktRx_Type()
)
hm2AgentSwitchGvrpPortPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchGvrpPortPktRx.setStatus("current")
_Hm2AgentSwitchGvrpPortPktTx_Type = Counter32
_Hm2AgentSwitchGvrpPortPktTx_Object = MibTableColumn
hm2AgentSwitchGvrpPortPktTx = _Hm2AgentSwitchGvrpPortPktTx_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 8, 249, 15, 1, 2),
    _Hm2AgentSwitchGvrpPortPktTx_Type()
)
hm2AgentSwitchGvrpPortPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentSwitchGvrpPortPktTx.setStatus("current")
_Hm2AgentPortMirroringGroup_ObjectIdentity = ObjectIdentity
hm2AgentPortMirroringGroup = _Hm2AgentPortMirroringGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10)
)
_Hm2AgentPortMirrorTable_Object = MibTable
hm2AgentPortMirrorTable = _Hm2AgentPortMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 4)
)
if mibBuilder.loadTexts:
    hm2AgentPortMirrorTable.setStatus("current")
_Hm2AgentPortMirrorEntry_Object = MibTableRow
hm2AgentPortMirrorEntry = _Hm2AgentPortMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 4, 1)
)
hm2AgentPortMirrorEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentPortMirrorSessionNum"),
)
if mibBuilder.loadTexts:
    hm2AgentPortMirrorEntry.setStatus("current")
_Hm2AgentPortMirrorSessionNum_Type = Unsigned32
_Hm2AgentPortMirrorSessionNum_Object = MibTableColumn
hm2AgentPortMirrorSessionNum = _Hm2AgentPortMirrorSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 4, 1, 1),
    _Hm2AgentPortMirrorSessionNum_Type()
)
hm2AgentPortMirrorSessionNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentPortMirrorSessionNum.setStatus("current")


class _Hm2AgentPortMirrorDestinationPort_Type(InterfaceIndexOrZero):
    """Custom type hm2AgentPortMirrorDestinationPort based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm2AgentPortMirrorDestinationPort_Object = MibTableColumn
hm2AgentPortMirrorDestinationPort = _Hm2AgentPortMirrorDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 4, 1, 2),
    _Hm2AgentPortMirrorDestinationPort_Type()
)
hm2AgentPortMirrorDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortMirrorDestinationPort.setStatus("current")
_Hm2AgentPortMirrorSourcePortMask_Type = Hm2AgentPortMask
_Hm2AgentPortMirrorSourcePortMask_Object = MibTableColumn
hm2AgentPortMirrorSourcePortMask = _Hm2AgentPortMirrorSourcePortMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 4, 1, 3),
    _Hm2AgentPortMirrorSourcePortMask_Type()
)
hm2AgentPortMirrorSourcePortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortMirrorSourcePortMask.setStatus("current")


class _Hm2AgentPortMirrorAdminMode_Type(Integer32):
    """Custom type hm2AgentPortMirrorAdminMode based on Integer32"""
    defaultValue = 2

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


_Hm2AgentPortMirrorAdminMode_Type.__name__ = "Integer32"
_Hm2AgentPortMirrorAdminMode_Object = MibTableColumn
hm2AgentPortMirrorAdminMode = _Hm2AgentPortMirrorAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 4, 1, 4),
    _Hm2AgentPortMirrorAdminMode_Type()
)
hm2AgentPortMirrorAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortMirrorAdminMode.setStatus("current")


class _Hm2AgentPortMirrorSourceVlan_Type(Unsigned32):
    """Custom type hm2AgentPortMirrorSourceVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4042),
    )


_Hm2AgentPortMirrorSourceVlan_Type.__name__ = "Unsigned32"
_Hm2AgentPortMirrorSourceVlan_Object = MibTableColumn
hm2AgentPortMirrorSourceVlan = _Hm2AgentPortMirrorSourceVlan_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 4, 1, 5),
    _Hm2AgentPortMirrorSourceVlan_Type()
)
hm2AgentPortMirrorSourceVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortMirrorSourceVlan.setStatus("current")


class _Hm2AgentPortMirrorRemoteSourceVlan_Type(Unsigned32):
    """Custom type hm2AgentPortMirrorRemoteSourceVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4042),
    )


_Hm2AgentPortMirrorRemoteSourceVlan_Type.__name__ = "Unsigned32"
_Hm2AgentPortMirrorRemoteSourceVlan_Object = MibTableColumn
hm2AgentPortMirrorRemoteSourceVlan = _Hm2AgentPortMirrorRemoteSourceVlan_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 4, 1, 6),
    _Hm2AgentPortMirrorRemoteSourceVlan_Type()
)
hm2AgentPortMirrorRemoteSourceVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortMirrorRemoteSourceVlan.setStatus("current")


class _Hm2AgentPortMirrorRemoteDestinationVlan_Type(Unsigned32):
    """Custom type hm2AgentPortMirrorRemoteDestinationVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 4042),
    )


_Hm2AgentPortMirrorRemoteDestinationVlan_Type.__name__ = "Unsigned32"
_Hm2AgentPortMirrorRemoteDestinationVlan_Object = MibTableColumn
hm2AgentPortMirrorRemoteDestinationVlan = _Hm2AgentPortMirrorRemoteDestinationVlan_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 4, 1, 7),
    _Hm2AgentPortMirrorRemoteDestinationVlan_Type()
)
hm2AgentPortMirrorRemoteDestinationVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortMirrorRemoteDestinationVlan.setStatus("current")
_Hm2AgentPortMirrorReflectorPort_Type = InterfaceIndexOrZero
_Hm2AgentPortMirrorReflectorPort_Object = MibTableColumn
hm2AgentPortMirrorReflectorPort = _Hm2AgentPortMirrorReflectorPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 4, 1, 8),
    _Hm2AgentPortMirrorReflectorPort_Type()
)
hm2AgentPortMirrorReflectorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortMirrorReflectorPort.setStatus("current")


class _Hm2AgentPortMirrorAllowMgmtMode_Type(HmEnabledStatus):
    """Custom type hm2AgentPortMirrorAllowMgmtMode based on HmEnabledStatus"""


_Hm2AgentPortMirrorAllowMgmtMode_Object = MibTableColumn
hm2AgentPortMirrorAllowMgmtMode = _Hm2AgentPortMirrorAllowMgmtMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 4, 1, 9),
    _Hm2AgentPortMirrorAllowMgmtMode_Type()
)
hm2AgentPortMirrorAllowMgmtMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortMirrorAllowMgmtMode.setStatus("current")


class _Hm2AgentPortMirrorReset_Type(Integer32):
    """Custom type hm2AgentPortMirrorReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_Hm2AgentPortMirrorReset_Type.__name__ = "Integer32"
_Hm2AgentPortMirrorReset_Object = MibTableColumn
hm2AgentPortMirrorReset = _Hm2AgentPortMirrorReset_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 4, 1, 248),
    _Hm2AgentPortMirrorReset_Type()
)
hm2AgentPortMirrorReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortMirrorReset.setStatus("current")
_Hm2AgentPortMirrorTypeTable_Object = MibTable
hm2AgentPortMirrorTypeTable = _Hm2AgentPortMirrorTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 5)
)
if mibBuilder.loadTexts:
    hm2AgentPortMirrorTypeTable.setStatus("current")
_Hm2AgentPortMirrorTypeEntry_Object = MibTableRow
hm2AgentPortMirrorTypeEntry = _Hm2AgentPortMirrorTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 5, 1)
)
hm2AgentPortMirrorTypeEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentPortMirrorSessionNum"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentPortMirrorTypeSourcePort"),
)
if mibBuilder.loadTexts:
    hm2AgentPortMirrorTypeEntry.setStatus("current")
_Hm2AgentPortMirrorTypeSourcePort_Type = Unsigned32
_Hm2AgentPortMirrorTypeSourcePort_Object = MibTableColumn
hm2AgentPortMirrorTypeSourcePort = _Hm2AgentPortMirrorTypeSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 5, 1, 1),
    _Hm2AgentPortMirrorTypeSourcePort_Type()
)
hm2AgentPortMirrorTypeSourcePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentPortMirrorTypeSourcePort.setStatus("current")


class _Hm2AgentPortMirrorTypeType_Type(Integer32):
    """Custom type hm2AgentPortMirrorTypeType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("rx", 2),
          ("tx", 1),
          ("txrx", 3))
    )


_Hm2AgentPortMirrorTypeType_Type.__name__ = "Integer32"
_Hm2AgentPortMirrorTypeType_Object = MibTableColumn
hm2AgentPortMirrorTypeType = _Hm2AgentPortMirrorTypeType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 5, 1, 2),
    _Hm2AgentPortMirrorTypeType_Type()
)
hm2AgentPortMirrorTypeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortMirrorTypeType.setStatus("current")
_Hm2AgentPortMirrorRemoteVlan_Type = Unsigned32
_Hm2AgentPortMirrorRemoteVlan_Object = MibScalar
hm2AgentPortMirrorRemoteVlan = _Hm2AgentPortMirrorRemoteVlan_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 6),
    _Hm2AgentPortMirrorRemoteVlan_Type()
)
hm2AgentPortMirrorRemoteVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortMirrorRemoteVlan.setStatus("current")
_Hm2AgentPortMirrorSNMPExtensionGroup_ObjectIdentity = ObjectIdentity
hm2AgentPortMirrorSNMPExtensionGroup = _Hm2AgentPortMirrorSNMPExtensionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 248)
)
_Hm2AgentPortMirrorVlanMirrorPortConflict_ObjectIdentity = ObjectIdentity
hm2AgentPortMirrorVlanMirrorPortConflict = _Hm2AgentPortMirrorVlanMirrorPortConflict_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 248, 1)
)
if mibBuilder.loadTexts:
    hm2AgentPortMirrorVlanMirrorPortConflict.setStatus("current")
_Hm2AgentPortMirrorPortVlanMirrorConflict_ObjectIdentity = ObjectIdentity
hm2AgentPortMirrorPortVlanMirrorConflict = _Hm2AgentPortMirrorPortVlanMirrorConflict_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 248, 2)
)
if mibBuilder.loadTexts:
    hm2AgentPortMirrorPortVlanMirrorConflict.setStatus("current")
_Hm2AgentPortMirrorProbePortAlreadySet_ObjectIdentity = ObjectIdentity
hm2AgentPortMirrorProbePortAlreadySet = _Hm2AgentPortMirrorProbePortAlreadySet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 248, 3)
)
if mibBuilder.loadTexts:
    hm2AgentPortMirrorProbePortAlreadySet.setStatus("current")
_Hm2AgentPortMirrorProbePortVlanConflict_ObjectIdentity = ObjectIdentity
hm2AgentPortMirrorProbePortVlanConflict = _Hm2AgentPortMirrorProbePortVlanConflict_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 248, 4)
)
if mibBuilder.loadTexts:
    hm2AgentPortMirrorProbePortVlanConflict.setStatus("current")
_Hm2AgentPortMirrorVlanNotCreated_ObjectIdentity = ObjectIdentity
hm2AgentPortMirrorVlanNotCreated = _Hm2AgentPortMirrorVlanNotCreated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 248, 5)
)
if mibBuilder.loadTexts:
    hm2AgentPortMirrorVlanNotCreated.setStatus("current")
_Hm2AgentPortMirrorInvalidSourcePort_ObjectIdentity = ObjectIdentity
hm2AgentPortMirrorInvalidSourcePort = _Hm2AgentPortMirrorInvalidSourcePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 248, 6)
)
if mibBuilder.loadTexts:
    hm2AgentPortMirrorInvalidSourcePort.setStatus("current")
_Hm2AgentPortMirrorSourcePortDestinationPortConflict_ObjectIdentity = ObjectIdentity
hm2AgentPortMirrorSourcePortDestinationPortConflict = _Hm2AgentPortMirrorSourcePortDestinationPortConflict_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 248, 7)
)
if mibBuilder.loadTexts:
    hm2AgentPortMirrorSourcePortDestinationPortConflict.setStatus("current")
_Hm2AgentPortMirrorDestinationPortInvalid_ObjectIdentity = ObjectIdentity
hm2AgentPortMirrorDestinationPortInvalid = _Hm2AgentPortMirrorDestinationPortInvalid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 248, 8)
)
if mibBuilder.loadTexts:
    hm2AgentPortMirrorDestinationPortInvalid.setStatus("current")
_Hm2AgentPortMirrorVlanRspanVlanConflict_ObjectIdentity = ObjectIdentity
hm2AgentPortMirrorVlanRspanVlanConflict = _Hm2AgentPortMirrorVlanRspanVlanConflict_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 248, 9)
)
if mibBuilder.loadTexts:
    hm2AgentPortMirrorVlanRspanVlanConflict.setStatus("current")
_Hm2AgentPortMirrorRemoteSourceRemoteDestinationConflict_ObjectIdentity = ObjectIdentity
hm2AgentPortMirrorRemoteSourceRemoteDestinationConflict = _Hm2AgentPortMirrorRemoteSourceRemoteDestinationConflict_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 248, 10)
)
if mibBuilder.loadTexts:
    hm2AgentPortMirrorRemoteSourceRemoteDestinationConflict.setStatus("current")
_Hm2AgentPortMirrorReflectorPortInvalid_ObjectIdentity = ObjectIdentity
hm2AgentPortMirrorReflectorPortInvalid = _Hm2AgentPortMirrorReflectorPortInvalid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 248, 11)
)
if mibBuilder.loadTexts:
    hm2AgentPortMirrorReflectorPortInvalid.setStatus("current")
_Hm2AgentPortMirrorSourcePortReflectorPortConflict_ObjectIdentity = ObjectIdentity
hm2AgentPortMirrorSourcePortReflectorPortConflict = _Hm2AgentPortMirrorSourcePortReflectorPortConflict_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 248, 12)
)
if mibBuilder.loadTexts:
    hm2AgentPortMirrorSourcePortReflectorPortConflict.setStatus("current")
_Hm2AgentPortMirrorReflectorPortVlanConflict_ObjectIdentity = ObjectIdentity
hm2AgentPortMirrorReflectorPortVlanConflict = _Hm2AgentPortMirrorReflectorPortVlanConflict_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 248, 13)
)
if mibBuilder.loadTexts:
    hm2AgentPortMirrorReflectorPortVlanConflict.setStatus("current")
_Hm2AgentPortMirrorPrivateVlanConfigured_ObjectIdentity = ObjectIdentity
hm2AgentPortMirrorPrivateVlanConfigured = _Hm2AgentPortMirrorPrivateVlanConfigured_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 248, 14)
)
if mibBuilder.loadTexts:
    hm2AgentPortMirrorPrivateVlanConfigured.setStatus("current")
_Hm2AgentPortMirrorDestinationRemotePortNotSet_ObjectIdentity = ObjectIdentity
hm2AgentPortMirrorDestinationRemotePortNotSet = _Hm2AgentPortMirrorDestinationRemotePortNotSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 248, 15)
)
if mibBuilder.loadTexts:
    hm2AgentPortMirrorDestinationRemotePortNotSet.setStatus("current")
_Hm2AgentPortMirrorRspanVlanInconsistent_ObjectIdentity = ObjectIdentity
hm2AgentPortMirrorRspanVlanInconsistent = _Hm2AgentPortMirrorRspanVlanInconsistent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 248, 16)
)
if mibBuilder.loadTexts:
    hm2AgentPortMirrorRspanVlanInconsistent.setStatus("current")
_Hm2AgentPortMirrorRspanVlanIdInvalid_ObjectIdentity = ObjectIdentity
hm2AgentPortMirrorRspanVlanIdInvalid = _Hm2AgentPortMirrorRspanVlanIdInvalid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 10, 248, 17)
)
if mibBuilder.loadTexts:
    hm2AgentPortMirrorRspanVlanIdInvalid.setStatus("current")
_Hm2AgentDot3adAggPortTable_Object = MibTable
hm2AgentDot3adAggPortTable = _Hm2AgentDot3adAggPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 12)
)
if mibBuilder.loadTexts:
    hm2AgentDot3adAggPortTable.setStatus("current")
_Hm2AgentDot3adAggPortEntry_Object = MibTableRow
hm2AgentDot3adAggPortEntry = _Hm2AgentDot3adAggPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 12, 1)
)
hm2AgentDot3adAggPortEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentDot3adAggPort"),
)
if mibBuilder.loadTexts:
    hm2AgentDot3adAggPortEntry.setStatus("current")


class _Hm2AgentDot3adAggPort_Type(Integer32):
    """Custom type hm2AgentDot3adAggPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2AgentDot3adAggPort_Type.__name__ = "Integer32"
_Hm2AgentDot3adAggPort_Object = MibTableColumn
hm2AgentDot3adAggPort = _Hm2AgentDot3adAggPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 12, 1, 1),
    _Hm2AgentDot3adAggPort_Type()
)
hm2AgentDot3adAggPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot3adAggPort.setStatus("current")
_Hm2AgentDot3adAggPortLACPMode_Type = HmEnabledStatus
_Hm2AgentDot3adAggPortLACPMode_Object = MibTableColumn
hm2AgentDot3adAggPortLACPMode = _Hm2AgentDot3adAggPortLACPMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 12, 1, 2),
    _Hm2AgentDot3adAggPortLACPMode_Type()
)
hm2AgentDot3adAggPortLACPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot3adAggPortLACPMode.setStatus("current")
_Hm2AgentPortConfigTable_Object = MibTable
hm2AgentPortConfigTable = _Hm2AgentPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13)
)
if mibBuilder.loadTexts:
    hm2AgentPortConfigTable.setStatus("current")
_Hm2AgentPortConfigEntry_Object = MibTableRow
hm2AgentPortConfigEntry = _Hm2AgentPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1)
)
hm2AgentPortConfigEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentPortDot1dBasePort"),
)
if mibBuilder.loadTexts:
    hm2AgentPortConfigEntry.setStatus("current")


class _Hm2AgentPortDot1dBasePort_Type(Integer32):
    """Custom type hm2AgentPortDot1dBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hm2AgentPortDot1dBasePort_Type.__name__ = "Integer32"
_Hm2AgentPortDot1dBasePort_Object = MibTableColumn
hm2AgentPortDot1dBasePort = _Hm2AgentPortDot1dBasePort_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 1),
    _Hm2AgentPortDot1dBasePort_Type()
)
hm2AgentPortDot1dBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentPortDot1dBasePort.setStatus("current")
_Hm2AgentPortIfIndex_Type = Integer32
_Hm2AgentPortIfIndex_Object = MibTableColumn
hm2AgentPortIfIndex = _Hm2AgentPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 2),
    _Hm2AgentPortIfIndex_Type()
)
hm2AgentPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentPortIfIndex.setStatus("current")
_Hm2AgentPortClearStats_Type = HmEnabledStatus
_Hm2AgentPortClearStats_Object = MibTableColumn
hm2AgentPortClearStats = _Hm2AgentPortClearStats_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 10),
    _Hm2AgentPortClearStats_Type()
)
hm2AgentPortClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortClearStats.setStatus("current")


class _Hm2AgentPortDot3FlowControlMode_Type(Integer32):
    """Custom type hm2AgentPortDot3FlowControlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asymmetric", 2),
          ("disable", 3),
          ("symmetric", 1))
    )


_Hm2AgentPortDot3FlowControlMode_Type.__name__ = "Integer32"
_Hm2AgentPortDot3FlowControlMode_Object = MibTableColumn
hm2AgentPortDot3FlowControlMode = _Hm2AgentPortDot3FlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 14),
    _Hm2AgentPortDot3FlowControlMode_Type()
)
hm2AgentPortDot3FlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortDot3FlowControlMode.setStatus("current")
_Hm2AgentPortMaxFrameSizeLimit_Type = Integer32
_Hm2AgentPortMaxFrameSizeLimit_Object = MibTableColumn
hm2AgentPortMaxFrameSizeLimit = _Hm2AgentPortMaxFrameSizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 18),
    _Hm2AgentPortMaxFrameSizeLimit_Type()
)
hm2AgentPortMaxFrameSizeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentPortMaxFrameSizeLimit.setStatus("current")
_Hm2AgentPortMaxFrameSize_Type = Integer32
_Hm2AgentPortMaxFrameSize_Object = MibTableColumn
hm2AgentPortMaxFrameSize = _Hm2AgentPortMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 19),
    _Hm2AgentPortMaxFrameSize_Type()
)
hm2AgentPortMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortMaxFrameSize.setStatus("current")
_Hm2AgentPortBroadcastControlMode_Type = HmEnabledStatus
_Hm2AgentPortBroadcastControlMode_Object = MibTableColumn
hm2AgentPortBroadcastControlMode = _Hm2AgentPortBroadcastControlMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 20),
    _Hm2AgentPortBroadcastControlMode_Type()
)
hm2AgentPortBroadcastControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortBroadcastControlMode.setStatus("current")


class _Hm2AgentPortBroadcastControlThreshold_Type(Integer32):
    """Custom type hm2AgentPortBroadcastControlThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14880000),
    )


_Hm2AgentPortBroadcastControlThreshold_Type.__name__ = "Integer32"
_Hm2AgentPortBroadcastControlThreshold_Object = MibTableColumn
hm2AgentPortBroadcastControlThreshold = _Hm2AgentPortBroadcastControlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 21),
    _Hm2AgentPortBroadcastControlThreshold_Type()
)
hm2AgentPortBroadcastControlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortBroadcastControlThreshold.setStatus("current")
_Hm2AgentPortMulticastControlMode_Type = HmEnabledStatus
_Hm2AgentPortMulticastControlMode_Object = MibTableColumn
hm2AgentPortMulticastControlMode = _Hm2AgentPortMulticastControlMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 22),
    _Hm2AgentPortMulticastControlMode_Type()
)
hm2AgentPortMulticastControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortMulticastControlMode.setStatus("current")


class _Hm2AgentPortMulticastControlThreshold_Type(Integer32):
    """Custom type hm2AgentPortMulticastControlThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14880000),
    )


_Hm2AgentPortMulticastControlThreshold_Type.__name__ = "Integer32"
_Hm2AgentPortMulticastControlThreshold_Object = MibTableColumn
hm2AgentPortMulticastControlThreshold = _Hm2AgentPortMulticastControlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 23),
    _Hm2AgentPortMulticastControlThreshold_Type()
)
hm2AgentPortMulticastControlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortMulticastControlThreshold.setStatus("current")
_Hm2AgentPortUnicastControlMode_Type = HmEnabledStatus
_Hm2AgentPortUnicastControlMode_Object = MibTableColumn
hm2AgentPortUnicastControlMode = _Hm2AgentPortUnicastControlMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 24),
    _Hm2AgentPortUnicastControlMode_Type()
)
hm2AgentPortUnicastControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortUnicastControlMode.setStatus("current")


class _Hm2AgentPortUnicastControlThreshold_Type(Integer32):
    """Custom type hm2AgentPortUnicastControlThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14880000),
    )


_Hm2AgentPortUnicastControlThreshold_Type.__name__ = "Integer32"
_Hm2AgentPortUnicastControlThreshold_Object = MibTableColumn
hm2AgentPortUnicastControlThreshold = _Hm2AgentPortUnicastControlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 25),
    _Hm2AgentPortUnicastControlThreshold_Type()
)
hm2AgentPortUnicastControlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortUnicastControlThreshold.setStatus("current")


class _Hm2AgentPortBroadcastControlThresholdUnit_Type(Integer32):
    """Custom type hm2AgentPortBroadcastControlThresholdUnit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("percent", 1),
          ("pps", 2))
    )


_Hm2AgentPortBroadcastControlThresholdUnit_Type.__name__ = "Integer32"
_Hm2AgentPortBroadcastControlThresholdUnit_Object = MibTableColumn
hm2AgentPortBroadcastControlThresholdUnit = _Hm2AgentPortBroadcastControlThresholdUnit_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 26),
    _Hm2AgentPortBroadcastControlThresholdUnit_Type()
)
hm2AgentPortBroadcastControlThresholdUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortBroadcastControlThresholdUnit.setStatus("current")


class _Hm2AgentPortMulticastControlThresholdUnit_Type(Integer32):
    """Custom type hm2AgentPortMulticastControlThresholdUnit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("percent", 1),
          ("pps", 2))
    )


_Hm2AgentPortMulticastControlThresholdUnit_Type.__name__ = "Integer32"
_Hm2AgentPortMulticastControlThresholdUnit_Object = MibTableColumn
hm2AgentPortMulticastControlThresholdUnit = _Hm2AgentPortMulticastControlThresholdUnit_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 27),
    _Hm2AgentPortMulticastControlThresholdUnit_Type()
)
hm2AgentPortMulticastControlThresholdUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortMulticastControlThresholdUnit.setStatus("current")


class _Hm2AgentPortUnicastControlThresholdUnit_Type(Integer32):
    """Custom type hm2AgentPortUnicastControlThresholdUnit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("percent", 1),
          ("pps", 2))
    )


_Hm2AgentPortUnicastControlThresholdUnit_Type.__name__ = "Integer32"
_Hm2AgentPortUnicastControlThresholdUnit_Object = MibTableColumn
hm2AgentPortUnicastControlThresholdUnit = _Hm2AgentPortUnicastControlThresholdUnit_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 28),
    _Hm2AgentPortUnicastControlThresholdUnit_Type()
)
hm2AgentPortUnicastControlThresholdUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortUnicastControlThresholdUnit.setStatus("current")


class _Hm2AgentPortVoiceVlanMode_Type(Integer32):
    """Custom type hm2AgentPortVoiceVlanMode based on Integer32"""
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
        *(("disable", 6),
          ("dot1p", 3),
          ("none", 1),
          ("untagged", 5),
          ("vlanid", 2),
          ("vlanidanddot1p", 4))
    )


_Hm2AgentPortVoiceVlanMode_Type.__name__ = "Integer32"
_Hm2AgentPortVoiceVlanMode_Object = MibTableColumn
hm2AgentPortVoiceVlanMode = _Hm2AgentPortVoiceVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 29),
    _Hm2AgentPortVoiceVlanMode_Type()
)
hm2AgentPortVoiceVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortVoiceVlanMode.setStatus("current")


class _Hm2AgentPortVoiceVlanID_Type(Integer32):
    """Custom type hm2AgentPortVoiceVlanID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4093),
    )


_Hm2AgentPortVoiceVlanID_Type.__name__ = "Integer32"
_Hm2AgentPortVoiceVlanID_Object = MibTableColumn
hm2AgentPortVoiceVlanID = _Hm2AgentPortVoiceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 30),
    _Hm2AgentPortVoiceVlanID_Type()
)
hm2AgentPortVoiceVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortVoiceVlanID.setStatus("current")


class _Hm2AgentPortVoiceVlanPriority_Type(Integer32):
    """Custom type hm2AgentPortVoiceVlanPriority based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_Hm2AgentPortVoiceVlanPriority_Type.__name__ = "Integer32"
_Hm2AgentPortVoiceVlanPriority_Object = MibTableColumn
hm2AgentPortVoiceVlanPriority = _Hm2AgentPortVoiceVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 31),
    _Hm2AgentPortVoiceVlanPriority_Type()
)
hm2AgentPortVoiceVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortVoiceVlanPriority.setStatus("current")


class _Hm2AgentPortVoiceVlanDataPriorityMode_Type(Integer32):
    """Custom type hm2AgentPortVoiceVlanDataPriorityMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trust", 1),
          ("untrust", 2))
    )


_Hm2AgentPortVoiceVlanDataPriorityMode_Type.__name__ = "Integer32"
_Hm2AgentPortVoiceVlanDataPriorityMode_Object = MibTableColumn
hm2AgentPortVoiceVlanDataPriorityMode = _Hm2AgentPortVoiceVlanDataPriorityMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 32),
    _Hm2AgentPortVoiceVlanDataPriorityMode_Type()
)
hm2AgentPortVoiceVlanDataPriorityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortVoiceVlanDataPriorityMode.setStatus("current")


class _Hm2AgentPortVoiceVlanOperationalStatus_Type(Integer32):
    """Custom type hm2AgentPortVoiceVlanOperationalStatus based on Integer32"""
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


_Hm2AgentPortVoiceVlanOperationalStatus_Type.__name__ = "Integer32"
_Hm2AgentPortVoiceVlanOperationalStatus_Object = MibTableColumn
hm2AgentPortVoiceVlanOperationalStatus = _Hm2AgentPortVoiceVlanOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 33),
    _Hm2AgentPortVoiceVlanOperationalStatus_Type()
)
hm2AgentPortVoiceVlanOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentPortVoiceVlanOperationalStatus.setStatus("current")


class _Hm2AgentPortVoiceVlanUntagged_Type(Integer32):
    """Custom type hm2AgentPortVoiceVlanUntagged based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Hm2AgentPortVoiceVlanUntagged_Type.__name__ = "Integer32"
_Hm2AgentPortVoiceVlanUntagged_Object = MibTableColumn
hm2AgentPortVoiceVlanUntagged = _Hm2AgentPortVoiceVlanUntagged_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 34),
    _Hm2AgentPortVoiceVlanUntagged_Type()
)
hm2AgentPortVoiceVlanUntagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortVoiceVlanUntagged.setStatus("current")


class _Hm2AgentPortVoiceVlanNoneMode_Type(Integer32):
    """Custom type hm2AgentPortVoiceVlanNoneMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Hm2AgentPortVoiceVlanNoneMode_Type.__name__ = "Integer32"
_Hm2AgentPortVoiceVlanNoneMode_Object = MibTableColumn
hm2AgentPortVoiceVlanNoneMode = _Hm2AgentPortVoiceVlanNoneMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 35),
    _Hm2AgentPortVoiceVlanNoneMode_Type()
)
hm2AgentPortVoiceVlanNoneMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortVoiceVlanNoneMode.setStatus("current")


class _Hm2AgentPortVoiceVlanDSCP_Type(Integer32):
    """Custom type hm2AgentPortVoiceVlanDSCP based on Integer32"""
    defaultValue = 0


_Hm2AgentPortVoiceVlanDSCP_Object = MibTableColumn
hm2AgentPortVoiceVlanDSCP = _Hm2AgentPortVoiceVlanDSCP_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 36),
    _Hm2AgentPortVoiceVlanDSCP_Type()
)
hm2AgentPortVoiceVlanDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortVoiceVlanDSCP.setStatus("current")


class _Hm2AgentPortVoiceVlanAuthMode_Type(HmEnabledStatus):
    """Custom type hm2AgentPortVoiceVlanAuthMode based on HmEnabledStatus"""


_Hm2AgentPortVoiceVlanAuthMode_Object = MibTableColumn
hm2AgentPortVoiceVlanAuthMode = _Hm2AgentPortVoiceVlanAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 37),
    _Hm2AgentPortVoiceVlanAuthMode_Type()
)
hm2AgentPortVoiceVlanAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortVoiceVlanAuthMode.setStatus("current")


class _Hm2AgentPortDot3FlowControlOperStatus_Type(Integer32):
    """Custom type hm2AgentPortDot3FlowControlOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_Hm2AgentPortDot3FlowControlOperStatus_Type.__name__ = "Integer32"
_Hm2AgentPortDot3FlowControlOperStatus_Object = MibTableColumn
hm2AgentPortDot3FlowControlOperStatus = _Hm2AgentPortDot3FlowControlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 38),
    _Hm2AgentPortDot3FlowControlOperStatus_Type()
)
hm2AgentPortDot3FlowControlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentPortDot3FlowControlOperStatus.setStatus("current")


class _Hm2AgentPortSfpLinkLossAlert_Type(HmEnabledStatus):
    """Custom type hm2AgentPortSfpLinkLossAlert based on HmEnabledStatus"""


_Hm2AgentPortSfpLinkLossAlert_Object = MibTableColumn
hm2AgentPortSfpLinkLossAlert = _Hm2AgentPortSfpLinkLossAlert_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 13, 1, 248),
    _Hm2AgentPortSfpLinkLossAlert_Type()
)
hm2AgentPortSfpLinkLossAlert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortSfpLinkLossAlert.setStatus("current")
_Hm2AgentProtocolConfigGroup_ObjectIdentity = ObjectIdentity
hm2AgentProtocolConfigGroup = _Hm2AgentProtocolConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 14)
)
_Hm2AgentProtocolGroupTable_Object = MibTable
hm2AgentProtocolGroupTable = _Hm2AgentProtocolGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 14, 2)
)
if mibBuilder.loadTexts:
    hm2AgentProtocolGroupTable.setStatus("current")
_Hm2AgentProtocolGroupEntry_Object = MibTableRow
hm2AgentProtocolGroupEntry = _Hm2AgentProtocolGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 14, 2, 1)
)
hm2AgentProtocolGroupEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentProtocolGroupId"),
)
if mibBuilder.loadTexts:
    hm2AgentProtocolGroupEntry.setStatus("current")


class _Hm2AgentProtocolGroupId_Type(Integer32):
    """Custom type hm2AgentProtocolGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2AgentProtocolGroupId_Type.__name__ = "Integer32"
_Hm2AgentProtocolGroupId_Object = MibTableColumn
hm2AgentProtocolGroupId = _Hm2AgentProtocolGroupId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 14, 2, 1, 1),
    _Hm2AgentProtocolGroupId_Type()
)
hm2AgentProtocolGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentProtocolGroupId.setStatus("current")


class _Hm2AgentProtocolGroupName_Type(DisplayString):
    """Custom type hm2AgentProtocolGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 16),
    )


_Hm2AgentProtocolGroupName_Type.__name__ = "DisplayString"
_Hm2AgentProtocolGroupName_Object = MibTableColumn
hm2AgentProtocolGroupName = _Hm2AgentProtocolGroupName_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 14, 2, 1, 2),
    _Hm2AgentProtocolGroupName_Type()
)
hm2AgentProtocolGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentProtocolGroupName.setStatus("current")


class _Hm2AgentProtocolGroupVlanId_Type(Integer32):
    """Custom type hm2AgentProtocolGroupVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4093),
    )


_Hm2AgentProtocolGroupVlanId_Type.__name__ = "Integer32"
_Hm2AgentProtocolGroupVlanId_Object = MibTableColumn
hm2AgentProtocolGroupVlanId = _Hm2AgentProtocolGroupVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 14, 2, 1, 3),
    _Hm2AgentProtocolGroupVlanId_Type()
)
hm2AgentProtocolGroupVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentProtocolGroupVlanId.setStatus("current")
_Hm2AgentProtocolGroupStatus_Type = RowStatus
_Hm2AgentProtocolGroupStatus_Object = MibTableColumn
hm2AgentProtocolGroupStatus = _Hm2AgentProtocolGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 14, 2, 1, 7),
    _Hm2AgentProtocolGroupStatus_Type()
)
hm2AgentProtocolGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentProtocolGroupStatus.setStatus("current")
_Hm2AgentProtocolGroupPortTable_Object = MibTable
hm2AgentProtocolGroupPortTable = _Hm2AgentProtocolGroupPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 14, 3)
)
if mibBuilder.loadTexts:
    hm2AgentProtocolGroupPortTable.setStatus("current")
_Hm2AgentProtocolGroupPortEntry_Object = MibTableRow
hm2AgentProtocolGroupPortEntry = _Hm2AgentProtocolGroupPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 14, 3, 1)
)
hm2AgentProtocolGroupPortEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentProtocolGroupId"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentProtocolGroupPortIfIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentProtocolGroupPortEntry.setStatus("current")


class _Hm2AgentProtocolGroupPortIfIndex_Type(Integer32):
    """Custom type hm2AgentProtocolGroupPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hm2AgentProtocolGroupPortIfIndex_Type.__name__ = "Integer32"
_Hm2AgentProtocolGroupPortIfIndex_Object = MibTableColumn
hm2AgentProtocolGroupPortIfIndex = _Hm2AgentProtocolGroupPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 14, 3, 1, 1),
    _Hm2AgentProtocolGroupPortIfIndex_Type()
)
hm2AgentProtocolGroupPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentProtocolGroupPortIfIndex.setStatus("current")
_Hm2AgentProtocolGroupPortStatus_Type = RowStatus
_Hm2AgentProtocolGroupPortStatus_Object = MibTableColumn
hm2AgentProtocolGroupPortStatus = _Hm2AgentProtocolGroupPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 14, 3, 1, 2),
    _Hm2AgentProtocolGroupPortStatus_Type()
)
hm2AgentProtocolGroupPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentProtocolGroupPortStatus.setStatus("current")
_Hm2AgentProtocolGroupProtocolTable_Object = MibTable
hm2AgentProtocolGroupProtocolTable = _Hm2AgentProtocolGroupProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 14, 4)
)
if mibBuilder.loadTexts:
    hm2AgentProtocolGroupProtocolTable.setStatus("current")
_Hm2AgentProtocolGroupProtocolEntry_Object = MibTableRow
hm2AgentProtocolGroupProtocolEntry = _Hm2AgentProtocolGroupProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 14, 4, 1)
)
hm2AgentProtocolGroupProtocolEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentProtocolGroupId"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentProtocolGroupProtocolID"),
)
if mibBuilder.loadTexts:
    hm2AgentProtocolGroupProtocolEntry.setStatus("current")


class _Hm2AgentProtocolGroupProtocolID_Type(Integer32):
    """Custom type hm2AgentProtocolGroupProtocolID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_Hm2AgentProtocolGroupProtocolID_Type.__name__ = "Integer32"
_Hm2AgentProtocolGroupProtocolID_Object = MibTableColumn
hm2AgentProtocolGroupProtocolID = _Hm2AgentProtocolGroupProtocolID_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 14, 4, 1, 1),
    _Hm2AgentProtocolGroupProtocolID_Type()
)
hm2AgentProtocolGroupProtocolID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentProtocolGroupProtocolID.setStatus("current")
_Hm2AgentProtocolGroupProtocolStatus_Type = RowStatus
_Hm2AgentProtocolGroupProtocolStatus_Object = MibTableColumn
hm2AgentProtocolGroupProtocolStatus = _Hm2AgentProtocolGroupProtocolStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 14, 4, 1, 2),
    _Hm2AgentProtocolGroupProtocolStatus_Type()
)
hm2AgentProtocolGroupProtocolStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentProtocolGroupProtocolStatus.setStatus("current")
_Hm2AgentStpSwitchConfigGroup_ObjectIdentity = ObjectIdentity
hm2AgentStpSwitchConfigGroup = _Hm2AgentStpSwitchConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15)
)


class _Hm2AgentStpConfigDigestKey_Type(OctetString):
    """Custom type hm2AgentStpConfigDigestKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_Hm2AgentStpConfigDigestKey_Type.__name__ = "OctetString"
_Hm2AgentStpConfigDigestKey_Object = MibScalar
hm2AgentStpConfigDigestKey = _Hm2AgentStpConfigDigestKey_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 1),
    _Hm2AgentStpConfigDigestKey_Type()
)
hm2AgentStpConfigDigestKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpConfigDigestKey.setStatus("current")


class _Hm2AgentStpConfigFormatSelector_Type(Unsigned32):
    """Custom type hm2AgentStpConfigFormatSelector based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hm2AgentStpConfigFormatSelector_Type.__name__ = "Unsigned32"
_Hm2AgentStpConfigFormatSelector_Object = MibScalar
hm2AgentStpConfigFormatSelector = _Hm2AgentStpConfigFormatSelector_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 2),
    _Hm2AgentStpConfigFormatSelector_Type()
)
hm2AgentStpConfigFormatSelector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpConfigFormatSelector.setStatus("current")


class _Hm2AgentStpConfigName_Type(DisplayString):
    """Custom type hm2AgentStpConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hm2AgentStpConfigName_Type.__name__ = "DisplayString"
_Hm2AgentStpConfigName_Object = MibScalar
hm2AgentStpConfigName = _Hm2AgentStpConfigName_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 3),
    _Hm2AgentStpConfigName_Type()
)
hm2AgentStpConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpConfigName.setStatus("current")


class _Hm2AgentStpConfigRevision_Type(Unsigned32):
    """Custom type hm2AgentStpConfigRevision based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hm2AgentStpConfigRevision_Type.__name__ = "Unsigned32"
_Hm2AgentStpConfigRevision_Object = MibScalar
hm2AgentStpConfigRevision = _Hm2AgentStpConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 4),
    _Hm2AgentStpConfigRevision_Type()
)
hm2AgentStpConfigRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpConfigRevision.setStatus("current")


class _Hm2AgentStpForceVersion_Type(Integer32):
    """Custom type hm2AgentStpForceVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 3),
          ("rstp", 2),
          ("stp", 1))
    )


_Hm2AgentStpForceVersion_Type.__name__ = "Integer32"
_Hm2AgentStpForceVersion_Object = MibScalar
hm2AgentStpForceVersion = _Hm2AgentStpForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 5),
    _Hm2AgentStpForceVersion_Type()
)
hm2AgentStpForceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpForceVersion.setStatus("current")


class _Hm2AgentStpAdminMode_Type(HmEnabledStatus):
    """Custom type hm2AgentStpAdminMode based on HmEnabledStatus"""


_Hm2AgentStpAdminMode_Object = MibScalar
hm2AgentStpAdminMode = _Hm2AgentStpAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 6),
    _Hm2AgentStpAdminMode_Type()
)
hm2AgentStpAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpAdminMode.setStatus("current")
_Hm2AgentStpPortTable_Object = MibTable
hm2AgentStpPortTable = _Hm2AgentStpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 7)
)
if mibBuilder.loadTexts:
    hm2AgentStpPortTable.setStatus("current")
_Hm2AgentStpPortEntry_Object = MibTableRow
hm2AgentStpPortEntry = _Hm2AgentStpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 7, 1)
)
hm2AgentStpPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentStpPortEntry.setStatus("current")
_Hm2AgentStpPortState_Type = HmEnabledStatus
_Hm2AgentStpPortState_Object = MibTableColumn
hm2AgentStpPortState = _Hm2AgentStpPortState_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 7, 1, 1),
    _Hm2AgentStpPortState_Type()
)
hm2AgentStpPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpPortState.setStatus("current")
_Hm2AgentStpPortStatsMstpBpduRx_Type = Counter32
_Hm2AgentStpPortStatsMstpBpduRx_Object = MibTableColumn
hm2AgentStpPortStatsMstpBpduRx = _Hm2AgentStpPortStatsMstpBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 7, 1, 2),
    _Hm2AgentStpPortStatsMstpBpduRx_Type()
)
hm2AgentStpPortStatsMstpBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpPortStatsMstpBpduRx.setStatus("current")
_Hm2AgentStpPortStatsMstpBpduTx_Type = Counter32
_Hm2AgentStpPortStatsMstpBpduTx_Object = MibTableColumn
hm2AgentStpPortStatsMstpBpduTx = _Hm2AgentStpPortStatsMstpBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 7, 1, 3),
    _Hm2AgentStpPortStatsMstpBpduTx_Type()
)
hm2AgentStpPortStatsMstpBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpPortStatsMstpBpduTx.setStatus("current")
_Hm2AgentStpPortStatsRstpBpduRx_Type = Counter32
_Hm2AgentStpPortStatsRstpBpduRx_Object = MibTableColumn
hm2AgentStpPortStatsRstpBpduRx = _Hm2AgentStpPortStatsRstpBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 7, 1, 4),
    _Hm2AgentStpPortStatsRstpBpduRx_Type()
)
hm2AgentStpPortStatsRstpBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpPortStatsRstpBpduRx.setStatus("current")
_Hm2AgentStpPortStatsRstpBpduTx_Type = Counter32
_Hm2AgentStpPortStatsRstpBpduTx_Object = MibTableColumn
hm2AgentStpPortStatsRstpBpduTx = _Hm2AgentStpPortStatsRstpBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 7, 1, 5),
    _Hm2AgentStpPortStatsRstpBpduTx_Type()
)
hm2AgentStpPortStatsRstpBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpPortStatsRstpBpduTx.setStatus("current")
_Hm2AgentStpPortStatsStpBpduRx_Type = Counter32
_Hm2AgentStpPortStatsStpBpduRx_Object = MibTableColumn
hm2AgentStpPortStatsStpBpduRx = _Hm2AgentStpPortStatsStpBpduRx_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 7, 1, 6),
    _Hm2AgentStpPortStatsStpBpduRx_Type()
)
hm2AgentStpPortStatsStpBpduRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpPortStatsStpBpduRx.setStatus("current")
_Hm2AgentStpPortStatsStpBpduTx_Type = Counter32
_Hm2AgentStpPortStatsStpBpduTx_Object = MibTableColumn
hm2AgentStpPortStatsStpBpduTx = _Hm2AgentStpPortStatsStpBpduTx_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 7, 1, 7),
    _Hm2AgentStpPortStatsStpBpduTx_Type()
)
hm2AgentStpPortStatsStpBpduTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpPortStatsStpBpduTx.setStatus("current")
_Hm2AgentStpPortUpTime_Type = TimeTicks
_Hm2AgentStpPortUpTime_Object = MibTableColumn
hm2AgentStpPortUpTime = _Hm2AgentStpPortUpTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 7, 1, 8),
    _Hm2AgentStpPortUpTime_Type()
)
hm2AgentStpPortUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpPortUpTime.setStatus("current")


class _Hm2AgentStpPortMigrationCheck_Type(Integer32):
    """Custom type hm2AgentStpPortMigrationCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Hm2AgentStpPortMigrationCheck_Type.__name__ = "Integer32"
_Hm2AgentStpPortMigrationCheck_Object = MibTableColumn
hm2AgentStpPortMigrationCheck = _Hm2AgentStpPortMigrationCheck_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 7, 1, 9),
    _Hm2AgentStpPortMigrationCheck_Type()
)
hm2AgentStpPortMigrationCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpPortMigrationCheck.setStatus("current")
_Hm2AgentStpCstConfigGroup_ObjectIdentity = ObjectIdentity
hm2AgentStpCstConfigGroup = _Hm2AgentStpCstConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 8)
)
_Hm2AgentStpCstHelloTime_Type = Unsigned32
_Hm2AgentStpCstHelloTime_Object = MibScalar
hm2AgentStpCstHelloTime = _Hm2AgentStpCstHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 8, 1),
    _Hm2AgentStpCstHelloTime_Type()
)
hm2AgentStpCstHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpCstHelloTime.setStatus("current")
_Hm2AgentStpCstMaxAge_Type = Unsigned32
_Hm2AgentStpCstMaxAge_Object = MibScalar
hm2AgentStpCstMaxAge = _Hm2AgentStpCstMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 8, 2),
    _Hm2AgentStpCstMaxAge_Type()
)
hm2AgentStpCstMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpCstMaxAge.setStatus("current")


class _Hm2AgentStpCstRegionalRootId_Type(OctetString):
    """Custom type hm2AgentStpCstRegionalRootId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Hm2AgentStpCstRegionalRootId_Type.__name__ = "OctetString"
_Hm2AgentStpCstRegionalRootId_Object = MibScalar
hm2AgentStpCstRegionalRootId = _Hm2AgentStpCstRegionalRootId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 8, 3),
    _Hm2AgentStpCstRegionalRootId_Type()
)
hm2AgentStpCstRegionalRootId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpCstRegionalRootId.setStatus("current")
_Hm2AgentStpCstRegionalRootPathCost_Type = Unsigned32
_Hm2AgentStpCstRegionalRootPathCost_Object = MibScalar
hm2AgentStpCstRegionalRootPathCost = _Hm2AgentStpCstRegionalRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 8, 4),
    _Hm2AgentStpCstRegionalRootPathCost_Type()
)
hm2AgentStpCstRegionalRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpCstRegionalRootPathCost.setStatus("current")
_Hm2AgentStpCstRootFwdDelay_Type = Unsigned32
_Hm2AgentStpCstRootFwdDelay_Object = MibScalar
hm2AgentStpCstRootFwdDelay = _Hm2AgentStpCstRootFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 8, 5),
    _Hm2AgentStpCstRootFwdDelay_Type()
)
hm2AgentStpCstRootFwdDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpCstRootFwdDelay.setStatus("current")


class _Hm2AgentStpCstBridgeFwdDelay_Type(Unsigned32):
    """Custom type hm2AgentStpCstBridgeFwdDelay based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_Hm2AgentStpCstBridgeFwdDelay_Type.__name__ = "Unsigned32"
_Hm2AgentStpCstBridgeFwdDelay_Object = MibScalar
hm2AgentStpCstBridgeFwdDelay = _Hm2AgentStpCstBridgeFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 8, 6),
    _Hm2AgentStpCstBridgeFwdDelay_Type()
)
hm2AgentStpCstBridgeFwdDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpCstBridgeFwdDelay.setStatus("current")


class _Hm2AgentStpCstBridgeHelloTime_Type(Unsigned32):
    """Custom type hm2AgentStpCstBridgeHelloTime based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Hm2AgentStpCstBridgeHelloTime_Type.__name__ = "Unsigned32"
_Hm2AgentStpCstBridgeHelloTime_Object = MibScalar
hm2AgentStpCstBridgeHelloTime = _Hm2AgentStpCstBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 8, 7),
    _Hm2AgentStpCstBridgeHelloTime_Type()
)
hm2AgentStpCstBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpCstBridgeHelloTime.setStatus("current")
_Hm2AgentStpCstBridgeHoldTime_Type = Unsigned32
_Hm2AgentStpCstBridgeHoldTime_Object = MibScalar
hm2AgentStpCstBridgeHoldTime = _Hm2AgentStpCstBridgeHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 8, 8),
    _Hm2AgentStpCstBridgeHoldTime_Type()
)
hm2AgentStpCstBridgeHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpCstBridgeHoldTime.setStatus("current")


class _Hm2AgentStpCstBridgeMaxAge_Type(Unsigned32):
    """Custom type hm2AgentStpCstBridgeMaxAge based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Hm2AgentStpCstBridgeMaxAge_Type.__name__ = "Unsigned32"
_Hm2AgentStpCstBridgeMaxAge_Object = MibScalar
hm2AgentStpCstBridgeMaxAge = _Hm2AgentStpCstBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 8, 9),
    _Hm2AgentStpCstBridgeMaxAge_Type()
)
hm2AgentStpCstBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpCstBridgeMaxAge.setStatus("current")


class _Hm2AgentStpCstBridgeMaxHops_Type(Unsigned32):
    """Custom type hm2AgentStpCstBridgeMaxHops based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_Hm2AgentStpCstBridgeMaxHops_Type.__name__ = "Unsigned32"
_Hm2AgentStpCstBridgeMaxHops_Object = MibScalar
hm2AgentStpCstBridgeMaxHops = _Hm2AgentStpCstBridgeMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 8, 10),
    _Hm2AgentStpCstBridgeMaxHops_Type()
)
hm2AgentStpCstBridgeMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpCstBridgeMaxHops.setStatus("current")


class _Hm2AgentStpCstBridgePriority_Type(Unsigned32):
    """Custom type hm2AgentStpCstBridgePriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Hm2AgentStpCstBridgePriority_Type.__name__ = "Unsigned32"
_Hm2AgentStpCstBridgePriority_Object = MibScalar
hm2AgentStpCstBridgePriority = _Hm2AgentStpCstBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 8, 11),
    _Hm2AgentStpCstBridgePriority_Type()
)
hm2AgentStpCstBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpCstBridgePriority.setStatus("current")


class _Hm2AgentStpCstBridgeHoldCount_Type(Unsigned32):
    """Custom type hm2AgentStpCstBridgeHoldCount based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_Hm2AgentStpCstBridgeHoldCount_Type.__name__ = "Unsigned32"
_Hm2AgentStpCstBridgeHoldCount_Object = MibScalar
hm2AgentStpCstBridgeHoldCount = _Hm2AgentStpCstBridgeHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 8, 12),
    _Hm2AgentStpCstBridgeHoldCount_Type()
)
hm2AgentStpCstBridgeHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpCstBridgeHoldCount.setStatus("current")
_Hm2AgentStpCstPortTable_Object = MibTable
hm2AgentStpCstPortTable = _Hm2AgentStpCstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 9)
)
if mibBuilder.loadTexts:
    hm2AgentStpCstPortTable.setStatus("current")
_Hm2AgentStpCstPortEntry_Object = MibTableRow
hm2AgentStpCstPortEntry = _Hm2AgentStpCstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 9, 1)
)
hm2AgentStpCstPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentStpCstPortEntry.setStatus("current")
_Hm2AgentStpCstPortOperEdge_Type = HmEnabledStatus
_Hm2AgentStpCstPortOperEdge_Object = MibTableColumn
hm2AgentStpCstPortOperEdge = _Hm2AgentStpCstPortOperEdge_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 9, 1, 1),
    _Hm2AgentStpCstPortOperEdge_Type()
)
hm2AgentStpCstPortOperEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpCstPortOperEdge.setStatus("current")


class _Hm2AgentStpCstPortOperPointToPoint_Type(Integer32):
    """Custom type hm2AgentStpCstPortOperPointToPoint based on Integer32"""
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


_Hm2AgentStpCstPortOperPointToPoint_Type.__name__ = "Integer32"
_Hm2AgentStpCstPortOperPointToPoint_Object = MibTableColumn
hm2AgentStpCstPortOperPointToPoint = _Hm2AgentStpCstPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 9, 1, 2),
    _Hm2AgentStpCstPortOperPointToPoint_Type()
)
hm2AgentStpCstPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpCstPortOperPointToPoint.setStatus("current")


class _Hm2AgentStpCstPortTopologyChangeAck_Type(Integer32):
    """Custom type hm2AgentStpCstPortTopologyChangeAck based on Integer32"""
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


_Hm2AgentStpCstPortTopologyChangeAck_Type.__name__ = "Integer32"
_Hm2AgentStpCstPortTopologyChangeAck_Object = MibTableColumn
hm2AgentStpCstPortTopologyChangeAck = _Hm2AgentStpCstPortTopologyChangeAck_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 9, 1, 3),
    _Hm2AgentStpCstPortTopologyChangeAck_Type()
)
hm2AgentStpCstPortTopologyChangeAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpCstPortTopologyChangeAck.setStatus("current")


class _Hm2AgentStpCstPortEdge_Type(HmEnabledStatus):
    """Custom type hm2AgentStpCstPortEdge based on HmEnabledStatus"""


_Hm2AgentStpCstPortEdge_Object = MibTableColumn
hm2AgentStpCstPortEdge = _Hm2AgentStpCstPortEdge_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 9, 1, 4),
    _Hm2AgentStpCstPortEdge_Type()
)
hm2AgentStpCstPortEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpCstPortEdge.setStatus("current")


class _Hm2AgentStpCstPortForwardingState_Type(Integer32):
    """Custom type hm2AgentStpCstPortForwardingState based on Integer32"""
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
        *(("disabled", 4),
          ("discarding", 1),
          ("forwarding", 3),
          ("learning", 2),
          ("manualFwd", 5),
          ("notParticipate", 6))
    )


_Hm2AgentStpCstPortForwardingState_Type.__name__ = "Integer32"
_Hm2AgentStpCstPortForwardingState_Object = MibTableColumn
hm2AgentStpCstPortForwardingState = _Hm2AgentStpCstPortForwardingState_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 9, 1, 5),
    _Hm2AgentStpCstPortForwardingState_Type()
)
hm2AgentStpCstPortForwardingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpCstPortForwardingState.setStatus("current")


class _Hm2AgentStpCstPortId_Type(OctetString):
    """Custom type hm2AgentStpCstPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Hm2AgentStpCstPortId_Type.__name__ = "OctetString"
_Hm2AgentStpCstPortId_Object = MibTableColumn
hm2AgentStpCstPortId = _Hm2AgentStpCstPortId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 9, 1, 6),
    _Hm2AgentStpCstPortId_Type()
)
hm2AgentStpCstPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpCstPortId.setStatus("current")


class _Hm2AgentStpCstPortPathCost_Type(Unsigned32):
    """Custom type hm2AgentStpCstPortPathCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Hm2AgentStpCstPortPathCost_Type.__name__ = "Unsigned32"
_Hm2AgentStpCstPortPathCost_Object = MibTableColumn
hm2AgentStpCstPortPathCost = _Hm2AgentStpCstPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 9, 1, 7),
    _Hm2AgentStpCstPortPathCost_Type()
)
hm2AgentStpCstPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpCstPortPathCost.setStatus("current")


class _Hm2AgentStpCstPortPriority_Type(Unsigned32):
    """Custom type hm2AgentStpCstPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Hm2AgentStpCstPortPriority_Type.__name__ = "Unsigned32"
_Hm2AgentStpCstPortPriority_Object = MibTableColumn
hm2AgentStpCstPortPriority = _Hm2AgentStpCstPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 9, 1, 8),
    _Hm2AgentStpCstPortPriority_Type()
)
hm2AgentStpCstPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpCstPortPriority.setStatus("current")


class _Hm2AgentStpCstDesignatedBridgeId_Type(OctetString):
    """Custom type hm2AgentStpCstDesignatedBridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Hm2AgentStpCstDesignatedBridgeId_Type.__name__ = "OctetString"
_Hm2AgentStpCstDesignatedBridgeId_Object = MibTableColumn
hm2AgentStpCstDesignatedBridgeId = _Hm2AgentStpCstDesignatedBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 9, 1, 9),
    _Hm2AgentStpCstDesignatedBridgeId_Type()
)
hm2AgentStpCstDesignatedBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpCstDesignatedBridgeId.setStatus("current")
_Hm2AgentStpCstDesignatedCost_Type = Unsigned32
_Hm2AgentStpCstDesignatedCost_Object = MibTableColumn
hm2AgentStpCstDesignatedCost = _Hm2AgentStpCstDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 9, 1, 10),
    _Hm2AgentStpCstDesignatedCost_Type()
)
hm2AgentStpCstDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpCstDesignatedCost.setStatus("current")


class _Hm2AgentStpCstDesignatedPortId_Type(OctetString):
    """Custom type hm2AgentStpCstDesignatedPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Hm2AgentStpCstDesignatedPortId_Type.__name__ = "OctetString"
_Hm2AgentStpCstDesignatedPortId_Object = MibTableColumn
hm2AgentStpCstDesignatedPortId = _Hm2AgentStpCstDesignatedPortId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 9, 1, 11),
    _Hm2AgentStpCstDesignatedPortId_Type()
)
hm2AgentStpCstDesignatedPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpCstDesignatedPortId.setStatus("current")


class _Hm2AgentStpCstExtPortPathCost_Type(Unsigned32):
    """Custom type hm2AgentStpCstExtPortPathCost based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Hm2AgentStpCstExtPortPathCost_Type.__name__ = "Unsigned32"
_Hm2AgentStpCstExtPortPathCost_Object = MibTableColumn
hm2AgentStpCstExtPortPathCost = _Hm2AgentStpCstExtPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 9, 1, 12),
    _Hm2AgentStpCstExtPortPathCost_Type()
)
hm2AgentStpCstExtPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpCstExtPortPathCost.setStatus("current")
_Hm2AgentStpCstPortBpduGuardEffect_Type = HmEnabledStatus
_Hm2AgentStpCstPortBpduGuardEffect_Object = MibTableColumn
hm2AgentStpCstPortBpduGuardEffect = _Hm2AgentStpCstPortBpduGuardEffect_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 9, 1, 13),
    _Hm2AgentStpCstPortBpduGuardEffect_Type()
)
hm2AgentStpCstPortBpduGuardEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpCstPortBpduGuardEffect.setStatus("current")


class _Hm2AgentStpCstPortBpduFilter_Type(HmEnabledStatus):
    """Custom type hm2AgentStpCstPortBpduFilter based on HmEnabledStatus"""


_Hm2AgentStpCstPortBpduFilter_Object = MibTableColumn
hm2AgentStpCstPortBpduFilter = _Hm2AgentStpCstPortBpduFilter_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 9, 1, 14),
    _Hm2AgentStpCstPortBpduFilter_Type()
)
hm2AgentStpCstPortBpduFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpCstPortBpduFilter.setStatus("current")


class _Hm2AgentStpCstPortBpduFlood_Type(HmEnabledStatus):
    """Custom type hm2AgentStpCstPortBpduFlood based on HmEnabledStatus"""


_Hm2AgentStpCstPortBpduFlood_Object = MibTableColumn
hm2AgentStpCstPortBpduFlood = _Hm2AgentStpCstPortBpduFlood_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 9, 1, 15),
    _Hm2AgentStpCstPortBpduFlood_Type()
)
hm2AgentStpCstPortBpduFlood.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpCstPortBpduFlood.setStatus("current")


class _Hm2AgentStpCstPortAutoEdge_Type(HmEnabledStatus):
    """Custom type hm2AgentStpCstPortAutoEdge based on HmEnabledStatus"""


_Hm2AgentStpCstPortAutoEdge_Object = MibTableColumn
hm2AgentStpCstPortAutoEdge = _Hm2AgentStpCstPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 9, 1, 16),
    _Hm2AgentStpCstPortAutoEdge_Type()
)
hm2AgentStpCstPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpCstPortAutoEdge.setStatus("current")


class _Hm2AgentStpCstPortRootGuard_Type(HmEnabledStatus):
    """Custom type hm2AgentStpCstPortRootGuard based on HmEnabledStatus"""


_Hm2AgentStpCstPortRootGuard_Object = MibTableColumn
hm2AgentStpCstPortRootGuard = _Hm2AgentStpCstPortRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 9, 1, 17),
    _Hm2AgentStpCstPortRootGuard_Type()
)
hm2AgentStpCstPortRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpCstPortRootGuard.setStatus("current")


class _Hm2AgentStpCstPortTCNGuard_Type(HmEnabledStatus):
    """Custom type hm2AgentStpCstPortTCNGuard based on HmEnabledStatus"""


_Hm2AgentStpCstPortTCNGuard_Object = MibTableColumn
hm2AgentStpCstPortTCNGuard = _Hm2AgentStpCstPortTCNGuard_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 9, 1, 18),
    _Hm2AgentStpCstPortTCNGuard_Type()
)
hm2AgentStpCstPortTCNGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpCstPortTCNGuard.setStatus("current")


class _Hm2AgentStpCstPortLoopGuard_Type(HmEnabledStatus):
    """Custom type hm2AgentStpCstPortLoopGuard based on HmEnabledStatus"""


_Hm2AgentStpCstPortLoopGuard_Object = MibTableColumn
hm2AgentStpCstPortLoopGuard = _Hm2AgentStpCstPortLoopGuard_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 9, 1, 19),
    _Hm2AgentStpCstPortLoopGuard_Type()
)
hm2AgentStpCstPortLoopGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpCstPortLoopGuard.setStatus("current")
_Hm2AgentStpMstTable_Object = MibTable
hm2AgentStpMstTable = _Hm2AgentStpMstTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 10)
)
if mibBuilder.loadTexts:
    hm2AgentStpMstTable.setStatus("current")
_Hm2AgentStpMstEntry_Object = MibTableRow
hm2AgentStpMstEntry = _Hm2AgentStpMstEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 10, 1)
)
hm2AgentStpMstEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentStpMstId"),
)
if mibBuilder.loadTexts:
    hm2AgentStpMstEntry.setStatus("current")
_Hm2AgentStpMstId_Type = Unsigned32
_Hm2AgentStpMstId_Object = MibTableColumn
hm2AgentStpMstId = _Hm2AgentStpMstId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 10, 1, 1),
    _Hm2AgentStpMstId_Type()
)
hm2AgentStpMstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpMstId.setStatus("current")


class _Hm2AgentStpMstBridgePriority_Type(Unsigned32):
    """Custom type hm2AgentStpMstBridgePriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Hm2AgentStpMstBridgePriority_Type.__name__ = "Unsigned32"
_Hm2AgentStpMstBridgePriority_Object = MibTableColumn
hm2AgentStpMstBridgePriority = _Hm2AgentStpMstBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 10, 1, 2),
    _Hm2AgentStpMstBridgePriority_Type()
)
hm2AgentStpMstBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpMstBridgePriority.setStatus("current")


class _Hm2AgentStpMstBridgeIdentifier_Type(OctetString):
    """Custom type hm2AgentStpMstBridgeIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Hm2AgentStpMstBridgeIdentifier_Type.__name__ = "OctetString"
_Hm2AgentStpMstBridgeIdentifier_Object = MibTableColumn
hm2AgentStpMstBridgeIdentifier = _Hm2AgentStpMstBridgeIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 10, 1, 3),
    _Hm2AgentStpMstBridgeIdentifier_Type()
)
hm2AgentStpMstBridgeIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpMstBridgeIdentifier.setStatus("current")


class _Hm2AgentStpMstDesignatedRootId_Type(OctetString):
    """Custom type hm2AgentStpMstDesignatedRootId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Hm2AgentStpMstDesignatedRootId_Type.__name__ = "OctetString"
_Hm2AgentStpMstDesignatedRootId_Object = MibTableColumn
hm2AgentStpMstDesignatedRootId = _Hm2AgentStpMstDesignatedRootId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 10, 1, 4),
    _Hm2AgentStpMstDesignatedRootId_Type()
)
hm2AgentStpMstDesignatedRootId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpMstDesignatedRootId.setStatus("current")
_Hm2AgentStpMstRootPathCost_Type = Unsigned32
_Hm2AgentStpMstRootPathCost_Object = MibTableColumn
hm2AgentStpMstRootPathCost = _Hm2AgentStpMstRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 10, 1, 5),
    _Hm2AgentStpMstRootPathCost_Type()
)
hm2AgentStpMstRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpMstRootPathCost.setStatus("current")


class _Hm2AgentStpMstRootPortId_Type(OctetString):
    """Custom type hm2AgentStpMstRootPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Hm2AgentStpMstRootPortId_Type.__name__ = "OctetString"
_Hm2AgentStpMstRootPortId_Object = MibTableColumn
hm2AgentStpMstRootPortId = _Hm2AgentStpMstRootPortId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 10, 1, 6),
    _Hm2AgentStpMstRootPortId_Type()
)
hm2AgentStpMstRootPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpMstRootPortId.setStatus("current")
_Hm2AgentStpMstTimeSinceTopologyChange_Type = TimeTicks
_Hm2AgentStpMstTimeSinceTopologyChange_Object = MibTableColumn
hm2AgentStpMstTimeSinceTopologyChange = _Hm2AgentStpMstTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 10, 1, 7),
    _Hm2AgentStpMstTimeSinceTopologyChange_Type()
)
hm2AgentStpMstTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpMstTimeSinceTopologyChange.setStatus("current")
_Hm2AgentStpMstTopologyChangeCount_Type = Counter32
_Hm2AgentStpMstTopologyChangeCount_Object = MibTableColumn
hm2AgentStpMstTopologyChangeCount = _Hm2AgentStpMstTopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 10, 1, 8),
    _Hm2AgentStpMstTopologyChangeCount_Type()
)
hm2AgentStpMstTopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpMstTopologyChangeCount.setStatus("current")


class _Hm2AgentStpMstTopologyChangeParm_Type(Integer32):
    """Custom type hm2AgentStpMstTopologyChangeParm based on Integer32"""
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


_Hm2AgentStpMstTopologyChangeParm_Type.__name__ = "Integer32"
_Hm2AgentStpMstTopologyChangeParm_Object = MibTableColumn
hm2AgentStpMstTopologyChangeParm = _Hm2AgentStpMstTopologyChangeParm_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 10, 1, 9),
    _Hm2AgentStpMstTopologyChangeParm_Type()
)
hm2AgentStpMstTopologyChangeParm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpMstTopologyChangeParm.setStatus("current")
_Hm2AgentStpMstRowStatus_Type = RowStatus
_Hm2AgentStpMstRowStatus_Object = MibTableColumn
hm2AgentStpMstRowStatus = _Hm2AgentStpMstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 10, 1, 10),
    _Hm2AgentStpMstRowStatus_Type()
)
hm2AgentStpMstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentStpMstRowStatus.setStatus("current")
_Hm2AgentStpMstPortTable_Object = MibTable
hm2AgentStpMstPortTable = _Hm2AgentStpMstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 11)
)
if mibBuilder.loadTexts:
    hm2AgentStpMstPortTable.setStatus("current")
_Hm2AgentStpMstPortEntry_Object = MibTableRow
hm2AgentStpMstPortEntry = _Hm2AgentStpMstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 11, 1)
)
hm2AgentStpMstPortEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentStpMstId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentStpMstPortEntry.setStatus("current")


class _Hm2AgentStpMstPortForwardingState_Type(Integer32):
    """Custom type hm2AgentStpMstPortForwardingState based on Integer32"""
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
        *(("disabled", 4),
          ("discarding", 1),
          ("forwarding", 3),
          ("learning", 2),
          ("manualFwd", 5),
          ("notParticipate", 6))
    )


_Hm2AgentStpMstPortForwardingState_Type.__name__ = "Integer32"
_Hm2AgentStpMstPortForwardingState_Object = MibTableColumn
hm2AgentStpMstPortForwardingState = _Hm2AgentStpMstPortForwardingState_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 11, 1, 1),
    _Hm2AgentStpMstPortForwardingState_Type()
)
hm2AgentStpMstPortForwardingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpMstPortForwardingState.setStatus("current")


class _Hm2AgentStpMstPortId_Type(OctetString):
    """Custom type hm2AgentStpMstPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Hm2AgentStpMstPortId_Type.__name__ = "OctetString"
_Hm2AgentStpMstPortId_Object = MibTableColumn
hm2AgentStpMstPortId = _Hm2AgentStpMstPortId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 11, 1, 2),
    _Hm2AgentStpMstPortId_Type()
)
hm2AgentStpMstPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpMstPortId.setStatus("current")


class _Hm2AgentStpMstPortPathCost_Type(Unsigned32):
    """Custom type hm2AgentStpMstPortPathCost based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Hm2AgentStpMstPortPathCost_Type.__name__ = "Unsigned32"
_Hm2AgentStpMstPortPathCost_Object = MibTableColumn
hm2AgentStpMstPortPathCost = _Hm2AgentStpMstPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 11, 1, 3),
    _Hm2AgentStpMstPortPathCost_Type()
)
hm2AgentStpMstPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpMstPortPathCost.setStatus("current")


class _Hm2AgentStpMstPortPriority_Type(Unsigned32):
    """Custom type hm2AgentStpMstPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_Hm2AgentStpMstPortPriority_Type.__name__ = "Unsigned32"
_Hm2AgentStpMstPortPriority_Object = MibTableColumn
hm2AgentStpMstPortPriority = _Hm2AgentStpMstPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 11, 1, 4),
    _Hm2AgentStpMstPortPriority_Type()
)
hm2AgentStpMstPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpMstPortPriority.setStatus("current")


class _Hm2AgentStpMstDesignatedBridgeId_Type(OctetString):
    """Custom type hm2AgentStpMstDesignatedBridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Hm2AgentStpMstDesignatedBridgeId_Type.__name__ = "OctetString"
_Hm2AgentStpMstDesignatedBridgeId_Object = MibTableColumn
hm2AgentStpMstDesignatedBridgeId = _Hm2AgentStpMstDesignatedBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 11, 1, 5),
    _Hm2AgentStpMstDesignatedBridgeId_Type()
)
hm2AgentStpMstDesignatedBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpMstDesignatedBridgeId.setStatus("current")
_Hm2AgentStpMstDesignatedCost_Type = Unsigned32
_Hm2AgentStpMstDesignatedCost_Object = MibTableColumn
hm2AgentStpMstDesignatedCost = _Hm2AgentStpMstDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 11, 1, 6),
    _Hm2AgentStpMstDesignatedCost_Type()
)
hm2AgentStpMstDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpMstDesignatedCost.setStatus("current")


class _Hm2AgentStpMstDesignatedPortId_Type(OctetString):
    """Custom type hm2AgentStpMstDesignatedPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Hm2AgentStpMstDesignatedPortId_Type.__name__ = "OctetString"
_Hm2AgentStpMstDesignatedPortId_Object = MibTableColumn
hm2AgentStpMstDesignatedPortId = _Hm2AgentStpMstDesignatedPortId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 11, 1, 7),
    _Hm2AgentStpMstDesignatedPortId_Type()
)
hm2AgentStpMstDesignatedPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpMstDesignatedPortId.setStatus("current")


class _Hm2AgentStpMstPortLoopInconsistentState_Type(Integer32):
    """Custom type hm2AgentStpMstPortLoopInconsistentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Hm2AgentStpMstPortLoopInconsistentState_Type.__name__ = "Integer32"
_Hm2AgentStpMstPortLoopInconsistentState_Object = MibTableColumn
hm2AgentStpMstPortLoopInconsistentState = _Hm2AgentStpMstPortLoopInconsistentState_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 11, 1, 8),
    _Hm2AgentStpMstPortLoopInconsistentState_Type()
)
hm2AgentStpMstPortLoopInconsistentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpMstPortLoopInconsistentState.setStatus("current")
_Hm2AgentStpMstPortTransitionsIntoLoopInconsistentState_Type = Counter32
_Hm2AgentStpMstPortTransitionsIntoLoopInconsistentState_Object = MibTableColumn
hm2AgentStpMstPortTransitionsIntoLoopInconsistentState = _Hm2AgentStpMstPortTransitionsIntoLoopInconsistentState_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 11, 1, 9),
    _Hm2AgentStpMstPortTransitionsIntoLoopInconsistentState_Type()
)
hm2AgentStpMstPortTransitionsIntoLoopInconsistentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpMstPortTransitionsIntoLoopInconsistentState.setStatus("current")
_Hm2AgentStpMstPortTransitionsOutOfLoopInconsistentState_Type = Counter32
_Hm2AgentStpMstPortTransitionsOutOfLoopInconsistentState_Object = MibTableColumn
hm2AgentStpMstPortTransitionsOutOfLoopInconsistentState = _Hm2AgentStpMstPortTransitionsOutOfLoopInconsistentState_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 11, 1, 10),
    _Hm2AgentStpMstPortTransitionsOutOfLoopInconsistentState_Type()
)
hm2AgentStpMstPortTransitionsOutOfLoopInconsistentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpMstPortTransitionsOutOfLoopInconsistentState.setStatus("current")


class _Hm2AgentStpMstPortRole_Type(Integer32):
    """Custom type hm2AgentStpMstPortRole based on Integer32"""
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
        *(("alternate", 2),
          ("backup", 4),
          ("designated", 3),
          ("disabled", 6),
          ("master", 5),
          ("root", 1))
    )


_Hm2AgentStpMstPortRole_Type.__name__ = "Integer32"
_Hm2AgentStpMstPortRole_Object = MibTableColumn
hm2AgentStpMstPortRole = _Hm2AgentStpMstPortRole_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 11, 1, 248),
    _Hm2AgentStpMstPortRole_Type()
)
hm2AgentStpMstPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpMstPortRole.setStatus("current")


class _Hm2AgentStpCstAutoPortPathCost_Type(Integer32):
    """Custom type hm2AgentStpCstAutoPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Hm2AgentStpCstAutoPortPathCost_Type.__name__ = "Integer32"
_Hm2AgentStpCstAutoPortPathCost_Object = MibTableColumn
hm2AgentStpCstAutoPortPathCost = _Hm2AgentStpCstAutoPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 11, 1, 249),
    _Hm2AgentStpCstAutoPortPathCost_Type()
)
hm2AgentStpCstAutoPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpCstAutoPortPathCost.setStatus("current")


class _Hm2AgentStpMstPortReceivedBridgeId_Type(OctetString):
    """Custom type hm2AgentStpMstPortReceivedBridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Hm2AgentStpMstPortReceivedBridgeId_Type.__name__ = "OctetString"
_Hm2AgentStpMstPortReceivedBridgeId_Object = MibTableColumn
hm2AgentStpMstPortReceivedBridgeId = _Hm2AgentStpMstPortReceivedBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 11, 1, 250),
    _Hm2AgentStpMstPortReceivedBridgeId_Type()
)
hm2AgentStpMstPortReceivedBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpMstPortReceivedBridgeId.setStatus("current")
_Hm2AgentStpMstPortReceivedRPC_Type = Unsigned32
_Hm2AgentStpMstPortReceivedRPC_Object = MibTableColumn
hm2AgentStpMstPortReceivedRPC = _Hm2AgentStpMstPortReceivedRPC_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 11, 1, 251),
    _Hm2AgentStpMstPortReceivedRPC_Type()
)
hm2AgentStpMstPortReceivedRPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpMstPortReceivedRPC.setStatus("current")


class _Hm2AgentStpMstPortReceivedPortId_Type(OctetString):
    """Custom type hm2AgentStpMstPortReceivedPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Hm2AgentStpMstPortReceivedPortId_Type.__name__ = "OctetString"
_Hm2AgentStpMstPortReceivedPortId_Object = MibTableColumn
hm2AgentStpMstPortReceivedPortId = _Hm2AgentStpMstPortReceivedPortId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 11, 1, 252),
    _Hm2AgentStpMstPortReceivedPortId_Type()
)
hm2AgentStpMstPortReceivedPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpMstPortReceivedPortId.setStatus("current")


class _Hm2AgentStpMstAutoPortPathCost_Type(Integer32):
    """Custom type hm2AgentStpMstAutoPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_Hm2AgentStpMstAutoPortPathCost_Type.__name__ = "Integer32"
_Hm2AgentStpMstAutoPortPathCost_Object = MibTableColumn
hm2AgentStpMstAutoPortPathCost = _Hm2AgentStpMstAutoPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 11, 1, 253),
    _Hm2AgentStpMstAutoPortPathCost_Type()
)
hm2AgentStpMstAutoPortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpMstAutoPortPathCost.setStatus("current")
_Hm2AgentStpMstPortReceivedRegionalRPC_Type = Unsigned32
_Hm2AgentStpMstPortReceivedRegionalRPC_Object = MibTableColumn
hm2AgentStpMstPortReceivedRegionalRPC = _Hm2AgentStpMstPortReceivedRegionalRPC_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 11, 1, 254),
    _Hm2AgentStpMstPortReceivedRegionalRPC_Type()
)
hm2AgentStpMstPortReceivedRegionalRPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentStpMstPortReceivedRegionalRPC.setStatus("current")
_Hm2AgentStpMstVlanTable_Object = MibTable
hm2AgentStpMstVlanTable = _Hm2AgentStpMstVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 12)
)
if mibBuilder.loadTexts:
    hm2AgentStpMstVlanTable.setStatus("current")
_Hm2AgentStpMstVlanEntry_Object = MibTableRow
hm2AgentStpMstVlanEntry = _Hm2AgentStpMstVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 12, 1)
)
hm2AgentStpMstVlanEntry.setIndexNames(
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentStpMstId"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentStpMstVlanEntry.setStatus("current")
_Hm2AgentStpMstVlanRowStatus_Type = RowStatus
_Hm2AgentStpMstVlanRowStatus_Object = MibTableColumn
hm2AgentStpMstVlanRowStatus = _Hm2AgentStpMstVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 12, 1, 1),
    _Hm2AgentStpMstVlanRowStatus_Type()
)
hm2AgentStpMstVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentStpMstVlanRowStatus.setStatus("current")


class _Hm2AgentStpBpduGuardMode_Type(HmEnabledStatus):
    """Custom type hm2AgentStpBpduGuardMode based on HmEnabledStatus"""


_Hm2AgentStpBpduGuardMode_Object = MibScalar
hm2AgentStpBpduGuardMode = _Hm2AgentStpBpduGuardMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 13),
    _Hm2AgentStpBpduGuardMode_Type()
)
hm2AgentStpBpduGuardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpBpduGuardMode.setStatus("current")


class _Hm2AgentStpBpduFilterDefault_Type(HmEnabledStatus):
    """Custom type hm2AgentStpBpduFilterDefault based on HmEnabledStatus"""


_Hm2AgentStpBpduFilterDefault_Object = MibScalar
hm2AgentStpBpduFilterDefault = _Hm2AgentStpBpduFilterDefault_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 14),
    _Hm2AgentStpBpduFilterDefault_Type()
)
hm2AgentStpBpduFilterDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpBpduFilterDefault.setStatus("current")


class _Hm2AgentStpRingOnlyMode_Type(HmEnabledStatus):
    """Custom type hm2AgentStpRingOnlyMode based on HmEnabledStatus"""


_Hm2AgentStpRingOnlyMode_Object = MibScalar
hm2AgentStpRingOnlyMode = _Hm2AgentStpRingOnlyMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 248),
    _Hm2AgentStpRingOnlyMode_Type()
)
hm2AgentStpRingOnlyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpRingOnlyMode.setStatus("current")


class _Hm2AgentStpRingOnlyModeIntfOne_Type(InterfaceIndexOrZero):
    """Custom type hm2AgentStpRingOnlyModeIntfOne based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm2AgentStpRingOnlyModeIntfOne_Object = MibScalar
hm2AgentStpRingOnlyModeIntfOne = _Hm2AgentStpRingOnlyModeIntfOne_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 249),
    _Hm2AgentStpRingOnlyModeIntfOne_Type()
)
hm2AgentStpRingOnlyModeIntfOne.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpRingOnlyModeIntfOne.setStatus("current")


class _Hm2AgentStpRingOnlyModeIntfTwo_Type(InterfaceIndexOrZero):
    """Custom type hm2AgentStpRingOnlyModeIntfTwo based on InterfaceIndexOrZero"""
    defaultValue = 0


_Hm2AgentStpRingOnlyModeIntfTwo_Object = MibScalar
hm2AgentStpRingOnlyModeIntfTwo = _Hm2AgentStpRingOnlyModeIntfTwo_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 250),
    _Hm2AgentStpRingOnlyModeIntfTwo_Type()
)
hm2AgentStpRingOnlyModeIntfTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentStpRingOnlyModeIntfTwo.setStatus("current")
_Hm2AgentStpMstSNMPExtensionGroup_ObjectIdentity = ObjectIdentity
hm2AgentStpMstSNMPExtensionGroup = _Hm2AgentStpMstSNMPExtensionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 260)
)
_Hm2AgentStpMstInstanceVlanErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentStpMstInstanceVlanErrorReturn = _Hm2AgentStpMstInstanceVlanErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 260, 1)
)
if mibBuilder.loadTexts:
    hm2AgentStpMstInstanceVlanErrorReturn.setStatus("current")
_Hm2AgentStpCstFwdDelayErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentStpCstFwdDelayErrorReturn = _Hm2AgentStpCstFwdDelayErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 260, 2)
)
if mibBuilder.loadTexts:
    hm2AgentStpCstFwdDelayErrorReturn.setStatus("current")
_Hm2AgentStpMstSwitchVersionConflict_ObjectIdentity = ObjectIdentity
hm2AgentStpMstSwitchVersionConflict = _Hm2AgentStpMstSwitchVersionConflict_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 15, 260, 3)
)
if mibBuilder.loadTexts:
    hm2AgentStpMstSwitchVersionConflict.setStatus("current")
_Hm2AgentClassOfServiceGroup_ObjectIdentity = ObjectIdentity
hm2AgentClassOfServiceGroup = _Hm2AgentClassOfServiceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 17)
)
_Hm2AgentClassOfServicePortTable_Object = MibTable
hm2AgentClassOfServicePortTable = _Hm2AgentClassOfServicePortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 17, 1)
)
if mibBuilder.loadTexts:
    hm2AgentClassOfServicePortTable.setStatus("current")
_Hm2AgentClassOfServicePortEntry_Object = MibTableRow
hm2AgentClassOfServicePortEntry = _Hm2AgentClassOfServicePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 17, 1, 1)
)
hm2AgentClassOfServicePortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HM2-PLATFORM-SWITCHING-MIB", "hm2AgentClassOfServicePortPriority"),
)
if mibBuilder.loadTexts:
    hm2AgentClassOfServicePortEntry.setStatus("current")


class _Hm2AgentClassOfServicePortPriority_Type(Integer32):
    """Custom type hm2AgentClassOfServicePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hm2AgentClassOfServicePortPriority_Type.__name__ = "Integer32"
_Hm2AgentClassOfServicePortPriority_Object = MibTableColumn
hm2AgentClassOfServicePortPriority = _Hm2AgentClassOfServicePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 17, 1, 1, 1),
    _Hm2AgentClassOfServicePortPriority_Type()
)
hm2AgentClassOfServicePortPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentClassOfServicePortPriority.setStatus("current")


class _Hm2AgentClassOfServicePortClass_Type(Integer32):
    """Custom type hm2AgentClassOfServicePortClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Hm2AgentClassOfServicePortClass_Type.__name__ = "Integer32"
_Hm2AgentClassOfServicePortClass_Object = MibTableColumn
hm2AgentClassOfServicePortClass = _Hm2AgentClassOfServicePortClass_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 2, 17, 1, 1, 2),
    _Hm2AgentClassOfServicePortClass_Type()
)
hm2AgentClassOfServicePortClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentClassOfServicePortClass.setStatus("current")
_Hm2AgentSystemGroup_ObjectIdentity = ObjectIdentity
hm2AgentSystemGroup = _Hm2AgentSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 3)
)
_Hm2AgentClearVlan_Type = HmEnabledStatus
_Hm2AgentClearVlan_Object = MibScalar
hm2AgentClearVlan = _Hm2AgentClearVlan_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 3, 9),
    _Hm2AgentClearVlan_Type()
)
hm2AgentClearVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentClearVlan.setStatus("current")
dot1dBasePortEntry.registerAugmentions(
    ("HM2-PLATFORM-SWITCHING-MIB",
     "hm2AgentSwitchGmrpPortEntry")
)
hm2AgentSwitchGmrpPortEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
dot1dBasePortEntry.registerAugmentions(
    ("HM2-PLATFORM-SWITCHING-MIB",
     "hm2AgentSwitchGvrpPortEntry")
)
hm2AgentSwitchGvrpPortEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())

# Managed Objects groups


# Notification objects

hm2PlatformStpInstanceNewRootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 0, 10)
)
hm2PlatformStpInstanceNewRootTrap.setObjects(
    ("HM2-PLATFORM-SWITCHING-MIB", "hm2AgentStpMstId")
)
if mibBuilder.loadTexts:
    hm2PlatformStpInstanceNewRootTrap.setStatus(
        "current"
    )

hm2PlatformStpInstanceTopologyChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 0, 11)
)
hm2PlatformStpInstanceTopologyChangeTrap.setObjects(
    ("HM2-PLATFORM-SWITCHING-MIB", "hm2AgentStpMstId")
)
if mibBuilder.loadTexts:
    hm2PlatformStpInstanceTopologyChangeTrap.setStatus(
        "current"
    )

hm2PlatformDaiIntfErrorDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 0, 15)
)
hm2PlatformDaiIntfErrorDisabledTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hm2PlatformDaiIntfErrorDisabledTrap.setStatus(
        "current"
    )

hm2PlatformStpInstanceLoopInconsistentStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 0, 16)
)
hm2PlatformStpInstanceLoopInconsistentStartTrap.setObjects(
      *(("HM2-PLATFORM-SWITCHING-MIB", "hm2AgentStpMstId"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    hm2PlatformStpInstanceLoopInconsistentStartTrap.setStatus(
        "current"
    )

hm2PlatformStpInstanceLoopInconsistentEndTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 0, 17)
)
hm2PlatformStpInstanceLoopInconsistentEndTrap.setObjects(
      *(("HM2-PLATFORM-SWITCHING-MIB", "hm2AgentStpMstId"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    hm2PlatformStpInstanceLoopInconsistentEndTrap.setStatus(
        "current"
    )

hm2PlatformDhcpSnoopingIntfErrorDisabledTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 0, 18)
)
hm2PlatformDhcpSnoopingIntfErrorDisabledTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hm2PlatformDhcpSnoopingIntfErrorDisabledTrap.setStatus(
        "current"
    )

hm2PlatformStpCstBpduGuardTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 12, 1, 0, 248)
)
hm2PlatformStpCstBpduGuardTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HM2-PLATFORM-SWITCHING-MIB", "hm2AgentStpCstPortEdge"),
        ("HM2-PLATFORM-SWITCHING-MIB", "hm2AgentStpCstPortBpduGuardEffect"))
)
if mibBuilder.loadTexts:
    hm2PlatformStpCstBpduGuardTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-PLATFORM-SWITCHING-MIB",
    **{"Hm2AgentPortMask": Hm2AgentPortMask,
       "LagList": LagList,
       "VlanList": VlanList,
       "Ipv6Address": Ipv6Address,
       "Ipv6AddressPrefix": Ipv6AddressPrefix,
       "Ipv6AddressIfIdentifier": Ipv6AddressIfIdentifier,
       "Ipv6IfIndex": Ipv6IfIndex,
       "Ipv6IfIndexOrZero": Ipv6IfIndexOrZero,
       "hm2PlatformSwitching": hm2PlatformSwitching,
       "hm2PlatformSwitchingTraps": hm2PlatformSwitchingTraps,
       "hm2PlatformStpInstanceNewRootTrap": hm2PlatformStpInstanceNewRootTrap,
       "hm2PlatformStpInstanceTopologyChangeTrap": hm2PlatformStpInstanceTopologyChangeTrap,
       "hm2PlatformDaiIntfErrorDisabledTrap": hm2PlatformDaiIntfErrorDisabledTrap,
       "hm2PlatformStpInstanceLoopInconsistentStartTrap": hm2PlatformStpInstanceLoopInconsistentStartTrap,
       "hm2PlatformStpInstanceLoopInconsistentEndTrap": hm2PlatformStpInstanceLoopInconsistentEndTrap,
       "hm2PlatformDhcpSnoopingIntfErrorDisabledTrap": hm2PlatformDhcpSnoopingIntfErrorDisabledTrap,
       "hm2PlatformStpCstBpduGuardTrap": hm2PlatformStpCstBpduGuardTrap,
       "hm2AgentConfigGroup": hm2AgentConfigGroup,
       "hm2AgentLagConfigGroup": hm2AgentLagConfigGroup,
       "hm2AgentLagConfigCreate": hm2AgentLagConfigCreate,
       "hm2AgentLagSummaryConfigTable": hm2AgentLagSummaryConfigTable,
       "hm2AgentLagSummaryConfigEntry": hm2AgentLagSummaryConfigEntry,
       "hm2AgentLagSummaryLagIndex": hm2AgentLagSummaryLagIndex,
       "hm2AgentLagSummaryName": hm2AgentLagSummaryName,
       "hm2AgentLagSummaryFlushTimer": hm2AgentLagSummaryFlushTimer,
       "hm2AgentLagSummaryLinkTrap": hm2AgentLagSummaryLinkTrap,
       "hm2AgentLagSummaryAdminMode": hm2AgentLagSummaryAdminMode,
       "hm2AgentLagSummaryStpMode": hm2AgentLagSummaryStpMode,
       "hm2AgentLagSummaryAddPort": hm2AgentLagSummaryAddPort,
       "hm2AgentLagSummaryDeletePort": hm2AgentLagSummaryDeletePort,
       "hm2AgentLagSummaryStatus": hm2AgentLagSummaryStatus,
       "hm2AgentLagSummaryType": hm2AgentLagSummaryType,
       "hm2AgentLagSummaryStaticCapability": hm2AgentLagSummaryStaticCapability,
       "hm2AgentLagSummaryHashOption": hm2AgentLagSummaryHashOption,
       "hm2AgentLagSummaryMinimumActiveLinks": hm2AgentLagSummaryMinimumActiveLinks,
       "hm2AgentLagSummaryMaxFrameSizeLimit": hm2AgentLagSummaryMaxFrameSizeLimit,
       "hm2AgentLagSummaryMaxFrameSize": hm2AgentLagSummaryMaxFrameSize,
       "hm2AgentLagDetailedConfigTable": hm2AgentLagDetailedConfigTable,
       "hm2AgentLagDetailedConfigEntry": hm2AgentLagDetailedConfigEntry,
       "hm2AgentLagDetailedLagIndex": hm2AgentLagDetailedLagIndex,
       "hm2AgentLagDetailedIfIndex": hm2AgentLagDetailedIfIndex,
       "hm2AgentLagDetailedPortSpeed": hm2AgentLagDetailedPortSpeed,
       "hm2AgentLagDetailedPortStatus": hm2AgentLagDetailedPortStatus,
       "hm2AgentLagConfigStaticCapability": hm2AgentLagConfigStaticCapability,
       "hm2AgentLagConfigGroupHashOption": hm2AgentLagConfigGroupHashOption,
       "hm2AgentLagConfigGroupMaxNumPortsPerLag": hm2AgentLagConfigGroupMaxNumPortsPerLag,
       "hm2AgentLagConfigGroupMaxNumOfLags": hm2AgentLagConfigGroupMaxNumOfLags,
       "hm2AgentLagConfigGroupNumOfLagsConfigured": hm2AgentLagConfigGroupNumOfLagsConfigured,
       "hm2AgentLagConfigGroupLagsConfigured": hm2AgentLagConfigGroupLagsConfigured,
       "hm2AgentLagConfigSNMPExtensionGroup": hm2AgentLagConfigSNMPExtensionGroup,
       "hm2AgentLagConfigGroupPortIsLagMemberErrorReturn": hm2AgentLagConfigGroupPortIsLagMemberErrorReturn,
       "hm2AgentLagMirrorProbePortLagMemberErrorReturn": hm2AgentLagMirrorProbePortLagMemberErrorReturn,
       "hm2AgentSwitchConfigGroup": hm2AgentSwitchConfigGroup,
       "hm2AgentSwitchAddressAgingTimeoutTable": hm2AgentSwitchAddressAgingTimeoutTable,
       "hm2AgentSwitchAddressAgingTimeoutEntry": hm2AgentSwitchAddressAgingTimeoutEntry,
       "hm2AgentSwitchAddressAgingTimeout": hm2AgentSwitchAddressAgingTimeout,
       "hm2AgentSwitchStaticMacFilteringTable": hm2AgentSwitchStaticMacFilteringTable,
       "hm2AgentSwitchStaticMacFilteringEntry": hm2AgentSwitchStaticMacFilteringEntry,
       "hm2AgentSwitchStaticMacFilteringVlanId": hm2AgentSwitchStaticMacFilteringVlanId,
       "hm2AgentSwitchStaticMacFilteringAddress": hm2AgentSwitchStaticMacFilteringAddress,
       "hm2AgentSwitchStaticMacFilteringSourcePortMask": hm2AgentSwitchStaticMacFilteringSourcePortMask,
       "hm2AgentSwitchStaticMacFilteringDestPortMask": hm2AgentSwitchStaticMacFilteringDestPortMask,
       "hm2AgentSwitchStaticMacFilteringStatus": hm2AgentSwitchStaticMacFilteringStatus,
       "hm2AgentSwitchSnoopingGroup": hm2AgentSwitchSnoopingGroup,
       "hm2AgentSwitchSnoopingCfgTable": hm2AgentSwitchSnoopingCfgTable,
       "hm2AgentSwitchSnoopingCfgEntry": hm2AgentSwitchSnoopingCfgEntry,
       "hm2AgentSwitchSnoopingProtocol": hm2AgentSwitchSnoopingProtocol,
       "hm2AgentSwitchSnoopingAdminMode": hm2AgentSwitchSnoopingAdminMode,
       "hm2AgentSwitchSnoopingPortMask": hm2AgentSwitchSnoopingPortMask,
       "hm2AgentSwitchSnoopingMulticastControlFramesProcessed": hm2AgentSwitchSnoopingMulticastControlFramesProcessed,
       "hm2AgentSwitchSnoopingIntfGroup": hm2AgentSwitchSnoopingIntfGroup,
       "hm2AgentSwitchSnoopingIntfTable": hm2AgentSwitchSnoopingIntfTable,
       "hm2AgentSwitchSnoopingIntfEntry": hm2AgentSwitchSnoopingIntfEntry,
       "hm2AgentSwitchSnoopingIntfIndex": hm2AgentSwitchSnoopingIntfIndex,
       "hm2AgentSwitchSnoopingIntfAdminMode": hm2AgentSwitchSnoopingIntfAdminMode,
       "hm2AgentSwitchSnoopingIntfGroupMembershipInterval": hm2AgentSwitchSnoopingIntfGroupMembershipInterval,
       "hm2AgentSwitchSnoopingIntfMaxResponseTime": hm2AgentSwitchSnoopingIntfMaxResponseTime,
       "hm2AgentSwitchSnoopingIntfMRPExpirationTime": hm2AgentSwitchSnoopingIntfMRPExpirationTime,
       "hm2AgentSwitchSnoopingIntfFastLeaveAdminMode": hm2AgentSwitchSnoopingIntfFastLeaveAdminMode,
       "hm2AgentSwitchSnoopingIntfMulticastRouterMode": hm2AgentSwitchSnoopingIntfMulticastRouterMode,
       "hm2AgentSwitchSnoopingIntfVlanIDs": hm2AgentSwitchSnoopingIntfVlanIDs,
       "hm2AgentSwitchSnoopingVlanGroup": hm2AgentSwitchSnoopingVlanGroup,
       "hm2AgentSwitchSnoopingVlanTable": hm2AgentSwitchSnoopingVlanTable,
       "hm2AgentSwitchSnoopingVlanEntry": hm2AgentSwitchSnoopingVlanEntry,
       "hm2AgentSwitchSnoopingVlanAdminMode": hm2AgentSwitchSnoopingVlanAdminMode,
       "hm2AgentSwitchSnoopingVlanGroupMembershipInterval": hm2AgentSwitchSnoopingVlanGroupMembershipInterval,
       "hm2AgentSwitchSnoopingVlanMaxResponseTime": hm2AgentSwitchSnoopingVlanMaxResponseTime,
       "hm2AgentSwitchSnoopingVlanFastLeaveAdminMode": hm2AgentSwitchSnoopingVlanFastLeaveAdminMode,
       "hm2AgentSwitchSnoopingVlanMRPExpirationTime": hm2AgentSwitchSnoopingVlanMRPExpirationTime,
       "hm2AgentSwitchSnoopingVlanReportSuppMode": hm2AgentSwitchSnoopingVlanReportSuppMode,
       "hm2AgentSwitchVlanStaticMrouterGroup": hm2AgentSwitchVlanStaticMrouterGroup,
       "hm2AgentSwitchVlanStaticMrouterTable": hm2AgentSwitchVlanStaticMrouterTable,
       "hm2AgentSwitchVlanStaticMrouterEntry": hm2AgentSwitchVlanStaticMrouterEntry,
       "hm2AgentSwitchVlanStaticMrouterAdminMode": hm2AgentSwitchVlanStaticMrouterAdminMode,
       "hm2AgentSwitchMFDBGroup": hm2AgentSwitchMFDBGroup,
       "hm2AgentSwitchMFDBTable": hm2AgentSwitchMFDBTable,
       "hm2AgentSwitchMFDBEntry": hm2AgentSwitchMFDBEntry,
       "hm2AgentSwitchMFDBVlanId": hm2AgentSwitchMFDBVlanId,
       "hm2AgentSwitchMFDBMacAddress": hm2AgentSwitchMFDBMacAddress,
       "hm2AgentSwitchMFDBProtocolType": hm2AgentSwitchMFDBProtocolType,
       "hm2AgentSwitchMFDBType": hm2AgentSwitchMFDBType,
       "hm2AgentSwitchMFDBDescription": hm2AgentSwitchMFDBDescription,
       "hm2AgentSwitchMFDBForwardingPortMask": hm2AgentSwitchMFDBForwardingPortMask,
       "hm2AgentSwitchMFDBFilteringPortMask": hm2AgentSwitchMFDBFilteringPortMask,
       "hm2AgentSwitchMFDBSummaryTable": hm2AgentSwitchMFDBSummaryTable,
       "hm2AgentSwitchMFDBSummaryEntry": hm2AgentSwitchMFDBSummaryEntry,
       "hm2AgentSwitchMFDBSummaryVlanId": hm2AgentSwitchMFDBSummaryVlanId,
       "hm2AgentSwitchMFDBSummaryMacAddress": hm2AgentSwitchMFDBSummaryMacAddress,
       "hm2AgentSwitchMFDBSummaryForwardingPortMask": hm2AgentSwitchMFDBSummaryForwardingPortMask,
       "hm2AgentSwitchMFDBMaxTableEntries": hm2AgentSwitchMFDBMaxTableEntries,
       "hm2AgentSwitchMFDBMostEntriesUsed": hm2AgentSwitchMFDBMostEntriesUsed,
       "hm2AgentSwitchMFDBCurrentEntries": hm2AgentSwitchMFDBCurrentEntries,
       "hm2AgentSwitchVlanMacAssociationGroup": hm2AgentSwitchVlanMacAssociationGroup,
       "hm2AgentSwitchVlanMacAssociationTable": hm2AgentSwitchVlanMacAssociationTable,
       "hm2AgentSwitchVlanMacAssociationEntry": hm2AgentSwitchVlanMacAssociationEntry,
       "hm2AgentSwitchVlanMacAssociationMacAddress": hm2AgentSwitchVlanMacAssociationMacAddress,
       "hm2AgentSwitchVlanMacAssociationVlanId": hm2AgentSwitchVlanMacAssociationVlanId,
       "hm2AgentSwitchVlanMacAssociationRowStatus": hm2AgentSwitchVlanMacAssociationRowStatus,
       "hm2AgentSwitchProtectedPortConfigGroup": hm2AgentSwitchProtectedPortConfigGroup,
       "hm2AgentSwitchProtectedPortTable": hm2AgentSwitchProtectedPortTable,
       "hm2AgentSwitchProtectedPortEntry": hm2AgentSwitchProtectedPortEntry,
       "hm2AgentSwitchProtectedPortGroupId": hm2AgentSwitchProtectedPortGroupId,
       "hm2AgentSwitchProtectedPortGroupName": hm2AgentSwitchProtectedPortGroupName,
       "hm2AgentSwitchProtectedPortPortList": hm2AgentSwitchProtectedPortPortList,
       "hm2AgentSwitchVlanSubnetAssociationGroup": hm2AgentSwitchVlanSubnetAssociationGroup,
       "hm2AgentSwitchVlanSubnetAssociationTable": hm2AgentSwitchVlanSubnetAssociationTable,
       "hm2AgentSwitchVlanSubnetAssociationEntry": hm2AgentSwitchVlanSubnetAssociationEntry,
       "hm2AgentSwitchVlanSubnetAssociationIPAddress": hm2AgentSwitchVlanSubnetAssociationIPAddress,
       "hm2AgentSwitchVlanSubnetAssociationSubnetMask": hm2AgentSwitchVlanSubnetAssociationSubnetMask,
       "hm2AgentSwitchVlanSubnetAssociationVlanId": hm2AgentSwitchVlanSubnetAssociationVlanId,
       "hm2AgentSwitchVlanSubnetAssociationRowStatus": hm2AgentSwitchVlanSubnetAssociationRowStatus,
       "hm2AgentSwitchSnoopingQuerierGroup": hm2AgentSwitchSnoopingQuerierGroup,
       "hm2AgentSwitchSnoopingQuerierCfgTable": hm2AgentSwitchSnoopingQuerierCfgTable,
       "hm2AgentSwitchSnoopingQuerierCfgEntry": hm2AgentSwitchSnoopingQuerierCfgEntry,
       "hm2AgentSwitchSnoopingQuerierAdminMode": hm2AgentSwitchSnoopingQuerierAdminMode,
       "hm2AgentSwitchSnoopingQuerierVersion": hm2AgentSwitchSnoopingQuerierVersion,
       "hm2AgentSwitchSnoopingQuerierQueryInterval": hm2AgentSwitchSnoopingQuerierQueryInterval,
       "hm2AgentSwitchSnoopingQuerierExpiryInterval": hm2AgentSwitchSnoopingQuerierExpiryInterval,
       "hm2AgentSwitchSnoopingQuerierVlanTable": hm2AgentSwitchSnoopingQuerierVlanTable,
       "hm2AgentSwitchSnoopingQuerierVlanEntry": hm2AgentSwitchSnoopingQuerierVlanEntry,
       "hm2AgentSwitchSnoopingQuerierVlanAdminMode": hm2AgentSwitchSnoopingQuerierVlanAdminMode,
       "hm2AgentSwitchSnoopingQuerierVlanOperMode": hm2AgentSwitchSnoopingQuerierVlanOperMode,
       "hm2AgentSwitchSnoopingQuerierElectionParticipateMode": hm2AgentSwitchSnoopingQuerierElectionParticipateMode,
       "hm2AgentSwitchSnoopingQuerierVlanAddress": hm2AgentSwitchSnoopingQuerierVlanAddress,
       "hm2AgentSwitchSnoopingQuerierOperVersion": hm2AgentSwitchSnoopingQuerierOperVersion,
       "hm2AgentSwitchSnoopingQuerierOperMaxResponseTime": hm2AgentSwitchSnoopingQuerierOperMaxResponseTime,
       "hm2AgentSwitchSnoopingQuerierLastQuerierAddress": hm2AgentSwitchSnoopingQuerierLastQuerierAddress,
       "hm2AgentSwitchSnoopingQuerierLastQuerierVersion": hm2AgentSwitchSnoopingQuerierLastQuerierVersion,
       "hm2AgentDaiConfigGroup": hm2AgentDaiConfigGroup,
       "hm2AgentDaiSrcMacValidate": hm2AgentDaiSrcMacValidate,
       "hm2AgentDaiDstMacValidate": hm2AgentDaiDstMacValidate,
       "hm2AgentDaiIPValidate": hm2AgentDaiIPValidate,
       "hm2AgentDaiVlanConfigTable": hm2AgentDaiVlanConfigTable,
       "hm2AgentDaiVlanConfigEntry": hm2AgentDaiVlanConfigEntry,
       "hm2AgentDaiVlanIndex": hm2AgentDaiVlanIndex,
       "hm2AgentDaiVlanDynArpInspEnable": hm2AgentDaiVlanDynArpInspEnable,
       "hm2AgentDaiVlanLoggingEnable": hm2AgentDaiVlanLoggingEnable,
       "hm2AgentDaiVlanArpAclName": hm2AgentDaiVlanArpAclName,
       "hm2AgentDaiVlanArpAclStaticFlag": hm2AgentDaiVlanArpAclStaticFlag,
       "hm2AgentDaiVlanBindingCheckEnable": hm2AgentDaiVlanBindingCheckEnable,
       "hm2AgentDaiStatsReset": hm2AgentDaiStatsReset,
       "hm2AgentDaiVlanStatsTable": hm2AgentDaiVlanStatsTable,
       "hm2AgentDaiVlanStatsEntry": hm2AgentDaiVlanStatsEntry,
       "hm2AgentDaiVlanStatsIndex": hm2AgentDaiVlanStatsIndex,
       "hm2AgentDaiVlanPktsForwarded": hm2AgentDaiVlanPktsForwarded,
       "hm2AgentDaiVlanPktsDropped": hm2AgentDaiVlanPktsDropped,
       "hm2AgentDaiVlanDhcpDrops": hm2AgentDaiVlanDhcpDrops,
       "hm2AgentDaiVlanDhcpPermits": hm2AgentDaiVlanDhcpPermits,
       "hm2AgentDaiVlanAclDrops": hm2AgentDaiVlanAclDrops,
       "hm2AgentDaiVlanAclPermits": hm2AgentDaiVlanAclPermits,
       "hm2AgentDaiVlanSrcMacFailures": hm2AgentDaiVlanSrcMacFailures,
       "hm2AgentDaiVlanDstMacFailures": hm2AgentDaiVlanDstMacFailures,
       "hm2AgentDaiVlanIpValidFailures": hm2AgentDaiVlanIpValidFailures,
       "hm2AgentDaiIfConfigTable": hm2AgentDaiIfConfigTable,
       "hm2AgentDaiIfConfigEntry": hm2AgentDaiIfConfigEntry,
       "hm2AgentDaiIfTrustEnable": hm2AgentDaiIfTrustEnable,
       "hm2AgentDaiIfRateLimit": hm2AgentDaiIfRateLimit,
       "hm2AgentDaiIfBurstInterval": hm2AgentDaiIfBurstInterval,
       "hm2AgentDaiIfAutoDisable": hm2AgentDaiIfAutoDisable,
       "hm2AgentArpAclGroup": hm2AgentArpAclGroup,
       "hm2AgentArpAclTable": hm2AgentArpAclTable,
       "hm2AgentArpAclEntry": hm2AgentArpAclEntry,
       "hm2AgentArpAclName": hm2AgentArpAclName,
       "hm2AgentArpAclRowStatus": hm2AgentArpAclRowStatus,
       "hm2AgentArpAclRuleTable": hm2AgentArpAclRuleTable,
       "hm2AgentArpAclRuleEntry": hm2AgentArpAclRuleEntry,
       "hm2AgentArpAclRuleMatchSenderIpAddr": hm2AgentArpAclRuleMatchSenderIpAddr,
       "hm2AgentArpAclRuleMatchSenderMacAddr": hm2AgentArpAclRuleMatchSenderMacAddr,
       "hm2AgentArpAclRuleRowStatus": hm2AgentArpAclRuleRowStatus,
       "hm2AgentDhcpSnoopingConfigGroup": hm2AgentDhcpSnoopingConfigGroup,
       "hm2AgentDhcpSnoopingAdminMode": hm2AgentDhcpSnoopingAdminMode,
       "hm2AgentDhcpSnoopingVerifyMac": hm2AgentDhcpSnoopingVerifyMac,
       "hm2AgentDhcpSnoopingVlanConfigTable": hm2AgentDhcpSnoopingVlanConfigTable,
       "hm2AgentDhcpSnoopingVlanConfigEntry": hm2AgentDhcpSnoopingVlanConfigEntry,
       "hm2AgentDhcpSnoopingVlanIndex": hm2AgentDhcpSnoopingVlanIndex,
       "hm2AgentDhcpSnoopingVlanEnable": hm2AgentDhcpSnoopingVlanEnable,
       "hm2AgentDhcpSnoopingIfConfigTable": hm2AgentDhcpSnoopingIfConfigTable,
       "hm2AgentDhcpSnoopingIfConfigEntry": hm2AgentDhcpSnoopingIfConfigEntry,
       "hm2AgentDhcpSnoopingIfTrustEnable": hm2AgentDhcpSnoopingIfTrustEnable,
       "hm2AgentDhcpSnoopingIfLogEnable": hm2AgentDhcpSnoopingIfLogEnable,
       "hm2AgentDhcpSnoopingIfRateLimit": hm2AgentDhcpSnoopingIfRateLimit,
       "hm2AgentDhcpSnoopingIfBurstInterval": hm2AgentDhcpSnoopingIfBurstInterval,
       "hm2AgentDhcpSnoopingIfAutoDisable": hm2AgentDhcpSnoopingIfAutoDisable,
       "hm2AgentIpsgIfConfigTable": hm2AgentIpsgIfConfigTable,
       "hm2AgentIpsgIfConfigEntry": hm2AgentIpsgIfConfigEntry,
       "hm2AgentIpsgIfVerifySource": hm2AgentIpsgIfVerifySource,
       "hm2AgentIpsgIfPortSecurity": hm2AgentIpsgIfPortSecurity,
       "hm2AgentDhcpSnoopingStatsReset": hm2AgentDhcpSnoopingStatsReset,
       "hm2AgentDhcpSnoopingStatsTable": hm2AgentDhcpSnoopingStatsTable,
       "hm2AgentDhcpSnoopingStatsEntry": hm2AgentDhcpSnoopingStatsEntry,
       "hm2AgentDhcpSnoopingMacVerifyFailures": hm2AgentDhcpSnoopingMacVerifyFailures,
       "hm2AgentDhcpSnoopingInvalidClientMessages": hm2AgentDhcpSnoopingInvalidClientMessages,
       "hm2AgentDhcpSnoopingInvalidServerMessages": hm2AgentDhcpSnoopingInvalidServerMessages,
       "hm2AgentStaticIpsgBindingTable": hm2AgentStaticIpsgBindingTable,
       "hm2AgentStaticIpsgBindingEntry": hm2AgentStaticIpsgBindingEntry,
       "hm2AgentStaticIpsgBindingIfIndex": hm2AgentStaticIpsgBindingIfIndex,
       "hm2AgentStaticIpsgBindingVlanId": hm2AgentStaticIpsgBindingVlanId,
       "hm2AgentStaticIpsgBindingMacAddr": hm2AgentStaticIpsgBindingMacAddr,
       "hm2AgentStaticIpsgBindingIpAddr": hm2AgentStaticIpsgBindingIpAddr,
       "hm2AgentStaticIpsgBindingRowStatus": hm2AgentStaticIpsgBindingRowStatus,
       "hm2AgentStaticIpsgBindingHwStatus": hm2AgentStaticIpsgBindingHwStatus,
       "hm2AgentDynamicIpsgBindingTable": hm2AgentDynamicIpsgBindingTable,
       "hm2AgentDynamicIpsgBindingEntry": hm2AgentDynamicIpsgBindingEntry,
       "hm2AgentDynamicIpsgBindingIfIndex": hm2AgentDynamicIpsgBindingIfIndex,
       "hm2AgentDynamicIpsgBindingVlanId": hm2AgentDynamicIpsgBindingVlanId,
       "hm2AgentDynamicIpsgBindingMacAddr": hm2AgentDynamicIpsgBindingMacAddr,
       "hm2AgentDynamicIpsgBindingIpAddr": hm2AgentDynamicIpsgBindingIpAddr,
       "hm2AgentDynamicIpsgBindingHwStatus": hm2AgentDynamicIpsgBindingHwStatus,
       "hm2AgentStaticDsBindingTable": hm2AgentStaticDsBindingTable,
       "hm2AgentStaticDsBindingEntry": hm2AgentStaticDsBindingEntry,
       "hm2AgentStaticDsBindingIfIndex": hm2AgentStaticDsBindingIfIndex,
       "hm2AgentStaticDsBindingVlanId": hm2AgentStaticDsBindingVlanId,
       "hm2AgentStaticDsBindingMacAddr": hm2AgentStaticDsBindingMacAddr,
       "hm2AgentStaticDsBindingIpAddr": hm2AgentStaticDsBindingIpAddr,
       "hm2AgentStaticDsBindingRowStatus": hm2AgentStaticDsBindingRowStatus,
       "hm2AgentDynamicDsBindingTable": hm2AgentDynamicDsBindingTable,
       "hm2AgentDynamicDsBindingEntry": hm2AgentDynamicDsBindingEntry,
       "hm2AgentDynamicDsBindingIfIndex": hm2AgentDynamicDsBindingIfIndex,
       "hm2AgentDynamicDsBindingVlanId": hm2AgentDynamicDsBindingVlanId,
       "hm2AgentDynamicDsBindingMacAddr": hm2AgentDynamicDsBindingMacAddr,
       "hm2AgentDynamicDsBindingIpAddr": hm2AgentDynamicDsBindingIpAddr,
       "hm2AgentDynamicDsBindingLeaseRemainingTime": hm2AgentDynamicDsBindingLeaseRemainingTime,
       "hm2AgentDhcpSnoopingRemoteFileName": hm2AgentDhcpSnoopingRemoteFileName,
       "hm2AgentDhcpSnoopingRemoteIpAddr": hm2AgentDhcpSnoopingRemoteIpAddr,
       "hm2AgentDhcpSnoopingStoreInterval": hm2AgentDhcpSnoopingStoreInterval,
       "hm2AgentDhcpL2RelayConfigGroup": hm2AgentDhcpL2RelayConfigGroup,
       "hm2AgentDhcpL2RelayAdminMode": hm2AgentDhcpL2RelayAdminMode,
       "hm2AgentDhcpL2RelayIfConfigTable": hm2AgentDhcpL2RelayIfConfigTable,
       "hm2AgentDhcpL2RelayIfConfigEntry": hm2AgentDhcpL2RelayIfConfigEntry,
       "hm2AgentDhcpL2RelayIfEnable": hm2AgentDhcpL2RelayIfEnable,
       "hm2AgentDhcpL2RelayIfTrustEnable": hm2AgentDhcpL2RelayIfTrustEnable,
       "hm2AgentDhcpL2RelayVlanConfigTable": hm2AgentDhcpL2RelayVlanConfigTable,
       "hm2AgentDhcpL2RelayVlanConfigEntry": hm2AgentDhcpL2RelayVlanConfigEntry,
       "hm2AgentDhcpL2RelayVlanIndex": hm2AgentDhcpL2RelayVlanIndex,
       "hm2AgentDhcpL2RelayVlanEnable": hm2AgentDhcpL2RelayVlanEnable,
       "hm2AgentDhcpL2RelayCircuitIdVlanEnable": hm2AgentDhcpL2RelayCircuitIdVlanEnable,
       "hm2AgentDhcpL2RelayRemoteIdVlanEnable": hm2AgentDhcpL2RelayRemoteIdVlanEnable,
       "hm2AgentDhcpL2RelayVlanRemoteIdType": hm2AgentDhcpL2RelayVlanRemoteIdType,
       "hm2AgentDhcpL2RelayStatsReset": hm2AgentDhcpL2RelayStatsReset,
       "hm2AgentDhcpL2RelayStatsTable": hm2AgentDhcpL2RelayStatsTable,
       "hm2AgentDhcpL2RelayStatsEntry": hm2AgentDhcpL2RelayStatsEntry,
       "hm2AgentDhcpL2RelayUntrustedSrvrMsgsWithOptn82": hm2AgentDhcpL2RelayUntrustedSrvrMsgsWithOptn82,
       "hm2AgentDhcpL2RelayUntrustedClntMsgsWithOptn82": hm2AgentDhcpL2RelayUntrustedClntMsgsWithOptn82,
       "hm2AgentDhcpL2RelayTrustedSrvrMsgsWithoutOptn82": hm2AgentDhcpL2RelayTrustedSrvrMsgsWithoutOptn82,
       "hm2AgentDhcpL2RelayTrustedClntMsgsWithoutOptn82": hm2AgentDhcpL2RelayTrustedClntMsgsWithoutOptn82,
       "hm2AgentSwitchVoiceVLANGroup": hm2AgentSwitchVoiceVLANGroup,
       "hm2AgentSwitchVoiceVLANAdminMode": hm2AgentSwitchVoiceVLANAdminMode,
       "hm2AgentSwitchVoiceVlanDeviceTable": hm2AgentSwitchVoiceVlanDeviceTable,
       "hm2AgentSwitchVoiceVlanDeviceEntry": hm2AgentSwitchVoiceVlanDeviceEntry,
       "hm2AgentSwitchVoiceVlanInterfaceNum": hm2AgentSwitchVoiceVlanInterfaceNum,
       "hm2AgentSwitchVoiceVlanDeviceMacAddress": hm2AgentSwitchVoiceVlanDeviceMacAddress,
       "hm2AgentSdmPreferConfigGroup": hm2AgentSdmPreferConfigGroup,
       "hm2AgentSdmPreferCurrentTemplate": hm2AgentSdmPreferCurrentTemplate,
       "hm2AgentSdmPreferNextTemplate": hm2AgentSdmPreferNextTemplate,
       "hm2AgentSdmTemplateSummaryTable": hm2AgentSdmTemplateSummaryTable,
       "hm2AgentSdmTemplateTable": hm2AgentSdmTemplateTable,
       "hm2AgentSdmTemplateEntry": hm2AgentSdmTemplateEntry,
       "hm2AgentSdmTemplateId": hm2AgentSdmTemplateId,
       "hm2AgentArpEntries": hm2AgentArpEntries,
       "hm2AgentIPv4UnicastRoutes": hm2AgentIPv4UnicastRoutes,
       "hm2AgentIPv6NdpEntries": hm2AgentIPv6NdpEntries,
       "hm2AgentIPv6UnicastRoutes": hm2AgentIPv6UnicastRoutes,
       "hm2AgentEcmpNextHops": hm2AgentEcmpNextHops,
       "hm2AgentIPv4MulticastRoutes": hm2AgentIPv4MulticastRoutes,
       "hm2AgentIPv6MulticastRoutes": hm2AgentIPv6MulticastRoutes,
       "hm2AgentSwitchStaticMacStatsGroup": hm2AgentSwitchStaticMacStatsGroup,
       "hm2AgentSwitchStaticMacEntries": hm2AgentSwitchStaticMacEntries,
       "hm2AgentSwitchGARPGroup": hm2AgentSwitchGARPGroup,
       "hm2AgentSwitchGmrpUnknownMulticastFilterMode": hm2AgentSwitchGmrpUnknownMulticastFilterMode,
       "hm2AgentSwitchGmrpPortTable": hm2AgentSwitchGmrpPortTable,
       "hm2AgentSwitchGmrpPortEntry": hm2AgentSwitchGmrpPortEntry,
       "hm2AgentSwitchGmrpPortPktRx": hm2AgentSwitchGmrpPortPktRx,
       "hm2AgentSwitchGmrpPortPktTx": hm2AgentSwitchGmrpPortPktTx,
       "hm2AgentSwitchGvrpPortTable": hm2AgentSwitchGvrpPortTable,
       "hm2AgentSwitchGvrpPortEntry": hm2AgentSwitchGvrpPortEntry,
       "hm2AgentSwitchGvrpPortPktRx": hm2AgentSwitchGvrpPortPktRx,
       "hm2AgentSwitchGvrpPortPktTx": hm2AgentSwitchGvrpPortPktTx,
       "hm2AgentPortMirroringGroup": hm2AgentPortMirroringGroup,
       "hm2AgentPortMirrorTable": hm2AgentPortMirrorTable,
       "hm2AgentPortMirrorEntry": hm2AgentPortMirrorEntry,
       "hm2AgentPortMirrorSessionNum": hm2AgentPortMirrorSessionNum,
       "hm2AgentPortMirrorDestinationPort": hm2AgentPortMirrorDestinationPort,
       "hm2AgentPortMirrorSourcePortMask": hm2AgentPortMirrorSourcePortMask,
       "hm2AgentPortMirrorAdminMode": hm2AgentPortMirrorAdminMode,
       "hm2AgentPortMirrorSourceVlan": hm2AgentPortMirrorSourceVlan,
       "hm2AgentPortMirrorRemoteSourceVlan": hm2AgentPortMirrorRemoteSourceVlan,
       "hm2AgentPortMirrorRemoteDestinationVlan": hm2AgentPortMirrorRemoteDestinationVlan,
       "hm2AgentPortMirrorReflectorPort": hm2AgentPortMirrorReflectorPort,
       "hm2AgentPortMirrorAllowMgmtMode": hm2AgentPortMirrorAllowMgmtMode,
       "hm2AgentPortMirrorReset": hm2AgentPortMirrorReset,
       "hm2AgentPortMirrorTypeTable": hm2AgentPortMirrorTypeTable,
       "hm2AgentPortMirrorTypeEntry": hm2AgentPortMirrorTypeEntry,
       "hm2AgentPortMirrorTypeSourcePort": hm2AgentPortMirrorTypeSourcePort,
       "hm2AgentPortMirrorTypeType": hm2AgentPortMirrorTypeType,
       "hm2AgentPortMirrorRemoteVlan": hm2AgentPortMirrorRemoteVlan,
       "hm2AgentPortMirrorSNMPExtensionGroup": hm2AgentPortMirrorSNMPExtensionGroup,
       "hm2AgentPortMirrorVlanMirrorPortConflict": hm2AgentPortMirrorVlanMirrorPortConflict,
       "hm2AgentPortMirrorPortVlanMirrorConflict": hm2AgentPortMirrorPortVlanMirrorConflict,
       "hm2AgentPortMirrorProbePortAlreadySet": hm2AgentPortMirrorProbePortAlreadySet,
       "hm2AgentPortMirrorProbePortVlanConflict": hm2AgentPortMirrorProbePortVlanConflict,
       "hm2AgentPortMirrorVlanNotCreated": hm2AgentPortMirrorVlanNotCreated,
       "hm2AgentPortMirrorInvalidSourcePort": hm2AgentPortMirrorInvalidSourcePort,
       "hm2AgentPortMirrorSourcePortDestinationPortConflict": hm2AgentPortMirrorSourcePortDestinationPortConflict,
       "hm2AgentPortMirrorDestinationPortInvalid": hm2AgentPortMirrorDestinationPortInvalid,
       "hm2AgentPortMirrorVlanRspanVlanConflict": hm2AgentPortMirrorVlanRspanVlanConflict,
       "hm2AgentPortMirrorRemoteSourceRemoteDestinationConflict": hm2AgentPortMirrorRemoteSourceRemoteDestinationConflict,
       "hm2AgentPortMirrorReflectorPortInvalid": hm2AgentPortMirrorReflectorPortInvalid,
       "hm2AgentPortMirrorSourcePortReflectorPortConflict": hm2AgentPortMirrorSourcePortReflectorPortConflict,
       "hm2AgentPortMirrorReflectorPortVlanConflict": hm2AgentPortMirrorReflectorPortVlanConflict,
       "hm2AgentPortMirrorPrivateVlanConfigured": hm2AgentPortMirrorPrivateVlanConfigured,
       "hm2AgentPortMirrorDestinationRemotePortNotSet": hm2AgentPortMirrorDestinationRemotePortNotSet,
       "hm2AgentPortMirrorRspanVlanInconsistent": hm2AgentPortMirrorRspanVlanInconsistent,
       "hm2AgentPortMirrorRspanVlanIdInvalid": hm2AgentPortMirrorRspanVlanIdInvalid,
       "hm2AgentDot3adAggPortTable": hm2AgentDot3adAggPortTable,
       "hm2AgentDot3adAggPortEntry": hm2AgentDot3adAggPortEntry,
       "hm2AgentDot3adAggPort": hm2AgentDot3adAggPort,
       "hm2AgentDot3adAggPortLACPMode": hm2AgentDot3adAggPortLACPMode,
       "hm2AgentPortConfigTable": hm2AgentPortConfigTable,
       "hm2AgentPortConfigEntry": hm2AgentPortConfigEntry,
       "hm2AgentPortDot1dBasePort": hm2AgentPortDot1dBasePort,
       "hm2AgentPortIfIndex": hm2AgentPortIfIndex,
       "hm2AgentPortClearStats": hm2AgentPortClearStats,
       "hm2AgentPortDot3FlowControlMode": hm2AgentPortDot3FlowControlMode,
       "hm2AgentPortMaxFrameSizeLimit": hm2AgentPortMaxFrameSizeLimit,
       "hm2AgentPortMaxFrameSize": hm2AgentPortMaxFrameSize,
       "hm2AgentPortBroadcastControlMode": hm2AgentPortBroadcastControlMode,
       "hm2AgentPortBroadcastControlThreshold": hm2AgentPortBroadcastControlThreshold,
       "hm2AgentPortMulticastControlMode": hm2AgentPortMulticastControlMode,
       "hm2AgentPortMulticastControlThreshold": hm2AgentPortMulticastControlThreshold,
       "hm2AgentPortUnicastControlMode": hm2AgentPortUnicastControlMode,
       "hm2AgentPortUnicastControlThreshold": hm2AgentPortUnicastControlThreshold,
       "hm2AgentPortBroadcastControlThresholdUnit": hm2AgentPortBroadcastControlThresholdUnit,
       "hm2AgentPortMulticastControlThresholdUnit": hm2AgentPortMulticastControlThresholdUnit,
       "hm2AgentPortUnicastControlThresholdUnit": hm2AgentPortUnicastControlThresholdUnit,
       "hm2AgentPortVoiceVlanMode": hm2AgentPortVoiceVlanMode,
       "hm2AgentPortVoiceVlanID": hm2AgentPortVoiceVlanID,
       "hm2AgentPortVoiceVlanPriority": hm2AgentPortVoiceVlanPriority,
       "hm2AgentPortVoiceVlanDataPriorityMode": hm2AgentPortVoiceVlanDataPriorityMode,
       "hm2AgentPortVoiceVlanOperationalStatus": hm2AgentPortVoiceVlanOperationalStatus,
       "hm2AgentPortVoiceVlanUntagged": hm2AgentPortVoiceVlanUntagged,
       "hm2AgentPortVoiceVlanNoneMode": hm2AgentPortVoiceVlanNoneMode,
       "hm2AgentPortVoiceVlanDSCP": hm2AgentPortVoiceVlanDSCP,
       "hm2AgentPortVoiceVlanAuthMode": hm2AgentPortVoiceVlanAuthMode,
       "hm2AgentPortDot3FlowControlOperStatus": hm2AgentPortDot3FlowControlOperStatus,
       "hm2AgentPortSfpLinkLossAlert": hm2AgentPortSfpLinkLossAlert,
       "hm2AgentProtocolConfigGroup": hm2AgentProtocolConfigGroup,
       "hm2AgentProtocolGroupTable": hm2AgentProtocolGroupTable,
       "hm2AgentProtocolGroupEntry": hm2AgentProtocolGroupEntry,
       "hm2AgentProtocolGroupId": hm2AgentProtocolGroupId,
       "hm2AgentProtocolGroupName": hm2AgentProtocolGroupName,
       "hm2AgentProtocolGroupVlanId": hm2AgentProtocolGroupVlanId,
       "hm2AgentProtocolGroupStatus": hm2AgentProtocolGroupStatus,
       "hm2AgentProtocolGroupPortTable": hm2AgentProtocolGroupPortTable,
       "hm2AgentProtocolGroupPortEntry": hm2AgentProtocolGroupPortEntry,
       "hm2AgentProtocolGroupPortIfIndex": hm2AgentProtocolGroupPortIfIndex,
       "hm2AgentProtocolGroupPortStatus": hm2AgentProtocolGroupPortStatus,
       "hm2AgentProtocolGroupProtocolTable": hm2AgentProtocolGroupProtocolTable,
       "hm2AgentProtocolGroupProtocolEntry": hm2AgentProtocolGroupProtocolEntry,
       "hm2AgentProtocolGroupProtocolID": hm2AgentProtocolGroupProtocolID,
       "hm2AgentProtocolGroupProtocolStatus": hm2AgentProtocolGroupProtocolStatus,
       "hm2AgentStpSwitchConfigGroup": hm2AgentStpSwitchConfigGroup,
       "hm2AgentStpConfigDigestKey": hm2AgentStpConfigDigestKey,
       "hm2AgentStpConfigFormatSelector": hm2AgentStpConfigFormatSelector,
       "hm2AgentStpConfigName": hm2AgentStpConfigName,
       "hm2AgentStpConfigRevision": hm2AgentStpConfigRevision,
       "hm2AgentStpForceVersion": hm2AgentStpForceVersion,
       "hm2AgentStpAdminMode": hm2AgentStpAdminMode,
       "hm2AgentStpPortTable": hm2AgentStpPortTable,
       "hm2AgentStpPortEntry": hm2AgentStpPortEntry,
       "hm2AgentStpPortState": hm2AgentStpPortState,
       "hm2AgentStpPortStatsMstpBpduRx": hm2AgentStpPortStatsMstpBpduRx,
       "hm2AgentStpPortStatsMstpBpduTx": hm2AgentStpPortStatsMstpBpduTx,
       "hm2AgentStpPortStatsRstpBpduRx": hm2AgentStpPortStatsRstpBpduRx,
       "hm2AgentStpPortStatsRstpBpduTx": hm2AgentStpPortStatsRstpBpduTx,
       "hm2AgentStpPortStatsStpBpduRx": hm2AgentStpPortStatsStpBpduRx,
       "hm2AgentStpPortStatsStpBpduTx": hm2AgentStpPortStatsStpBpduTx,
       "hm2AgentStpPortUpTime": hm2AgentStpPortUpTime,
       "hm2AgentStpPortMigrationCheck": hm2AgentStpPortMigrationCheck,
       "hm2AgentStpCstConfigGroup": hm2AgentStpCstConfigGroup,
       "hm2AgentStpCstHelloTime": hm2AgentStpCstHelloTime,
       "hm2AgentStpCstMaxAge": hm2AgentStpCstMaxAge,
       "hm2AgentStpCstRegionalRootId": hm2AgentStpCstRegionalRootId,
       "hm2AgentStpCstRegionalRootPathCost": hm2AgentStpCstRegionalRootPathCost,
       "hm2AgentStpCstRootFwdDelay": hm2AgentStpCstRootFwdDelay,
       "hm2AgentStpCstBridgeFwdDelay": hm2AgentStpCstBridgeFwdDelay,
       "hm2AgentStpCstBridgeHelloTime": hm2AgentStpCstBridgeHelloTime,
       "hm2AgentStpCstBridgeHoldTime": hm2AgentStpCstBridgeHoldTime,
       "hm2AgentStpCstBridgeMaxAge": hm2AgentStpCstBridgeMaxAge,
       "hm2AgentStpCstBridgeMaxHops": hm2AgentStpCstBridgeMaxHops,
       "hm2AgentStpCstBridgePriority": hm2AgentStpCstBridgePriority,
       "hm2AgentStpCstBridgeHoldCount": hm2AgentStpCstBridgeHoldCount,
       "hm2AgentStpCstPortTable": hm2AgentStpCstPortTable,
       "hm2AgentStpCstPortEntry": hm2AgentStpCstPortEntry,
       "hm2AgentStpCstPortOperEdge": hm2AgentStpCstPortOperEdge,
       "hm2AgentStpCstPortOperPointToPoint": hm2AgentStpCstPortOperPointToPoint,
       "hm2AgentStpCstPortTopologyChangeAck": hm2AgentStpCstPortTopologyChangeAck,
       "hm2AgentStpCstPortEdge": hm2AgentStpCstPortEdge,
       "hm2AgentStpCstPortForwardingState": hm2AgentStpCstPortForwardingState,
       "hm2AgentStpCstPortId": hm2AgentStpCstPortId,
       "hm2AgentStpCstPortPathCost": hm2AgentStpCstPortPathCost,
       "hm2AgentStpCstPortPriority": hm2AgentStpCstPortPriority,
       "hm2AgentStpCstDesignatedBridgeId": hm2AgentStpCstDesignatedBridgeId,
       "hm2AgentStpCstDesignatedCost": hm2AgentStpCstDesignatedCost,
       "hm2AgentStpCstDesignatedPortId": hm2AgentStpCstDesignatedPortId,
       "hm2AgentStpCstExtPortPathCost": hm2AgentStpCstExtPortPathCost,
       "hm2AgentStpCstPortBpduGuardEffect": hm2AgentStpCstPortBpduGuardEffect,
       "hm2AgentStpCstPortBpduFilter": hm2AgentStpCstPortBpduFilter,
       "hm2AgentStpCstPortBpduFlood": hm2AgentStpCstPortBpduFlood,
       "hm2AgentStpCstPortAutoEdge": hm2AgentStpCstPortAutoEdge,
       "hm2AgentStpCstPortRootGuard": hm2AgentStpCstPortRootGuard,
       "hm2AgentStpCstPortTCNGuard": hm2AgentStpCstPortTCNGuard,
       "hm2AgentStpCstPortLoopGuard": hm2AgentStpCstPortLoopGuard,
       "hm2AgentStpMstTable": hm2AgentStpMstTable,
       "hm2AgentStpMstEntry": hm2AgentStpMstEntry,
       "hm2AgentStpMstId": hm2AgentStpMstId,
       "hm2AgentStpMstBridgePriority": hm2AgentStpMstBridgePriority,
       "hm2AgentStpMstBridgeIdentifier": hm2AgentStpMstBridgeIdentifier,
       "hm2AgentStpMstDesignatedRootId": hm2AgentStpMstDesignatedRootId,
       "hm2AgentStpMstRootPathCost": hm2AgentStpMstRootPathCost,
       "hm2AgentStpMstRootPortId": hm2AgentStpMstRootPortId,
       "hm2AgentStpMstTimeSinceTopologyChange": hm2AgentStpMstTimeSinceTopologyChange,
       "hm2AgentStpMstTopologyChangeCount": hm2AgentStpMstTopologyChangeCount,
       "hm2AgentStpMstTopologyChangeParm": hm2AgentStpMstTopologyChangeParm,
       "hm2AgentStpMstRowStatus": hm2AgentStpMstRowStatus,
       "hm2AgentStpMstPortTable": hm2AgentStpMstPortTable,
       "hm2AgentStpMstPortEntry": hm2AgentStpMstPortEntry,
       "hm2AgentStpMstPortForwardingState": hm2AgentStpMstPortForwardingState,
       "hm2AgentStpMstPortId": hm2AgentStpMstPortId,
       "hm2AgentStpMstPortPathCost": hm2AgentStpMstPortPathCost,
       "hm2AgentStpMstPortPriority": hm2AgentStpMstPortPriority,
       "hm2AgentStpMstDesignatedBridgeId": hm2AgentStpMstDesignatedBridgeId,
       "hm2AgentStpMstDesignatedCost": hm2AgentStpMstDesignatedCost,
       "hm2AgentStpMstDesignatedPortId": hm2AgentStpMstDesignatedPortId,
       "hm2AgentStpMstPortLoopInconsistentState": hm2AgentStpMstPortLoopInconsistentState,
       "hm2AgentStpMstPortTransitionsIntoLoopInconsistentState": hm2AgentStpMstPortTransitionsIntoLoopInconsistentState,
       "hm2AgentStpMstPortTransitionsOutOfLoopInconsistentState": hm2AgentStpMstPortTransitionsOutOfLoopInconsistentState,
       "hm2AgentStpMstPortRole": hm2AgentStpMstPortRole,
       "hm2AgentStpCstAutoPortPathCost": hm2AgentStpCstAutoPortPathCost,
       "hm2AgentStpMstPortReceivedBridgeId": hm2AgentStpMstPortReceivedBridgeId,
       "hm2AgentStpMstPortReceivedRPC": hm2AgentStpMstPortReceivedRPC,
       "hm2AgentStpMstPortReceivedPortId": hm2AgentStpMstPortReceivedPortId,
       "hm2AgentStpMstAutoPortPathCost": hm2AgentStpMstAutoPortPathCost,
       "hm2AgentStpMstPortReceivedRegionalRPC": hm2AgentStpMstPortReceivedRegionalRPC,
       "hm2AgentStpMstVlanTable": hm2AgentStpMstVlanTable,
       "hm2AgentStpMstVlanEntry": hm2AgentStpMstVlanEntry,
       "hm2AgentStpMstVlanRowStatus": hm2AgentStpMstVlanRowStatus,
       "hm2AgentStpBpduGuardMode": hm2AgentStpBpduGuardMode,
       "hm2AgentStpBpduFilterDefault": hm2AgentStpBpduFilterDefault,
       "hm2AgentStpRingOnlyMode": hm2AgentStpRingOnlyMode,
       "hm2AgentStpRingOnlyModeIntfOne": hm2AgentStpRingOnlyModeIntfOne,
       "hm2AgentStpRingOnlyModeIntfTwo": hm2AgentStpRingOnlyModeIntfTwo,
       "hm2AgentStpMstSNMPExtensionGroup": hm2AgentStpMstSNMPExtensionGroup,
       "hm2AgentStpMstInstanceVlanErrorReturn": hm2AgentStpMstInstanceVlanErrorReturn,
       "hm2AgentStpCstFwdDelayErrorReturn": hm2AgentStpCstFwdDelayErrorReturn,
       "hm2AgentStpMstSwitchVersionConflict": hm2AgentStpMstSwitchVersionConflict,
       "hm2AgentClassOfServiceGroup": hm2AgentClassOfServiceGroup,
       "hm2AgentClassOfServicePortTable": hm2AgentClassOfServicePortTable,
       "hm2AgentClassOfServicePortEntry": hm2AgentClassOfServicePortEntry,
       "hm2AgentClassOfServicePortPriority": hm2AgentClassOfServicePortPriority,
       "hm2AgentClassOfServicePortClass": hm2AgentClassOfServicePortClass,
       "hm2AgentSystemGroup": hm2AgentSystemGroup,
       "hm2AgentClearVlan": hm2AgentClearVlan}
)
