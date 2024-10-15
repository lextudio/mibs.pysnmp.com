# SNMP MIB module (CISCO-SWITCH-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SWITCH-MULTICAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:11 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoInterfaceIndexList,
 EntPhysicalIndexOrZero) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoInterfaceIndexList",
    "EntPhysicalIndexOrZero")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(MplsVpnId,) = mibBuilder.importSymbols(
    "MPLS-VPN-MIB",
    "MplsVpnId")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoSwitchMulticastMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 504)
)
ciscoSwitchMulticastMIB.setRevisions(
        ("2010-05-27 00:01",
         "2008-03-20 00:00",
         "2006-01-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CswmMIBNotifs_ObjectIdentity = ObjectIdentity
cswmMIBNotifs = _CswmMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 0)
)
_CswmMIBObjects_ObjectIdentity = ObjectIdentity
cswmMIBObjects = _CswmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1)
)
_CswmGlobal_ObjectIdentity = ObjectIdentity
cswmGlobal = _CswmGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 1)
)


class _CswmMvpnHwSwitchingStatus_Type(Integer32):
    """Custom type cswmMvpnHwSwitchingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("notCapable", 1))
    )


_CswmMvpnHwSwitchingStatus_Type.__name__ = "Integer32"
_CswmMvpnHwSwitchingStatus_Object = MibScalar
cswmMvpnHwSwitchingStatus = _CswmMvpnHwSwitchingStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 1, 1),
    _CswmMvpnHwSwitchingStatus_Type()
)
cswmMvpnHwSwitchingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmMvpnHwSwitchingStatus.setStatus("current")


class _CswmVrfLiteStatus_Type(Integer32):
    """Custom type cswmVrfLiteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("notCapable", 1))
    )


_CswmVrfLiteStatus_Type.__name__ = "Integer32"
_CswmVrfLiteStatus_Object = MibScalar
cswmVrfLiteStatus = _CswmVrfLiteStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 1, 2),
    _CswmVrfLiteStatus_Type()
)
cswmVrfLiteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmVrfLiteStatus.setStatus("current")


class _CswmMRouteConsistCheck_Type(Integer32):
    """Custom type cswmMRouteConsistCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("notCapable", 1))
    )


_CswmMRouteConsistCheck_Type.__name__ = "Integer32"
_CswmMRouteConsistCheck_Object = MibScalar
cswmMRouteConsistCheck = _CswmMRouteConsistCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 1, 3),
    _CswmMRouteConsistCheck_Type()
)
cswmMRouteConsistCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cswmMRouteConsistCheck.setStatus("current")


class _CswmProcessorConsistCheck_Type(Integer32):
    """Custom type cswmProcessorConsistCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("notCapable", 1))
    )


_CswmProcessorConsistCheck_Type.__name__ = "Integer32"
_CswmProcessorConsistCheck_Object = MibScalar
cswmProcessorConsistCheck = _CswmProcessorConsistCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 1, 4),
    _CswmProcessorConsistCheck_Type()
)
cswmProcessorConsistCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cswmProcessorConsistCheck.setStatus("current")
_CswmReplication_ObjectIdentity = ObjectIdentity
cswmReplication = _CswmReplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 2)
)
_CswmReplCapabilityTable_Object = MibTable
cswmReplCapabilityTable = _CswmReplCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cswmReplCapabilityTable.setStatus("current")
_CswmReplCapabilityEntry_Object = MibTableRow
cswmReplCapabilityEntry = _CswmReplCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 2, 1, 1)
)
cswmReplCapabilityEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SWITCH-MULTICAST-MIB", "cswmReplConfigAddrType"),
)
if mibBuilder.loadTexts:
    cswmReplCapabilityEntry.setStatus("current")


class _CswmReplCapability_Type(Bits):
    """Custom type cswmReplCapability based on Bits"""
    namedValues = NamedValues(
        *(("egress", 1),
          ("ingress", 0))
    )

_CswmReplCapability_Type.__name__ = "Bits"
_CswmReplCapability_Object = MibTableColumn
cswmReplCapability = _CswmReplCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 2, 1, 1, 1),
    _CswmReplCapability_Type()
)
cswmReplCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmReplCapability.setStatus("current")
_CswmReplConfigTable_Object = MibTable
cswmReplConfigTable = _CswmReplConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cswmReplConfigTable.setStatus("current")
_CswmReplConfigEntry_Object = MibTableRow
cswmReplConfigEntry = _CswmReplConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 2, 2, 1)
)
cswmReplConfigEntry.setIndexNames(
    (0, "CISCO-SWITCH-MULTICAST-MIB", "cswmReplConfigAddrType"),
)
if mibBuilder.loadTexts:
    cswmReplConfigEntry.setStatus("current")
_CswmReplConfigAddrType_Type = InetAddressType
_CswmReplConfigAddrType_Object = MibTableColumn
cswmReplConfigAddrType = _CswmReplConfigAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 2, 2, 1, 1),
    _CswmReplConfigAddrType_Type()
)
cswmReplConfigAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cswmReplConfigAddrType.setStatus("current")


class _CswmReplConfigCurMode_Type(Integer32):
    """Custom type cswmReplConfigCurMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egressAndIngress", 3),
          ("ingress", 2),
          ("notCapable", 1))
    )


_CswmReplConfigCurMode_Type.__name__ = "Integer32"
_CswmReplConfigCurMode_Object = MibTableColumn
cswmReplConfigCurMode = _CswmReplConfigCurMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 2, 2, 1, 2),
    _CswmReplConfigCurMode_Type()
)
cswmReplConfigCurMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cswmReplConfigCurMode.setStatus("current")


class _CswmReplConfigAutoDetect_Type(Integer32):
    """Custom type cswmReplConfigAutoDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("notCapable", 1))
    )


_CswmReplConfigAutoDetect_Type.__name__ = "Integer32"
_CswmReplConfigAutoDetect_Object = MibTableColumn
cswmReplConfigAutoDetect = _CswmReplConfigAutoDetect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 2, 2, 1, 3),
    _CswmReplConfigAutoDetect_Type()
)
cswmReplConfigAutoDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cswmReplConfigAutoDetect.setStatus("current")


class _CswmGlobalReplcationMode_Type(Integer32):
    """Custom type cswmGlobalReplcationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egress", 3),
          ("ingress", 2),
          ("notCapable", 1))
    )


_CswmGlobalReplcationMode_Type.__name__ = "Integer32"
_CswmGlobalReplcationMode_Object = MibScalar
cswmGlobalReplcationMode = _CswmGlobalReplcationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 2, 3),
    _CswmGlobalReplcationMode_Type()
)
cswmGlobalReplcationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cswmGlobalReplcationMode.setStatus("current")
_CswmMvrfStats_ObjectIdentity = ObjectIdentity
cswmMvrfStats = _CswmMvrfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 3)
)
_CswmMvrfStatsTable_Object = MibTable
cswmMvrfStatsTable = _CswmMvrfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cswmMvrfStatsTable.setStatus("current")
_CswmMvrfStatsEntry_Object = MibTableRow
cswmMvrfStatsEntry = _CswmMvrfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 3, 1, 1)
)
cswmMvrfStatsEntry.setIndexNames(
    (0, "CISCO-SWITCH-MULTICAST-MIB", "cswmMvrfName"),
)
if mibBuilder.loadTexts:
    cswmMvrfStatsEntry.setStatus("current")
_CswmMvrfName_Type = MplsVpnId
_CswmMvrfName_Object = MibTableColumn
cswmMvrfName = _CswmMvrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 3, 1, 1, 1),
    _CswmMvrfName_Type()
)
cswmMvrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cswmMvrfName.setStatus("current")
_CswmMvrfTotalFlows_Type = Gauge32
_CswmMvrfTotalFlows_Object = MibTableColumn
cswmMvrfTotalFlows = _CswmMvrfTotalFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 3, 1, 1, 2),
    _CswmMvrfTotalFlows_Type()
)
cswmMvrfTotalFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmMvrfTotalFlows.setStatus("current")
_CswmMvrfPartialFlows_Type = Gauge32
_CswmMvrfPartialFlows_Object = MibTableColumn
cswmMvrfPartialFlows = _CswmMvrfPartialFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 3, 1, 1, 3),
    _CswmMvrfPartialFlows_Type()
)
cswmMvrfPartialFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmMvrfPartialFlows.setStatus("current")
_CswmMvrfRpfMfdFlows_Type = Gauge32
_CswmMvrfRpfMfdFlows_Object = MibTableColumn
cswmMvrfRpfMfdFlows = _CswmMvrfRpfMfdFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 3, 1, 1, 4),
    _CswmMvrfRpfMfdFlows_Type()
)
cswmMvrfRpfMfdFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmMvrfRpfMfdFlows.setStatus("current")
_CswmBiDirPimDfStats_ObjectIdentity = ObjectIdentity
cswmBiDirPimDfStats = _CswmBiDirPimDfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 4)
)
_CswmBiDirPimDfUsed_Type = Unsigned32
_CswmBiDirPimDfUsed_Object = MibScalar
cswmBiDirPimDfUsed = _CswmBiDirPimDfUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 4, 1),
    _CswmBiDirPimDfUsed_Type()
)
cswmBiDirPimDfUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmBiDirPimDfUsed.setStatus("current")
if mibBuilder.loadTexts:
    cswmBiDirPimDfUsed.setUnits("entries")
_CswmBiDirPimDfTotal_Type = Unsigned32
_CswmBiDirPimDfTotal_Object = MibScalar
cswmBiDirPimDfTotal = _CswmBiDirPimDfTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 4, 2),
    _CswmBiDirPimDfTotal_Type()
)
cswmBiDirPimDfTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmBiDirPimDfTotal.setStatus("current")
if mibBuilder.loadTexts:
    cswmBiDirPimDfTotal.setUnits("entries")
_CswmMvrfBiDirPimDfUsageTable_Object = MibTable
cswmMvrfBiDirPimDfUsageTable = _CswmMvrfBiDirPimDfUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cswmMvrfBiDirPimDfUsageTable.setStatus("current")
_CswmMvrfBiDirPimDfUsageEntry_Object = MibTableRow
cswmMvrfBiDirPimDfUsageEntry = _CswmMvrfBiDirPimDfUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 4, 3, 1)
)
cswmMvrfBiDirPimDfUsageEntry.setIndexNames(
    (0, "CISCO-SWITCH-MULTICAST-MIB", "cswmMvrfName"),
    (0, "CISCO-SWITCH-MULTICAST-MIB", "cswmMvrfBiDirPimDfAddrType"),
)
if mibBuilder.loadTexts:
    cswmMvrfBiDirPimDfUsageEntry.setStatus("current")
_CswmMvrfBiDirPimDfAddrType_Type = InetAddressType
_CswmMvrfBiDirPimDfAddrType_Object = MibTableColumn
cswmMvrfBiDirPimDfAddrType = _CswmMvrfBiDirPimDfAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 4, 3, 1, 1),
    _CswmMvrfBiDirPimDfAddrType_Type()
)
cswmMvrfBiDirPimDfAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cswmMvrfBiDirPimDfAddrType.setStatus("current")
_CswmMvrfBiDirPimDfUsed_Type = Unsigned32
_CswmMvrfBiDirPimDfUsed_Object = MibTableColumn
cswmMvrfBiDirPimDfUsed = _CswmMvrfBiDirPimDfUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 4, 3, 1, 2),
    _CswmMvrfBiDirPimDfUsed_Type()
)
cswmMvrfBiDirPimDfUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmMvrfBiDirPimDfUsed.setStatus("current")
if mibBuilder.loadTexts:
    cswmMvrfBiDirPimDfUsed.setUnits("entries")
_CswmMvrfBiDirPimDfTotal_Type = Unsigned32
_CswmMvrfBiDirPimDfTotal_Object = MibTableColumn
cswmMvrfBiDirPimDfTotal = _CswmMvrfBiDirPimDfTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 4, 3, 1, 3),
    _CswmMvrfBiDirPimDfTotal_Type()
)
cswmMvrfBiDirPimDfTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmMvrfBiDirPimDfTotal.setStatus("current")
if mibBuilder.loadTexts:
    cswmMvrfBiDirPimDfTotal.setUnits("entries")
_CswmLtlStats_ObjectIdentity = ObjectIdentity
cswmLtlStats = _CswmLtlStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 5)
)
_CswmLtlUsed_Type = Unsigned32
_CswmLtlUsed_Object = MibScalar
cswmLtlUsed = _CswmLtlUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 5, 1),
    _CswmLtlUsed_Type()
)
cswmLtlUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmLtlUsed.setStatus("current")
_CswmLtlTotal_Type = Unsigned32
_CswmLtlTotal_Object = MibScalar
cswmLtlTotal = _CswmLtlTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 5, 2),
    _CswmLtlTotal_Type()
)
cswmLtlTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmLtlTotal.setStatus("current")
_CswmForwarding_ObjectIdentity = ObjectIdentity
cswmForwarding = _CswmForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 6)
)
_CswmForwardingTable_Object = MibTable
cswmForwardingTable = _CswmForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cswmForwardingTable.setStatus("current")
_CswmForwardingEntry_Object = MibTableRow
cswmForwardingEntry = _CswmForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 6, 1, 1)
)
cswmForwardingEntry.setIndexNames(
    (0, "CISCO-SWITCH-MULTICAST-MIB", "cswmInterfaceIndex"),
    (0, "CISCO-SWITCH-MULTICAST-MIB", "cswmForwardingAddrType"),
)
if mibBuilder.loadTexts:
    cswmForwardingEntry.setStatus("current")
_CswmInterfaceIndex_Type = InterfaceIndex
_CswmInterfaceIndex_Object = MibTableColumn
cswmInterfaceIndex = _CswmInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 6, 1, 1, 1),
    _CswmInterfaceIndex_Type()
)
cswmInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cswmInterfaceIndex.setStatus("current")
_CswmForwardingAddrType_Type = InetAddressType
_CswmForwardingAddrType_Object = MibTableColumn
cswmForwardingAddrType = _CswmForwardingAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 6, 1, 1, 2),
    _CswmForwardingAddrType_Type()
)
cswmForwardingAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cswmForwardingAddrType.setStatus("current")


class _CswmForwardingEnabled_Type(Integer32):
    """Custom type cswmForwardingEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("notCapable", 1))
    )


_CswmForwardingEnabled_Type.__name__ = "Integer32"
_CswmForwardingEnabled_Object = MibTableColumn
cswmForwardingEnabled = _CswmForwardingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 6, 1, 1, 3),
    _CswmForwardingEnabled_Type()
)
cswmForwardingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cswmForwardingEnabled.setStatus("current")
_CswmFlowQueryResult_ObjectIdentity = ObjectIdentity
cswmFlowQueryResult = _CswmFlowQueryResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7)
)
_CswmFlowMaxQueries_Type = Unsigned32
_CswmFlowMaxQueries_Object = MibScalar
cswmFlowMaxQueries = _CswmFlowMaxQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 1),
    _CswmFlowMaxQueries_Type()
)
cswmFlowMaxQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmFlowMaxQueries.setStatus("current")
_CswmFlowQueryTable_Object = MibTable
cswmFlowQueryTable = _CswmFlowQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 2)
)
if mibBuilder.loadTexts:
    cswmFlowQueryTable.setStatus("current")
_CswmFlowQueryEntry_Object = MibTableRow
cswmFlowQueryEntry = _CswmFlowQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 2, 1)
)
cswmFlowQueryEntry.setIndexNames(
    (0, "CISCO-SWITCH-MULTICAST-MIB", "cswmFlowQueryIndex"),
)
if mibBuilder.loadTexts:
    cswmFlowQueryEntry.setStatus("current")
_CswmFlowQueryIndex_Type = Unsigned32
_CswmFlowQueryIndex_Object = MibTableColumn
cswmFlowQueryIndex = _CswmFlowQueryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 2, 1, 1),
    _CswmFlowQueryIndex_Type()
)
cswmFlowQueryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cswmFlowQueryIndex.setStatus("current")


class _CswmFlowQueryMask_Type(Bits):
    """Custom type cswmFlowQueryMask based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("group", 1),
          ("groupmask", 2),
          ("source", 3),
          ("vrf", 0))
    )

_CswmFlowQueryMask_Type.__name__ = "Bits"
_CswmFlowQueryMask_Object = MibTableColumn
cswmFlowQueryMask = _CswmFlowQueryMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 2, 1, 2),
    _CswmFlowQueryMask_Type()
)
cswmFlowQueryMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cswmFlowQueryMask.setStatus("current")
_CswmFlowQueryMvrf_Type = MplsVpnId
_CswmFlowQueryMvrf_Object = MibTableColumn
cswmFlowQueryMvrf = _CswmFlowQueryMvrf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 2, 1, 3),
    _CswmFlowQueryMvrf_Type()
)
cswmFlowQueryMvrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cswmFlowQueryMvrf.setStatus("current")


class _CswmFlowQueryAddrType_Type(InetAddressType):
    """Custom type cswmFlowQueryAddrType based on InetAddressType"""


_CswmFlowQueryAddrType_Object = MibTableColumn
cswmFlowQueryAddrType = _CswmFlowQueryAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 2, 1, 4),
    _CswmFlowQueryAddrType_Type()
)
cswmFlowQueryAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cswmFlowQueryAddrType.setStatus("current")


class _CswmFlowQuerySource_Type(InetAddress):
    """Custom type cswmFlowQuerySource based on InetAddress"""
    defaultHexValue = "00000000"


_CswmFlowQuerySource_Object = MibTableColumn
cswmFlowQuerySource = _CswmFlowQuerySource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 2, 1, 5),
    _CswmFlowQuerySource_Type()
)
cswmFlowQuerySource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cswmFlowQuerySource.setStatus("current")


class _CswmFlowQueryGroup_Type(InetAddress):
    """Custom type cswmFlowQueryGroup based on InetAddress"""
    defaultHexValue = "00000000"


_CswmFlowQueryGroup_Object = MibTableColumn
cswmFlowQueryGroup = _CswmFlowQueryGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 2, 1, 6),
    _CswmFlowQueryGroup_Type()
)
cswmFlowQueryGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cswmFlowQueryGroup.setStatus("current")


class _CswmFlowQueryGroupMask_Type(InetAddressPrefixLength):
    """Custom type cswmFlowQueryGroupMask based on InetAddressPrefixLength"""
    defaultValue = 0


_CswmFlowQueryGroupMask_Object = MibTableColumn
cswmFlowQueryGroupMask = _CswmFlowQueryGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 2, 1, 7),
    _CswmFlowQueryGroupMask_Type()
)
cswmFlowQueryGroupMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cswmFlowQueryGroupMask.setStatus("current")


class _CswmFlowQueryType_Type(Bits):
    """Custom type cswmFlowQueryType based on Bits"""
    namedValues = NamedValues(
        *(("dfList", 2),
          ("oifList", 1),
          ("perFlow", 0))
    )

_CswmFlowQueryType_Type.__name__ = "Bits"
_CswmFlowQueryType_Object = MibTableColumn
cswmFlowQueryType = _CswmFlowQueryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 2, 1, 8),
    _CswmFlowQueryType_Type()
)
cswmFlowQueryType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cswmFlowQueryType.setStatus("current")


class _CswmFlowQueryEntityIndex_Type(EntPhysicalIndexOrZero):
    """Custom type cswmFlowQueryEntityIndex based on EntPhysicalIndexOrZero"""
    defaultValue = 0


_CswmFlowQueryEntityIndex_Object = MibTableColumn
cswmFlowQueryEntityIndex = _CswmFlowQueryEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 2, 1, 9),
    _CswmFlowQueryEntityIndex_Type()
)
cswmFlowQueryEntityIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cswmFlowQueryEntityIndex.setStatus("current")


class _CswmFlowQuerySkipNFlows_Type(Integer32):
    """Custom type cswmFlowQuerySkipNFlows based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CswmFlowQuerySkipNFlows_Type.__name__ = "Integer32"
_CswmFlowQuerySkipNFlows_Object = MibTableColumn
cswmFlowQuerySkipNFlows = _CswmFlowQuerySkipNFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 2, 1, 10),
    _CswmFlowQuerySkipNFlows_Type()
)
cswmFlowQuerySkipNFlows.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cswmFlowQuerySkipNFlows.setStatus("current")


class _CswmFlowQueryTotalFlows_Type(Integer32):
    """Custom type cswmFlowQueryTotalFlows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CswmFlowQueryTotalFlows_Type.__name__ = "Integer32"
_CswmFlowQueryTotalFlows_Object = MibTableColumn
cswmFlowQueryTotalFlows = _CswmFlowQueryTotalFlows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 2, 1, 11),
    _CswmFlowQueryTotalFlows_Type()
)
cswmFlowQueryTotalFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmFlowQueryTotalFlows.setStatus("current")


class _CswmFlowMcastQueryRows_Type(Integer32):
    """Custom type cswmFlowMcastQueryRows based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_CswmFlowMcastQueryRows_Type.__name__ = "Integer32"
_CswmFlowMcastQueryRows_Object = MibTableColumn
cswmFlowMcastQueryRows = _CswmFlowMcastQueryRows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 2, 1, 12),
    _CswmFlowMcastQueryRows_Type()
)
cswmFlowMcastQueryRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmFlowMcastQueryRows.setStatus("current")
_CswmFlowMcastQueryMoreRows_Type = TruthValue
_CswmFlowMcastQueryMoreRows_Object = MibTableColumn
cswmFlowMcastQueryMoreRows = _CswmFlowMcastQueryMoreRows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 2, 1, 13),
    _CswmFlowMcastQueryMoreRows_Type()
)
cswmFlowMcastQueryMoreRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmFlowMcastQueryMoreRows.setStatus("current")
_CswmFlowQueryOwner_Type = SnmpAdminString
_CswmFlowQueryOwner_Object = MibTableColumn
cswmFlowQueryOwner = _CswmFlowQueryOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 2, 1, 14),
    _CswmFlowQueryOwner_Type()
)
cswmFlowQueryOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cswmFlowQueryOwner.setStatus("current")
_CswmFlowQueryCreateTime_Type = TimeStamp
_CswmFlowQueryCreateTime_Object = MibTableColumn
cswmFlowQueryCreateTime = _CswmFlowQueryCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 2, 1, 15),
    _CswmFlowQueryCreateTime_Type()
)
cswmFlowQueryCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmFlowQueryCreateTime.setStatus("current")


class _CswmFlowQueryStorage_Type(StorageType):
    """Custom type cswmFlowQueryStorage based on StorageType"""


_CswmFlowQueryStorage_Object = MibTableColumn
cswmFlowQueryStorage = _CswmFlowQueryStorage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 2, 1, 16),
    _CswmFlowQueryStorage_Type()
)
cswmFlowQueryStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cswmFlowQueryStorage.setStatus("current")
_CswmFlowQueryStatus_Type = RowStatus
_CswmFlowQueryStatus_Object = MibTableColumn
cswmFlowQueryStatus = _CswmFlowQueryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 2, 1, 17),
    _CswmFlowQueryStatus_Type()
)
cswmFlowQueryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cswmFlowQueryStatus.setStatus("current")
_CswmFlowResultTable_Object = MibTable
cswmFlowResultTable = _CswmFlowResultTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 3)
)
if mibBuilder.loadTexts:
    cswmFlowResultTable.setStatus("current")
_CswmFlowResultEntry_Object = MibTableRow
cswmFlowResultEntry = _CswmFlowResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 3, 1)
)
cswmFlowResultEntry.setIndexNames(
    (0, "CISCO-SWITCH-MULTICAST-MIB", "cswmFlowQueryIndex"),
    (0, "CISCO-SWITCH-MULTICAST-MIB", "cswmFlowResultIndex"),
)
if mibBuilder.loadTexts:
    cswmFlowResultEntry.setStatus("current")


class _CswmFlowResultIndex_Type(Unsigned32):
    """Custom type cswmFlowResultIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CswmFlowResultIndex_Type.__name__ = "Unsigned32"
_CswmFlowResultIndex_Object = MibTableColumn
cswmFlowResultIndex = _CswmFlowResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 3, 1, 1),
    _CswmFlowResultIndex_Type()
)
cswmFlowResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cswmFlowResultIndex.setStatus("current")
_CswmFlowResultMvrf_Type = MplsVpnId
_CswmFlowResultMvrf_Object = MibTableColumn
cswmFlowResultMvrf = _CswmFlowResultMvrf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 3, 1, 2),
    _CswmFlowResultMvrf_Type()
)
cswmFlowResultMvrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmFlowResultMvrf.setStatus("current")
_CswmFlowResultAddrType_Type = InetAddressType
_CswmFlowResultAddrType_Object = MibTableColumn
cswmFlowResultAddrType = _CswmFlowResultAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 3, 1, 3),
    _CswmFlowResultAddrType_Type()
)
cswmFlowResultAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmFlowResultAddrType.setStatus("current")
_CswmFlowResultGroup_Type = InetAddress
_CswmFlowResultGroup_Object = MibTableColumn
cswmFlowResultGroup = _CswmFlowResultGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 3, 1, 4),
    _CswmFlowResultGroup_Type()
)
cswmFlowResultGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmFlowResultGroup.setStatus("current")
_CswmFlowResultGroupMask_Type = InetAddressPrefixLength
_CswmFlowResultGroupMask_Object = MibTableColumn
cswmFlowResultGroupMask = _CswmFlowResultGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 3, 1, 5),
    _CswmFlowResultGroupMask_Type()
)
cswmFlowResultGroupMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmFlowResultGroupMask.setStatus("current")
_CswmFlowResultSource_Type = InetAddress
_CswmFlowResultSource_Object = MibTableColumn
cswmFlowResultSource = _CswmFlowResultSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 3, 1, 6),
    _CswmFlowResultSource_Type()
)
cswmFlowResultSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmFlowResultSource.setStatus("current")


class _CswmFlowResultFlags_Type(Bits):
    """Custom type cswmFlowResultFlags based on Bits"""
    namedValues = NamedValues(
        *(("bidir", 4),
          ("copy", 0),
          ("hwFail", 3),
          ("ineligible", 2),
          ("punt", 1))
    )

_CswmFlowResultFlags_Type.__name__ = "Bits"
_CswmFlowResultFlags_Object = MibTableColumn
cswmFlowResultFlags = _CswmFlowResultFlags_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 3, 1, 7),
    _CswmFlowResultFlags_Type()
)
cswmFlowResultFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmFlowResultFlags.setStatus("current")
_CswmFlowResultRpfInterface_Type = InterfaceIndexOrZero
_CswmFlowResultRpfInterface_Object = MibTableColumn
cswmFlowResultRpfInterface = _CswmFlowResultRpfInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 3, 1, 8),
    _CswmFlowResultRpfInterface_Type()
)
cswmFlowResultRpfInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmFlowResultRpfInterface.setStatus("current")
_CswmFlowResultPackets_Type = Counter64
_CswmFlowResultPackets_Object = MibTableColumn
cswmFlowResultPackets = _CswmFlowResultPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 3, 1, 11),
    _CswmFlowResultPackets_Type()
)
cswmFlowResultPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmFlowResultPackets.setStatus("current")
_CswmFlowResultOctets_Type = Counter64
_CswmFlowResultOctets_Object = MibTableColumn
cswmFlowResultOctets = _CswmFlowResultOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 3, 1, 12),
    _CswmFlowResultOctets_Type()
)
cswmFlowResultOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmFlowResultOctets.setStatus("current")
_CswmFlowResultOIFTable_Object = MibTable
cswmFlowResultOIFTable = _CswmFlowResultOIFTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 4)
)
if mibBuilder.loadTexts:
    cswmFlowResultOIFTable.setStatus("current")
_CswmFlowResultOIFEntry_Object = MibTableRow
cswmFlowResultOIFEntry = _CswmFlowResultOIFEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 4, 1)
)
cswmFlowResultOIFEntry.setIndexNames(
    (0, "CISCO-SWITCH-MULTICAST-MIB", "cswmFlowQueryIndex"),
    (0, "CISCO-SWITCH-MULTICAST-MIB", "cswmFlowResultIndex"),
    (0, "CISCO-SWITCH-MULTICAST-MIB", "cswmFlowResultOIFIndex"),
)
if mibBuilder.loadTexts:
    cswmFlowResultOIFEntry.setStatus("current")


class _CswmFlowResultOIFIndex_Type(Unsigned32):
    """Custom type cswmFlowResultOIFIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CswmFlowResultOIFIndex_Type.__name__ = "Unsigned32"
_CswmFlowResultOIFIndex_Object = MibTableColumn
cswmFlowResultOIFIndex = _CswmFlowResultOIFIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 4, 1, 1),
    _CswmFlowResultOIFIndex_Type()
)
cswmFlowResultOIFIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cswmFlowResultOIFIndex.setStatus("current")
_CswmFlowResultOIFIntList_Type = CiscoInterfaceIndexList
_CswmFlowResultOIFIntList_Object = MibTableColumn
cswmFlowResultOIFIntList = _CswmFlowResultOIFIntList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 4, 1, 2),
    _CswmFlowResultOIFIntList_Type()
)
cswmFlowResultOIFIntList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmFlowResultOIFIntList.setStatus("current")
_CswmFlowResultDFTable_Object = MibTable
cswmFlowResultDFTable = _CswmFlowResultDFTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 5)
)
if mibBuilder.loadTexts:
    cswmFlowResultDFTable.setStatus("current")
_CswmFlowResultDFEntry_Object = MibTableRow
cswmFlowResultDFEntry = _CswmFlowResultDFEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 5, 1)
)
cswmFlowResultDFEntry.setIndexNames(
    (0, "CISCO-SWITCH-MULTICAST-MIB", "cswmFlowQueryIndex"),
    (0, "CISCO-SWITCH-MULTICAST-MIB", "cswmFlowResultIndex"),
    (0, "CISCO-SWITCH-MULTICAST-MIB", "cswmFlowResultDFIndex"),
)
if mibBuilder.loadTexts:
    cswmFlowResultDFEntry.setStatus("current")


class _CswmFlowResultDFIndex_Type(Unsigned32):
    """Custom type cswmFlowResultDFIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CswmFlowResultDFIndex_Type.__name__ = "Unsigned32"
_CswmFlowResultDFIndex_Object = MibTableColumn
cswmFlowResultDFIndex = _CswmFlowResultDFIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 5, 1, 1),
    _CswmFlowResultDFIndex_Type()
)
cswmFlowResultDFIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cswmFlowResultDFIndex.setStatus("current")
_CswmFlowResultDFIntList_Type = CiscoInterfaceIndexList
_CswmFlowResultDFIntList_Object = MibTableColumn
cswmFlowResultDFIntList = _CswmFlowResultDFIntList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 1, 7, 5, 1, 2),
    _CswmFlowResultDFIntList_Type()
)
cswmFlowResultDFIntList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cswmFlowResultDFIntList.setStatus("current")
_CswmMIBConform_ObjectIdentity = ObjectIdentity
cswmMIBConform = _CswmMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 2)
)
_CswmMIBCompliances_ObjectIdentity = ObjectIdentity
cswmMIBCompliances = _CswmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 2, 1)
)
_CswmMIBGroups_ObjectIdentity = ObjectIdentity
cswmMIBGroups = _CswmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 2, 2)
)

# Managed Objects groups

cswmGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 2, 2, 1)
)
cswmGlobalGroup.setObjects(
      *(("CISCO-SWITCH-MULTICAST-MIB", "cswmMvpnHwSwitchingStatus"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmVrfLiteStatus"))
)
if mibBuilder.loadTexts:
    cswmGlobalGroup.setStatus("current")

cswmConsistCheckGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 2, 2, 2)
)
cswmConsistCheckGroup.setObjects(
      *(("CISCO-SWITCH-MULTICAST-MIB", "cswmMRouteConsistCheck"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmProcessorConsistCheck"))
)
if mibBuilder.loadTexts:
    cswmConsistCheckGroup.setStatus("current")

cswmReplicationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 2, 2, 3)
)
cswmReplicationGroup.setObjects(
      *(("CISCO-SWITCH-MULTICAST-MIB", "cswmReplCapability"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmReplConfigCurMode"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmReplConfigAutoDetect"))
)
if mibBuilder.loadTexts:
    cswmReplicationGroup.setStatus("current")

cswmMvrfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 2, 2, 4)
)
cswmMvrfStatsGroup.setObjects(
      *(("CISCO-SWITCH-MULTICAST-MIB", "cswmMvrfTotalFlows"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmMvrfPartialFlows"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmMvrfRpfMfdFlows"))
)
if mibBuilder.loadTexts:
    cswmMvrfStatsGroup.setStatus("current")

cswmBiDirPimDfUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 2, 2, 5)
)
cswmBiDirPimDfUsageGroup.setObjects(
      *(("CISCO-SWITCH-MULTICAST-MIB", "cswmBiDirPimDfUsed"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmBiDirPimDfTotal"))
)
if mibBuilder.loadTexts:
    cswmBiDirPimDfUsageGroup.setStatus("current")

cswmLtlUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 2, 2, 6)
)
cswmLtlUsageGroup.setObjects(
      *(("CISCO-SWITCH-MULTICAST-MIB", "cswmLtlUsed"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmLtlTotal"))
)
if mibBuilder.loadTexts:
    cswmLtlUsageGroup.setStatus("current")

cswmGlobalReplicationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 2, 2, 7)
)
cswmGlobalReplicationGroup.setObjects(
    ("CISCO-SWITCH-MULTICAST-MIB", "cswmGlobalReplcationMode")
)
if mibBuilder.loadTexts:
    cswmGlobalReplicationGroup.setStatus("current")

cswmMvrfBiDirPimDfUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 2, 2, 8)
)
cswmMvrfBiDirPimDfUsageGroup.setObjects(
      *(("CISCO-SWITCH-MULTICAST-MIB", "cswmMvrfBiDirPimDfUsed"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmMvrfBiDirPimDfTotal"))
)
if mibBuilder.loadTexts:
    cswmMvrfBiDirPimDfUsageGroup.setStatus("current")

cswmForwardingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 2, 2, 9)
)
cswmForwardingGroup.setObjects(
    ("CISCO-SWITCH-MULTICAST-MIB", "cswmForwardingEnabled")
)
if mibBuilder.loadTexts:
    cswmForwardingGroup.setStatus("current")

cswmFlowQueryResultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 2, 2, 10)
)
cswmFlowQueryResultGroup.setObjects(
      *(("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowMaxQueries"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowQueryMask"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowQueryAddrType"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowQuerySource"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowQueryGroup"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowQueryGroupMask"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowQueryType"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowQueryMvrf"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowQueryEntityIndex"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowQuerySkipNFlows"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowQueryTotalFlows"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowMcastQueryRows"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowMcastQueryMoreRows"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowQueryOwner"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowQueryCreateTime"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowQueryStorage"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowQueryStatus"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowResultMvrf"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowResultAddrType"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowResultGroup"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowResultGroupMask"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowResultSource"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowResultFlags"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowResultPackets"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowResultOctets"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowResultRpfInterface"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowResultOIFIntList"),
        ("CISCO-SWITCH-MULTICAST-MIB", "cswmFlowResultDFIntList"))
)
if mibBuilder.loadTexts:
    cswmFlowQueryResultGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cswmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cswmMIBCompliance.setStatus(
        "deprecated"
    )

cswmMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cswmMIBCompliance2.setStatus(
        "deprecated"
    )

cswmMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 504, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cswmMIBCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SWITCH-MULTICAST-MIB",
    **{"ciscoSwitchMulticastMIB": ciscoSwitchMulticastMIB,
       "cswmMIBNotifs": cswmMIBNotifs,
       "cswmMIBObjects": cswmMIBObjects,
       "cswmGlobal": cswmGlobal,
       "cswmMvpnHwSwitchingStatus": cswmMvpnHwSwitchingStatus,
       "cswmVrfLiteStatus": cswmVrfLiteStatus,
       "cswmMRouteConsistCheck": cswmMRouteConsistCheck,
       "cswmProcessorConsistCheck": cswmProcessorConsistCheck,
       "cswmReplication": cswmReplication,
       "cswmReplCapabilityTable": cswmReplCapabilityTable,
       "cswmReplCapabilityEntry": cswmReplCapabilityEntry,
       "cswmReplCapability": cswmReplCapability,
       "cswmReplConfigTable": cswmReplConfigTable,
       "cswmReplConfigEntry": cswmReplConfigEntry,
       "cswmReplConfigAddrType": cswmReplConfigAddrType,
       "cswmReplConfigCurMode": cswmReplConfigCurMode,
       "cswmReplConfigAutoDetect": cswmReplConfigAutoDetect,
       "cswmGlobalReplcationMode": cswmGlobalReplcationMode,
       "cswmMvrfStats": cswmMvrfStats,
       "cswmMvrfStatsTable": cswmMvrfStatsTable,
       "cswmMvrfStatsEntry": cswmMvrfStatsEntry,
       "cswmMvrfName": cswmMvrfName,
       "cswmMvrfTotalFlows": cswmMvrfTotalFlows,
       "cswmMvrfPartialFlows": cswmMvrfPartialFlows,
       "cswmMvrfRpfMfdFlows": cswmMvrfRpfMfdFlows,
       "cswmBiDirPimDfStats": cswmBiDirPimDfStats,
       "cswmBiDirPimDfUsed": cswmBiDirPimDfUsed,
       "cswmBiDirPimDfTotal": cswmBiDirPimDfTotal,
       "cswmMvrfBiDirPimDfUsageTable": cswmMvrfBiDirPimDfUsageTable,
       "cswmMvrfBiDirPimDfUsageEntry": cswmMvrfBiDirPimDfUsageEntry,
       "cswmMvrfBiDirPimDfAddrType": cswmMvrfBiDirPimDfAddrType,
       "cswmMvrfBiDirPimDfUsed": cswmMvrfBiDirPimDfUsed,
       "cswmMvrfBiDirPimDfTotal": cswmMvrfBiDirPimDfTotal,
       "cswmLtlStats": cswmLtlStats,
       "cswmLtlUsed": cswmLtlUsed,
       "cswmLtlTotal": cswmLtlTotal,
       "cswmForwarding": cswmForwarding,
       "cswmForwardingTable": cswmForwardingTable,
       "cswmForwardingEntry": cswmForwardingEntry,
       "cswmInterfaceIndex": cswmInterfaceIndex,
       "cswmForwardingAddrType": cswmForwardingAddrType,
       "cswmForwardingEnabled": cswmForwardingEnabled,
       "cswmFlowQueryResult": cswmFlowQueryResult,
       "cswmFlowMaxQueries": cswmFlowMaxQueries,
       "cswmFlowQueryTable": cswmFlowQueryTable,
       "cswmFlowQueryEntry": cswmFlowQueryEntry,
       "cswmFlowQueryIndex": cswmFlowQueryIndex,
       "cswmFlowQueryMask": cswmFlowQueryMask,
       "cswmFlowQueryMvrf": cswmFlowQueryMvrf,
       "cswmFlowQueryAddrType": cswmFlowQueryAddrType,
       "cswmFlowQuerySource": cswmFlowQuerySource,
       "cswmFlowQueryGroup": cswmFlowQueryGroup,
       "cswmFlowQueryGroupMask": cswmFlowQueryGroupMask,
       "cswmFlowQueryType": cswmFlowQueryType,
       "cswmFlowQueryEntityIndex": cswmFlowQueryEntityIndex,
       "cswmFlowQuerySkipNFlows": cswmFlowQuerySkipNFlows,
       "cswmFlowQueryTotalFlows": cswmFlowQueryTotalFlows,
       "cswmFlowMcastQueryRows": cswmFlowMcastQueryRows,
       "cswmFlowMcastQueryMoreRows": cswmFlowMcastQueryMoreRows,
       "cswmFlowQueryOwner": cswmFlowQueryOwner,
       "cswmFlowQueryCreateTime": cswmFlowQueryCreateTime,
       "cswmFlowQueryStorage": cswmFlowQueryStorage,
       "cswmFlowQueryStatus": cswmFlowQueryStatus,
       "cswmFlowResultTable": cswmFlowResultTable,
       "cswmFlowResultEntry": cswmFlowResultEntry,
       "cswmFlowResultIndex": cswmFlowResultIndex,
       "cswmFlowResultMvrf": cswmFlowResultMvrf,
       "cswmFlowResultAddrType": cswmFlowResultAddrType,
       "cswmFlowResultGroup": cswmFlowResultGroup,
       "cswmFlowResultGroupMask": cswmFlowResultGroupMask,
       "cswmFlowResultSource": cswmFlowResultSource,
       "cswmFlowResultFlags": cswmFlowResultFlags,
       "cswmFlowResultRpfInterface": cswmFlowResultRpfInterface,
       "cswmFlowResultPackets": cswmFlowResultPackets,
       "cswmFlowResultOctets": cswmFlowResultOctets,
       "cswmFlowResultOIFTable": cswmFlowResultOIFTable,
       "cswmFlowResultOIFEntry": cswmFlowResultOIFEntry,
       "cswmFlowResultOIFIndex": cswmFlowResultOIFIndex,
       "cswmFlowResultOIFIntList": cswmFlowResultOIFIntList,
       "cswmFlowResultDFTable": cswmFlowResultDFTable,
       "cswmFlowResultDFEntry": cswmFlowResultDFEntry,
       "cswmFlowResultDFIndex": cswmFlowResultDFIndex,
       "cswmFlowResultDFIntList": cswmFlowResultDFIntList,
       "cswmMIBConform": cswmMIBConform,
       "cswmMIBCompliances": cswmMIBCompliances,
       "cswmMIBCompliance": cswmMIBCompliance,
       "cswmMIBCompliance2": cswmMIBCompliance2,
       "cswmMIBCompliance3": cswmMIBCompliance3,
       "cswmMIBGroups": cswmMIBGroups,
       "cswmGlobalGroup": cswmGlobalGroup,
       "cswmConsistCheckGroup": cswmConsistCheckGroup,
       "cswmReplicationGroup": cswmReplicationGroup,
       "cswmMvrfStatsGroup": cswmMvrfStatsGroup,
       "cswmBiDirPimDfUsageGroup": cswmBiDirPimDfUsageGroup,
       "cswmLtlUsageGroup": cswmLtlUsageGroup,
       "cswmGlobalReplicationGroup": cswmGlobalReplicationGroup,
       "cswmMvrfBiDirPimDfUsageGroup": cswmMvrfBiDirPimDfUsageGroup,
       "cswmForwardingGroup": cswmForwardingGroup,
       "cswmFlowQueryResultGroup": cswmFlowQueryResultGroup}
)
