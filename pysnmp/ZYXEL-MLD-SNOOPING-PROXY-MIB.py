# SNMP MIB module (ZYXEL-MLD-SNOOPING-PROXY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-MLD-SNOOPING-PROXY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:22 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelMldSnoopingProxy = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelMldSnoopingProxyFilteringSetup_ObjectIdentity = ObjectIdentity
zyxelMldSnoopingProxyFilteringSetup = _ZyxelMldSnoopingProxyFilteringSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 1)
)
_ZyMldSnoopingProxyFilteringMaxNumberOfProfiles_Type = Integer32
_ZyMldSnoopingProxyFilteringMaxNumberOfProfiles_Object = MibScalar
zyMldSnoopingProxyFilteringMaxNumberOfProfiles = _ZyMldSnoopingProxyFilteringMaxNumberOfProfiles_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 1, 1),
    _ZyMldSnoopingProxyFilteringMaxNumberOfProfiles_Type()
)
zyMldSnoopingProxyFilteringMaxNumberOfProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyFilteringMaxNumberOfProfiles.setStatus("current")
_ZyxelMldSnoopingProxyFilteringProfileTable_Object = MibTable
zyxelMldSnoopingProxyFilteringProfileTable = _ZyxelMldSnoopingProxyFilteringProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelMldSnoopingProxyFilteringProfileTable.setStatus("current")
_ZyxelMldSnoopingProxyFilteringProfileEntry_Object = MibTableRow
zyxelMldSnoopingProxyFilteringProfileEntry = _ZyxelMldSnoopingProxyFilteringProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 1, 2, 1)
)
zyxelMldSnoopingProxyFilteringProfileEntry.setIndexNames(
    (0, "ZYXEL-MLD-SNOOPING-PROXY-MIB", "zyMldSnoopingProxyFilteringProfileName"),
    (0, "ZYXEL-MLD-SNOOPING-PROXY-MIB", "zyMldSnoopingProxyFilteringProfileStartIpAddressType"),
    (0, "ZYXEL-MLD-SNOOPING-PROXY-MIB", "zyMldSnoopingProxyFilteringProfileStartIpAddress"),
    (0, "ZYXEL-MLD-SNOOPING-PROXY-MIB", "zyMldSnoopingProxyFilteringProfileEndIpAddressType"),
    (0, "ZYXEL-MLD-SNOOPING-PROXY-MIB", "zyMldSnoopingProxyFilteringProfileEndIpAddress"),
)
if mibBuilder.loadTexts:
    zyxelMldSnoopingProxyFilteringProfileEntry.setStatus("current")
_ZyMldSnoopingProxyFilteringProfileName_Type = OctetString
_ZyMldSnoopingProxyFilteringProfileName_Object = MibTableColumn
zyMldSnoopingProxyFilteringProfileName = _ZyMldSnoopingProxyFilteringProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 1, 2, 1, 1),
    _ZyMldSnoopingProxyFilteringProfileName_Type()
)
zyMldSnoopingProxyFilteringProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyFilteringProfileName.setStatus("current")
_ZyMldSnoopingProxyFilteringProfileStartIpAddressType_Type = InetAddressType
_ZyMldSnoopingProxyFilteringProfileStartIpAddressType_Object = MibTableColumn
zyMldSnoopingProxyFilteringProfileStartIpAddressType = _ZyMldSnoopingProxyFilteringProfileStartIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 1, 2, 1, 2),
    _ZyMldSnoopingProxyFilteringProfileStartIpAddressType_Type()
)
zyMldSnoopingProxyFilteringProfileStartIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyFilteringProfileStartIpAddressType.setStatus("current")
_ZyMldSnoopingProxyFilteringProfileStartIpAddress_Type = InetAddress
_ZyMldSnoopingProxyFilteringProfileStartIpAddress_Object = MibTableColumn
zyMldSnoopingProxyFilteringProfileStartIpAddress = _ZyMldSnoopingProxyFilteringProfileStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 1, 2, 1, 3),
    _ZyMldSnoopingProxyFilteringProfileStartIpAddress_Type()
)
zyMldSnoopingProxyFilteringProfileStartIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyFilteringProfileStartIpAddress.setStatus("current")
_ZyMldSnoopingProxyFilteringProfileEndIpAddressType_Type = InetAddressType
_ZyMldSnoopingProxyFilteringProfileEndIpAddressType_Object = MibTableColumn
zyMldSnoopingProxyFilteringProfileEndIpAddressType = _ZyMldSnoopingProxyFilteringProfileEndIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 1, 2, 1, 4),
    _ZyMldSnoopingProxyFilteringProfileEndIpAddressType_Type()
)
zyMldSnoopingProxyFilteringProfileEndIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyFilteringProfileEndIpAddressType.setStatus("current")
_ZyMldSnoopingProxyFilteringProfileEndIpAddress_Type = InetAddress
_ZyMldSnoopingProxyFilteringProfileEndIpAddress_Object = MibTableColumn
zyMldSnoopingProxyFilteringProfileEndIpAddress = _ZyMldSnoopingProxyFilteringProfileEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 1, 2, 1, 5),
    _ZyMldSnoopingProxyFilteringProfileEndIpAddress_Type()
)
zyMldSnoopingProxyFilteringProfileEndIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyFilteringProfileEndIpAddress.setStatus("current")
_ZyMldSnoopingProxyFilteringProfileRowStatus_Type = RowStatus
_ZyMldSnoopingProxyFilteringProfileRowStatus_Object = MibTableColumn
zyMldSnoopingProxyFilteringProfileRowStatus = _ZyMldSnoopingProxyFilteringProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 1, 2, 1, 6),
    _ZyMldSnoopingProxyFilteringProfileRowStatus_Type()
)
zyMldSnoopingProxyFilteringProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyFilteringProfileRowStatus.setStatus("current")
_ZyxelMldSnoopingProxyFilteringPortTable_Object = MibTable
zyxelMldSnoopingProxyFilteringPortTable = _ZyxelMldSnoopingProxyFilteringPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelMldSnoopingProxyFilteringPortTable.setStatus("current")
_ZyxelMldSnoopingProxyFilteringPortEntry_Object = MibTableRow
zyxelMldSnoopingProxyFilteringPortEntry = _ZyxelMldSnoopingProxyFilteringPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 1, 3, 1)
)
zyxelMldSnoopingProxyFilteringPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelMldSnoopingProxyFilteringPortEntry.setStatus("current")
_ZyMldSnoopingProxyFilteringPortProfile_Type = OctetString
_ZyMldSnoopingProxyFilteringPortProfile_Object = MibTableColumn
zyMldSnoopingProxyFilteringPortProfile = _ZyMldSnoopingProxyFilteringPortProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 1, 3, 1, 1),
    _ZyMldSnoopingProxyFilteringPortProfile_Type()
)
zyMldSnoopingProxyFilteringPortProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyFilteringPortProfile.setStatus("current")
_ZyMldSnoopingProxyFilteringPortGroupLimitState_Type = EnabledStatus
_ZyMldSnoopingProxyFilteringPortGroupLimitState_Object = MibTableColumn
zyMldSnoopingProxyFilteringPortGroupLimitState = _ZyMldSnoopingProxyFilteringPortGroupLimitState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 1, 3, 1, 2),
    _ZyMldSnoopingProxyFilteringPortGroupLimitState_Type()
)
zyMldSnoopingProxyFilteringPortGroupLimitState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyFilteringPortGroupLimitState.setStatus("current")
_ZyMldSnoopingProxyFilteringPortMaxNumberOfGroups_Type = Integer32
_ZyMldSnoopingProxyFilteringPortMaxNumberOfGroups_Object = MibTableColumn
zyMldSnoopingProxyFilteringPortMaxNumberOfGroups = _ZyMldSnoopingProxyFilteringPortMaxNumberOfGroups_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 1, 3, 1, 3),
    _ZyMldSnoopingProxyFilteringPortMaxNumberOfGroups_Type()
)
zyMldSnoopingProxyFilteringPortMaxNumberOfGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyFilteringPortMaxNumberOfGroups.setStatus("current")
_ZyxelMldSnoopingProxyStatistics_ObjectIdentity = ObjectIdentity
zyxelMldSnoopingProxyStatistics = _ZyxelMldSnoopingProxyStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2)
)
_ZyMldSnoopingProxySysStatisticsV1QueryRx_Type = Integer32
_ZyMldSnoopingProxySysStatisticsV1QueryRx_Object = MibScalar
zyMldSnoopingProxySysStatisticsV1QueryRx = _ZyMldSnoopingProxySysStatisticsV1QueryRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 1),
    _ZyMldSnoopingProxySysStatisticsV1QueryRx_Type()
)
zyMldSnoopingProxySysStatisticsV1QueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxySysStatisticsV1QueryRx.setStatus("current")
_ZyMldSnoopingProxySysStatisticsV1QueryTx_Type = Integer32
_ZyMldSnoopingProxySysStatisticsV1QueryTx_Object = MibScalar
zyMldSnoopingProxySysStatisticsV1QueryTx = _ZyMldSnoopingProxySysStatisticsV1QueryTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 2),
    _ZyMldSnoopingProxySysStatisticsV1QueryTx_Type()
)
zyMldSnoopingProxySysStatisticsV1QueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxySysStatisticsV1QueryTx.setStatus("current")
_ZyMldSnoopingProxySysStatisticsV1QueryDrop_Type = Integer32
_ZyMldSnoopingProxySysStatisticsV1QueryDrop_Object = MibScalar
zyMldSnoopingProxySysStatisticsV1QueryDrop = _ZyMldSnoopingProxySysStatisticsV1QueryDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 3),
    _ZyMldSnoopingProxySysStatisticsV1QueryDrop_Type()
)
zyMldSnoopingProxySysStatisticsV1QueryDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxySysStatisticsV1QueryDrop.setStatus("current")
_ZyMldSnoopingProxySysStatisticsV1ReportRx_Type = Integer32
_ZyMldSnoopingProxySysStatisticsV1ReportRx_Object = MibScalar
zyMldSnoopingProxySysStatisticsV1ReportRx = _ZyMldSnoopingProxySysStatisticsV1ReportRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 4),
    _ZyMldSnoopingProxySysStatisticsV1ReportRx_Type()
)
zyMldSnoopingProxySysStatisticsV1ReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxySysStatisticsV1ReportRx.setStatus("current")
_ZyMldSnoopingProxySysStatisticsV1ReportTx_Type = Integer32
_ZyMldSnoopingProxySysStatisticsV1ReportTx_Object = MibScalar
zyMldSnoopingProxySysStatisticsV1ReportTx = _ZyMldSnoopingProxySysStatisticsV1ReportTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 5),
    _ZyMldSnoopingProxySysStatisticsV1ReportTx_Type()
)
zyMldSnoopingProxySysStatisticsV1ReportTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxySysStatisticsV1ReportTx.setStatus("current")
_ZyMldSnoopingProxySysStatisticsV1ReportDrop_Type = Integer32
_ZyMldSnoopingProxySysStatisticsV1ReportDrop_Object = MibScalar
zyMldSnoopingProxySysStatisticsV1ReportDrop = _ZyMldSnoopingProxySysStatisticsV1ReportDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 6),
    _ZyMldSnoopingProxySysStatisticsV1ReportDrop_Type()
)
zyMldSnoopingProxySysStatisticsV1ReportDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxySysStatisticsV1ReportDrop.setStatus("current")
_ZyMldSnoopingProxySysStatisticsV1DoneRx_Type = Integer32
_ZyMldSnoopingProxySysStatisticsV1DoneRx_Object = MibScalar
zyMldSnoopingProxySysStatisticsV1DoneRx = _ZyMldSnoopingProxySysStatisticsV1DoneRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 7),
    _ZyMldSnoopingProxySysStatisticsV1DoneRx_Type()
)
zyMldSnoopingProxySysStatisticsV1DoneRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxySysStatisticsV1DoneRx.setStatus("current")
_ZyMldSnoopingProxySysStatisticsV1DoneTx_Type = Integer32
_ZyMldSnoopingProxySysStatisticsV1DoneTx_Object = MibScalar
zyMldSnoopingProxySysStatisticsV1DoneTx = _ZyMldSnoopingProxySysStatisticsV1DoneTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 8),
    _ZyMldSnoopingProxySysStatisticsV1DoneTx_Type()
)
zyMldSnoopingProxySysStatisticsV1DoneTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxySysStatisticsV1DoneTx.setStatus("current")
_ZyMldSnoopingProxySysStatisticsV1DoneDrop_Type = Integer32
_ZyMldSnoopingProxySysStatisticsV1DoneDrop_Object = MibScalar
zyMldSnoopingProxySysStatisticsV1DoneDrop = _ZyMldSnoopingProxySysStatisticsV1DoneDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 9),
    _ZyMldSnoopingProxySysStatisticsV1DoneDrop_Type()
)
zyMldSnoopingProxySysStatisticsV1DoneDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxySysStatisticsV1DoneDrop.setStatus("current")
_ZyMldSnoopingProxySysStatisticsV2QueryRx_Type = Integer32
_ZyMldSnoopingProxySysStatisticsV2QueryRx_Object = MibScalar
zyMldSnoopingProxySysStatisticsV2QueryRx = _ZyMldSnoopingProxySysStatisticsV2QueryRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 10),
    _ZyMldSnoopingProxySysStatisticsV2QueryRx_Type()
)
zyMldSnoopingProxySysStatisticsV2QueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxySysStatisticsV2QueryRx.setStatus("current")
_ZyMldSnoopingProxySysStatisticsV2QueryTx_Type = Integer32
_ZyMldSnoopingProxySysStatisticsV2QueryTx_Object = MibScalar
zyMldSnoopingProxySysStatisticsV2QueryTx = _ZyMldSnoopingProxySysStatisticsV2QueryTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 11),
    _ZyMldSnoopingProxySysStatisticsV2QueryTx_Type()
)
zyMldSnoopingProxySysStatisticsV2QueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxySysStatisticsV2QueryTx.setStatus("current")
_ZyMldSnoopingProxySysStatisticsV2QueryDrop_Type = Integer32
_ZyMldSnoopingProxySysStatisticsV2QueryDrop_Object = MibScalar
zyMldSnoopingProxySysStatisticsV2QueryDrop = _ZyMldSnoopingProxySysStatisticsV2QueryDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 12),
    _ZyMldSnoopingProxySysStatisticsV2QueryDrop_Type()
)
zyMldSnoopingProxySysStatisticsV2QueryDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxySysStatisticsV2QueryDrop.setStatus("current")
_ZyMldSnoopingProxySysStatisticsV2ReportRx_Type = Integer32
_ZyMldSnoopingProxySysStatisticsV2ReportRx_Object = MibScalar
zyMldSnoopingProxySysStatisticsV2ReportRx = _ZyMldSnoopingProxySysStatisticsV2ReportRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 13),
    _ZyMldSnoopingProxySysStatisticsV2ReportRx_Type()
)
zyMldSnoopingProxySysStatisticsV2ReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxySysStatisticsV2ReportRx.setStatus("current")
_ZyMldSnoopingProxySysStatisticsV2ReportTx_Type = Integer32
_ZyMldSnoopingProxySysStatisticsV2ReportTx_Object = MibScalar
zyMldSnoopingProxySysStatisticsV2ReportTx = _ZyMldSnoopingProxySysStatisticsV2ReportTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 14),
    _ZyMldSnoopingProxySysStatisticsV2ReportTx_Type()
)
zyMldSnoopingProxySysStatisticsV2ReportTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxySysStatisticsV2ReportTx.setStatus("current")
_ZyMldSnoopingProxySysStatisticsV2ReportDrop_Type = Integer32
_ZyMldSnoopingProxySysStatisticsV2ReportDrop_Object = MibScalar
zyMldSnoopingProxySysStatisticsV2ReportDrop = _ZyMldSnoopingProxySysStatisticsV2ReportDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 15),
    _ZyMldSnoopingProxySysStatisticsV2ReportDrop_Type()
)
zyMldSnoopingProxySysStatisticsV2ReportDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxySysStatisticsV2ReportDrop.setStatus("current")
_ZyxelMldSnoopingProxyStatisticsVlanTable_Object = MibTable
zyxelMldSnoopingProxyStatisticsVlanTable = _ZyxelMldSnoopingProxyStatisticsVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 16)
)
if mibBuilder.loadTexts:
    zyxelMldSnoopingProxyStatisticsVlanTable.setStatus("current")
_ZyxelMldSnoopingProxyStatisticsVlanEntry_Object = MibTableRow
zyxelMldSnoopingProxyStatisticsVlanEntry = _ZyxelMldSnoopingProxyStatisticsVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 16, 1)
)
zyxelMldSnoopingProxyStatisticsVlanEntry.setIndexNames(
    (0, "ZYXEL-MLD-SNOOPING-PROXY-MIB", "zyMldSnoopingProxyVlanVid"),
)
if mibBuilder.loadTexts:
    zyxelMldSnoopingProxyStatisticsVlanEntry.setStatus("current")
_ZyMldSnoopingProxyStatisticsVlanV1QueryRx_Type = Integer32
_ZyMldSnoopingProxyStatisticsVlanV1QueryRx_Object = MibTableColumn
zyMldSnoopingProxyStatisticsVlanV1QueryRx = _ZyMldSnoopingProxyStatisticsVlanV1QueryRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 16, 1, 1),
    _ZyMldSnoopingProxyStatisticsVlanV1QueryRx_Type()
)
zyMldSnoopingProxyStatisticsVlanV1QueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsVlanV1QueryRx.setStatus("current")
_ZyMldSnoopingProxyStatisticsVlanV1QueryTx_Type = Integer32
_ZyMldSnoopingProxyStatisticsVlanV1QueryTx_Object = MibTableColumn
zyMldSnoopingProxyStatisticsVlanV1QueryTx = _ZyMldSnoopingProxyStatisticsVlanV1QueryTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 16, 1, 2),
    _ZyMldSnoopingProxyStatisticsVlanV1QueryTx_Type()
)
zyMldSnoopingProxyStatisticsVlanV1QueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsVlanV1QueryTx.setStatus("current")
_ZyMldSnoopingProxyStatisticsVlanV1QueryDrop_Type = Integer32
_ZyMldSnoopingProxyStatisticsVlanV1QueryDrop_Object = MibTableColumn
zyMldSnoopingProxyStatisticsVlanV1QueryDrop = _ZyMldSnoopingProxyStatisticsVlanV1QueryDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 16, 1, 3),
    _ZyMldSnoopingProxyStatisticsVlanV1QueryDrop_Type()
)
zyMldSnoopingProxyStatisticsVlanV1QueryDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsVlanV1QueryDrop.setStatus("current")
_ZyMldSnoopingProxyStatisticsVlanV1ReportRx_Type = Integer32
_ZyMldSnoopingProxyStatisticsVlanV1ReportRx_Object = MibTableColumn
zyMldSnoopingProxyStatisticsVlanV1ReportRx = _ZyMldSnoopingProxyStatisticsVlanV1ReportRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 16, 1, 4),
    _ZyMldSnoopingProxyStatisticsVlanV1ReportRx_Type()
)
zyMldSnoopingProxyStatisticsVlanV1ReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsVlanV1ReportRx.setStatus("current")
_ZyMldSnoopingProxyStatisticsVlanV1ReportTx_Type = Integer32
_ZyMldSnoopingProxyStatisticsVlanV1ReportTx_Object = MibTableColumn
zyMldSnoopingProxyStatisticsVlanV1ReportTx = _ZyMldSnoopingProxyStatisticsVlanV1ReportTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 16, 1, 5),
    _ZyMldSnoopingProxyStatisticsVlanV1ReportTx_Type()
)
zyMldSnoopingProxyStatisticsVlanV1ReportTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsVlanV1ReportTx.setStatus("current")
_ZyMldSnoopingProxyStatisticsVlanV1ReportDrop_Type = Integer32
_ZyMldSnoopingProxyStatisticsVlanV1ReportDrop_Object = MibTableColumn
zyMldSnoopingProxyStatisticsVlanV1ReportDrop = _ZyMldSnoopingProxyStatisticsVlanV1ReportDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 16, 1, 6),
    _ZyMldSnoopingProxyStatisticsVlanV1ReportDrop_Type()
)
zyMldSnoopingProxyStatisticsVlanV1ReportDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsVlanV1ReportDrop.setStatus("current")
_ZyMldSnoopingProxyStatisticsVlanV1DoneRx_Type = Integer32
_ZyMldSnoopingProxyStatisticsVlanV1DoneRx_Object = MibTableColumn
zyMldSnoopingProxyStatisticsVlanV1DoneRx = _ZyMldSnoopingProxyStatisticsVlanV1DoneRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 16, 1, 7),
    _ZyMldSnoopingProxyStatisticsVlanV1DoneRx_Type()
)
zyMldSnoopingProxyStatisticsVlanV1DoneRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsVlanV1DoneRx.setStatus("current")
_ZyMldSnoopingProxyStatisticsVlanV1DoneTx_Type = Integer32
_ZyMldSnoopingProxyStatisticsVlanV1DoneTx_Object = MibTableColumn
zyMldSnoopingProxyStatisticsVlanV1DoneTx = _ZyMldSnoopingProxyStatisticsVlanV1DoneTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 16, 1, 8),
    _ZyMldSnoopingProxyStatisticsVlanV1DoneTx_Type()
)
zyMldSnoopingProxyStatisticsVlanV1DoneTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsVlanV1DoneTx.setStatus("current")
_ZyMldSnoopingProxyStatisticsVlanV1DoneDrop_Type = Integer32
_ZyMldSnoopingProxyStatisticsVlanV1DoneDrop_Object = MibTableColumn
zyMldSnoopingProxyStatisticsVlanV1DoneDrop = _ZyMldSnoopingProxyStatisticsVlanV1DoneDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 16, 1, 9),
    _ZyMldSnoopingProxyStatisticsVlanV1DoneDrop_Type()
)
zyMldSnoopingProxyStatisticsVlanV1DoneDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsVlanV1DoneDrop.setStatus("current")
_ZyMldSnoopingProxyStatisticsVlanV2QueryRx_Type = Integer32
_ZyMldSnoopingProxyStatisticsVlanV2QueryRx_Object = MibTableColumn
zyMldSnoopingProxyStatisticsVlanV2QueryRx = _ZyMldSnoopingProxyStatisticsVlanV2QueryRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 16, 1, 10),
    _ZyMldSnoopingProxyStatisticsVlanV2QueryRx_Type()
)
zyMldSnoopingProxyStatisticsVlanV2QueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsVlanV2QueryRx.setStatus("current")
_ZyMldSnoopingProxyStatisticsVlanV2QueryTx_Type = Integer32
_ZyMldSnoopingProxyStatisticsVlanV2QueryTx_Object = MibTableColumn
zyMldSnoopingProxyStatisticsVlanV2QueryTx = _ZyMldSnoopingProxyStatisticsVlanV2QueryTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 16, 1, 11),
    _ZyMldSnoopingProxyStatisticsVlanV2QueryTx_Type()
)
zyMldSnoopingProxyStatisticsVlanV2QueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsVlanV2QueryTx.setStatus("current")
_ZyMldSnoopingProxyStatisticsVlanV2QueryDrop_Type = Integer32
_ZyMldSnoopingProxyStatisticsVlanV2QueryDrop_Object = MibTableColumn
zyMldSnoopingProxyStatisticsVlanV2QueryDrop = _ZyMldSnoopingProxyStatisticsVlanV2QueryDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 16, 1, 12),
    _ZyMldSnoopingProxyStatisticsVlanV2QueryDrop_Type()
)
zyMldSnoopingProxyStatisticsVlanV2QueryDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsVlanV2QueryDrop.setStatus("current")
_ZyMldSnoopingProxyStatisticsVlanV2ReportRx_Type = Integer32
_ZyMldSnoopingProxyStatisticsVlanV2ReportRx_Object = MibTableColumn
zyMldSnoopingProxyStatisticsVlanV2ReportRx = _ZyMldSnoopingProxyStatisticsVlanV2ReportRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 16, 1, 13),
    _ZyMldSnoopingProxyStatisticsVlanV2ReportRx_Type()
)
zyMldSnoopingProxyStatisticsVlanV2ReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsVlanV2ReportRx.setStatus("current")
_ZyMldSnoopingProxyStatisticsVlanV2ReportTx_Type = Integer32
_ZyMldSnoopingProxyStatisticsVlanV2ReportTx_Object = MibTableColumn
zyMldSnoopingProxyStatisticsVlanV2ReportTx = _ZyMldSnoopingProxyStatisticsVlanV2ReportTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 16, 1, 14),
    _ZyMldSnoopingProxyStatisticsVlanV2ReportTx_Type()
)
zyMldSnoopingProxyStatisticsVlanV2ReportTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsVlanV2ReportTx.setStatus("current")
_ZyMldSnoopingProxyStatisticsVlanV2ReportDrop_Type = Integer32
_ZyMldSnoopingProxyStatisticsVlanV2ReportDrop_Object = MibTableColumn
zyMldSnoopingProxyStatisticsVlanV2ReportDrop = _ZyMldSnoopingProxyStatisticsVlanV2ReportDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 16, 1, 15),
    _ZyMldSnoopingProxyStatisticsVlanV2ReportDrop_Type()
)
zyMldSnoopingProxyStatisticsVlanV2ReportDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsVlanV2ReportDrop.setStatus("current")
_ZyxelMldSnoopingProxyStatisticsPortTable_Object = MibTable
zyxelMldSnoopingProxyStatisticsPortTable = _ZyxelMldSnoopingProxyStatisticsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 17)
)
if mibBuilder.loadTexts:
    zyxelMldSnoopingProxyStatisticsPortTable.setStatus("current")
_ZyxelMldSnoopingProxyStatisticsPortEntry_Object = MibTableRow
zyxelMldSnoopingProxyStatisticsPortEntry = _ZyxelMldSnoopingProxyStatisticsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 17, 1)
)
zyxelMldSnoopingProxyStatisticsPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelMldSnoopingProxyStatisticsPortEntry.setStatus("current")
_ZyMldSnoopingProxyStatisticsPortV1QueryRx_Type = Integer32
_ZyMldSnoopingProxyStatisticsPortV1QueryRx_Object = MibTableColumn
zyMldSnoopingProxyStatisticsPortV1QueryRx = _ZyMldSnoopingProxyStatisticsPortV1QueryRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 17, 1, 1),
    _ZyMldSnoopingProxyStatisticsPortV1QueryRx_Type()
)
zyMldSnoopingProxyStatisticsPortV1QueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsPortV1QueryRx.setStatus("current")
_ZyMldSnoopingProxyStatisticsPortV1QueryTx_Type = Integer32
_ZyMldSnoopingProxyStatisticsPortV1QueryTx_Object = MibTableColumn
zyMldSnoopingProxyStatisticsPortV1QueryTx = _ZyMldSnoopingProxyStatisticsPortV1QueryTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 17, 1, 2),
    _ZyMldSnoopingProxyStatisticsPortV1QueryTx_Type()
)
zyMldSnoopingProxyStatisticsPortV1QueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsPortV1QueryTx.setStatus("current")
_ZyMldSnoopingProxyStatisticsPortV1QueryDrop_Type = Integer32
_ZyMldSnoopingProxyStatisticsPortV1QueryDrop_Object = MibTableColumn
zyMldSnoopingProxyStatisticsPortV1QueryDrop = _ZyMldSnoopingProxyStatisticsPortV1QueryDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 17, 1, 3),
    _ZyMldSnoopingProxyStatisticsPortV1QueryDrop_Type()
)
zyMldSnoopingProxyStatisticsPortV1QueryDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsPortV1QueryDrop.setStatus("current")
_ZyMldSnoopingProxyStatisticsPortV1ReportRx_Type = Integer32
_ZyMldSnoopingProxyStatisticsPortV1ReportRx_Object = MibTableColumn
zyMldSnoopingProxyStatisticsPortV1ReportRx = _ZyMldSnoopingProxyStatisticsPortV1ReportRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 17, 1, 4),
    _ZyMldSnoopingProxyStatisticsPortV1ReportRx_Type()
)
zyMldSnoopingProxyStatisticsPortV1ReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsPortV1ReportRx.setStatus("current")
_ZyMldSnoopingProxyStatisticsPortV1ReportTx_Type = Integer32
_ZyMldSnoopingProxyStatisticsPortV1ReportTx_Object = MibTableColumn
zyMldSnoopingProxyStatisticsPortV1ReportTx = _ZyMldSnoopingProxyStatisticsPortV1ReportTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 17, 1, 5),
    _ZyMldSnoopingProxyStatisticsPortV1ReportTx_Type()
)
zyMldSnoopingProxyStatisticsPortV1ReportTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsPortV1ReportTx.setStatus("current")
_ZyMldSnoopingProxyStatisticsPortV1ReportDrop_Type = Integer32
_ZyMldSnoopingProxyStatisticsPortV1ReportDrop_Object = MibTableColumn
zyMldSnoopingProxyStatisticsPortV1ReportDrop = _ZyMldSnoopingProxyStatisticsPortV1ReportDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 17, 1, 6),
    _ZyMldSnoopingProxyStatisticsPortV1ReportDrop_Type()
)
zyMldSnoopingProxyStatisticsPortV1ReportDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsPortV1ReportDrop.setStatus("current")
_ZyMldSnoopingProxyStatisticsPortV1DoneRx_Type = Integer32
_ZyMldSnoopingProxyStatisticsPortV1DoneRx_Object = MibTableColumn
zyMldSnoopingProxyStatisticsPortV1DoneRx = _ZyMldSnoopingProxyStatisticsPortV1DoneRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 17, 1, 7),
    _ZyMldSnoopingProxyStatisticsPortV1DoneRx_Type()
)
zyMldSnoopingProxyStatisticsPortV1DoneRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsPortV1DoneRx.setStatus("current")
_ZyMldSnoopingProxyStatisticsPortV1DoneTx_Type = Integer32
_ZyMldSnoopingProxyStatisticsPortV1DoneTx_Object = MibTableColumn
zyMldSnoopingProxyStatisticsPortV1DoneTx = _ZyMldSnoopingProxyStatisticsPortV1DoneTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 17, 1, 8),
    _ZyMldSnoopingProxyStatisticsPortV1DoneTx_Type()
)
zyMldSnoopingProxyStatisticsPortV1DoneTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsPortV1DoneTx.setStatus("current")
_ZyMldSnoopingProxyStatisticsPortV1DoneDrop_Type = Integer32
_ZyMldSnoopingProxyStatisticsPortV1DoneDrop_Object = MibTableColumn
zyMldSnoopingProxyStatisticsPortV1DoneDrop = _ZyMldSnoopingProxyStatisticsPortV1DoneDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 17, 1, 9),
    _ZyMldSnoopingProxyStatisticsPortV1DoneDrop_Type()
)
zyMldSnoopingProxyStatisticsPortV1DoneDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsPortV1DoneDrop.setStatus("current")
_ZyMldSnoopingProxyStatisticsPortV2QueryRx_Type = Integer32
_ZyMldSnoopingProxyStatisticsPortV2QueryRx_Object = MibTableColumn
zyMldSnoopingProxyStatisticsPortV2QueryRx = _ZyMldSnoopingProxyStatisticsPortV2QueryRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 17, 1, 10),
    _ZyMldSnoopingProxyStatisticsPortV2QueryRx_Type()
)
zyMldSnoopingProxyStatisticsPortV2QueryRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsPortV2QueryRx.setStatus("current")
_ZyMldSnoopingProxyStatisticsPortV2QueryTx_Type = Integer32
_ZyMldSnoopingProxyStatisticsPortV2QueryTx_Object = MibTableColumn
zyMldSnoopingProxyStatisticsPortV2QueryTx = _ZyMldSnoopingProxyStatisticsPortV2QueryTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 17, 1, 11),
    _ZyMldSnoopingProxyStatisticsPortV2QueryTx_Type()
)
zyMldSnoopingProxyStatisticsPortV2QueryTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsPortV2QueryTx.setStatus("current")
_ZyMldSnoopingProxyStatisticsPortV2QueryDrop_Type = Integer32
_ZyMldSnoopingProxyStatisticsPortV2QueryDrop_Object = MibTableColumn
zyMldSnoopingProxyStatisticsPortV2QueryDrop = _ZyMldSnoopingProxyStatisticsPortV2QueryDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 17, 1, 12),
    _ZyMldSnoopingProxyStatisticsPortV2QueryDrop_Type()
)
zyMldSnoopingProxyStatisticsPortV2QueryDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsPortV2QueryDrop.setStatus("current")
_ZyMldSnoopingProxyStatisticsPortV2ReportRx_Type = Integer32
_ZyMldSnoopingProxyStatisticsPortV2ReportRx_Object = MibTableColumn
zyMldSnoopingProxyStatisticsPortV2ReportRx = _ZyMldSnoopingProxyStatisticsPortV2ReportRx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 17, 1, 13),
    _ZyMldSnoopingProxyStatisticsPortV2ReportRx_Type()
)
zyMldSnoopingProxyStatisticsPortV2ReportRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsPortV2ReportRx.setStatus("current")
_ZyMldSnoopingProxyStatisticsPortV2ReportTx_Type = Integer32
_ZyMldSnoopingProxyStatisticsPortV2ReportTx_Object = MibTableColumn
zyMldSnoopingProxyStatisticsPortV2ReportTx = _ZyMldSnoopingProxyStatisticsPortV2ReportTx_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 17, 1, 14),
    _ZyMldSnoopingProxyStatisticsPortV2ReportTx_Type()
)
zyMldSnoopingProxyStatisticsPortV2ReportTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsPortV2ReportTx.setStatus("current")
_ZyMldSnoopingProxyStatisticsPortV2ReportDrop_Type = Integer32
_ZyMldSnoopingProxyStatisticsPortV2ReportDrop_Object = MibTableColumn
zyMldSnoopingProxyStatisticsPortV2ReportDrop = _ZyMldSnoopingProxyStatisticsPortV2ReportDrop_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 17, 1, 15),
    _ZyMldSnoopingProxyStatisticsPortV2ReportDrop_Type()
)
zyMldSnoopingProxyStatisticsPortV2ReportDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsPortV2ReportDrop.setStatus("current")
_ZyMldSnoopingProxyStatisticsClear_Type = EnabledStatus
_ZyMldSnoopingProxyStatisticsClear_Object = MibScalar
zyMldSnoopingProxyStatisticsClear = _ZyMldSnoopingProxyStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 18),
    _ZyMldSnoopingProxyStatisticsClear_Type()
)
zyMldSnoopingProxyStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsClear.setStatus("current")
_ZyMldSnoopingProxyStatisticsClearSystem_Type = EnabledStatus
_ZyMldSnoopingProxyStatisticsClearSystem_Object = MibScalar
zyMldSnoopingProxyStatisticsClearSystem = _ZyMldSnoopingProxyStatisticsClearSystem_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 19),
    _ZyMldSnoopingProxyStatisticsClearSystem_Type()
)
zyMldSnoopingProxyStatisticsClearSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsClearSystem.setStatus("current")
_ZyMldSnoopingProxyStatisticsClearPort_Type = EnabledStatus
_ZyMldSnoopingProxyStatisticsClearPort_Object = MibScalar
zyMldSnoopingProxyStatisticsClearPort = _ZyMldSnoopingProxyStatisticsClearPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 20),
    _ZyMldSnoopingProxyStatisticsClearPort_Type()
)
zyMldSnoopingProxyStatisticsClearPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsClearPort.setStatus("current")
_ZyMldSnoopingProxyStatisticsClearVlan_Type = EnabledStatus
_ZyMldSnoopingProxyStatisticsClearVlan_Object = MibScalar
zyMldSnoopingProxyStatisticsClearVlan = _ZyMldSnoopingProxyStatisticsClearVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 2, 21),
    _ZyMldSnoopingProxyStatisticsClearVlan_Type()
)
zyMldSnoopingProxyStatisticsClearVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyStatisticsClearVlan.setStatus("current")
_ZyxelMldSnoopingProxySetup_ObjectIdentity = ObjectIdentity
zyxelMldSnoopingProxySetup = _ZyxelMldSnoopingProxySetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3)
)
_ZyMldSnoopingProxyState_Type = EnabledStatus
_ZyMldSnoopingProxyState_Object = MibScalar
zyMldSnoopingProxyState = _ZyMldSnoopingProxyState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 1),
    _ZyMldSnoopingProxyState_Type()
)
zyMldSnoopingProxyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyState.setStatus("current")
_ZyMldSnoopingProxyFilteringState_Type = EnabledStatus
_ZyMldSnoopingProxyFilteringState_Object = MibScalar
zyMldSnoopingProxyFilteringState = _ZyMldSnoopingProxyFilteringState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 2),
    _ZyMldSnoopingProxyFilteringState_Type()
)
zyMldSnoopingProxyFilteringState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyFilteringState.setStatus("current")
_ZyMldSnoopingProxy8021pPriority_Type = Integer32
_ZyMldSnoopingProxy8021pPriority_Object = MibScalar
zyMldSnoopingProxy8021pPriority = _ZyMldSnoopingProxy8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 3),
    _ZyMldSnoopingProxy8021pPriority_Type()
)
zyMldSnoopingProxy8021pPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMldSnoopingProxy8021pPriority.setStatus("current")
_ZyMldSnoopingProxyMaxNumberOfVlans_Type = Integer32
_ZyMldSnoopingProxyMaxNumberOfVlans_Object = MibScalar
zyMldSnoopingProxyMaxNumberOfVlans = _ZyMldSnoopingProxyMaxNumberOfVlans_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 4),
    _ZyMldSnoopingProxyMaxNumberOfVlans_Type()
)
zyMldSnoopingProxyMaxNumberOfVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyMaxNumberOfVlans.setStatus("current")
_ZyxelMldSnoopingProxyVlanTable_Object = MibTable
zyxelMldSnoopingProxyVlanTable = _ZyxelMldSnoopingProxyVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 5)
)
if mibBuilder.loadTexts:
    zyxelMldSnoopingProxyVlanTable.setStatus("current")
_ZyxelMldSnoopingProxyVlanEntry_Object = MibTableRow
zyxelMldSnoopingProxyVlanEntry = _ZyxelMldSnoopingProxyVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 5, 1)
)
zyxelMldSnoopingProxyVlanEntry.setIndexNames(
    (0, "ZYXEL-MLD-SNOOPING-PROXY-MIB", "zyMldSnoopingProxyVlanVid"),
)
if mibBuilder.loadTexts:
    zyxelMldSnoopingProxyVlanEntry.setStatus("current")
_ZyMldSnoopingProxyVlanVid_Type = Integer32
_ZyMldSnoopingProxyVlanVid_Object = MibTableColumn
zyMldSnoopingProxyVlanVid = _ZyMldSnoopingProxyVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 5, 1, 1),
    _ZyMldSnoopingProxyVlanVid_Type()
)
zyMldSnoopingProxyVlanVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyVlanVid.setStatus("current")
_ZyMldSnoopingProxyVlanRowStatus_Type = RowStatus
_ZyMldSnoopingProxyVlanRowStatus_Object = MibTableColumn
zyMldSnoopingProxyVlanRowStatus = _ZyMldSnoopingProxyVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 5, 1, 2),
    _ZyMldSnoopingProxyVlanRowStatus_Type()
)
zyMldSnoopingProxyVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyVlanRowStatus.setStatus("current")
_ZyxelMldSnoopingProxyUpstreamVlanTable_Object = MibTable
zyxelMldSnoopingProxyUpstreamVlanTable = _ZyxelMldSnoopingProxyUpstreamVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 6)
)
if mibBuilder.loadTexts:
    zyxelMldSnoopingProxyUpstreamVlanTable.setStatus("current")
_ZyxelMldSnoopingProxyUpstreamVlanEntry_Object = MibTableRow
zyxelMldSnoopingProxyUpstreamVlanEntry = _ZyxelMldSnoopingProxyUpstreamVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 6, 1)
)
zyxelMldSnoopingProxyUpstreamVlanEntry.setIndexNames(
    (0, "ZYXEL-MLD-SNOOPING-PROXY-MIB", "zyMldSnoopingProxyVlanVid"),
)
if mibBuilder.loadTexts:
    zyxelMldSnoopingProxyUpstreamVlanEntry.setStatus("current")
_ZyMldSnoopingProxyUpstreamVlanPorts_Type = PortList
_ZyMldSnoopingProxyUpstreamVlanPorts_Object = MibTableColumn
zyMldSnoopingProxyUpstreamVlanPorts = _ZyMldSnoopingProxyUpstreamVlanPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 6, 1, 1),
    _ZyMldSnoopingProxyUpstreamVlanPorts_Type()
)
zyMldSnoopingProxyUpstreamVlanPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyUpstreamVlanPorts.setStatus("current")


class _ZyMldSnoopingProxyUpstreamVlanQueryInterval_Type(Integer32):
    """Custom type zyMldSnoopingProxyUpstreamVlanQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 31744000),
    )


_ZyMldSnoopingProxyUpstreamVlanQueryInterval_Type.__name__ = "Integer32"
_ZyMldSnoopingProxyUpstreamVlanQueryInterval_Object = MibTableColumn
zyMldSnoopingProxyUpstreamVlanQueryInterval = _ZyMldSnoopingProxyUpstreamVlanQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 6, 1, 2),
    _ZyMldSnoopingProxyUpstreamVlanQueryInterval_Type()
)
zyMldSnoopingProxyUpstreamVlanQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyUpstreamVlanQueryInterval.setStatus("current")


class _ZyMldSnoopingProxyUpstreamVlanMaxResponseTime_Type(Integer32):
    """Custom type zyMldSnoopingProxyUpstreamVlanMaxResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 25000),
    )


_ZyMldSnoopingProxyUpstreamVlanMaxResponseTime_Type.__name__ = "Integer32"
_ZyMldSnoopingProxyUpstreamVlanMaxResponseTime_Object = MibTableColumn
zyMldSnoopingProxyUpstreamVlanMaxResponseTime = _ZyMldSnoopingProxyUpstreamVlanMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 6, 1, 3),
    _ZyMldSnoopingProxyUpstreamVlanMaxResponseTime_Type()
)
zyMldSnoopingProxyUpstreamVlanMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyUpstreamVlanMaxResponseTime.setStatus("current")


class _ZyMldSnoopingProxyUpstreamVlanRobustness_Type(Integer32):
    """Custom type zyMldSnoopingProxyUpstreamVlanRobustness based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_ZyMldSnoopingProxyUpstreamVlanRobustness_Type.__name__ = "Integer32"
_ZyMldSnoopingProxyUpstreamVlanRobustness_Object = MibTableColumn
zyMldSnoopingProxyUpstreamVlanRobustness = _ZyMldSnoopingProxyUpstreamVlanRobustness_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 6, 1, 4),
    _ZyMldSnoopingProxyUpstreamVlanRobustness_Type()
)
zyMldSnoopingProxyUpstreamVlanRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyUpstreamVlanRobustness.setStatus("current")


class _ZyMldSnoopingProxyUpstreamVlanLastMemberQueryInterval_Type(Integer32):
    """Custom type zyMldSnoopingProxyUpstreamVlanLastMemberQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8387584),
    )


_ZyMldSnoopingProxyUpstreamVlanLastMemberQueryInterval_Type.__name__ = "Integer32"
_ZyMldSnoopingProxyUpstreamVlanLastMemberQueryInterval_Object = MibTableColumn
zyMldSnoopingProxyUpstreamVlanLastMemberQueryInterval = _ZyMldSnoopingProxyUpstreamVlanLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 6, 1, 5),
    _ZyMldSnoopingProxyUpstreamVlanLastMemberQueryInterval_Type()
)
zyMldSnoopingProxyUpstreamVlanLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyUpstreamVlanLastMemberQueryInterval.setStatus("current")
_ZyxelMldSnoopingProxyDownstreamVlanTable_Object = MibTable
zyxelMldSnoopingProxyDownstreamVlanTable = _ZyxelMldSnoopingProxyDownstreamVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 7)
)
if mibBuilder.loadTexts:
    zyxelMldSnoopingProxyDownstreamVlanTable.setStatus("current")
_ZyxelMldSnoopingProxyDownstreamVlanEntry_Object = MibTableRow
zyxelMldSnoopingProxyDownstreamVlanEntry = _ZyxelMldSnoopingProxyDownstreamVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 7, 1)
)
zyxelMldSnoopingProxyDownstreamVlanEntry.setIndexNames(
    (0, "ZYXEL-MLD-SNOOPING-PROXY-MIB", "zyMldSnoopingProxyVlanVid"),
)
if mibBuilder.loadTexts:
    zyxelMldSnoopingProxyDownstreamVlanEntry.setStatus("current")
_ZyMldSnoopingProxyDownstreamVlanPorts_Type = PortList
_ZyMldSnoopingProxyDownstreamVlanPorts_Object = MibTableColumn
zyMldSnoopingProxyDownstreamVlanPorts = _ZyMldSnoopingProxyDownstreamVlanPorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 7, 1, 1),
    _ZyMldSnoopingProxyDownstreamVlanPorts_Type()
)
zyMldSnoopingProxyDownstreamVlanPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyDownstreamVlanPorts.setStatus("current")


class _ZyMldSnoopingProxyDownstreamVlanQueryInterval_Type(Integer32):
    """Custom type zyMldSnoopingProxyDownstreamVlanQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 31744000),
    )


_ZyMldSnoopingProxyDownstreamVlanQueryInterval_Type.__name__ = "Integer32"
_ZyMldSnoopingProxyDownstreamVlanQueryInterval_Object = MibTableColumn
zyMldSnoopingProxyDownstreamVlanQueryInterval = _ZyMldSnoopingProxyDownstreamVlanQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 7, 1, 2),
    _ZyMldSnoopingProxyDownstreamVlanQueryInterval_Type()
)
zyMldSnoopingProxyDownstreamVlanQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyDownstreamVlanQueryInterval.setStatus("current")


class _ZyMldSnoopingProxyDownstreamVlanMaxResponseTime_Type(Integer32):
    """Custom type zyMldSnoopingProxyDownstreamVlanMaxResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 25000),
    )


_ZyMldSnoopingProxyDownstreamVlanMaxResponseTime_Type.__name__ = "Integer32"
_ZyMldSnoopingProxyDownstreamVlanMaxResponseTime_Object = MibTableColumn
zyMldSnoopingProxyDownstreamVlanMaxResponseTime = _ZyMldSnoopingProxyDownstreamVlanMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 7, 1, 3),
    _ZyMldSnoopingProxyDownstreamVlanMaxResponseTime_Type()
)
zyMldSnoopingProxyDownstreamVlanMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyDownstreamVlanMaxResponseTime.setStatus("current")
_ZyxelMldSnoopingProxyDownstreamVlanPortTable_Object = MibTable
zyxelMldSnoopingProxyDownstreamVlanPortTable = _ZyxelMldSnoopingProxyDownstreamVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 8)
)
if mibBuilder.loadTexts:
    zyxelMldSnoopingProxyDownstreamVlanPortTable.setStatus("current")
_ZyxelMldSnoopingProxyDownstreamVlanPortEntry_Object = MibTableRow
zyxelMldSnoopingProxyDownstreamVlanPortEntry = _ZyxelMldSnoopingProxyDownstreamVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 8, 1)
)
zyxelMldSnoopingProxyDownstreamVlanPortEntry.setIndexNames(
    (0, "ZYXEL-MLD-SNOOPING-PROXY-MIB", "zyMldSnoopingProxyVlanVid"),
    (0, "ZYXEL-MLD-SNOOPING-PROXY-MIB", "zyMldSnoopingProxyDownstreamVlanPortIndex"),
)
if mibBuilder.loadTexts:
    zyxelMldSnoopingProxyDownstreamVlanPortEntry.setStatus("current")
_ZyMldSnoopingProxyDownstreamVlanPortIndex_Type = Integer32
_ZyMldSnoopingProxyDownstreamVlanPortIndex_Object = MibTableColumn
zyMldSnoopingProxyDownstreamVlanPortIndex = _ZyMldSnoopingProxyDownstreamVlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 8, 1, 1),
    _ZyMldSnoopingProxyDownstreamVlanPortIndex_Type()
)
zyMldSnoopingProxyDownstreamVlanPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyDownstreamVlanPortIndex.setStatus("current")


class _ZyMldSnoopingProxyDownstreamVlanPortLeaveMode_Type(Integer32):
    """Custom type zyMldSnoopingProxyDownstreamVlanPortLeaveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 2),
          ("immediate", 0),
          ("normal", 1))
    )


_ZyMldSnoopingProxyDownstreamVlanPortLeaveMode_Type.__name__ = "Integer32"
_ZyMldSnoopingProxyDownstreamVlanPortLeaveMode_Object = MibTableColumn
zyMldSnoopingProxyDownstreamVlanPortLeaveMode = _ZyMldSnoopingProxyDownstreamVlanPortLeaveMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 8, 1, 2),
    _ZyMldSnoopingProxyDownstreamVlanPortLeaveMode_Type()
)
zyMldSnoopingProxyDownstreamVlanPortLeaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyDownstreamVlanPortLeaveMode.setStatus("current")
_ZyMldSnoopingProxyDownstreamVlanPortLeaveTimeout_Type = Integer32
_ZyMldSnoopingProxyDownstreamVlanPortLeaveTimeout_Object = MibTableColumn
zyMldSnoopingProxyDownstreamVlanPortLeaveTimeout = _ZyMldSnoopingProxyDownstreamVlanPortLeaveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 8, 1, 3),
    _ZyMldSnoopingProxyDownstreamVlanPortLeaveTimeout_Type()
)
zyMldSnoopingProxyDownstreamVlanPortLeaveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyDownstreamVlanPortLeaveTimeout.setStatus("current")
_ZyMldSnoopingProxyDownstreamVlanPortFastLeaveTimeout_Type = Integer32
_ZyMldSnoopingProxyDownstreamVlanPortFastLeaveTimeout_Object = MibTableColumn
zyMldSnoopingProxyDownstreamVlanPortFastLeaveTimeout = _ZyMldSnoopingProxyDownstreamVlanPortFastLeaveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 3, 8, 1, 4),
    _ZyMldSnoopingProxyDownstreamVlanPortFastLeaveTimeout_Type()
)
zyMldSnoopingProxyDownstreamVlanPortFastLeaveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyDownstreamVlanPortFastLeaveTimeout.setStatus("current")
_ZyxelMldSnoopingProxyMembershipStatus_ObjectIdentity = ObjectIdentity
zyxelMldSnoopingProxyMembershipStatus = _ZyxelMldSnoopingProxyMembershipStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 4)
)
_ZyxelMldSnoopingProxyMembershipTable_Object = MibTable
zyxelMldSnoopingProxyMembershipTable = _ZyxelMldSnoopingProxyMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 4, 1)
)
if mibBuilder.loadTexts:
    zyxelMldSnoopingProxyMembershipTable.setStatus("current")
_ZyxelMldSnoopingProxyMembershipEntry_Object = MibTableRow
zyxelMldSnoopingProxyMembershipEntry = _ZyxelMldSnoopingProxyMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 4, 1, 1)
)
zyxelMldSnoopingProxyMembershipEntry.setIndexNames(
    (0, "ZYXEL-MLD-SNOOPING-PROXY-MIB", "zyMldSnoopingProxyMembershipVid"),
    (0, "ZYXEL-MLD-SNOOPING-PROXY-MIB", "zyMldSnoopingProxyMembershipPort"),
    (0, "ZYXEL-MLD-SNOOPING-PROXY-MIB", "zyMldSnoopingProxyMembershipGroupIpAddressType"),
    (0, "ZYXEL-MLD-SNOOPING-PROXY-MIB", "zyMldSnoopingProxyMembershipGroupIpAddress"),
)
if mibBuilder.loadTexts:
    zyxelMldSnoopingProxyMembershipEntry.setStatus("current")


class _ZyMldSnoopingProxyMembershipVid_Type(Integer32):
    """Custom type zyMldSnoopingProxyMembershipVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZyMldSnoopingProxyMembershipVid_Type.__name__ = "Integer32"
_ZyMldSnoopingProxyMembershipVid_Object = MibTableColumn
zyMldSnoopingProxyMembershipVid = _ZyMldSnoopingProxyMembershipVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 4, 1, 1, 1),
    _ZyMldSnoopingProxyMembershipVid_Type()
)
zyMldSnoopingProxyMembershipVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyMembershipVid.setStatus("current")
_ZyMldSnoopingProxyMembershipPort_Type = Integer32
_ZyMldSnoopingProxyMembershipPort_Object = MibTableColumn
zyMldSnoopingProxyMembershipPort = _ZyMldSnoopingProxyMembershipPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 4, 1, 1, 2),
    _ZyMldSnoopingProxyMembershipPort_Type()
)
zyMldSnoopingProxyMembershipPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyMembershipPort.setStatus("current")
_ZyMldSnoopingProxyMembershipGroupIpAddressType_Type = InetAddressType
_ZyMldSnoopingProxyMembershipGroupIpAddressType_Object = MibTableColumn
zyMldSnoopingProxyMembershipGroupIpAddressType = _ZyMldSnoopingProxyMembershipGroupIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 4, 1, 1, 3),
    _ZyMldSnoopingProxyMembershipGroupIpAddressType_Type()
)
zyMldSnoopingProxyMembershipGroupIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyMembershipGroupIpAddressType.setStatus("current")
_ZyMldSnoopingProxyMembershipGroupIpAddress_Type = InetAddress
_ZyMldSnoopingProxyMembershipGroupIpAddress_Object = MibTableColumn
zyMldSnoopingProxyMembershipGroupIpAddress = _ZyMldSnoopingProxyMembershipGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 4, 1, 1, 4),
    _ZyMldSnoopingProxyMembershipGroupIpAddress_Type()
)
zyMldSnoopingProxyMembershipGroupIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyMembershipGroupIpAddress.setStatus("current")
_ZyMldSnoopingProxyMembershipGroupTimeout_Type = Integer32
_ZyMldSnoopingProxyMembershipGroupTimeout_Object = MibTableColumn
zyMldSnoopingProxyMembershipGroupTimeout = _ZyMldSnoopingProxyMembershipGroupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 51, 4, 1, 1, 5),
    _ZyMldSnoopingProxyMembershipGroupTimeout_Type()
)
zyMldSnoopingProxyMembershipGroupTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMldSnoopingProxyMembershipGroupTimeout.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-MLD-SNOOPING-PROXY-MIB",
    **{"zyxelMldSnoopingProxy": zyxelMldSnoopingProxy,
       "zyxelMldSnoopingProxyFilteringSetup": zyxelMldSnoopingProxyFilteringSetup,
       "zyMldSnoopingProxyFilteringMaxNumberOfProfiles": zyMldSnoopingProxyFilteringMaxNumberOfProfiles,
       "zyxelMldSnoopingProxyFilteringProfileTable": zyxelMldSnoopingProxyFilteringProfileTable,
       "zyxelMldSnoopingProxyFilteringProfileEntry": zyxelMldSnoopingProxyFilteringProfileEntry,
       "zyMldSnoopingProxyFilteringProfileName": zyMldSnoopingProxyFilteringProfileName,
       "zyMldSnoopingProxyFilteringProfileStartIpAddressType": zyMldSnoopingProxyFilteringProfileStartIpAddressType,
       "zyMldSnoopingProxyFilteringProfileStartIpAddress": zyMldSnoopingProxyFilteringProfileStartIpAddress,
       "zyMldSnoopingProxyFilteringProfileEndIpAddressType": zyMldSnoopingProxyFilteringProfileEndIpAddressType,
       "zyMldSnoopingProxyFilteringProfileEndIpAddress": zyMldSnoopingProxyFilteringProfileEndIpAddress,
       "zyMldSnoopingProxyFilteringProfileRowStatus": zyMldSnoopingProxyFilteringProfileRowStatus,
       "zyxelMldSnoopingProxyFilteringPortTable": zyxelMldSnoopingProxyFilteringPortTable,
       "zyxelMldSnoopingProxyFilteringPortEntry": zyxelMldSnoopingProxyFilteringPortEntry,
       "zyMldSnoopingProxyFilteringPortProfile": zyMldSnoopingProxyFilteringPortProfile,
       "zyMldSnoopingProxyFilteringPortGroupLimitState": zyMldSnoopingProxyFilteringPortGroupLimitState,
       "zyMldSnoopingProxyFilteringPortMaxNumberOfGroups": zyMldSnoopingProxyFilteringPortMaxNumberOfGroups,
       "zyxelMldSnoopingProxyStatistics": zyxelMldSnoopingProxyStatistics,
       "zyMldSnoopingProxySysStatisticsV1QueryRx": zyMldSnoopingProxySysStatisticsV1QueryRx,
       "zyMldSnoopingProxySysStatisticsV1QueryTx": zyMldSnoopingProxySysStatisticsV1QueryTx,
       "zyMldSnoopingProxySysStatisticsV1QueryDrop": zyMldSnoopingProxySysStatisticsV1QueryDrop,
       "zyMldSnoopingProxySysStatisticsV1ReportRx": zyMldSnoopingProxySysStatisticsV1ReportRx,
       "zyMldSnoopingProxySysStatisticsV1ReportTx": zyMldSnoopingProxySysStatisticsV1ReportTx,
       "zyMldSnoopingProxySysStatisticsV1ReportDrop": zyMldSnoopingProxySysStatisticsV1ReportDrop,
       "zyMldSnoopingProxySysStatisticsV1DoneRx": zyMldSnoopingProxySysStatisticsV1DoneRx,
       "zyMldSnoopingProxySysStatisticsV1DoneTx": zyMldSnoopingProxySysStatisticsV1DoneTx,
       "zyMldSnoopingProxySysStatisticsV1DoneDrop": zyMldSnoopingProxySysStatisticsV1DoneDrop,
       "zyMldSnoopingProxySysStatisticsV2QueryRx": zyMldSnoopingProxySysStatisticsV2QueryRx,
       "zyMldSnoopingProxySysStatisticsV2QueryTx": zyMldSnoopingProxySysStatisticsV2QueryTx,
       "zyMldSnoopingProxySysStatisticsV2QueryDrop": zyMldSnoopingProxySysStatisticsV2QueryDrop,
       "zyMldSnoopingProxySysStatisticsV2ReportRx": zyMldSnoopingProxySysStatisticsV2ReportRx,
       "zyMldSnoopingProxySysStatisticsV2ReportTx": zyMldSnoopingProxySysStatisticsV2ReportTx,
       "zyMldSnoopingProxySysStatisticsV2ReportDrop": zyMldSnoopingProxySysStatisticsV2ReportDrop,
       "zyxelMldSnoopingProxyStatisticsVlanTable": zyxelMldSnoopingProxyStatisticsVlanTable,
       "zyxelMldSnoopingProxyStatisticsVlanEntry": zyxelMldSnoopingProxyStatisticsVlanEntry,
       "zyMldSnoopingProxyStatisticsVlanV1QueryRx": zyMldSnoopingProxyStatisticsVlanV1QueryRx,
       "zyMldSnoopingProxyStatisticsVlanV1QueryTx": zyMldSnoopingProxyStatisticsVlanV1QueryTx,
       "zyMldSnoopingProxyStatisticsVlanV1QueryDrop": zyMldSnoopingProxyStatisticsVlanV1QueryDrop,
       "zyMldSnoopingProxyStatisticsVlanV1ReportRx": zyMldSnoopingProxyStatisticsVlanV1ReportRx,
       "zyMldSnoopingProxyStatisticsVlanV1ReportTx": zyMldSnoopingProxyStatisticsVlanV1ReportTx,
       "zyMldSnoopingProxyStatisticsVlanV1ReportDrop": zyMldSnoopingProxyStatisticsVlanV1ReportDrop,
       "zyMldSnoopingProxyStatisticsVlanV1DoneRx": zyMldSnoopingProxyStatisticsVlanV1DoneRx,
       "zyMldSnoopingProxyStatisticsVlanV1DoneTx": zyMldSnoopingProxyStatisticsVlanV1DoneTx,
       "zyMldSnoopingProxyStatisticsVlanV1DoneDrop": zyMldSnoopingProxyStatisticsVlanV1DoneDrop,
       "zyMldSnoopingProxyStatisticsVlanV2QueryRx": zyMldSnoopingProxyStatisticsVlanV2QueryRx,
       "zyMldSnoopingProxyStatisticsVlanV2QueryTx": zyMldSnoopingProxyStatisticsVlanV2QueryTx,
       "zyMldSnoopingProxyStatisticsVlanV2QueryDrop": zyMldSnoopingProxyStatisticsVlanV2QueryDrop,
       "zyMldSnoopingProxyStatisticsVlanV2ReportRx": zyMldSnoopingProxyStatisticsVlanV2ReportRx,
       "zyMldSnoopingProxyStatisticsVlanV2ReportTx": zyMldSnoopingProxyStatisticsVlanV2ReportTx,
       "zyMldSnoopingProxyStatisticsVlanV2ReportDrop": zyMldSnoopingProxyStatisticsVlanV2ReportDrop,
       "zyxelMldSnoopingProxyStatisticsPortTable": zyxelMldSnoopingProxyStatisticsPortTable,
       "zyxelMldSnoopingProxyStatisticsPortEntry": zyxelMldSnoopingProxyStatisticsPortEntry,
       "zyMldSnoopingProxyStatisticsPortV1QueryRx": zyMldSnoopingProxyStatisticsPortV1QueryRx,
       "zyMldSnoopingProxyStatisticsPortV1QueryTx": zyMldSnoopingProxyStatisticsPortV1QueryTx,
       "zyMldSnoopingProxyStatisticsPortV1QueryDrop": zyMldSnoopingProxyStatisticsPortV1QueryDrop,
       "zyMldSnoopingProxyStatisticsPortV1ReportRx": zyMldSnoopingProxyStatisticsPortV1ReportRx,
       "zyMldSnoopingProxyStatisticsPortV1ReportTx": zyMldSnoopingProxyStatisticsPortV1ReportTx,
       "zyMldSnoopingProxyStatisticsPortV1ReportDrop": zyMldSnoopingProxyStatisticsPortV1ReportDrop,
       "zyMldSnoopingProxyStatisticsPortV1DoneRx": zyMldSnoopingProxyStatisticsPortV1DoneRx,
       "zyMldSnoopingProxyStatisticsPortV1DoneTx": zyMldSnoopingProxyStatisticsPortV1DoneTx,
       "zyMldSnoopingProxyStatisticsPortV1DoneDrop": zyMldSnoopingProxyStatisticsPortV1DoneDrop,
       "zyMldSnoopingProxyStatisticsPortV2QueryRx": zyMldSnoopingProxyStatisticsPortV2QueryRx,
       "zyMldSnoopingProxyStatisticsPortV2QueryTx": zyMldSnoopingProxyStatisticsPortV2QueryTx,
       "zyMldSnoopingProxyStatisticsPortV2QueryDrop": zyMldSnoopingProxyStatisticsPortV2QueryDrop,
       "zyMldSnoopingProxyStatisticsPortV2ReportRx": zyMldSnoopingProxyStatisticsPortV2ReportRx,
       "zyMldSnoopingProxyStatisticsPortV2ReportTx": zyMldSnoopingProxyStatisticsPortV2ReportTx,
       "zyMldSnoopingProxyStatisticsPortV2ReportDrop": zyMldSnoopingProxyStatisticsPortV2ReportDrop,
       "zyMldSnoopingProxyStatisticsClear": zyMldSnoopingProxyStatisticsClear,
       "zyMldSnoopingProxyStatisticsClearSystem": zyMldSnoopingProxyStatisticsClearSystem,
       "zyMldSnoopingProxyStatisticsClearPort": zyMldSnoopingProxyStatisticsClearPort,
       "zyMldSnoopingProxyStatisticsClearVlan": zyMldSnoopingProxyStatisticsClearVlan,
       "zyxelMldSnoopingProxySetup": zyxelMldSnoopingProxySetup,
       "zyMldSnoopingProxyState": zyMldSnoopingProxyState,
       "zyMldSnoopingProxyFilteringState": zyMldSnoopingProxyFilteringState,
       "zyMldSnoopingProxy8021pPriority": zyMldSnoopingProxy8021pPriority,
       "zyMldSnoopingProxyMaxNumberOfVlans": zyMldSnoopingProxyMaxNumberOfVlans,
       "zyxelMldSnoopingProxyVlanTable": zyxelMldSnoopingProxyVlanTable,
       "zyxelMldSnoopingProxyVlanEntry": zyxelMldSnoopingProxyVlanEntry,
       "zyMldSnoopingProxyVlanVid": zyMldSnoopingProxyVlanVid,
       "zyMldSnoopingProxyVlanRowStatus": zyMldSnoopingProxyVlanRowStatus,
       "zyxelMldSnoopingProxyUpstreamVlanTable": zyxelMldSnoopingProxyUpstreamVlanTable,
       "zyxelMldSnoopingProxyUpstreamVlanEntry": zyxelMldSnoopingProxyUpstreamVlanEntry,
       "zyMldSnoopingProxyUpstreamVlanPorts": zyMldSnoopingProxyUpstreamVlanPorts,
       "zyMldSnoopingProxyUpstreamVlanQueryInterval": zyMldSnoopingProxyUpstreamVlanQueryInterval,
       "zyMldSnoopingProxyUpstreamVlanMaxResponseTime": zyMldSnoopingProxyUpstreamVlanMaxResponseTime,
       "zyMldSnoopingProxyUpstreamVlanRobustness": zyMldSnoopingProxyUpstreamVlanRobustness,
       "zyMldSnoopingProxyUpstreamVlanLastMemberQueryInterval": zyMldSnoopingProxyUpstreamVlanLastMemberQueryInterval,
       "zyxelMldSnoopingProxyDownstreamVlanTable": zyxelMldSnoopingProxyDownstreamVlanTable,
       "zyxelMldSnoopingProxyDownstreamVlanEntry": zyxelMldSnoopingProxyDownstreamVlanEntry,
       "zyMldSnoopingProxyDownstreamVlanPorts": zyMldSnoopingProxyDownstreamVlanPorts,
       "zyMldSnoopingProxyDownstreamVlanQueryInterval": zyMldSnoopingProxyDownstreamVlanQueryInterval,
       "zyMldSnoopingProxyDownstreamVlanMaxResponseTime": zyMldSnoopingProxyDownstreamVlanMaxResponseTime,
       "zyxelMldSnoopingProxyDownstreamVlanPortTable": zyxelMldSnoopingProxyDownstreamVlanPortTable,
       "zyxelMldSnoopingProxyDownstreamVlanPortEntry": zyxelMldSnoopingProxyDownstreamVlanPortEntry,
       "zyMldSnoopingProxyDownstreamVlanPortIndex": zyMldSnoopingProxyDownstreamVlanPortIndex,
       "zyMldSnoopingProxyDownstreamVlanPortLeaveMode": zyMldSnoopingProxyDownstreamVlanPortLeaveMode,
       "zyMldSnoopingProxyDownstreamVlanPortLeaveTimeout": zyMldSnoopingProxyDownstreamVlanPortLeaveTimeout,
       "zyMldSnoopingProxyDownstreamVlanPortFastLeaveTimeout": zyMldSnoopingProxyDownstreamVlanPortFastLeaveTimeout,
       "zyxelMldSnoopingProxyMembershipStatus": zyxelMldSnoopingProxyMembershipStatus,
       "zyxelMldSnoopingProxyMembershipTable": zyxelMldSnoopingProxyMembershipTable,
       "zyxelMldSnoopingProxyMembershipEntry": zyxelMldSnoopingProxyMembershipEntry,
       "zyMldSnoopingProxyMembershipVid": zyMldSnoopingProxyMembershipVid,
       "zyMldSnoopingProxyMembershipPort": zyMldSnoopingProxyMembershipPort,
       "zyMldSnoopingProxyMembershipGroupIpAddressType": zyMldSnoopingProxyMembershipGroupIpAddressType,
       "zyMldSnoopingProxyMembershipGroupIpAddress": zyMldSnoopingProxyMembershipGroupIpAddress,
       "zyMldSnoopingProxyMembershipGroupTimeout": zyMldSnoopingProxyMembershipGroupTimeout}
)
