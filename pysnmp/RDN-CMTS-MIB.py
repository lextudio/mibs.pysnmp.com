# SNMP MIB module (RDN-CMTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RDN-CMTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:06 2024
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

(DocsisQosVersion,
 DocsisUpstreamType,
 TenthdB,
 TenthdBmV,
 docsIfCmtsCmStatusDocsisRegMode,
 docsIfCmtsCmStatusEntry,
 docsIfCmtsCmStatusIndex,
 docsIfCmtsCmStatusIpAddress,
 docsIfCmtsCmStatusMacAddress,
 docsIfDownChannelId,
 docsIfUpChannelId) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "DocsisQosVersion",
    "DocsisUpstreamType",
    "TenthdB",
    "TenthdBmV",
    "docsIfCmtsCmStatusDocsisRegMode",
    "docsIfCmtsCmStatusEntry",
    "docsIfCmtsCmStatusIndex",
    "docsIfCmtsCmStatusIpAddress",
    "docsIfCmtsCmStatusMacAddress",
    "docsIfDownChannelId",
    "docsIfUpChannelId")

(IfDirection,
 docsIf3CmtsCmRegStatusIPv6Addr) = mibBuilder.importSymbols(
    "DOCS-IF3-MIB",
    "IfDirection",
    "docsIf3CmtsCmRegStatusIPv6Addr")

(docsQosServiceClassName,) = mibBuilder.importSymbols(
    "DOCS-QOS3-MIB",
    "docsQosServiceClassName")

(IpV4orV6Addr,) = mibBuilder.importSymbols(
    "DOCS-SUBMGT-MIB",
    "IpV4orV6Addr")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifAdminStatus,
 ifDescr,
 ifIndex,
 ifOperStatus,
 ifType) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifAdminStatus",
    "ifDescr",
    "ifIndex",
    "ifOperStatus",
    "ifType")

(InetAddress,
 InetAddressIPv6,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressType",
    "InetPortNumber")

(rdnSpectrumGroupName,) = mibBuilder.importSymbols(
    "RDN-CABLE-SPECTRUM-GROUP-MIB",
    "rdnSpectrumGroupName")

(riverdelta,) = mibBuilder.importSymbols(
    "RDN-MIB",
    "riverdelta")

(rdnPktDQoSClassName,) = mibBuilder.importSymbols(
    "RDN-PKTCABLE-GROUP-MIB",
    "rdnPktDQoSClassName")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

rdnCmtsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 2)
)
rdnCmtsMib.setRevisions(
        ("2011-03-08 00:00",
         "2011-02-23 00:00",
         "2009-11-20 00:00",
         "2008-08-08 00:00",
         "2007-06-21 00:00",
         "2006-05-25 00:00",
         "2006-05-24 00:00",
         "2006-04-17 00:00",
         "2006-01-25 00:00",
         "2006-01-23 00:00",
         "2006-01-13 00:00",
         "2005-03-18 00:00",
         "2005-02-22 00:00",
         "2004-08-17 00:00",
         "1904-04-14 00:00",
         "2003-12-16 00:00",
         "2003-11-05 00:00",
         "2003-11-03 00:00",
         "2003-07-20 00:00",
         "2003-05-01 00:00",
         "2000-04-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RdnCmtsIfObjects_ObjectIdentity = ObjectIdentity
rdnCmtsIfObjects = _RdnCmtsIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 2, 1)
)
_RdnCmtsDownstreamChannelTable_Object = MibTable
rdnCmtsDownstreamChannelTable = _RdnCmtsDownstreamChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rdnCmtsDownstreamChannelTable.setStatus("current")
_RdnCmtsDownstreamChannelEntry_Object = MibTableRow
rdnCmtsDownstreamChannelEntry = _RdnCmtsDownstreamChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 1, 1, 1)
)
rdnCmtsDownstreamChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rdnCmtsDownstreamChannelEntry.setStatus("current")
_RdnCmtsDSModulation_Type = TruthValue
_RdnCmtsDSModulation_Object = MibTableColumn
rdnCmtsDSModulation = _RdnCmtsDSModulation_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 1, 1, 1, 1),
    _RdnCmtsDSModulation_Type()
)
rdnCmtsDSModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCmtsDSModulation.setStatus("current")
_RdnCmtsUpstreamChannelTable_Object = MibTable
rdnCmtsUpstreamChannelTable = _RdnCmtsUpstreamChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 1, 2)
)
if mibBuilder.loadTexts:
    rdnCmtsUpstreamChannelTable.setStatus("current")
_RdnCmtsUpstreamChannelEntry_Object = MibTableRow
rdnCmtsUpstreamChannelEntry = _RdnCmtsUpstreamChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 1, 2, 1)
)
rdnCmtsUpstreamChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rdnCmtsUpstreamChannelEntry.setStatus("current")


class _RdnCmtsUSNominalRxPower_Type(Integer32):
    """Custom type rdnCmtsUSNominalRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-160, 290),
    )


_RdnCmtsUSNominalRxPower_Type.__name__ = "Integer32"
_RdnCmtsUSNominalRxPower_Object = MibTableColumn
rdnCmtsUSNominalRxPower = _RdnCmtsUSNominalRxPower_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 1, 2, 1, 1),
    _RdnCmtsUSNominalRxPower_Type()
)
rdnCmtsUSNominalRxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCmtsUSNominalRxPower.setStatus("current")


class _RdnCmtsUSNominalRxPowerMode_Type(Integer32):
    """Custom type rdnCmtsUSNominalRxPowerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("default", 0))
    )


_RdnCmtsUSNominalRxPowerMode_Type.__name__ = "Integer32"
_RdnCmtsUSNominalRxPowerMode_Object = MibTableColumn
rdnCmtsUSNominalRxPowerMode = _RdnCmtsUSNominalRxPowerMode_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 1, 2, 1, 2),
    _RdnCmtsUSNominalRxPowerMode_Type()
)
rdnCmtsUSNominalRxPowerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCmtsUSNominalRxPowerMode.setStatus("current")


class _RdnCmtsUSInvitedRangingInterval_Type(Integer32):
    """Custom type rdnCmtsUSInvitedRangingInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_RdnCmtsUSInvitedRangingInterval_Type.__name__ = "Integer32"
_RdnCmtsUSInvitedRangingInterval_Object = MibTableColumn
rdnCmtsUSInvitedRangingInterval = _RdnCmtsUSInvitedRangingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 1, 2, 1, 3),
    _RdnCmtsUSInvitedRangingInterval_Type()
)
rdnCmtsUSInvitedRangingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCmtsUSInvitedRangingInterval.setStatus("current")


class _RdnCmtsUSRangingResponseControl_Type(Integer32):
    """Custom type rdnCmtsUSRangingResponseControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("override", 1))
    )


_RdnCmtsUSRangingResponseControl_Type.__name__ = "Integer32"
_RdnCmtsUSRangingResponseControl_Object = MibTableColumn
rdnCmtsUSRangingResponseControl = _RdnCmtsUSRangingResponseControl_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 1, 2, 1, 4),
    _RdnCmtsUSRangingResponseControl_Type()
)
rdnCmtsUSRangingResponseControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCmtsUSRangingResponseControl.setStatus("current")
_RdnCmtsUSRangingPowerOverride_Type = TruthValue
_RdnCmtsUSRangingPowerOverride_Object = MibTableColumn
rdnCmtsUSRangingPowerOverride = _RdnCmtsUSRangingPowerOverride_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 1, 2, 1, 5),
    _RdnCmtsUSRangingPowerOverride_Type()
)
rdnCmtsUSRangingPowerOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCmtsUSRangingPowerOverride.setStatus("current")


class _RdnCmtsUSTotalModemCount_Type(Integer32):
    """Custom type rdnCmtsUSTotalModemCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RdnCmtsUSTotalModemCount_Type.__name__ = "Integer32"
_RdnCmtsUSTotalModemCount_Object = MibTableColumn
rdnCmtsUSTotalModemCount = _RdnCmtsUSTotalModemCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 1, 2, 1, 6),
    _RdnCmtsUSTotalModemCount_Type()
)
rdnCmtsUSTotalModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCmtsUSTotalModemCount.setStatus("current")


class _RdnCmtsUSRegisteredModemCount_Type(Integer32):
    """Custom type rdnCmtsUSRegisteredModemCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RdnCmtsUSRegisteredModemCount_Type.__name__ = "Integer32"
_RdnCmtsUSRegisteredModemCount_Object = MibTableColumn
rdnCmtsUSRegisteredModemCount = _RdnCmtsUSRegisteredModemCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 1, 2, 1, 7),
    _RdnCmtsUSRegisteredModemCount_Type()
)
rdnCmtsUSRegisteredModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCmtsUSRegisteredModemCount.setStatus("current")


class _RdnCmtsUSUnregisteredModemCount_Type(Integer32):
    """Custom type rdnCmtsUSUnregisteredModemCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RdnCmtsUSUnregisteredModemCount_Type.__name__ = "Integer32"
_RdnCmtsUSUnregisteredModemCount_Object = MibTableColumn
rdnCmtsUSUnregisteredModemCount = _RdnCmtsUSUnregisteredModemCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 1, 2, 1, 8),
    _RdnCmtsUSUnregisteredModemCount_Type()
)
rdnCmtsUSUnregisteredModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCmtsUSUnregisteredModemCount.setStatus("current")


class _RdnCmtsUSOfflineModemCount_Type(Integer32):
    """Custom type rdnCmtsUSOfflineModemCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RdnCmtsUSOfflineModemCount_Type.__name__ = "Integer32"
_RdnCmtsUSOfflineModemCount_Object = MibTableColumn
rdnCmtsUSOfflineModemCount = _RdnCmtsUSOfflineModemCount_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 1, 2, 1, 9),
    _RdnCmtsUSOfflineModemCount_Type()
)
rdnCmtsUSOfflineModemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCmtsUSOfflineModemCount.setStatus("current")
_RdnCmtsStpObjects_ObjectIdentity = ObjectIdentity
rdnCmtsStpObjects = _RdnCmtsStpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 2, 1, 3)
)
_RdnCmtsStpEnable_Type = TruthValue
_RdnCmtsStpEnable_Object = MibScalar
rdnCmtsStpEnable = _RdnCmtsStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 1, 3, 1),
    _RdnCmtsStpEnable_Type()
)
rdnCmtsStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCmtsStpEnable.setStatus("current")
_RdnCmtsStpTCNEnable_Type = TruthValue
_RdnCmtsStpTCNEnable_Object = MibScalar
rdnCmtsStpTCNEnable = _RdnCmtsStpTCNEnable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 1, 3, 2),
    _RdnCmtsStpTCNEnable_Type()
)
rdnCmtsStpTCNEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCmtsStpTCNEnable.setStatus("current")
_RdnCmtsLinkUpDownTrapEnableTable_Object = MibTable
rdnCmtsLinkUpDownTrapEnableTable = _RdnCmtsLinkUpDownTrapEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 1, 4)
)
if mibBuilder.loadTexts:
    rdnCmtsLinkUpDownTrapEnableTable.setStatus("current")
_RdnCmtsLinkUpDownTrapEnableEntry_Object = MibTableRow
rdnCmtsLinkUpDownTrapEnableEntry = _RdnCmtsLinkUpDownTrapEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 1, 4, 1)
)
rdnCmtsLinkUpDownTrapEnableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rdnCmtsLinkUpDownTrapEnableEntry.setStatus("current")


class _RdnCmtsLinkUpDownTrapEnable_Type(Integer32):
    """Custom type rdnCmtsLinkUpDownTrapEnable based on Integer32"""
    defaultValue = 2

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


_RdnCmtsLinkUpDownTrapEnable_Type.__name__ = "Integer32"
_RdnCmtsLinkUpDownTrapEnable_Object = MibTableColumn
rdnCmtsLinkUpDownTrapEnable = _RdnCmtsLinkUpDownTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 1, 4, 1, 1),
    _RdnCmtsLinkUpDownTrapEnable_Type()
)
rdnCmtsLinkUpDownTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCmtsLinkUpDownTrapEnable.setStatus("current")
_RdnCmtsMiscObjects_ObjectIdentity = ObjectIdentity
rdnCmtsMiscObjects = _RdnCmtsMiscObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2)
)
_RdnCmtsSaveConfig_Type = TruthValue
_RdnCmtsSaveConfig_Object = MibScalar
rdnCmtsSaveConfig = _RdnCmtsSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 1),
    _RdnCmtsSaveConfig_Type()
)
rdnCmtsSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCmtsSaveConfig.setStatus("current")
_RdnCmtsCmResetByMacAddr_Type = MacAddress
_RdnCmtsCmResetByMacAddr_Object = MibScalar
rdnCmtsCmResetByMacAddr = _RdnCmtsCmResetByMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 2),
    _RdnCmtsCmResetByMacAddr_Type()
)
rdnCmtsCmResetByMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCmtsCmResetByMacAddr.setStatus("current")
_RdnCmtsCmResetByIpAddr_Type = IpAddress
_RdnCmtsCmResetByIpAddr_Object = MibScalar
rdnCmtsCmResetByIpAddr = _RdnCmtsCmResetByIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 3),
    _RdnCmtsCmResetByIpAddr_Type()
)
rdnCmtsCmResetByIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCmtsCmResetByIpAddr.setStatus("current")
_RdnCmtsCmResetAll_Type = TruthValue
_RdnCmtsCmResetAll_Object = MibScalar
rdnCmtsCmResetAll = _RdnCmtsCmResetAll_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 4),
    _RdnCmtsCmResetAll_Type()
)
rdnCmtsCmResetAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCmtsCmResetAll.setStatus("current")


class _RdnCmtsHostAuthControl_Type(OctetString):
    """Custom type rdnCmtsHostAuthControl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )


_RdnCmtsHostAuthControl_Type.__name__ = "OctetString"
_RdnCmtsHostAuthControl_Object = MibScalar
rdnCmtsHostAuthControl = _RdnCmtsHostAuthControl_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 5),
    _RdnCmtsHostAuthControl_Type()
)
rdnCmtsHostAuthControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCmtsHostAuthControl.setStatus("obsolete")


class _RdnCmtsModemAgingTimer_Type(Integer32):
    """Custom type rdnCmtsModemAgingTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 30240),
    )


_RdnCmtsModemAgingTimer_Type.__name__ = "Integer32"
_RdnCmtsModemAgingTimer_Object = MibScalar
rdnCmtsModemAgingTimer = _RdnCmtsModemAgingTimer_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 6),
    _RdnCmtsModemAgingTimer_Type()
)
rdnCmtsModemAgingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCmtsModemAgingTimer.setStatus("current")
_RdnCmtsCpeToCmObject_ObjectIdentity = ObjectIdentity
rdnCmtsCpeToCmObject = _RdnCmtsCpeToCmObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 7)
)
_RdnCmtsCpeToCmTable_Object = MibTable
rdnCmtsCpeToCmTable = _RdnCmtsCpeToCmTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 7, 1)
)
if mibBuilder.loadTexts:
    rdnCmtsCpeToCmTable.setStatus("current")
_RdnCmtsCpeToCmEntry_Object = MibTableRow
rdnCmtsCpeToCmEntry = _RdnCmtsCpeToCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 7, 1, 1)
)
rdnCmtsCpeToCmEntry.setIndexNames(
    (0, "RDN-CMTS-MIB", "rdnCmtsCpeMac"),
)
if mibBuilder.loadTexts:
    rdnCmtsCpeToCmEntry.setStatus("current")
_RdnCmtsCpeMac_Type = MacAddress
_RdnCmtsCpeMac_Object = MibTableColumn
rdnCmtsCpeMac = _RdnCmtsCpeMac_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 7, 1, 1, 1),
    _RdnCmtsCpeMac_Type()
)
rdnCmtsCpeMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnCmtsCpeMac.setStatus("current")
_RdnCmtsCmMac_Type = MacAddress
_RdnCmtsCmMac_Object = MibTableColumn
rdnCmtsCmMac = _RdnCmtsCmMac_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 7, 1, 1, 2),
    _RdnCmtsCmMac_Type()
)
rdnCmtsCmMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCmtsCmMac.setStatus("current")
_RdnIfCmtsCmStatusTable_Object = MibTable
rdnIfCmtsCmStatusTable = _RdnIfCmtsCmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 8)
)
if mibBuilder.loadTexts:
    rdnIfCmtsCmStatusTable.setStatus("current")
_RdnIfCmtsCmStatusEntry_Object = MibTableRow
rdnIfCmtsCmStatusEntry = _RdnIfCmtsCmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 8, 1)
)
if mibBuilder.loadTexts:
    rdnIfCmtsCmStatusEntry.setStatus("current")
_RdnIfCmtsCmStatusRegistrationTime_Type = Integer32
_RdnIfCmtsCmStatusRegistrationTime_Object = MibTableColumn
rdnIfCmtsCmStatusRegistrationTime = _RdnIfCmtsCmStatusRegistrationTime_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 8, 1, 1),
    _RdnIfCmtsCmStatusRegistrationTime_Type()
)
rdnIfCmtsCmStatusRegistrationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsCmStatusRegistrationTime.setStatus("current")
_RdnIfCmtsCmStatusTxUnicastKbytes_Type = Counter32
_RdnIfCmtsCmStatusTxUnicastKbytes_Object = MibTableColumn
rdnIfCmtsCmStatusTxUnicastKbytes = _RdnIfCmtsCmStatusTxUnicastKbytes_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 8, 1, 2),
    _RdnIfCmtsCmStatusTxUnicastKbytes_Type()
)
rdnIfCmtsCmStatusTxUnicastKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsCmStatusTxUnicastKbytes.setStatus("current")
_RdnIfCmtsCmStatusRxUnicastKbytes_Type = Counter32
_RdnIfCmtsCmStatusRxUnicastKbytes_Object = MibTableColumn
rdnIfCmtsCmStatusRxUnicastKbytes = _RdnIfCmtsCmStatusRxUnicastKbytes_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 8, 1, 3),
    _RdnIfCmtsCmStatusRxUnicastKbytes_Type()
)
rdnIfCmtsCmStatusRxUnicastKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsCmStatusRxUnicastKbytes.setStatus("current")
_RdnIfCmtsCmStatusTxUnicastExtKbytes_Type = Counter64
_RdnIfCmtsCmStatusTxUnicastExtKbytes_Object = MibTableColumn
rdnIfCmtsCmStatusTxUnicastExtKbytes = _RdnIfCmtsCmStatusTxUnicastExtKbytes_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 8, 1, 4),
    _RdnIfCmtsCmStatusTxUnicastExtKbytes_Type()
)
rdnIfCmtsCmStatusTxUnicastExtKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsCmStatusTxUnicastExtKbytes.setStatus("current")
_RdnIfCmtsCmStatusRxUnicastExtKbytes_Type = Counter64
_RdnIfCmtsCmStatusRxUnicastExtKbytes_Object = MibTableColumn
rdnIfCmtsCmStatusRxUnicastExtKbytes = _RdnIfCmtsCmStatusRxUnicastExtKbytes_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 8, 1, 5),
    _RdnIfCmtsCmStatusRxUnicastExtKbytes_Type()
)
rdnIfCmtsCmStatusRxUnicastExtKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsCmStatusRxUnicastExtKbytes.setStatus("current")
_RdnIfCmtsCmStatusSpectrumGroupName_Type = DisplayString
_RdnIfCmtsCmStatusSpectrumGroupName_Object = MibTableColumn
rdnIfCmtsCmStatusSpectrumGroupName = _RdnIfCmtsCmStatusSpectrumGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 8, 1, 6),
    _RdnIfCmtsCmStatusSpectrumGroupName_Type()
)
rdnIfCmtsCmStatusSpectrumGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsCmStatusSpectrumGroupName.setStatus("current")


class _RdnIfCmtsCmStatusUpstreamPort_Type(Integer32):
    """Custom type rdnIfCmtsCmStatusUpstreamPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RdnIfCmtsCmStatusUpstreamPort_Type.__name__ = "Integer32"
_RdnIfCmtsCmStatusUpstreamPort_Object = MibTableColumn
rdnIfCmtsCmStatusUpstreamPort = _RdnIfCmtsCmStatusUpstreamPort_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 8, 1, 7),
    _RdnIfCmtsCmStatusUpstreamPort_Type()
)
rdnIfCmtsCmStatusUpstreamPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsCmStatusUpstreamPort.setStatus("current")


class _RdnIfCmtsCmStatusDownStreamPort_Type(Integer32):
    """Custom type rdnIfCmtsCmStatusDownStreamPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RdnIfCmtsCmStatusDownStreamPort_Type.__name__ = "Integer32"
_RdnIfCmtsCmStatusDownStreamPort_Object = MibTableColumn
rdnIfCmtsCmStatusDownStreamPort = _RdnIfCmtsCmStatusDownStreamPort_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 8, 1, 8),
    _RdnIfCmtsCmStatusDownStreamPort_Type()
)
rdnIfCmtsCmStatusDownStreamPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsCmStatusDownStreamPort.setStatus("current")


class _RdnIfCmtsCmStatusValue_Type(Integer32):
    """Custom type rdnIfCmtsCmStatusValue based on Integer32"""
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
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("dhcp-ack", 9),
          ("dhcp-d", 6),
          ("dhcp-o", 7),
          ("dhcp-req", 8),
          ("init-o", 1),
          ("init-r1", 3),
          ("init-r2", 4),
          ("init-rc", 5),
          ("init-t", 2),
          ("offline", 20),
          ("online", 10),
          ("online-d", 11),
          ("online-pk", 13),
          ("online-pt", 14),
          ("online-un", 12),
          ("reject-c", 16),
          ("reject-m", 15),
          ("reject-pk", 18),
          ("reject-pt", 19),
          ("reject-r", 17))
    )


_RdnIfCmtsCmStatusValue_Type.__name__ = "Integer32"
_RdnIfCmtsCmStatusValue_Object = MibTableColumn
rdnIfCmtsCmStatusValue = _RdnIfCmtsCmStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 8, 1, 9),
    _RdnIfCmtsCmStatusValue_Type()
)
rdnIfCmtsCmStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsCmStatusValue.setStatus("current")


class _RdnIfCmtsCmStatusDSBondingGroupId_Type(Integer32):
    """Custom type rdnIfCmtsCmStatusDSBondingGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RdnIfCmtsCmStatusDSBondingGroupId_Type.__name__ = "Integer32"
_RdnIfCmtsCmStatusDSBondingGroupId_Object = MibTableColumn
rdnIfCmtsCmStatusDSBondingGroupId = _RdnIfCmtsCmStatusDSBondingGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 8, 1, 10),
    _RdnIfCmtsCmStatusDSBondingGroupId_Type()
)
rdnIfCmtsCmStatusDSBondingGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsCmStatusDSBondingGroupId.setStatus("current")
_RdnIfCmtsCmStatusOnlineTimes_Type = Counter32
_RdnIfCmtsCmStatusOnlineTimes_Object = MibTableColumn
rdnIfCmtsCmStatusOnlineTimes = _RdnIfCmtsCmStatusOnlineTimes_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 8, 1, 11),
    _RdnIfCmtsCmStatusOnlineTimes_Type()
)
rdnIfCmtsCmStatusOnlineTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsCmStatusOnlineTimes.setStatus("current")


class _RdnIfCmtsCmStatusPercentOnline_Type(Integer32):
    """Custom type rdnIfCmtsCmStatusPercentOnline based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RdnIfCmtsCmStatusPercentOnline_Type.__name__ = "Integer32"
_RdnIfCmtsCmStatusPercentOnline_Object = MibTableColumn
rdnIfCmtsCmStatusPercentOnline = _RdnIfCmtsCmStatusPercentOnline_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 8, 1, 12),
    _RdnIfCmtsCmStatusPercentOnline_Type()
)
rdnIfCmtsCmStatusPercentOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsCmStatusPercentOnline.setStatus("current")
_RdnIfCmtsCmStatusMinOnlineTime_Type = TimeInterval
_RdnIfCmtsCmStatusMinOnlineTime_Object = MibTableColumn
rdnIfCmtsCmStatusMinOnlineTime = _RdnIfCmtsCmStatusMinOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 8, 1, 13),
    _RdnIfCmtsCmStatusMinOnlineTime_Type()
)
rdnIfCmtsCmStatusMinOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsCmStatusMinOnlineTime.setStatus("current")
_RdnIfCmtsCmStatusAvgOnlineTime_Type = TimeInterval
_RdnIfCmtsCmStatusAvgOnlineTime_Object = MibTableColumn
rdnIfCmtsCmStatusAvgOnlineTime = _RdnIfCmtsCmStatusAvgOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 8, 1, 14),
    _RdnIfCmtsCmStatusAvgOnlineTime_Type()
)
rdnIfCmtsCmStatusAvgOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsCmStatusAvgOnlineTime.setStatus("current")
_RdnIfCmtsCmStatusMaxOnlineTime_Type = TimeInterval
_RdnIfCmtsCmStatusMaxOnlineTime_Object = MibTableColumn
rdnIfCmtsCmStatusMaxOnlineTime = _RdnIfCmtsCmStatusMaxOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 8, 1, 15),
    _RdnIfCmtsCmStatusMaxOnlineTime_Type()
)
rdnIfCmtsCmStatusMaxOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsCmStatusMaxOnlineTime.setStatus("current")
_RdnIfCmtsCmStatusMinOfflineTime_Type = TimeInterval
_RdnIfCmtsCmStatusMinOfflineTime_Object = MibTableColumn
rdnIfCmtsCmStatusMinOfflineTime = _RdnIfCmtsCmStatusMinOfflineTime_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 8, 1, 16),
    _RdnIfCmtsCmStatusMinOfflineTime_Type()
)
rdnIfCmtsCmStatusMinOfflineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsCmStatusMinOfflineTime.setStatus("current")
_RdnIfCmtsCmStatusAvgOfflineTime_Type = TimeInterval
_RdnIfCmtsCmStatusAvgOfflineTime_Object = MibTableColumn
rdnIfCmtsCmStatusAvgOfflineTime = _RdnIfCmtsCmStatusAvgOfflineTime_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 8, 1, 17),
    _RdnIfCmtsCmStatusAvgOfflineTime_Type()
)
rdnIfCmtsCmStatusAvgOfflineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsCmStatusAvgOfflineTime.setStatus("current")
_RdnIfCmtsCmStatusMaxOfflineTime_Type = TimeInterval
_RdnIfCmtsCmStatusMaxOfflineTime_Object = MibTableColumn
rdnIfCmtsCmStatusMaxOfflineTime = _RdnIfCmtsCmStatusMaxOfflineTime_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 8, 1, 18),
    _RdnIfCmtsCmStatusMaxOfflineTime_Type()
)
rdnIfCmtsCmStatusMaxOfflineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsCmStatusMaxOfflineTime.setStatus("current")


class _RdnModemDeregReason_Type(Integer32):
    """Custom type rdnModemDeregReason based on Integer32"""
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
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("channelDeleted", 12),
          ("channelErrors", 13),
          ("dnChanChangeFailure", 17),
          ("freqTolerance", 20),
          ("incompleteReg", 14),
          ("noDeregReason", 18),
          ("noResponseUCC", 23),
          ("normal", 1),
          ("operatorDeleted", 4),
          ("operatorDisabled", 3),
          ("operatorReset", 2),
          ("powerTolerance", 19),
          ("profileUpdateComplete", 15),
          ("rangingTolerance", 22),
          ("receiverDeleted", 11),
          ("receiverDisabled", 10),
          ("receiverFailed", 9),
          ("servingGroupChanged", 8),
          ("skeyFailure", 16),
          ("timingTolerance", 21),
          ("transmissionDeleted", 7),
          ("transmissionDisabled", 6),
          ("transmissionFailed", 5))
    )


_RdnModemDeregReason_Type.__name__ = "Integer32"
_RdnModemDeregReason_Object = MibScalar
rdnModemDeregReason = _RdnModemDeregReason_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 9),
    _RdnModemDeregReason_Type()
)
rdnModemDeregReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnModemDeregReason.setStatus("current")
_RdnModemRegIndex_Type = Integer32
_RdnModemRegIndex_Object = MibScalar
rdnModemRegIndex = _RdnModemRegIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 11),
    _RdnModemRegIndex_Type()
)
rdnModemRegIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnModemRegIndex.setStatus("current")
_RdnCmToCpeTable_Object = MibTable
rdnCmToCpeTable = _RdnCmToCpeTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 12)
)
if mibBuilder.loadTexts:
    rdnCmToCpeTable.setStatus("current")
_RdnCmToCpeEntry_Object = MibTableRow
rdnCmToCpeEntry = _RdnCmToCpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 12, 1)
)
rdnCmToCpeEntry.setIndexNames(
    (0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"),
    (0, "RDN-CMTS-MIB", "rdnCmToCpeIndex"),
)
if mibBuilder.loadTexts:
    rdnCmToCpeEntry.setStatus("current")


class _RdnCmToCpeIndex_Type(Integer32):
    """Custom type rdnCmToCpeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RdnCmToCpeIndex_Type.__name__ = "Integer32"
_RdnCmToCpeIndex_Object = MibTableColumn
rdnCmToCpeIndex = _RdnCmToCpeIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 12, 1, 1),
    _RdnCmToCpeIndex_Type()
)
rdnCmToCpeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnCmToCpeIndex.setStatus("current")
_RdnCmToCpeMacAddress_Type = MacAddress
_RdnCmToCpeMacAddress_Object = MibTableColumn
rdnCmToCpeMacAddress = _RdnCmToCpeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 12, 1, 2),
    _RdnCmToCpeMacAddress_Type()
)
rdnCmToCpeMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCmToCpeMacAddress.setStatus("current")
_RdnCmToCpeIpAddress_Type = IpAddress
_RdnCmToCpeIpAddress_Object = MibTableColumn
rdnCmToCpeIpAddress = _RdnCmToCpeIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 12, 1, 3),
    _RdnCmToCpeIpAddress_Type()
)
rdnCmToCpeIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCmToCpeIpAddress.setStatus("current")
_RdnCmToCpeIPv6Addr_Type = InetAddressIPv6
_RdnCmToCpeIPv6Addr_Object = MibTableColumn
rdnCmToCpeIPv6Addr = _RdnCmToCpeIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 12, 1, 4),
    _RdnCmToCpeIPv6Addr_Type()
)
rdnCmToCpeIPv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCmToCpeIPv6Addr.setStatus("current")


class _RdnCmtsCmRegisteredTrapEnable_Type(Integer32):
    """Custom type rdnCmtsCmRegisteredTrapEnable based on Integer32"""
    defaultValue = 1

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


_RdnCmtsCmRegisteredTrapEnable_Type.__name__ = "Integer32"
_RdnCmtsCmRegisteredTrapEnable_Object = MibScalar
rdnCmtsCmRegisteredTrapEnable = _RdnCmtsCmRegisteredTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 13),
    _RdnCmtsCmRegisteredTrapEnable_Type()
)
rdnCmtsCmRegisteredTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCmtsCmRegisteredTrapEnable.setStatus("current")


class _RdnCmtsCardType_Type(Integer32):
    """Custom type rdnCmtsCardType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("domestic", 1),
          ("japan", 2))
    )


_RdnCmtsCardType_Type.__name__ = "Integer32"
_RdnCmtsCardType_Object = MibScalar
rdnCmtsCardType = _RdnCmtsCardType_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 14),
    _RdnCmtsCardType_Type()
)
rdnCmtsCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCmtsCardType.setStatus("current")
_RdnRQueryCmtsCmStatusTable_Object = MibTable
rdnRQueryCmtsCmStatusTable = _RdnRQueryCmtsCmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 15)
)
if mibBuilder.loadTexts:
    rdnRQueryCmtsCmStatusTable.setStatus("current")
_RdnRQueryCmtsCmStatusEntry_Object = MibTableRow
rdnRQueryCmtsCmStatusEntry = _RdnRQueryCmtsCmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 15, 1)
)
rdnRQueryCmtsCmStatusEntry.setIndexNames(
    (0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"),
)
if mibBuilder.loadTexts:
    rdnRQueryCmtsCmStatusEntry.setStatus("current")
_RdnRQueryCmtsCmDownChannelPower_Type = TenthdBmV
_RdnRQueryCmtsCmDownChannelPower_Object = MibTableColumn
rdnRQueryCmtsCmDownChannelPower = _RdnRQueryCmtsCmDownChannelPower_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 15, 1, 1),
    _RdnRQueryCmtsCmDownChannelPower_Type()
)
rdnRQueryCmtsCmDownChannelPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnRQueryCmtsCmDownChannelPower.setStatus("current")
_RdnRQueryCmStatusTxPower_Type = TenthdBmV
_RdnRQueryCmStatusTxPower_Object = MibTableColumn
rdnRQueryCmStatusTxPower = _RdnRQueryCmStatusTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 15, 1, 2),
    _RdnRQueryCmStatusTxPower_Type()
)
rdnRQueryCmStatusTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnRQueryCmStatusTxPower.setStatus("current")
_RdnRQueryUpChannelTxTimingOffset_Type = Unsigned32
_RdnRQueryUpChannelTxTimingOffset_Object = MibTableColumn
rdnRQueryUpChannelTxTimingOffset = _RdnRQueryUpChannelTxTimingOffset_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 15, 1, 3),
    _RdnRQueryUpChannelTxTimingOffset_Type()
)
rdnRQueryUpChannelTxTimingOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnRQueryUpChannelTxTimingOffset.setStatus("current")
_RdnRQuerySigQSignalNoise_Type = TenthdB
_RdnRQuerySigQSignalNoise_Object = MibTableColumn
rdnRQuerySigQSignalNoise = _RdnRQuerySigQSignalNoise_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 15, 1, 4),
    _RdnRQuerySigQSignalNoise_Type()
)
rdnRQuerySigQSignalNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnRQuerySigQSignalNoise.setStatus("current")
if mibBuilder.loadTexts:
    rdnRQuerySigQSignalNoise.setUnits("dB")


class _RdnRQuerySigQMicroreflections_Type(Integer32):
    """Custom type rdnRQuerySigQMicroreflections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RdnRQuerySigQMicroreflections_Type.__name__ = "Integer32"
_RdnRQuerySigQMicroreflections_Object = MibTableColumn
rdnRQuerySigQMicroreflections = _RdnRQuerySigQMicroreflections_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 15, 1, 5),
    _RdnRQuerySigQMicroreflections_Type()
)
rdnRQuerySigQMicroreflections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnRQuerySigQMicroreflections.setStatus("current")
if mibBuilder.loadTexts:
    rdnRQuerySigQMicroreflections.setUnits("dBc")
_RdnRQueryPollTime_Type = TimeStamp
_RdnRQueryPollTime_Object = MibTableColumn
rdnRQueryPollTime = _RdnRQueryPollTime_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 15, 1, 6),
    _RdnRQueryPollTime_Type()
)
rdnRQueryPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnRQueryPollTime.setStatus("current")


class _RdnUgsStatsWindow_Type(Integer32):
    """Custom type rdnUgsStatsWindow based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 120),
    )


_RdnUgsStatsWindow_Type.__name__ = "Integer32"
_RdnUgsStatsWindow_Object = MibScalar
rdnUgsStatsWindow = _RdnUgsStatsWindow_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 16),
    _RdnUgsStatsWindow_Type()
)
rdnUgsStatsWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnUgsStatsWindow.setStatus("current")
if mibBuilder.loadTexts:
    rdnUgsStatsWindow.setUnits("minutes")
_RdnCableUgsStatsTable_Object = MibTable
rdnCableUgsStatsTable = _RdnCableUgsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 17)
)
if mibBuilder.loadTexts:
    rdnCableUgsStatsTable.setStatus("current")
_RdnCableUgsStatsEntry_Object = MibTableRow
rdnCableUgsStatsEntry = _RdnCableUgsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 17, 1)
)
rdnCableUgsStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rdnCableUgsStatsEntry.setStatus("current")


class _RdnCableUgsStatsSlot_Type(Integer32):
    """Custom type rdnCableUgsStatsSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RdnCableUgsStatsSlot_Type.__name__ = "Integer32"
_RdnCableUgsStatsSlot_Object = MibTableColumn
rdnCableUgsStatsSlot = _RdnCableUgsStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 17, 1, 1),
    _RdnCableUgsStatsSlot_Type()
)
rdnCableUgsStatsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCableUgsStatsSlot.setStatus("current")
_RdnCableUgsStatsPort_Type = Integer32
_RdnCableUgsStatsPort_Object = MibTableColumn
rdnCableUgsStatsPort = _RdnCableUgsStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 17, 1, 2),
    _RdnCableUgsStatsPort_Type()
)
rdnCableUgsStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCableUgsStatsPort.setStatus("current")
_RdnCableUgsCurrentTotalFlows_Type = Integer32
_RdnCableUgsCurrentTotalFlows_Object = MibTableColumn
rdnCableUgsCurrentTotalFlows = _RdnCableUgsCurrentTotalFlows_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 17, 1, 3),
    _RdnCableUgsCurrentTotalFlows_Type()
)
rdnCableUgsCurrentTotalFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCableUgsCurrentTotalFlows.setStatus("current")
_RdnCableUgsMaxFlowsLastFiveMinutes_Type = Integer32
_RdnCableUgsMaxFlowsLastFiveMinutes_Object = MibTableColumn
rdnCableUgsMaxFlowsLastFiveMinutes = _RdnCableUgsMaxFlowsLastFiveMinutes_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 17, 1, 4),
    _RdnCableUgsMaxFlowsLastFiveMinutes_Type()
)
rdnCableUgsMaxFlowsLastFiveMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCableUgsMaxFlowsLastFiveMinutes.setStatus("current")
_RdnCableUgsAvFlowsLastFiveMinutes_Type = Integer32
_RdnCableUgsAvFlowsLastFiveMinutes_Object = MibTableColumn
rdnCableUgsAvFlowsLastFiveMinutes = _RdnCableUgsAvFlowsLastFiveMinutes_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 17, 1, 5),
    _RdnCableUgsAvFlowsLastFiveMinutes_Type()
)
rdnCableUgsAvFlowsLastFiveMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCableUgsAvFlowsLastFiveMinutes.setStatus("current")
_RdnCableUgsMinFlowsLastFiveMinutes_Type = Integer32
_RdnCableUgsMinFlowsLastFiveMinutes_Object = MibTableColumn
rdnCableUgsMinFlowsLastFiveMinutes = _RdnCableUgsMinFlowsLastFiveMinutes_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 17, 1, 6),
    _RdnCableUgsMinFlowsLastFiveMinutes_Type()
)
rdnCableUgsMinFlowsLastFiveMinutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCableUgsMinFlowsLastFiveMinutes.setStatus("current")
_RdnCableUgsMaxFlowsLastWindow_Type = Integer32
_RdnCableUgsMaxFlowsLastWindow_Object = MibTableColumn
rdnCableUgsMaxFlowsLastWindow = _RdnCableUgsMaxFlowsLastWindow_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 17, 1, 7),
    _RdnCableUgsMaxFlowsLastWindow_Type()
)
rdnCableUgsMaxFlowsLastWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCableUgsMaxFlowsLastWindow.setStatus("current")
_RdnCableUgsAvFlowsLastWindow_Type = Integer32
_RdnCableUgsAvFlowsLastWindow_Object = MibTableColumn
rdnCableUgsAvFlowsLastWindow = _RdnCableUgsAvFlowsLastWindow_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 17, 1, 8),
    _RdnCableUgsAvFlowsLastWindow_Type()
)
rdnCableUgsAvFlowsLastWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCableUgsAvFlowsLastWindow.setStatus("current")
_RdnCableUgsMinFlowsLastWindow_Type = Integer32
_RdnCableUgsMinFlowsLastWindow_Object = MibTableColumn
rdnCableUgsMinFlowsLastWindow = _RdnCableUgsMinFlowsLastWindow_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 17, 1, 9),
    _RdnCableUgsMinFlowsLastWindow_Type()
)
rdnCableUgsMinFlowsLastWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCableUgsMinFlowsLastWindow.setStatus("current")
_RdnCableUgsResetStats_Type = TruthValue
_RdnCableUgsResetStats_Object = MibTableColumn
rdnCableUgsResetStats = _RdnCableUgsResetStats_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 17, 1, 10),
    _RdnCableUgsResetStats_Type()
)
rdnCableUgsResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCableUgsResetStats.setStatus("current")
_RdnServiceClassStatsTable_Object = MibTable
rdnServiceClassStatsTable = _RdnServiceClassStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 18)
)
if mibBuilder.loadTexts:
    rdnServiceClassStatsTable.setStatus("current")
_RdnServiceClassStatsEntry_Object = MibTableRow
rdnServiceClassStatsEntry = _RdnServiceClassStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 18, 1)
)
rdnServiceClassStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DOCS-QOS3-MIB", "docsQosServiceClassName"),
)
if mibBuilder.loadTexts:
    rdnServiceClassStatsEntry.setStatus("current")
_RdnServiceClassStatsIfDirection_Type = IfDirection
_RdnServiceClassStatsIfDirection_Object = MibTableColumn
rdnServiceClassStatsIfDirection = _RdnServiceClassStatsIfDirection_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 18, 1, 1),
    _RdnServiceClassStatsIfDirection_Type()
)
rdnServiceClassStatsIfDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnServiceClassStatsIfDirection.setStatus("current")


class _RdnServiceClassStatsSlot_Type(Integer32):
    """Custom type rdnServiceClassStatsSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RdnServiceClassStatsSlot_Type.__name__ = "Integer32"
_RdnServiceClassStatsSlot_Object = MibTableColumn
rdnServiceClassStatsSlot = _RdnServiceClassStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 18, 1, 2),
    _RdnServiceClassStatsSlot_Type()
)
rdnServiceClassStatsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnServiceClassStatsSlot.setStatus("current")
_RdnServiceClassStatsPort_Type = Integer32
_RdnServiceClassStatsPort_Object = MibTableColumn
rdnServiceClassStatsPort = _RdnServiceClassStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 18, 1, 3),
    _RdnServiceClassStatsPort_Type()
)
rdnServiceClassStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnServiceClassStatsPort.setStatus("current")
_RdnServiceClassStatsTotalPackets_Type = Counter32
_RdnServiceClassStatsTotalPackets_Object = MibTableColumn
rdnServiceClassStatsTotalPackets = _RdnServiceClassStatsTotalPackets_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 18, 1, 4),
    _RdnServiceClassStatsTotalPackets_Type()
)
rdnServiceClassStatsTotalPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnServiceClassStatsTotalPackets.setStatus("current")
_RdnServiceClassStatsTotalBytes_Type = Counter32
_RdnServiceClassStatsTotalBytes_Object = MibTableColumn
rdnServiceClassStatsTotalBytes = _RdnServiceClassStatsTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 18, 1, 5),
    _RdnServiceClassStatsTotalBytes_Type()
)
rdnServiceClassStatsTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnServiceClassStatsTotalBytes.setStatus("current")
_RdnServiceClassCurrentTotalFlows_Type = Integer32
_RdnServiceClassCurrentTotalFlows_Object = MibTableColumn
rdnServiceClassCurrentTotalFlows = _RdnServiceClassCurrentTotalFlows_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 18, 1, 6),
    _RdnServiceClassCurrentTotalFlows_Type()
)
rdnServiceClassCurrentTotalFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnServiceClassCurrentTotalFlows.setStatus("current")
_RdnServiceClassDeferredFlows_Type = Integer32
_RdnServiceClassDeferredFlows_Object = MibTableColumn
rdnServiceClassDeferredFlows = _RdnServiceClassDeferredFlows_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 18, 1, 7),
    _RdnServiceClassDeferredFlows_Type()
)
rdnServiceClassDeferredFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnServiceClassDeferredFlows.setStatus("current")
_RdnServiceClassRestrictedFlows_Type = Integer32
_RdnServiceClassRestrictedFlows_Object = MibTableColumn
rdnServiceClassRestrictedFlows = _RdnServiceClassRestrictedFlows_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 18, 1, 8),
    _RdnServiceClassRestrictedFlows_Type()
)
rdnServiceClassRestrictedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnServiceClassRestrictedFlows.setStatus("current")
_RdnServiceClassRejectedFlows_Type = Integer32
_RdnServiceClassRejectedFlows_Object = MibTableColumn
rdnServiceClassRejectedFlows = _RdnServiceClassRejectedFlows_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 18, 1, 9),
    _RdnServiceClassRejectedFlows_Type()
)
rdnServiceClassRejectedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnServiceClassRejectedFlows.setStatus("current")
_RdnServiceClassBandWidth_Type = Integer32
_RdnServiceClassBandWidth_Object = MibTableColumn
rdnServiceClassBandWidth = _RdnServiceClassBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 18, 1, 10),
    _RdnServiceClassBandWidth_Type()
)
rdnServiceClassBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnServiceClassBandWidth.setStatus("current")
_RdnServiceClassResetStats_Type = TruthValue
_RdnServiceClassResetStats_Object = MibTableColumn
rdnServiceClassResetStats = _RdnServiceClassResetStats_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 18, 1, 11),
    _RdnServiceClassResetStats_Type()
)
rdnServiceClassResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnServiceClassResetStats.setStatus("current")
_RdnCmtsServiceClassObjects_ObjectIdentity = ObjectIdentity
rdnCmtsServiceClassObjects = _RdnCmtsServiceClassObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 19)
)
_RdnCmtsServiceClassTable_Object = MibTable
rdnCmtsServiceClassTable = _RdnCmtsServiceClassTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 19, 1)
)
if mibBuilder.loadTexts:
    rdnCmtsServiceClassTable.setStatus("current")
_RdnCmtsServiceClassEntry_Object = MibTableRow
rdnCmtsServiceClassEntry = _RdnCmtsServiceClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 19, 1, 1)
)
rdnCmtsServiceClassEntry.setIndexNames(
    (0, "RDN-CMTS-MIB", "rdnCmtsServiceClassName"),
)
if mibBuilder.loadTexts:
    rdnCmtsServiceClassEntry.setStatus("current")


class _RdnCmtsServiceClassName_Type(DisplayString):
    """Custom type rdnCmtsServiceClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_RdnCmtsServiceClassName_Type.__name__ = "DisplayString"
_RdnCmtsServiceClassName_Object = MibTableColumn
rdnCmtsServiceClassName = _RdnCmtsServiceClassName_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 19, 1, 1, 1),
    _RdnCmtsServiceClassName_Type()
)
rdnCmtsServiceClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnCmtsServiceClassName.setStatus("current")
_RdnCmtsServiceClassMab_Type = Unsigned32
_RdnCmtsServiceClassMab_Object = MibTableColumn
rdnCmtsServiceClassMab = _RdnCmtsServiceClassMab_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 19, 1, 1, 2),
    _RdnCmtsServiceClassMab_Type()
)
rdnCmtsServiceClassMab.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCmtsServiceClassMab.setStatus("current")
_RdnCmtsServiceClassCap_Type = Unsigned32
_RdnCmtsServiceClassCap_Object = MibTableColumn
rdnCmtsServiceClassCap = _RdnCmtsServiceClassCap_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 19, 1, 1, 3),
    _RdnCmtsServiceClassCap_Type()
)
rdnCmtsServiceClassCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCmtsServiceClassCap.setStatus("current")
_RdnCmtsServiceClassSchedulingPriority_Type = Unsigned32
_RdnCmtsServiceClassSchedulingPriority_Object = MibTableColumn
rdnCmtsServiceClassSchedulingPriority = _RdnCmtsServiceClassSchedulingPriority_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 19, 1, 1, 4),
    _RdnCmtsServiceClassSchedulingPriority_Type()
)
rdnCmtsServiceClassSchedulingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCmtsServiceClassSchedulingPriority.setStatus("current")
_RdnCmtsServiceClassAdmittedBWThreshold_Type = Unsigned32
_RdnCmtsServiceClassAdmittedBWThreshold_Object = MibTableColumn
rdnCmtsServiceClassAdmittedBWThreshold = _RdnCmtsServiceClassAdmittedBWThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 19, 1, 1, 5),
    _RdnCmtsServiceClassAdmittedBWThreshold_Type()
)
rdnCmtsServiceClassAdmittedBWThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCmtsServiceClassAdmittedBWThreshold.setStatus("current")


class _RdnCmtsServiceClassAllowShare_Type(TruthValue):
    """Custom type rdnCmtsServiceClassAllowShare based on TruthValue"""


_RdnCmtsServiceClassAllowShare_Object = MibTableColumn
rdnCmtsServiceClassAllowShare = _RdnCmtsServiceClassAllowShare_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 19, 1, 1, 6),
    _RdnCmtsServiceClassAllowShare_Type()
)
rdnCmtsServiceClassAllowShare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCmtsServiceClassAllowShare.setStatus("current")
_RdnRQueryCmtsCmStatusExtTable_Object = MibTable
rdnRQueryCmtsCmStatusExtTable = _RdnRQueryCmtsCmStatusExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 20)
)
if mibBuilder.loadTexts:
    rdnRQueryCmtsCmStatusExtTable.setStatus("current")
_RdnRQueryCmtsCmStatusExtEntry_Object = MibTableRow
rdnRQueryCmtsCmStatusExtEntry = _RdnRQueryCmtsCmStatusExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 20, 1)
)
if mibBuilder.loadTexts:
    rdnRQueryCmtsCmStatusExtEntry.setStatus("current")
_RdnRQuerySwCurrentVers_Type = DisplayString
_RdnRQuerySwCurrentVers_Object = MibTableColumn
rdnRQuerySwCurrentVers = _RdnRQuerySwCurrentVers_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 20, 1, 1),
    _RdnRQuerySwCurrentVers_Type()
)
rdnRQuerySwCurrentVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnRQuerySwCurrentVers.setStatus("current")
_RdnRQueryServerConfigFile_Type = DisplayString
_RdnRQueryServerConfigFile_Object = MibTableColumn
rdnRQueryServerConfigFile = _RdnRQueryServerConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 20, 1, 2),
    _RdnRQueryServerConfigFile_Type()
)
rdnRQueryServerConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnRQueryServerConfigFile.setStatus("current")
_RdnIfCmtsCmTable_Object = MibTable
rdnIfCmtsCmTable = _RdnIfCmtsCmTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 21)
)
if mibBuilder.loadTexts:
    rdnIfCmtsCmTable.setStatus("current")
_RdnIfCmtsCmEntry_Object = MibTableRow
rdnIfCmtsCmEntry = _RdnIfCmtsCmEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 21, 1)
)
if mibBuilder.loadTexts:
    rdnIfCmtsCmEntry.setStatus("current")


class _RdnIfCmtsCmMaxCpeNumber_Type(Integer32):
    """Custom type rdnIfCmtsCmMaxCpeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RdnIfCmtsCmMaxCpeNumber_Type.__name__ = "Integer32"
_RdnIfCmtsCmMaxCpeNumber_Object = MibTableColumn
rdnIfCmtsCmMaxCpeNumber = _RdnIfCmtsCmMaxCpeNumber_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 21, 1, 1),
    _RdnIfCmtsCmMaxCpeNumber_Type()
)
rdnIfCmtsCmMaxCpeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnIfCmtsCmMaxCpeNumber.setStatus("current")


class _RdnIfCmtsCmCurrCpeNumber_Type(Integer32):
    """Custom type rdnIfCmtsCmCurrCpeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RdnIfCmtsCmCurrCpeNumber_Type.__name__ = "Integer32"
_RdnIfCmtsCmCurrCpeNumber_Object = MibTableColumn
rdnIfCmtsCmCurrCpeNumber = _RdnIfCmtsCmCurrCpeNumber_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 21, 1, 2),
    _RdnIfCmtsCmCurrCpeNumber_Type()
)
rdnIfCmtsCmCurrCpeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsCmCurrCpeNumber.setStatus("current")
_RdnIfCmtsMTAOnlyStatusTable_Object = MibTable
rdnIfCmtsMTAOnlyStatusTable = _RdnIfCmtsMTAOnlyStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23)
)
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusTable.setStatus("current")
_RdnIfCmtsMTAOnlyStatusEntry_Object = MibTableRow
rdnIfCmtsMTAOnlyStatusEntry = _RdnIfCmtsMTAOnlyStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23, 1)
)
rdnIfCmtsMTAOnlyStatusEntry.setIndexNames(
    (0, "RDN-CMTS-MIB", "rdnIfCmtsMTAOnlyStatusIndex"),
)
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusEntry.setStatus("current")


class _RdnIfCmtsMTAOnlyStatusIndex_Type(Integer32):
    """Custom type rdnIfCmtsMTAOnlyStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RdnIfCmtsMTAOnlyStatusIndex_Type.__name__ = "Integer32"
_RdnIfCmtsMTAOnlyStatusIndex_Object = MibTableColumn
rdnIfCmtsMTAOnlyStatusIndex = _RdnIfCmtsMTAOnlyStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23, 1, 1),
    _RdnIfCmtsMTAOnlyStatusIndex_Type()
)
rdnIfCmtsMTAOnlyStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusIndex.setStatus("current")
_RdnIfCmtsMTAOnlyStatusMacAddress_Type = MacAddress
_RdnIfCmtsMTAOnlyStatusMacAddress_Object = MibTableColumn
rdnIfCmtsMTAOnlyStatusMacAddress = _RdnIfCmtsMTAOnlyStatusMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23, 1, 2),
    _RdnIfCmtsMTAOnlyStatusMacAddress_Type()
)
rdnIfCmtsMTAOnlyStatusMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusMacAddress.setStatus("current")
_RdnIfCmtsMTAOnlyStatusIpAddress_Type = IpAddress
_RdnIfCmtsMTAOnlyStatusIpAddress_Object = MibTableColumn
rdnIfCmtsMTAOnlyStatusIpAddress = _RdnIfCmtsMTAOnlyStatusIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23, 1, 3),
    _RdnIfCmtsMTAOnlyStatusIpAddress_Type()
)
rdnIfCmtsMTAOnlyStatusIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusIpAddress.setStatus("deprecated")
_RdnIfCmtsMTAOnlyStatusDownChannelIfIndex_Type = InterfaceIndexOrZero
_RdnIfCmtsMTAOnlyStatusDownChannelIfIndex_Object = MibTableColumn
rdnIfCmtsMTAOnlyStatusDownChannelIfIndex = _RdnIfCmtsMTAOnlyStatusDownChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23, 1, 4),
    _RdnIfCmtsMTAOnlyStatusDownChannelIfIndex_Type()
)
rdnIfCmtsMTAOnlyStatusDownChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusDownChannelIfIndex.setStatus("current")
_RdnIfCmtsMTAOnlyStatusUpChannelIfIndex_Type = InterfaceIndexOrZero
_RdnIfCmtsMTAOnlyStatusUpChannelIfIndex_Object = MibTableColumn
rdnIfCmtsMTAOnlyStatusUpChannelIfIndex = _RdnIfCmtsMTAOnlyStatusUpChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23, 1, 5),
    _RdnIfCmtsMTAOnlyStatusUpChannelIfIndex_Type()
)
rdnIfCmtsMTAOnlyStatusUpChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusUpChannelIfIndex.setStatus("current")
_RdnIfCmtsMTAOnlyStatusRxPower_Type = TenthdBmV
_RdnIfCmtsMTAOnlyStatusRxPower_Object = MibTableColumn
rdnIfCmtsMTAOnlyStatusRxPower = _RdnIfCmtsMTAOnlyStatusRxPower_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23, 1, 6),
    _RdnIfCmtsMTAOnlyStatusRxPower_Type()
)
rdnIfCmtsMTAOnlyStatusRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusRxPower.setStatus("current")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusRxPower.setUnits("dBmV")
_RdnIfCmtsMTAOnlyStatusTimingOffset_Type = Unsigned32
_RdnIfCmtsMTAOnlyStatusTimingOffset_Object = MibTableColumn
rdnIfCmtsMTAOnlyStatusTimingOffset = _RdnIfCmtsMTAOnlyStatusTimingOffset_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23, 1, 7),
    _RdnIfCmtsMTAOnlyStatusTimingOffset_Type()
)
rdnIfCmtsMTAOnlyStatusTimingOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusTimingOffset.setStatus("current")
_RdnIfCmtsMTAOnlyStatusEqualizationData_Type = OctetString
_RdnIfCmtsMTAOnlyStatusEqualizationData_Object = MibTableColumn
rdnIfCmtsMTAOnlyStatusEqualizationData = _RdnIfCmtsMTAOnlyStatusEqualizationData_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23, 1, 8),
    _RdnIfCmtsMTAOnlyStatusEqualizationData_Type()
)
rdnIfCmtsMTAOnlyStatusEqualizationData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusEqualizationData.setStatus("current")


class _RdnIfCmtsMTAOnlyStatusValue_Type(Integer32):
    """Custom type rdnIfCmtsMTAOnlyStatusValue based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("accessDenied", 7),
          ("ipComplete", 5),
          ("operational", 8),
          ("other", 1),
          ("ranging", 2),
          ("rangingAborted", 3),
          ("rangingComplete", 4),
          ("registeredBPIInitializing", 9),
          ("registrationComplete", 6))
    )


_RdnIfCmtsMTAOnlyStatusValue_Type.__name__ = "Integer32"
_RdnIfCmtsMTAOnlyStatusValue_Object = MibTableColumn
rdnIfCmtsMTAOnlyStatusValue = _RdnIfCmtsMTAOnlyStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23, 1, 9),
    _RdnIfCmtsMTAOnlyStatusValue_Type()
)
rdnIfCmtsMTAOnlyStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusValue.setStatus("current")
_RdnIfCmtsMTAOnlyStatusUnerroreds_Type = Counter32
_RdnIfCmtsMTAOnlyStatusUnerroreds_Object = MibTableColumn
rdnIfCmtsMTAOnlyStatusUnerroreds = _RdnIfCmtsMTAOnlyStatusUnerroreds_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23, 1, 10),
    _RdnIfCmtsMTAOnlyStatusUnerroreds_Type()
)
rdnIfCmtsMTAOnlyStatusUnerroreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusUnerroreds.setStatus("current")
_RdnIfCmtsMTAOnlyStatusCorrecteds_Type = Counter32
_RdnIfCmtsMTAOnlyStatusCorrecteds_Object = MibTableColumn
rdnIfCmtsMTAOnlyStatusCorrecteds = _RdnIfCmtsMTAOnlyStatusCorrecteds_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23, 1, 11),
    _RdnIfCmtsMTAOnlyStatusCorrecteds_Type()
)
rdnIfCmtsMTAOnlyStatusCorrecteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusCorrecteds.setStatus("current")
_RdnIfCmtsMTAOnlyStatusUncorrectables_Type = Counter32
_RdnIfCmtsMTAOnlyStatusUncorrectables_Object = MibTableColumn
rdnIfCmtsMTAOnlyStatusUncorrectables = _RdnIfCmtsMTAOnlyStatusUncorrectables_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23, 1, 12),
    _RdnIfCmtsMTAOnlyStatusUncorrectables_Type()
)
rdnIfCmtsMTAOnlyStatusUncorrectables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusUncorrectables.setStatus("current")
_RdnIfCmtsMTAOnlyStatusSignalNoise_Type = TenthdB
_RdnIfCmtsMTAOnlyStatusSignalNoise_Object = MibTableColumn
rdnIfCmtsMTAOnlyStatusSignalNoise = _RdnIfCmtsMTAOnlyStatusSignalNoise_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23, 1, 13),
    _RdnIfCmtsMTAOnlyStatusSignalNoise_Type()
)
rdnIfCmtsMTAOnlyStatusSignalNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusSignalNoise.setStatus("current")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusSignalNoise.setUnits("dB")


class _RdnIfCmtsMTAOnlyStatusMicroreflections_Type(Integer32):
    """Custom type rdnIfCmtsMTAOnlyStatusMicroreflections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RdnIfCmtsMTAOnlyStatusMicroreflections_Type.__name__ = "Integer32"
_RdnIfCmtsMTAOnlyStatusMicroreflections_Object = MibTableColumn
rdnIfCmtsMTAOnlyStatusMicroreflections = _RdnIfCmtsMTAOnlyStatusMicroreflections_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23, 1, 14),
    _RdnIfCmtsMTAOnlyStatusMicroreflections_Type()
)
rdnIfCmtsMTAOnlyStatusMicroreflections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusMicroreflections.setStatus("current")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusMicroreflections.setUnits("dBc")
_RdnIfCmtsMTAOnlyStatusExtUnerroreds_Type = Counter64
_RdnIfCmtsMTAOnlyStatusExtUnerroreds_Object = MibTableColumn
rdnIfCmtsMTAOnlyStatusExtUnerroreds = _RdnIfCmtsMTAOnlyStatusExtUnerroreds_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23, 1, 15),
    _RdnIfCmtsMTAOnlyStatusExtUnerroreds_Type()
)
rdnIfCmtsMTAOnlyStatusExtUnerroreds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusExtUnerroreds.setStatus("current")
_RdnIfCmtsMTAOnlyStatusExtCorrecteds_Type = Counter64
_RdnIfCmtsMTAOnlyStatusExtCorrecteds_Object = MibTableColumn
rdnIfCmtsMTAOnlyStatusExtCorrecteds = _RdnIfCmtsMTAOnlyStatusExtCorrecteds_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23, 1, 16),
    _RdnIfCmtsMTAOnlyStatusExtCorrecteds_Type()
)
rdnIfCmtsMTAOnlyStatusExtCorrecteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusExtCorrecteds.setStatus("current")
_RdnIfCmtsMTAOnlyStatusExtUncorrectables_Type = Counter64
_RdnIfCmtsMTAOnlyStatusExtUncorrectables_Object = MibTableColumn
rdnIfCmtsMTAOnlyStatusExtUncorrectables = _RdnIfCmtsMTAOnlyStatusExtUncorrectables_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23, 1, 17),
    _RdnIfCmtsMTAOnlyStatusExtUncorrectables_Type()
)
rdnIfCmtsMTAOnlyStatusExtUncorrectables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusExtUncorrectables.setStatus("current")
_RdnIfCmtsMTAOnlyStatusDocsisRegMode_Type = DocsisQosVersion
_RdnIfCmtsMTAOnlyStatusDocsisRegMode_Object = MibTableColumn
rdnIfCmtsMTAOnlyStatusDocsisRegMode = _RdnIfCmtsMTAOnlyStatusDocsisRegMode_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23, 1, 18),
    _RdnIfCmtsMTAOnlyStatusDocsisRegMode_Type()
)
rdnIfCmtsMTAOnlyStatusDocsisRegMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusDocsisRegMode.setStatus("current")
_RdnIfCmtsMTAOnlyStatusModulationType_Type = DocsisUpstreamType
_RdnIfCmtsMTAOnlyStatusModulationType_Object = MibTableColumn
rdnIfCmtsMTAOnlyStatusModulationType = _RdnIfCmtsMTAOnlyStatusModulationType_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23, 1, 19),
    _RdnIfCmtsMTAOnlyStatusModulationType_Type()
)
rdnIfCmtsMTAOnlyStatusModulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusModulationType.setStatus("current")
_RdnIfCmtsMTAOnlyStatusInetAddressType_Type = InetAddressType
_RdnIfCmtsMTAOnlyStatusInetAddressType_Object = MibTableColumn
rdnIfCmtsMTAOnlyStatusInetAddressType = _RdnIfCmtsMTAOnlyStatusInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23, 1, 20),
    _RdnIfCmtsMTAOnlyStatusInetAddressType_Type()
)
rdnIfCmtsMTAOnlyStatusInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusInetAddressType.setStatus("current")
_RdnIfCmtsMTAOnlyStatusInetAddress_Type = InetAddress
_RdnIfCmtsMTAOnlyStatusInetAddress_Object = MibTableColumn
rdnIfCmtsMTAOnlyStatusInetAddress = _RdnIfCmtsMTAOnlyStatusInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23, 1, 21),
    _RdnIfCmtsMTAOnlyStatusInetAddress_Type()
)
rdnIfCmtsMTAOnlyStatusInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusInetAddress.setStatus("current")
_RdnIfCmtsMTAOnlyStatusValueLastUpdate_Type = TimeStamp
_RdnIfCmtsMTAOnlyStatusValueLastUpdate_Object = MibTableColumn
rdnIfCmtsMTAOnlyStatusValueLastUpdate = _RdnIfCmtsMTAOnlyStatusValueLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 23, 1, 22),
    _RdnIfCmtsMTAOnlyStatusValueLastUpdate_Type()
)
rdnIfCmtsMTAOnlyStatusValueLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsMTAOnlyStatusValueLastUpdate.setStatus("current")
_RdnServiceClassBondingStatsTable_Object = MibTable
rdnServiceClassBondingStatsTable = _RdnServiceClassBondingStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 24)
)
if mibBuilder.loadTexts:
    rdnServiceClassBondingStatsTable.setStatus("current")
_RdnServiceClassBondingStatsEntry_Object = MibTableRow
rdnServiceClassBondingStatsEntry = _RdnServiceClassBondingStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 24, 1)
)
rdnServiceClassBondingStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RDN-CMTS-MIB", "rdnServiceClassBondingStatsIfDirection"),
    (0, "DOCS-QOS3-MIB", "docsQosServiceClassName"),
    (0, "RDN-CMTS-MIB", "rdnServiceClassBondingStatsMacIfIndex"),
    (0, "RDN-CMTS-MIB", "rdnServiceClassBondingStatsGroupId"),
)
if mibBuilder.loadTexts:
    rdnServiceClassBondingStatsEntry.setStatus("current")
_RdnServiceClassBondingStatsMacIfIndex_Type = InterfaceIndex
_RdnServiceClassBondingStatsMacIfIndex_Object = MibTableColumn
rdnServiceClassBondingStatsMacIfIndex = _RdnServiceClassBondingStatsMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 24, 1, 1),
    _RdnServiceClassBondingStatsMacIfIndex_Type()
)
rdnServiceClassBondingStatsMacIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnServiceClassBondingStatsMacIfIndex.setStatus("current")


class _RdnServiceClassBondingStatsGroupId_Type(Integer32):
    """Custom type rdnServiceClassBondingStatsGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RdnServiceClassBondingStatsGroupId_Type.__name__ = "Integer32"
_RdnServiceClassBondingStatsGroupId_Object = MibTableColumn
rdnServiceClassBondingStatsGroupId = _RdnServiceClassBondingStatsGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 24, 1, 2),
    _RdnServiceClassBondingStatsGroupId_Type()
)
rdnServiceClassBondingStatsGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnServiceClassBondingStatsGroupId.setStatus("current")
_RdnServiceClassBondingStatsIfDirection_Type = IfDirection
_RdnServiceClassBondingStatsIfDirection_Object = MibTableColumn
rdnServiceClassBondingStatsIfDirection = _RdnServiceClassBondingStatsIfDirection_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 24, 1, 3),
    _RdnServiceClassBondingStatsIfDirection_Type()
)
rdnServiceClassBondingStatsIfDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdnServiceClassBondingStatsIfDirection.setStatus("current")


class _RdnServiceClassBondingStatsSlot_Type(Integer32):
    """Custom type rdnServiceClassBondingStatsSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RdnServiceClassBondingStatsSlot_Type.__name__ = "Integer32"
_RdnServiceClassBondingStatsSlot_Object = MibTableColumn
rdnServiceClassBondingStatsSlot = _RdnServiceClassBondingStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 24, 1, 4),
    _RdnServiceClassBondingStatsSlot_Type()
)
rdnServiceClassBondingStatsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnServiceClassBondingStatsSlot.setStatus("current")
_RdnServiceClassBondingStatsChan_Type = Integer32
_RdnServiceClassBondingStatsChan_Object = MibTableColumn
rdnServiceClassBondingStatsChan = _RdnServiceClassBondingStatsChan_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 24, 1, 5),
    _RdnServiceClassBondingStatsChan_Type()
)
rdnServiceClassBondingStatsChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnServiceClassBondingStatsChan.setStatus("current")
_RdnServiceClassBondingCurrentTotalFlows_Type = Integer32
_RdnServiceClassBondingCurrentTotalFlows_Object = MibTableColumn
rdnServiceClassBondingCurrentTotalFlows = _RdnServiceClassBondingCurrentTotalFlows_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 24, 1, 6),
    _RdnServiceClassBondingCurrentTotalFlows_Type()
)
rdnServiceClassBondingCurrentTotalFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnServiceClassBondingCurrentTotalFlows.setStatus("current")
_RdnServiceClassBondingDeferredFlows_Type = Integer32
_RdnServiceClassBondingDeferredFlows_Object = MibTableColumn
rdnServiceClassBondingDeferredFlows = _RdnServiceClassBondingDeferredFlows_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 24, 1, 7),
    _RdnServiceClassBondingDeferredFlows_Type()
)
rdnServiceClassBondingDeferredFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnServiceClassBondingDeferredFlows.setStatus("current")
_RdnServiceClassBondingRestrictedFlows_Type = Integer32
_RdnServiceClassBondingRestrictedFlows_Object = MibTableColumn
rdnServiceClassBondingRestrictedFlows = _RdnServiceClassBondingRestrictedFlows_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 24, 1, 8),
    _RdnServiceClassBondingRestrictedFlows_Type()
)
rdnServiceClassBondingRestrictedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnServiceClassBondingRestrictedFlows.setStatus("current")
_RdnServiceClassBondingRejectedFlows_Type = Integer32
_RdnServiceClassBondingRejectedFlows_Object = MibTableColumn
rdnServiceClassBondingRejectedFlows = _RdnServiceClassBondingRejectedFlows_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 24, 1, 9),
    _RdnServiceClassBondingRejectedFlows_Type()
)
rdnServiceClassBondingRejectedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnServiceClassBondingRejectedFlows.setStatus("current")
_RdnServiceClassBondingBandWidth_Type = Integer32
_RdnServiceClassBondingBandWidth_Object = MibTableColumn
rdnServiceClassBondingBandWidth = _RdnServiceClassBondingBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 24, 1, 10),
    _RdnServiceClassBondingBandWidth_Type()
)
rdnServiceClassBondingBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnServiceClassBondingBandWidth.setStatus("current")
_RdnCmtsCmResetByIpv6Addr_Type = InetAddressIPv6
_RdnCmtsCmResetByIpv6Addr_Object = MibScalar
rdnCmtsCmResetByIpv6Addr = _RdnCmtsCmResetByIpv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 25),
    _RdnCmtsCmResetByIpv6Addr_Type()
)
rdnCmtsCmResetByIpv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnCmtsCmResetByIpv6Addr.setStatus("current")
_RdnCableInterceptScalars_ObjectIdentity = ObjectIdentity
rdnCableInterceptScalars = _RdnCableInterceptScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 26)
)
_RdnCableInterceptAccessPermitted_Type = TruthValue
_RdnCableInterceptAccessPermitted_Object = MibScalar
rdnCableInterceptAccessPermitted = _RdnCableInterceptAccessPermitted_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 26, 1),
    _RdnCableInterceptAccessPermitted_Type()
)
rdnCableInterceptAccessPermitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCableInterceptAccessPermitted.setStatus("current")
_RdnCableInterceptTable_Object = MibTable
rdnCableInterceptTable = _RdnCableInterceptTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 27)
)
if mibBuilder.loadTexts:
    rdnCableInterceptTable.setStatus("current")
_RdnCableInterceptEntry_Object = MibTableRow
rdnCableInterceptEntry = _RdnCableInterceptEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 27, 1)
)
rdnCableInterceptEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RDN-CMTS-MIB", "rdnCableInterceptCpeMac"),
)
if mibBuilder.loadTexts:
    rdnCableInterceptEntry.setStatus("current")
_RdnCableInterceptCpeMac_Type = MacAddress
_RdnCableInterceptCpeMac_Object = MibTableColumn
rdnCableInterceptCpeMac = _RdnCableInterceptCpeMac_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 27, 1, 1),
    _RdnCableInterceptCpeMac_Type()
)
rdnCableInterceptCpeMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnCableInterceptCpeMac.setStatus("current")
_RdnCableInterceptCmMac_Type = MacAddress
_RdnCableInterceptCmMac_Object = MibTableColumn
rdnCableInterceptCmMac = _RdnCableInterceptCmMac_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 27, 1, 2),
    _RdnCableInterceptCmMac_Type()
)
rdnCableInterceptCmMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnCableInterceptCmMac.setStatus("current")
_RdnCableInterceptDestination1Type_Type = InetAddressType
_RdnCableInterceptDestination1Type_Object = MibTableColumn
rdnCableInterceptDestination1Type = _RdnCableInterceptDestination1Type_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 27, 1, 3),
    _RdnCableInterceptDestination1Type_Type()
)
rdnCableInterceptDestination1Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnCableInterceptDestination1Type.setStatus("current")
_RdnCableInterceptDestination1Ip_Type = InetAddress
_RdnCableInterceptDestination1Ip_Object = MibTableColumn
rdnCableInterceptDestination1Ip = _RdnCableInterceptDestination1Ip_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 27, 1, 4),
    _RdnCableInterceptDestination1Ip_Type()
)
rdnCableInterceptDestination1Ip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnCableInterceptDestination1Ip.setStatus("current")
_RdnCableInterceptDestination1Port_Type = InetPortNumber
_RdnCableInterceptDestination1Port_Object = MibTableColumn
rdnCableInterceptDestination1Port = _RdnCableInterceptDestination1Port_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 27, 1, 5),
    _RdnCableInterceptDestination1Port_Type()
)
rdnCableInterceptDestination1Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnCableInterceptDestination1Port.setStatus("current")
_RdnCableInterceptDestination2Type_Type = InetAddressType
_RdnCableInterceptDestination2Type_Object = MibTableColumn
rdnCableInterceptDestination2Type = _RdnCableInterceptDestination2Type_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 27, 1, 6),
    _RdnCableInterceptDestination2Type_Type()
)
rdnCableInterceptDestination2Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnCableInterceptDestination2Type.setStatus("current")
_RdnCableInterceptDestination2Ip_Type = InetAddress
_RdnCableInterceptDestination2Ip_Object = MibTableColumn
rdnCableInterceptDestination2Ip = _RdnCableInterceptDestination2Ip_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 27, 1, 7),
    _RdnCableInterceptDestination2Ip_Type()
)
rdnCableInterceptDestination2Ip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnCableInterceptDestination2Ip.setStatus("current")
_RdnCableInterceptDestination2Port_Type = InetPortNumber
_RdnCableInterceptDestination2Port_Object = MibTableColumn
rdnCableInterceptDestination2Port = _RdnCableInterceptDestination2Port_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 27, 1, 8),
    _RdnCableInterceptDestination2Port_Type()
)
rdnCableInterceptDestination2Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnCableInterceptDestination2Port.setStatus("current")
_RdnCableInterceptDestination3Type_Type = InetAddressType
_RdnCableInterceptDestination3Type_Object = MibTableColumn
rdnCableInterceptDestination3Type = _RdnCableInterceptDestination3Type_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 27, 1, 9),
    _RdnCableInterceptDestination3Type_Type()
)
rdnCableInterceptDestination3Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnCableInterceptDestination3Type.setStatus("current")
_RdnCableInterceptDestination3Ip_Type = InetAddress
_RdnCableInterceptDestination3Ip_Object = MibTableColumn
rdnCableInterceptDestination3Ip = _RdnCableInterceptDestination3Ip_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 27, 1, 10),
    _RdnCableInterceptDestination3Ip_Type()
)
rdnCableInterceptDestination3Ip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnCableInterceptDestination3Ip.setStatus("current")
_RdnCableInterceptDestination3Port_Type = InetPortNumber
_RdnCableInterceptDestination3Port_Object = MibTableColumn
rdnCableInterceptDestination3Port = _RdnCableInterceptDestination3Port_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 27, 1, 11),
    _RdnCableInterceptDestination3Port_Type()
)
rdnCableInterceptDestination3Port.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnCableInterceptDestination3Port.setStatus("current")
_RdnCableInterceptSourceType_Type = InetAddressType
_RdnCableInterceptSourceType_Object = MibTableColumn
rdnCableInterceptSourceType = _RdnCableInterceptSourceType_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 27, 1, 12),
    _RdnCableInterceptSourceType_Type()
)
rdnCableInterceptSourceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnCableInterceptSourceType.setStatus("current")
_RdnCableInterceptSourceIp_Type = InetAddress
_RdnCableInterceptSourceIp_Object = MibTableColumn
rdnCableInterceptSourceIp = _RdnCableInterceptSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 27, 1, 13),
    _RdnCableInterceptSourceIp_Type()
)
rdnCableInterceptSourceIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnCableInterceptSourceIp.setStatus("current")
_RdnCableInterceptPktCnt_Type = Counter64
_RdnCableInterceptPktCnt_Object = MibTableColumn
rdnCableInterceptPktCnt = _RdnCableInterceptPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 27, 1, 14),
    _RdnCableInterceptPktCnt_Type()
)
rdnCableInterceptPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCableInterceptPktCnt.setStatus("current")
_RdnCableInterceptByteCnt_Type = Counter64
_RdnCableInterceptByteCnt_Object = MibTableColumn
rdnCableInterceptByteCnt = _RdnCableInterceptByteCnt_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 27, 1, 15),
    _RdnCableInterceptByteCnt_Type()
)
rdnCableInterceptByteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnCableInterceptByteCnt.setStatus("current")
_RdnCableInterceptRowStatus_Type = RowStatus
_RdnCableInterceptRowStatus_Object = MibTableColumn
rdnCableInterceptRowStatus = _RdnCableInterceptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 27, 1, 16),
    _RdnCableInterceptRowStatus_Type()
)
rdnCableInterceptRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rdnCableInterceptRowStatus.setStatus("current")
_RdnCmtsUpChannelCounterTable_Object = MibTable
rdnCmtsUpChannelCounterTable = _RdnCmtsUpChannelCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 28)
)
if mibBuilder.loadTexts:
    rdnCmtsUpChannelCounterTable.setStatus("current")
_RdnCmtsUpChannelCounterEntry_Object = MibTableRow
rdnCmtsUpChannelCounterEntry = _RdnCmtsUpChannelCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 28, 1)
)
rdnCmtsUpChannelCounterEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rdnCmtsUpChannelCounterEntry.setStatus("current")
_RdnIfCmtsUpChCtrReqNoise_Type = Counter32
_RdnIfCmtsUpChCtrReqNoise_Object = MibTableColumn
rdnIfCmtsUpChCtrReqNoise = _RdnIfCmtsUpChCtrReqNoise_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 28, 1, 1),
    _RdnIfCmtsUpChCtrReqNoise_Type()
)
rdnIfCmtsUpChCtrReqNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsUpChCtrReqNoise.setStatus("current")
_RdnIfCmtsUpChCtrReqNoEnergy_Type = Counter32
_RdnIfCmtsUpChCtrReqNoEnergy_Object = MibTableColumn
rdnIfCmtsUpChCtrReqNoEnergy = _RdnIfCmtsUpChCtrReqNoEnergy_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 28, 1, 2),
    _RdnIfCmtsUpChCtrReqNoEnergy_Type()
)
rdnIfCmtsUpChCtrReqNoEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsUpChCtrReqNoEnergy.setStatus("current")
_RdnIfCmtsUpChCtrExtReqNoise_Type = Counter64
_RdnIfCmtsUpChCtrExtReqNoise_Object = MibTableColumn
rdnIfCmtsUpChCtrExtReqNoise = _RdnIfCmtsUpChCtrExtReqNoise_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 28, 1, 3),
    _RdnIfCmtsUpChCtrExtReqNoise_Type()
)
rdnIfCmtsUpChCtrExtReqNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsUpChCtrExtReqNoise.setStatus("current")
_RdnIfCmtsUpChCtrExtReqNoEnergy_Type = Counter64
_RdnIfCmtsUpChCtrExtReqNoEnergy_Object = MibTableColumn
rdnIfCmtsUpChCtrExtReqNoEnergy = _RdnIfCmtsUpChCtrExtReqNoEnergy_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 2, 28, 1, 4),
    _RdnIfCmtsUpChCtrExtReqNoEnergy_Type()
)
rdnIfCmtsUpChCtrExtReqNoEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnIfCmtsUpChCtrExtReqNoEnergy.setStatus("current")
_RdnCmtsMibNotifications_ObjectIdentity = ObjectIdentity
rdnCmtsMibNotifications = _RdnCmtsMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 2, 4)
)
_RdnCmtsMibNotificationPrefix_ObjectIdentity = ObjectIdentity
rdnCmtsMibNotificationPrefix = _RdnCmtsMibNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 2, 4, 0)
)
_RdnCmtsMibNotificationObjects_ObjectIdentity = ObjectIdentity
rdnCmtsMibNotificationObjects = _RdnCmtsMibNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 2, 4, 1)
)
_RdnRQueryLastPollStartTime_Type = TimeStamp
_RdnRQueryLastPollStartTime_Object = MibScalar
rdnRQueryLastPollStartTime = _RdnRQueryLastPollStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 4, 1, 1),
    _RdnRQueryLastPollStartTime_Type()
)
rdnRQueryLastPollStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnRQueryLastPollStartTime.setStatus("current")
_RdnRQueryLastPollStopTime_Type = TimeStamp
_RdnRQueryLastPollStopTime_Object = MibScalar
rdnRQueryLastPollStopTime = _RdnRQueryLastPollStopTime_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 4, 1, 2),
    _RdnRQueryLastPollStopTime_Type()
)
rdnRQueryLastPollStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnRQueryLastPollStopTime.setStatus("current")


class _RdnPktDQoSAdmittedBwThresholdReason_Type(Integer32):
    """Custom type rdnPktDQoSAdmittedBwThresholdReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admittedBwClearsOfThreshold", 2),
          ("admittedBwExceedsThreshold", 1))
    )


_RdnPktDQoSAdmittedBwThresholdReason_Type.__name__ = "Integer32"
_RdnPktDQoSAdmittedBwThresholdReason_Object = MibScalar
rdnPktDQoSAdmittedBwThresholdReason = _RdnPktDQoSAdmittedBwThresholdReason_Object(
    (1, 3, 6, 1, 4, 1, 4981, 2, 4, 1, 3),
    _RdnPktDQoSAdmittedBwThresholdReason_Type()
)
rdnPktDQoSAdmittedBwThresholdReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rdnPktDQoSAdmittedBwThresholdReason.setStatus("current")
_RdnCmtsMibConformance_ObjectIdentity = ObjectIdentity
rdnCmtsMibConformance = _RdnCmtsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 2, 5)
)
_RdnCmtsCompliances_ObjectIdentity = ObjectIdentity
rdnCmtsCompliances = _RdnCmtsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 2, 5, 1)
)
_RdnCmtsMibGroups_ObjectIdentity = ObjectIdentity
rdnCmtsMibGroups = _RdnCmtsMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 2, 5, 2)
)
docsIfCmtsCmStatusEntry.registerAugmentions(
    ("RDN-CMTS-MIB",
     "rdnIfCmtsCmStatusEntry")
)
rdnIfCmtsCmStatusEntry.setIndexNames(*docsIfCmtsCmStatusEntry.getIndexNames())
rdnRQueryCmtsCmStatusEntry.registerAugmentions(
    ("RDN-CMTS-MIB",
     "rdnRQueryCmtsCmStatusExtEntry")
)
rdnRQueryCmtsCmStatusExtEntry.setIndexNames(*rdnRQueryCmtsCmStatusEntry.getIndexNames())
docsIfCmtsCmStatusEntry.registerAugmentions(
    ("RDN-CMTS-MIB",
     "rdnIfCmtsCmEntry")
)
rdnIfCmtsCmEntry.setIndexNames(*docsIfCmtsCmStatusEntry.getIndexNames())

# Managed Objects groups

rdnCmtsIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4981, 2, 5, 2, 1)
)
rdnCmtsIfGroup.setObjects(
      *(("RDN-CMTS-MIB", "rdnCmtsDSModulation"),
        ("RDN-CMTS-MIB", "rdnCmtsUSNominalRxPower"),
        ("RDN-CMTS-MIB", "rdnCmtsUSInvitedRangingInterval"),
        ("RDN-CMTS-MIB", "rdnCmtsUSRangingResponseControl"),
        ("RDN-CMTS-MIB", "rdnCmtsUSRangingPowerOverride"),
        ("RDN-CMTS-MIB", "rdnCmtsUSNominalRxPowerMode"),
        ("RDN-CMTS-MIB", "rdnCmtsStpTCNEnable"),
        ("RDN-CMTS-MIB", "rdnCmtsLinkUpDownTrapEnable"))
)
if mibBuilder.loadTexts:
    rdnCmtsIfGroup.setStatus("current")

rdnCmtsMiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4981, 2, 5, 2, 2)
)
rdnCmtsMiscGroup.setObjects(
      *(("RDN-CMTS-MIB", "rdnCmtsSaveConfig"),
        ("RDN-CMTS-MIB", "rdnCmtsCmResetByMacAddr"),
        ("RDN-CMTS-MIB", "rdnCmtsCmResetByIpAddr"),
        ("RDN-CMTS-MIB", "rdnCmtsCmResetAll"),
        ("RDN-CMTS-MIB", "rdnCmtsModemAgingTimer"),
        ("RDN-CMTS-MIB", "rdnCmtsCmMac"),
        ("RDN-CMTS-MIB", "rdnIfCmtsCmStatusRegistrationTime"),
        ("RDN-CMTS-MIB", "rdnIfCmtsCmStatusTxUnicastKbytes"),
        ("RDN-CMTS-MIB", "rdnIfCmtsCmStatusRxUnicastKbytes"),
        ("RDN-CMTS-MIB", "rdnIfCmtsCmStatusTxUnicastExtKbytes"),
        ("RDN-CMTS-MIB", "rdnIfCmtsCmStatusRxUnicastExtKbytes"),
        ("RDN-CMTS-MIB", "rdnIfCmtsCmStatusSpectrumGroupName"),
        ("RDN-CMTS-MIB", "rdnIfCmtsCmStatusUpstreamPort"),
        ("RDN-CMTS-MIB", "rdnIfCmtsCmStatusDownStreamPort"),
        ("RDN-CMTS-MIB", "rdnIfCmtsCmStatusValue"),
        ("RDN-CMTS-MIB", "rdnIfCmtsCmStatusDSBondingGroupId"),
        ("RDN-CMTS-MIB", "rdnIfCmtsCmStatusOnlineTimes"),
        ("RDN-CMTS-MIB", "rdnIfCmtsCmStatusPercentOnline"),
        ("RDN-CMTS-MIB", "rdnIfCmtsCmStatusMinOnlineTime"),
        ("RDN-CMTS-MIB", "rdnIfCmtsCmStatusAvgOnlineTime"),
        ("RDN-CMTS-MIB", "rdnIfCmtsCmStatusMaxOnlineTime"),
        ("RDN-CMTS-MIB", "rdnIfCmtsCmStatusMinOfflineTime"),
        ("RDN-CMTS-MIB", "rdnIfCmtsCmStatusAvgOfflineTime"),
        ("RDN-CMTS-MIB", "rdnIfCmtsCmStatusMaxOfflineTime"),
        ("RDN-CMTS-MIB", "rdnModemDeregReason"),
        ("RDN-CMTS-MIB", "rdnModemRegIndex"),
        ("RDN-CMTS-MIB", "rdnCmToCpeMacAddress"),
        ("RDN-CMTS-MIB", "rdnCmToCpeIpAddress"),
        ("RDN-CMTS-MIB", "rdnCmtsCmRegisteredTrapEnable"),
        ("RDN-CMTS-MIB", "rdnCmtsCardType"),
        ("RDN-CMTS-MIB", "rdnRQueryCmtsCmDownChannelPower"),
        ("RDN-CMTS-MIB", "rdnRQueryCmStatusTxPower"),
        ("RDN-CMTS-MIB", "rdnRQueryUpChannelTxTimingOffset"),
        ("RDN-CMTS-MIB", "rdnRQuerySigQSignalNoise"),
        ("RDN-CMTS-MIB", "rdnRQuerySigQMicroreflections"),
        ("RDN-CMTS-MIB", "rdnRQueryPollTime"),
        ("RDN-CMTS-MIB", "rdnUgsStatsWindow"),
        ("RDN-CMTS-MIB", "rdnCableUgsStatsSlot"),
        ("RDN-CMTS-MIB", "rdnCableUgsStatsPort"),
        ("RDN-CMTS-MIB", "rdnCableUgsCurrentTotalFlows"),
        ("RDN-CMTS-MIB", "rdnCableUgsMaxFlowsLastFiveMinutes"),
        ("RDN-CMTS-MIB", "rdnCableUgsAvFlowsLastFiveMinutes"),
        ("RDN-CMTS-MIB", "rdnCableUgsMinFlowsLastFiveMinutes"),
        ("RDN-CMTS-MIB", "rdnCableUgsMaxFlowsLastWindow"),
        ("RDN-CMTS-MIB", "rdnCableUgsAvFlowsLastWindow"),
        ("RDN-CMTS-MIB", "rdnCableUgsMinFlowsLastWindow"),
        ("RDN-CMTS-MIB", "rdnCableUgsResetStats"),
        ("RDN-CMTS-MIB", "rdnServiceClassStatsIfDirection"),
        ("RDN-CMTS-MIB", "rdnServiceClassStatsSlot"),
        ("RDN-CMTS-MIB", "rdnServiceClassStatsPort"),
        ("RDN-CMTS-MIB", "rdnServiceClassStatsTotalPackets"),
        ("RDN-CMTS-MIB", "rdnServiceClassStatsTotalBytes"),
        ("RDN-CMTS-MIB", "rdnServiceClassCurrentTotalFlows"),
        ("RDN-CMTS-MIB", "rdnServiceClassDeferredFlows"),
        ("RDN-CMTS-MIB", "rdnServiceClassRestrictedFlows"),
        ("RDN-CMTS-MIB", "rdnServiceClassRejectedFlows"),
        ("RDN-CMTS-MIB", "rdnServiceClassBandWidth"),
        ("RDN-CMTS-MIB", "rdnServiceClassResetStats"),
        ("RDN-CMTS-MIB", "rdnServiceClassBondingStatsSlot"),
        ("RDN-CMTS-MIB", "rdnServiceClassBondingStatsChan"),
        ("RDN-CMTS-MIB", "rdnServiceClassBondingCurrentTotalFlows"),
        ("RDN-CMTS-MIB", "rdnServiceClassBondingDeferredFlows"),
        ("RDN-CMTS-MIB", "rdnServiceClassBondingRestrictedFlows"),
        ("RDN-CMTS-MIB", "rdnServiceClassBondingRejectedFlows"),
        ("RDN-CMTS-MIB", "rdnServiceClassBondingBandWidth"),
        ("RDN-CMTS-MIB", "rdnRQuerySwCurrentVers"),
        ("RDN-CMTS-MIB", "rdnCmtsCmResetByIpv6Addr"))
)
if mibBuilder.loadTexts:
    rdnCmtsMiscGroup.setStatus("current")


# Notification objects

rdnCmtsCmRegisteredNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 2, 4, 0, 1)
)
rdnCmtsCmRegisteredNotification.setObjects(
      *(("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusIpAddress"),
        ("DOCS-IF3-MIB", "docsIf3CmtsCmRegStatusIPv6Addr"),
        ("DOCS-IF-MIB", "docsIfUpChannelId"),
        ("DOCS-IF-MIB", "docsIfDownChannelId"),
        ("RDN-CMTS-MIB", "rdnModemRegIndex"),
        ("RDN-CABLE-SPECTRUM-GROUP-MIB", "rdnSpectrumGroupName"))
)
if mibBuilder.loadTexts:
    rdnCmtsCmRegisteredNotification.setStatus(
        "current"
    )

rdnCmtsCmDeregisteredNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 2, 4, 0, 2)
)
rdnCmtsCmDeregisteredNotification.setObjects(
      *(("DOCS-IF-MIB", "docsIfCmtsCmStatusDocsisRegMode"),
        ("DOCS-IF-MIB", "docsIfCmtsCmStatusMacAddress"),
        ("DOCS-IF-MIB", "docsIfUpChannelId"),
        ("DOCS-IF-MIB", "docsIfDownChannelId"),
        ("RDN-CMTS-MIB", "rdnModemRegIndex"),
        ("RDN-CMTS-MIB", "rdnModemDeregReason"),
        ("RDN-CABLE-SPECTRUM-GROUP-MIB", "rdnSpectrumGroupName"))
)
if mibBuilder.loadTexts:
    rdnCmtsCmDeregisteredNotification.setStatus(
        "current"
    )

rdnCmtsUpstreamIfLinkUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 2, 4, 0, 3)
)
rdnCmtsUpstreamIfLinkUpTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifType"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("RDN-CABLE-SPECTRUM-GROUP-MIB", "rdnSpectrumGroupName"))
)
if mibBuilder.loadTexts:
    rdnCmtsUpstreamIfLinkUpTrap.setStatus(
        "current"
    )

rdnCmtsUpstreamIfLinkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 2, 4, 0, 4)
)
rdnCmtsUpstreamIfLinkDownTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifType"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("RDN-CABLE-SPECTRUM-GROUP-MIB", "rdnSpectrumGroupName"))
)
if mibBuilder.loadTexts:
    rdnCmtsUpstreamIfLinkDownTrap.setStatus(
        "current"
    )

rdnRQueryPollDoneNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 2, 4, 0, 5)
)
rdnRQueryPollDoneNotification.setObjects(
      *(("RDN-CMTS-MIB", "rdnRQueryLastPollStartTime"),
        ("RDN-CMTS-MIB", "rdnRQueryLastPollStopTime"))
)
if mibBuilder.loadTexts:
    rdnRQueryPollDoneNotification.setStatus(
        "current"
    )

rdnPktDQoSAdmittedBwThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4981, 2, 4, 0, 6)
)
rdnPktDQoSAdmittedBwThresholdTrap.setObjects(
      *(("RDN-CMTS-MIB", "rdnPktDQoSAdmittedBwThresholdReason"),
        ("RDN-PKTCABLE-GROUP-MIB", "rdnPktDQoSClassName"))
)
if mibBuilder.loadTexts:
    rdnPktDQoSAdmittedBwThresholdTrap.setStatus(
        "current"
    )


# Notifications groups

rdnCmtsNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4981, 2, 5, 2, 3)
)
rdnCmtsNotificationsGroup.setObjects(
      *(("RDN-CMTS-MIB", "rdnCmtsCmRegisteredNotification"),
        ("RDN-CMTS-MIB", "rdnCmtsCmDeregisteredNotification"),
        ("RDN-CMTS-MIB", "rdnCmtsUpstreamIfLinkUpTrap"),
        ("RDN-CMTS-MIB", "rdnCmtsUpstreamIfLinkDownTrap"),
        ("RDN-CMTS-MIB", "rdnRQueryPollDoneNotification"),
        ("RDN-CMTS-MIB", "rdnPktDQoSAdmittedBwThresholdTrap"))
)
if mibBuilder.loadTexts:
    rdnCmtsNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rdnCmtsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4981, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    rdnCmtsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RDN-CMTS-MIB",
    **{"rdnCmtsMib": rdnCmtsMib,
       "rdnCmtsIfObjects": rdnCmtsIfObjects,
       "rdnCmtsDownstreamChannelTable": rdnCmtsDownstreamChannelTable,
       "rdnCmtsDownstreamChannelEntry": rdnCmtsDownstreamChannelEntry,
       "rdnCmtsDSModulation": rdnCmtsDSModulation,
       "rdnCmtsUpstreamChannelTable": rdnCmtsUpstreamChannelTable,
       "rdnCmtsUpstreamChannelEntry": rdnCmtsUpstreamChannelEntry,
       "rdnCmtsUSNominalRxPower": rdnCmtsUSNominalRxPower,
       "rdnCmtsUSNominalRxPowerMode": rdnCmtsUSNominalRxPowerMode,
       "rdnCmtsUSInvitedRangingInterval": rdnCmtsUSInvitedRangingInterval,
       "rdnCmtsUSRangingResponseControl": rdnCmtsUSRangingResponseControl,
       "rdnCmtsUSRangingPowerOverride": rdnCmtsUSRangingPowerOverride,
       "rdnCmtsUSTotalModemCount": rdnCmtsUSTotalModemCount,
       "rdnCmtsUSRegisteredModemCount": rdnCmtsUSRegisteredModemCount,
       "rdnCmtsUSUnregisteredModemCount": rdnCmtsUSUnregisteredModemCount,
       "rdnCmtsUSOfflineModemCount": rdnCmtsUSOfflineModemCount,
       "rdnCmtsStpObjects": rdnCmtsStpObjects,
       "rdnCmtsStpEnable": rdnCmtsStpEnable,
       "rdnCmtsStpTCNEnable": rdnCmtsStpTCNEnable,
       "rdnCmtsLinkUpDownTrapEnableTable": rdnCmtsLinkUpDownTrapEnableTable,
       "rdnCmtsLinkUpDownTrapEnableEntry": rdnCmtsLinkUpDownTrapEnableEntry,
       "rdnCmtsLinkUpDownTrapEnable": rdnCmtsLinkUpDownTrapEnable,
       "rdnCmtsMiscObjects": rdnCmtsMiscObjects,
       "rdnCmtsSaveConfig": rdnCmtsSaveConfig,
       "rdnCmtsCmResetByMacAddr": rdnCmtsCmResetByMacAddr,
       "rdnCmtsCmResetByIpAddr": rdnCmtsCmResetByIpAddr,
       "rdnCmtsCmResetAll": rdnCmtsCmResetAll,
       "rdnCmtsHostAuthControl": rdnCmtsHostAuthControl,
       "rdnCmtsModemAgingTimer": rdnCmtsModemAgingTimer,
       "rdnCmtsCpeToCmObject": rdnCmtsCpeToCmObject,
       "rdnCmtsCpeToCmTable": rdnCmtsCpeToCmTable,
       "rdnCmtsCpeToCmEntry": rdnCmtsCpeToCmEntry,
       "rdnCmtsCpeMac": rdnCmtsCpeMac,
       "rdnCmtsCmMac": rdnCmtsCmMac,
       "rdnIfCmtsCmStatusTable": rdnIfCmtsCmStatusTable,
       "rdnIfCmtsCmStatusEntry": rdnIfCmtsCmStatusEntry,
       "rdnIfCmtsCmStatusRegistrationTime": rdnIfCmtsCmStatusRegistrationTime,
       "rdnIfCmtsCmStatusTxUnicastKbytes": rdnIfCmtsCmStatusTxUnicastKbytes,
       "rdnIfCmtsCmStatusRxUnicastKbytes": rdnIfCmtsCmStatusRxUnicastKbytes,
       "rdnIfCmtsCmStatusTxUnicastExtKbytes": rdnIfCmtsCmStatusTxUnicastExtKbytes,
       "rdnIfCmtsCmStatusRxUnicastExtKbytes": rdnIfCmtsCmStatusRxUnicastExtKbytes,
       "rdnIfCmtsCmStatusSpectrumGroupName": rdnIfCmtsCmStatusSpectrumGroupName,
       "rdnIfCmtsCmStatusUpstreamPort": rdnIfCmtsCmStatusUpstreamPort,
       "rdnIfCmtsCmStatusDownStreamPort": rdnIfCmtsCmStatusDownStreamPort,
       "rdnIfCmtsCmStatusValue": rdnIfCmtsCmStatusValue,
       "rdnIfCmtsCmStatusDSBondingGroupId": rdnIfCmtsCmStatusDSBondingGroupId,
       "rdnIfCmtsCmStatusOnlineTimes": rdnIfCmtsCmStatusOnlineTimes,
       "rdnIfCmtsCmStatusPercentOnline": rdnIfCmtsCmStatusPercentOnline,
       "rdnIfCmtsCmStatusMinOnlineTime": rdnIfCmtsCmStatusMinOnlineTime,
       "rdnIfCmtsCmStatusAvgOnlineTime": rdnIfCmtsCmStatusAvgOnlineTime,
       "rdnIfCmtsCmStatusMaxOnlineTime": rdnIfCmtsCmStatusMaxOnlineTime,
       "rdnIfCmtsCmStatusMinOfflineTime": rdnIfCmtsCmStatusMinOfflineTime,
       "rdnIfCmtsCmStatusAvgOfflineTime": rdnIfCmtsCmStatusAvgOfflineTime,
       "rdnIfCmtsCmStatusMaxOfflineTime": rdnIfCmtsCmStatusMaxOfflineTime,
       "rdnModemDeregReason": rdnModemDeregReason,
       "rdnModemRegIndex": rdnModemRegIndex,
       "rdnCmToCpeTable": rdnCmToCpeTable,
       "rdnCmToCpeEntry": rdnCmToCpeEntry,
       "rdnCmToCpeIndex": rdnCmToCpeIndex,
       "rdnCmToCpeMacAddress": rdnCmToCpeMacAddress,
       "rdnCmToCpeIpAddress": rdnCmToCpeIpAddress,
       "rdnCmToCpeIPv6Addr": rdnCmToCpeIPv6Addr,
       "rdnCmtsCmRegisteredTrapEnable": rdnCmtsCmRegisteredTrapEnable,
       "rdnCmtsCardType": rdnCmtsCardType,
       "rdnRQueryCmtsCmStatusTable": rdnRQueryCmtsCmStatusTable,
       "rdnRQueryCmtsCmStatusEntry": rdnRQueryCmtsCmStatusEntry,
       "rdnRQueryCmtsCmDownChannelPower": rdnRQueryCmtsCmDownChannelPower,
       "rdnRQueryCmStatusTxPower": rdnRQueryCmStatusTxPower,
       "rdnRQueryUpChannelTxTimingOffset": rdnRQueryUpChannelTxTimingOffset,
       "rdnRQuerySigQSignalNoise": rdnRQuerySigQSignalNoise,
       "rdnRQuerySigQMicroreflections": rdnRQuerySigQMicroreflections,
       "rdnRQueryPollTime": rdnRQueryPollTime,
       "rdnUgsStatsWindow": rdnUgsStatsWindow,
       "rdnCableUgsStatsTable": rdnCableUgsStatsTable,
       "rdnCableUgsStatsEntry": rdnCableUgsStatsEntry,
       "rdnCableUgsStatsSlot": rdnCableUgsStatsSlot,
       "rdnCableUgsStatsPort": rdnCableUgsStatsPort,
       "rdnCableUgsCurrentTotalFlows": rdnCableUgsCurrentTotalFlows,
       "rdnCableUgsMaxFlowsLastFiveMinutes": rdnCableUgsMaxFlowsLastFiveMinutes,
       "rdnCableUgsAvFlowsLastFiveMinutes": rdnCableUgsAvFlowsLastFiveMinutes,
       "rdnCableUgsMinFlowsLastFiveMinutes": rdnCableUgsMinFlowsLastFiveMinutes,
       "rdnCableUgsMaxFlowsLastWindow": rdnCableUgsMaxFlowsLastWindow,
       "rdnCableUgsAvFlowsLastWindow": rdnCableUgsAvFlowsLastWindow,
       "rdnCableUgsMinFlowsLastWindow": rdnCableUgsMinFlowsLastWindow,
       "rdnCableUgsResetStats": rdnCableUgsResetStats,
       "rdnServiceClassStatsTable": rdnServiceClassStatsTable,
       "rdnServiceClassStatsEntry": rdnServiceClassStatsEntry,
       "rdnServiceClassStatsIfDirection": rdnServiceClassStatsIfDirection,
       "rdnServiceClassStatsSlot": rdnServiceClassStatsSlot,
       "rdnServiceClassStatsPort": rdnServiceClassStatsPort,
       "rdnServiceClassStatsTotalPackets": rdnServiceClassStatsTotalPackets,
       "rdnServiceClassStatsTotalBytes": rdnServiceClassStatsTotalBytes,
       "rdnServiceClassCurrentTotalFlows": rdnServiceClassCurrentTotalFlows,
       "rdnServiceClassDeferredFlows": rdnServiceClassDeferredFlows,
       "rdnServiceClassRestrictedFlows": rdnServiceClassRestrictedFlows,
       "rdnServiceClassRejectedFlows": rdnServiceClassRejectedFlows,
       "rdnServiceClassBandWidth": rdnServiceClassBandWidth,
       "rdnServiceClassResetStats": rdnServiceClassResetStats,
       "rdnCmtsServiceClassObjects": rdnCmtsServiceClassObjects,
       "rdnCmtsServiceClassTable": rdnCmtsServiceClassTable,
       "rdnCmtsServiceClassEntry": rdnCmtsServiceClassEntry,
       "rdnCmtsServiceClassName": rdnCmtsServiceClassName,
       "rdnCmtsServiceClassMab": rdnCmtsServiceClassMab,
       "rdnCmtsServiceClassCap": rdnCmtsServiceClassCap,
       "rdnCmtsServiceClassSchedulingPriority": rdnCmtsServiceClassSchedulingPriority,
       "rdnCmtsServiceClassAdmittedBWThreshold": rdnCmtsServiceClassAdmittedBWThreshold,
       "rdnCmtsServiceClassAllowShare": rdnCmtsServiceClassAllowShare,
       "rdnRQueryCmtsCmStatusExtTable": rdnRQueryCmtsCmStatusExtTable,
       "rdnRQueryCmtsCmStatusExtEntry": rdnRQueryCmtsCmStatusExtEntry,
       "rdnRQuerySwCurrentVers": rdnRQuerySwCurrentVers,
       "rdnRQueryServerConfigFile": rdnRQueryServerConfigFile,
       "rdnIfCmtsCmTable": rdnIfCmtsCmTable,
       "rdnIfCmtsCmEntry": rdnIfCmtsCmEntry,
       "rdnIfCmtsCmMaxCpeNumber": rdnIfCmtsCmMaxCpeNumber,
       "rdnIfCmtsCmCurrCpeNumber": rdnIfCmtsCmCurrCpeNumber,
       "rdnIfCmtsMTAOnlyStatusTable": rdnIfCmtsMTAOnlyStatusTable,
       "rdnIfCmtsMTAOnlyStatusEntry": rdnIfCmtsMTAOnlyStatusEntry,
       "rdnIfCmtsMTAOnlyStatusIndex": rdnIfCmtsMTAOnlyStatusIndex,
       "rdnIfCmtsMTAOnlyStatusMacAddress": rdnIfCmtsMTAOnlyStatusMacAddress,
       "rdnIfCmtsMTAOnlyStatusIpAddress": rdnIfCmtsMTAOnlyStatusIpAddress,
       "rdnIfCmtsMTAOnlyStatusDownChannelIfIndex": rdnIfCmtsMTAOnlyStatusDownChannelIfIndex,
       "rdnIfCmtsMTAOnlyStatusUpChannelIfIndex": rdnIfCmtsMTAOnlyStatusUpChannelIfIndex,
       "rdnIfCmtsMTAOnlyStatusRxPower": rdnIfCmtsMTAOnlyStatusRxPower,
       "rdnIfCmtsMTAOnlyStatusTimingOffset": rdnIfCmtsMTAOnlyStatusTimingOffset,
       "rdnIfCmtsMTAOnlyStatusEqualizationData": rdnIfCmtsMTAOnlyStatusEqualizationData,
       "rdnIfCmtsMTAOnlyStatusValue": rdnIfCmtsMTAOnlyStatusValue,
       "rdnIfCmtsMTAOnlyStatusUnerroreds": rdnIfCmtsMTAOnlyStatusUnerroreds,
       "rdnIfCmtsMTAOnlyStatusCorrecteds": rdnIfCmtsMTAOnlyStatusCorrecteds,
       "rdnIfCmtsMTAOnlyStatusUncorrectables": rdnIfCmtsMTAOnlyStatusUncorrectables,
       "rdnIfCmtsMTAOnlyStatusSignalNoise": rdnIfCmtsMTAOnlyStatusSignalNoise,
       "rdnIfCmtsMTAOnlyStatusMicroreflections": rdnIfCmtsMTAOnlyStatusMicroreflections,
       "rdnIfCmtsMTAOnlyStatusExtUnerroreds": rdnIfCmtsMTAOnlyStatusExtUnerroreds,
       "rdnIfCmtsMTAOnlyStatusExtCorrecteds": rdnIfCmtsMTAOnlyStatusExtCorrecteds,
       "rdnIfCmtsMTAOnlyStatusExtUncorrectables": rdnIfCmtsMTAOnlyStatusExtUncorrectables,
       "rdnIfCmtsMTAOnlyStatusDocsisRegMode": rdnIfCmtsMTAOnlyStatusDocsisRegMode,
       "rdnIfCmtsMTAOnlyStatusModulationType": rdnIfCmtsMTAOnlyStatusModulationType,
       "rdnIfCmtsMTAOnlyStatusInetAddressType": rdnIfCmtsMTAOnlyStatusInetAddressType,
       "rdnIfCmtsMTAOnlyStatusInetAddress": rdnIfCmtsMTAOnlyStatusInetAddress,
       "rdnIfCmtsMTAOnlyStatusValueLastUpdate": rdnIfCmtsMTAOnlyStatusValueLastUpdate,
       "rdnServiceClassBondingStatsTable": rdnServiceClassBondingStatsTable,
       "rdnServiceClassBondingStatsEntry": rdnServiceClassBondingStatsEntry,
       "rdnServiceClassBondingStatsMacIfIndex": rdnServiceClassBondingStatsMacIfIndex,
       "rdnServiceClassBondingStatsGroupId": rdnServiceClassBondingStatsGroupId,
       "rdnServiceClassBondingStatsIfDirection": rdnServiceClassBondingStatsIfDirection,
       "rdnServiceClassBondingStatsSlot": rdnServiceClassBondingStatsSlot,
       "rdnServiceClassBondingStatsChan": rdnServiceClassBondingStatsChan,
       "rdnServiceClassBondingCurrentTotalFlows": rdnServiceClassBondingCurrentTotalFlows,
       "rdnServiceClassBondingDeferredFlows": rdnServiceClassBondingDeferredFlows,
       "rdnServiceClassBondingRestrictedFlows": rdnServiceClassBondingRestrictedFlows,
       "rdnServiceClassBondingRejectedFlows": rdnServiceClassBondingRejectedFlows,
       "rdnServiceClassBondingBandWidth": rdnServiceClassBondingBandWidth,
       "rdnCmtsCmResetByIpv6Addr": rdnCmtsCmResetByIpv6Addr,
       "rdnCableInterceptScalars": rdnCableInterceptScalars,
       "rdnCableInterceptAccessPermitted": rdnCableInterceptAccessPermitted,
       "rdnCableInterceptTable": rdnCableInterceptTable,
       "rdnCableInterceptEntry": rdnCableInterceptEntry,
       "rdnCableInterceptCpeMac": rdnCableInterceptCpeMac,
       "rdnCableInterceptCmMac": rdnCableInterceptCmMac,
       "rdnCableInterceptDestination1Type": rdnCableInterceptDestination1Type,
       "rdnCableInterceptDestination1Ip": rdnCableInterceptDestination1Ip,
       "rdnCableInterceptDestination1Port": rdnCableInterceptDestination1Port,
       "rdnCableInterceptDestination2Type": rdnCableInterceptDestination2Type,
       "rdnCableInterceptDestination2Ip": rdnCableInterceptDestination2Ip,
       "rdnCableInterceptDestination2Port": rdnCableInterceptDestination2Port,
       "rdnCableInterceptDestination3Type": rdnCableInterceptDestination3Type,
       "rdnCableInterceptDestination3Ip": rdnCableInterceptDestination3Ip,
       "rdnCableInterceptDestination3Port": rdnCableInterceptDestination3Port,
       "rdnCableInterceptSourceType": rdnCableInterceptSourceType,
       "rdnCableInterceptSourceIp": rdnCableInterceptSourceIp,
       "rdnCableInterceptPktCnt": rdnCableInterceptPktCnt,
       "rdnCableInterceptByteCnt": rdnCableInterceptByteCnt,
       "rdnCableInterceptRowStatus": rdnCableInterceptRowStatus,
       "rdnCmtsUpChannelCounterTable": rdnCmtsUpChannelCounterTable,
       "rdnCmtsUpChannelCounterEntry": rdnCmtsUpChannelCounterEntry,
       "rdnIfCmtsUpChCtrReqNoise": rdnIfCmtsUpChCtrReqNoise,
       "rdnIfCmtsUpChCtrReqNoEnergy": rdnIfCmtsUpChCtrReqNoEnergy,
       "rdnIfCmtsUpChCtrExtReqNoise": rdnIfCmtsUpChCtrExtReqNoise,
       "rdnIfCmtsUpChCtrExtReqNoEnergy": rdnIfCmtsUpChCtrExtReqNoEnergy,
       "rdnCmtsMibNotifications": rdnCmtsMibNotifications,
       "rdnCmtsMibNotificationPrefix": rdnCmtsMibNotificationPrefix,
       "rdnCmtsCmRegisteredNotification": rdnCmtsCmRegisteredNotification,
       "rdnCmtsCmDeregisteredNotification": rdnCmtsCmDeregisteredNotification,
       "rdnCmtsUpstreamIfLinkUpTrap": rdnCmtsUpstreamIfLinkUpTrap,
       "rdnCmtsUpstreamIfLinkDownTrap": rdnCmtsUpstreamIfLinkDownTrap,
       "rdnRQueryPollDoneNotification": rdnRQueryPollDoneNotification,
       "rdnPktDQoSAdmittedBwThresholdTrap": rdnPktDQoSAdmittedBwThresholdTrap,
       "rdnCmtsMibNotificationObjects": rdnCmtsMibNotificationObjects,
       "rdnRQueryLastPollStartTime": rdnRQueryLastPollStartTime,
       "rdnRQueryLastPollStopTime": rdnRQueryLastPollStopTime,
       "rdnPktDQoSAdmittedBwThresholdReason": rdnPktDQoSAdmittedBwThresholdReason,
       "rdnCmtsMibConformance": rdnCmtsMibConformance,
       "rdnCmtsCompliances": rdnCmtsCompliances,
       "rdnCmtsMibCompliance": rdnCmtsMibCompliance,
       "rdnCmtsMibGroups": rdnCmtsMibGroups,
       "rdnCmtsIfGroup": rdnCmtsIfGroup,
       "rdnCmtsMiscGroup": rdnCmtsMiscGroup,
       "rdnCmtsNotificationsGroup": rdnCmtsNotificationsGroup}
)
