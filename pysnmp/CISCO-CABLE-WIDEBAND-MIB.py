# SNMP MIB module (CISCO-CABLE-WIDEBAND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CABLE-WIDEBAND-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:42 2024
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

(docsIfCmtsCmStatusIndex,) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "docsIfCmtsCmStatusIndex")

(PhysicalIndexOrZero,
 entPhysicalIndex,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndexOrZero",
    "entPhysicalIndex",
    "entPhysicalName")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoCableWidebandMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 479)
)
ciscoCableWidebandMIB.setRevisions(
        ("2011-01-05 00:00",
         "2010-07-15 00:00",
         "2008-12-03 00:00",
         "2006-06-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCableWidebandMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCableWidebandMIBNotifs = _CiscoCableWidebandMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 0)
)
_CiscoCableWidebandMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCableWidebandMIBObjects = _CiscoCableWidebandMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1)
)
_CcwbRFChannelTable_Object = MibTable
ccwbRFChannelTable = _CcwbRFChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 1)
)
if mibBuilder.loadTexts:
    ccwbRFChannelTable.setStatus("current")
_CcwbRFChannelEntry_Object = MibTableRow
ccwbRFChannelEntry = _CcwbRFChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 1, 1)
)
ccwbRFChannelEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChannelNum"),
)
if mibBuilder.loadTexts:
    ccwbRFChannelEntry.setStatus("current")


class _CcwbRFChannelNum_Type(Unsigned32):
    """Custom type ccwbRFChannelNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CcwbRFChannelNum_Type.__name__ = "Unsigned32"
_CcwbRFChannelNum_Object = MibTableColumn
ccwbRFChannelNum = _CcwbRFChannelNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 1, 1, 1),
    _CcwbRFChannelNum_Type()
)
ccwbRFChannelNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccwbRFChannelNum.setStatus("current")


class _CcwbRFChannelFrequency_Type(Unsigned32):
    """Custom type ccwbRFChannelFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )


_CcwbRFChannelFrequency_Type.__name__ = "Unsigned32"
_CcwbRFChannelFrequency_Object = MibTableColumn
ccwbRFChannelFrequency = _CcwbRFChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 1, 1, 2),
    _CcwbRFChannelFrequency_Type()
)
ccwbRFChannelFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbRFChannelFrequency.setStatus("deprecated")
if mibBuilder.loadTexts:
    ccwbRFChannelFrequency.setUnits("hertz")


class _CcwbRFChannelWidth_Type(Unsigned32):
    """Custom type ccwbRFChannelWidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16000000),
    )


_CcwbRFChannelWidth_Type.__name__ = "Unsigned32"
_CcwbRFChannelWidth_Object = MibTableColumn
ccwbRFChannelWidth = _CcwbRFChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 1, 1, 3),
    _CcwbRFChannelWidth_Type()
)
ccwbRFChannelWidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbRFChannelWidth.setStatus("current")
if mibBuilder.loadTexts:
    ccwbRFChannelWidth.setUnits("hertz")


class _CcwbRFChannelModulation_Type(Integer32):
    """Custom type ccwbRFChannelModulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("qam1024", 3),
          ("qam256", 2),
          ("qam64", 1))
    )


_CcwbRFChannelModulation_Type.__name__ = "Integer32"
_CcwbRFChannelModulation_Object = MibTableColumn
ccwbRFChannelModulation = _CcwbRFChannelModulation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 1, 1, 4),
    _CcwbRFChannelModulation_Type()
)
ccwbRFChannelModulation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbRFChannelModulation.setStatus("current")


class _CcwbRFChannelAnnex_Type(Integer32):
    """Custom type ccwbRFChannelAnnex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("annexA", 1),
          ("annexB", 2),
          ("annexC", 3))
    )


_CcwbRFChannelAnnex_Type.__name__ = "Integer32"
_CcwbRFChannelAnnex_Object = MibTableColumn
ccwbRFChannelAnnex = _CcwbRFChannelAnnex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 1, 1, 5),
    _CcwbRFChannelAnnex_Type()
)
ccwbRFChannelAnnex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbRFChannelAnnex.setStatus("current")
_CcwbRFChannelMpegPkts_Type = Counter64
_CcwbRFChannelMpegPkts_Object = MibTableColumn
ccwbRFChannelMpegPkts = _CcwbRFChannelMpegPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 1, 1, 6),
    _CcwbRFChannelMpegPkts_Type()
)
ccwbRFChannelMpegPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccwbRFChannelMpegPkts.setStatus("current")
if mibBuilder.loadTexts:
    ccwbRFChannelMpegPkts.setUnits("Packets")


class _CcwbRFChannelStorageType_Type(StorageType):
    """Custom type ccwbRFChannelStorageType based on StorageType"""


_CcwbRFChannelStorageType_Object = MibTableColumn
ccwbRFChannelStorageType = _CcwbRFChannelStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 1, 1, 7),
    _CcwbRFChannelStorageType_Type()
)
ccwbRFChannelStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbRFChannelStorageType.setStatus("current")
_CcwbRFChannelRowStatus_Type = RowStatus
_CcwbRFChannelRowStatus_Object = MibTableColumn
ccwbRFChannelRowStatus = _CcwbRFChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 1, 1, 8),
    _CcwbRFChannelRowStatus_Type()
)
ccwbRFChannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbRFChannelRowStatus.setStatus("current")


class _CcwbRFChannelUtilization_Type(Unsigned32):
    """Custom type ccwbRFChannelUtilization based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CcwbRFChannelUtilization_Type.__name__ = "Unsigned32"
_CcwbRFChannelUtilization_Object = MibTableColumn
ccwbRFChannelUtilization = _CcwbRFChannelUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 1, 1, 9),
    _CcwbRFChannelUtilization_Type()
)
ccwbRFChannelUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccwbRFChannelUtilization.setStatus("current")
if mibBuilder.loadTexts:
    ccwbRFChannelUtilization.setUnits("percent")


class _CcwbRFChannelFrequencyRev1_Type(Unsigned32):
    """Custom type ccwbRFChannelFrequencyRev1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(55000000, 1050000000),
    )


_CcwbRFChannelFrequencyRev1_Type.__name__ = "Unsigned32"
_CcwbRFChannelFrequencyRev1_Object = MibTableColumn
ccwbRFChannelFrequencyRev1 = _CcwbRFChannelFrequencyRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 1, 1, 10),
    _CcwbRFChannelFrequencyRev1_Type()
)
ccwbRFChannelFrequencyRev1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbRFChannelFrequencyRev1.setStatus("current")
if mibBuilder.loadTexts:
    ccwbRFChannelFrequencyRev1.setUnits("hertz")
_CcwbRFChannelQamTable_Object = MibTable
ccwbRFChannelQamTable = _CcwbRFChannelQamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 2)
)
if mibBuilder.loadTexts:
    ccwbRFChannelQamTable.setStatus("current")
_CcwbRFChannelQamEntry_Object = MibTableRow
ccwbRFChannelQamEntry = _CcwbRFChannelQamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ccwbRFChannelQamEntry.setStatus("current")


class _CcwbRFChanQamIPAddressType_Type(InetAddressType):
    """Custom type ccwbRFChanQamIPAddressType based on InetAddressType"""


_CcwbRFChanQamIPAddressType_Object = MibTableColumn
ccwbRFChanQamIPAddressType = _CcwbRFChanQamIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 2, 1, 1),
    _CcwbRFChanQamIPAddressType_Type()
)
ccwbRFChanQamIPAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbRFChanQamIPAddressType.setStatus("current")
_CcwbRFChanQamIPAddress_Type = InetAddress
_CcwbRFChanQamIPAddress_Object = MibTableColumn
ccwbRFChanQamIPAddress = _CcwbRFChanQamIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 2, 1, 2),
    _CcwbRFChanQamIPAddress_Type()
)
ccwbRFChanQamIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbRFChanQamIPAddress.setStatus("current")
_CcwbRFChanQamMacAddress_Type = MacAddress
_CcwbRFChanQamMacAddress_Object = MibTableColumn
ccwbRFChanQamMacAddress = _CcwbRFChanQamMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 2, 1, 3),
    _CcwbRFChanQamMacAddress_Type()
)
ccwbRFChanQamMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbRFChanQamMacAddress.setStatus("current")
_CcwbRFChanQamUdpPort_Type = InetPortNumber
_CcwbRFChanQamUdpPort_Object = MibTableColumn
ccwbRFChanQamUdpPort = _CcwbRFChanQamUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 2, 1, 4),
    _CcwbRFChanQamUdpPort_Type()
)
ccwbRFChanQamUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbRFChanQamUdpPort.setStatus("current")


class _CcwbRFChanQamTos_Type(Unsigned32):
    """Custom type ccwbRFChanQamTos based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CcwbRFChanQamTos_Type.__name__ = "Unsigned32"
_CcwbRFChanQamTos_Object = MibTableColumn
ccwbRFChanQamTos = _CcwbRFChanQamTos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 2, 1, 5),
    _CcwbRFChanQamTos_Type()
)
ccwbRFChanQamTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbRFChanQamTos.setStatus("current")


class _CcwbRFChanQamVlanId_Type(Unsigned32):
    """Custom type ccwbRFChanQamVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_CcwbRFChanQamVlanId_Type.__name__ = "Unsigned32"
_CcwbRFChanQamVlanId_Object = MibTableColumn
ccwbRFChanQamVlanId = _CcwbRFChanQamVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 2, 1, 6),
    _CcwbRFChanQamVlanId_Type()
)
ccwbRFChanQamVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbRFChanQamVlanId.setStatus("current")


class _CcwbRFChanQamPriorityBits_Type(Unsigned32):
    """Custom type ccwbRFChanQamPriorityBits based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CcwbRFChanQamPriorityBits_Type.__name__ = "Unsigned32"
_CcwbRFChanQamPriorityBits_Object = MibTableColumn
ccwbRFChanQamPriorityBits = _CcwbRFChanQamPriorityBits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 2, 1, 7),
    _CcwbRFChanQamPriorityBits_Type()
)
ccwbRFChanQamPriorityBits.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbRFChanQamPriorityBits.setStatus("current")


class _CcwbRFChanQamDepiRemoteId_Type(Unsigned32):
    """Custom type ccwbRFChanQamDepiRemoteId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CcwbRFChanQamDepiRemoteId_Type.__name__ = "Unsigned32"
_CcwbRFChanQamDepiRemoteId_Object = MibTableColumn
ccwbRFChanQamDepiRemoteId = _CcwbRFChanQamDepiRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 2, 1, 8),
    _CcwbRFChanQamDepiRemoteId_Type()
)
ccwbRFChanQamDepiRemoteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbRFChanQamDepiRemoteId.setStatus("current")


class _CcwbRFChanQamDepiTunnel_Type(SnmpAdminString):
    """Custom type ccwbRFChanQamDepiTunnel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CcwbRFChanQamDepiTunnel_Type.__name__ = "SnmpAdminString"
_CcwbRFChanQamDepiTunnel_Object = MibTableColumn
ccwbRFChanQamDepiTunnel = _CcwbRFChanQamDepiTunnel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 2, 1, 9),
    _CcwbRFChanQamDepiTunnel_Type()
)
ccwbRFChanQamDepiTunnel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbRFChanQamDepiTunnel.setStatus("current")


class _CcwbRFChanQamTsid_Type(Unsigned32):
    """Custom type ccwbRFChanQamTsid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CcwbRFChanQamTsid_Type.__name__ = "Unsigned32"
_CcwbRFChanQamTsid_Object = MibTableColumn
ccwbRFChanQamTsid = _CcwbRFChanQamTsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 2, 1, 10),
    _CcwbRFChanQamTsid_Type()
)
ccwbRFChanQamTsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbRFChanQamTsid.setStatus("current")
_CcwbWBtoRFMappingTable_Object = MibTable
ccwbWBtoRFMappingTable = _CcwbWBtoRFMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 3)
)
if mibBuilder.loadTexts:
    ccwbWBtoRFMappingTable.setStatus("current")
_CcwbWBtoRFMappingEntry_Object = MibTableRow
ccwbWBtoRFMappingEntry = _CcwbWBtoRFMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 3, 1)
)
ccwbWBtoRFMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChannelNum"),
)
if mibBuilder.loadTexts:
    ccwbWBtoRFMappingEntry.setStatus("current")


class _CcwbWBtoRFBandwidth_Type(Gauge32):
    """Custom type ccwbWBtoRFBandwidth based on Gauge32"""
    defaultValue = 100

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CcwbWBtoRFBandwidth_Type.__name__ = "Gauge32"
_CcwbWBtoRFBandwidth_Object = MibTableColumn
ccwbWBtoRFBandwidth = _CcwbWBtoRFBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 3, 1, 1),
    _CcwbWBtoRFBandwidth_Type()
)
ccwbWBtoRFBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbWBtoRFBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    ccwbWBtoRFBandwidth.setUnits("percent")


class _CcwbWBtoRFStorageType_Type(StorageType):
    """Custom type ccwbWBtoRFStorageType based on StorageType"""


_CcwbWBtoRFStorageType_Object = MibTableColumn
ccwbWBtoRFStorageType = _CcwbWBtoRFStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 3, 1, 2),
    _CcwbWBtoRFStorageType_Type()
)
ccwbWBtoRFStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbWBtoRFStorageType.setStatus("current")
_CcwbWBtoRFRowStatus_Type = RowStatus
_CcwbWBtoRFRowStatus_Object = MibTableColumn
ccwbWBtoRFRowStatus = _CcwbWBtoRFRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 3, 1, 3),
    _CcwbWBtoRFRowStatus_Type()
)
ccwbWBtoRFRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbWBtoRFRowStatus.setStatus("current")
_CcwbWBtoNBMappingTable_Object = MibTable
ccwbWBtoNBMappingTable = _CcwbWBtoNBMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 4)
)
if mibBuilder.loadTexts:
    ccwbWBtoNBMappingTable.setStatus("current")
_CcwbWBtoNBMappingEntry_Object = MibTableRow
ccwbWBtoNBMappingEntry = _CcwbWBtoNBMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 4, 1)
)
ccwbWBtoNBMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-CABLE-WIDEBAND-MIB", "ccwbWBtoNBifIndexForNB"),
)
if mibBuilder.loadTexts:
    ccwbWBtoNBMappingEntry.setStatus("current")
_CcwbWBtoNBifIndexForNB_Type = InterfaceIndex
_CcwbWBtoNBifIndexForNB_Object = MibTableColumn
ccwbWBtoNBifIndexForNB = _CcwbWBtoNBifIndexForNB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 4, 1, 1),
    _CcwbWBtoNBifIndexForNB_Type()
)
ccwbWBtoNBifIndexForNB.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccwbWBtoNBifIndexForNB.setStatus("current")


class _CcwbWBtoNBStorageType_Type(StorageType):
    """Custom type ccwbWBtoNBStorageType based on StorageType"""


_CcwbWBtoNBStorageType_Object = MibTableColumn
ccwbWBtoNBStorageType = _CcwbWBtoNBStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 4, 1, 2),
    _CcwbWBtoNBStorageType_Type()
)
ccwbWBtoNBStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbWBtoNBStorageType.setStatus("current")
_CcwbWBtoNBRowStatus_Type = RowStatus
_CcwbWBtoNBRowStatus_Object = MibTableColumn
ccwbWBtoNBRowStatus = _CcwbWBtoNBRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 4, 1, 3),
    _CcwbWBtoNBRowStatus_Type()
)
ccwbWBtoNBRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbWBtoNBRowStatus.setStatus("current")
_CcwbWBBondGrpTable_Object = MibTable
ccwbWBBondGrpTable = _CcwbWBBondGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 5)
)
if mibBuilder.loadTexts:
    ccwbWBBondGrpTable.setStatus("current")
_CcwbWBBondGrpEntry_Object = MibTableRow
ccwbWBBondGrpEntry = _CcwbWBBondGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 5, 1)
)
ccwbWBBondGrpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ccwbWBBondGrpEntry.setStatus("current")
_CcwbWBBondGrpSecondary_Type = TruthValue
_CcwbWBBondGrpSecondary_Object = MibTableColumn
ccwbWBBondGrpSecondary = _CcwbWBBondGrpSecondary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 5, 1, 1),
    _CcwbWBBondGrpSecondary_Type()
)
ccwbWBBondGrpSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccwbWBBondGrpSecondary.setStatus("current")
_CcwbWBCmStatusTable_Object = MibTable
ccwbWBCmStatusTable = _CcwbWBCmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 6)
)
if mibBuilder.loadTexts:
    ccwbWBCmStatusTable.setStatus("current")
_CcwbWBCmStatusEntry_Object = MibTableRow
ccwbWBCmStatusEntry = _CcwbWBCmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 6, 1)
)
ccwbWBCmStatusEntry.setIndexNames(
    (0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"),
)
if mibBuilder.loadTexts:
    ccwbWBCmStatusEntry.setStatus("current")


class _CcwbWBCmStatusValue_Type(Integer32):
    """Custom type ccwbWBCmStatusValue based on Integer32"""
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
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39)
        )
    )
    namedValues = NamedValues(
        *(("bpiKekExpired", 22),
          ("bpiTekExpired", 23),
          ("channelChgInitRangingRcvd", 25),
          ("channelChgRangingInProgress", 26),
          ("dhcpGotIpAddr", 17),
          ("initDhcpReqRcvd", 4),
          ("initRangingRcvd", 3),
          ("initTftpPacketRcvd", 13),
          ("initTodRequestRcvd", 14),
          ("kekRejected", 10),
          ("offline", 1),
          ("online", 12),
          ("onlineKekAssigned", 6),
          ("onlineNetAccessDisabled", 5),
          ("onlineTekAssigned", 7),
          ("others", 2),
          ("rangingInProgress", 16),
          ("rejClassFail", 20),
          ("rejIpSpoof", 19),
          ("rejRegNack", 21),
          ("rejStaleConfig", 18),
          ("rejectBadCos", 9),
          ("rejectBadMic", 8),
          ("reset", 15),
          ("shutdown", 24),
          ("tekRejected", 11),
          ("wbKekExpire", 36),
          ("wbKekReject", 32),
          ("wbNetAccessDisExpire", 38),
          ("wbNetAccessDisReject", 34),
          ("wbOnline", 27),
          ("wbOnlineKekAssigned", 29),
          ("wbOnlineNetAccessDis", 31),
          ("wbOnlinePrivacy", 28),
          ("wbOnlineTekAssigned", 30),
          ("wbPrivacyEnabExpire", 39),
          ("wbPrivacyEnabReject", 35),
          ("wbTekExpire", 37),
          ("wbTekReject", 33))
    )


_CcwbWBCmStatusValue_Type.__name__ = "Integer32"
_CcwbWBCmStatusValue_Object = MibTableColumn
ccwbWBCmStatusValue = _CcwbWBCmStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 6, 1, 1),
    _CcwbWBCmStatusValue_Type()
)
ccwbWBCmStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccwbWBCmStatusValue.setStatus("current")
_CcwbWBCmStatusExtTable_Object = MibTable
ccwbWBCmStatusExtTable = _CcwbWBCmStatusExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 7)
)
if mibBuilder.loadTexts:
    ccwbWBCmStatusExtTable.setStatus("current")
_CcwbWBCmStatusExtEntry_Object = MibTableRow
ccwbWBCmStatusExtEntry = _CcwbWBCmStatusExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 7, 1)
)
ccwbWBCmStatusExtEntry.setIndexNames(
    (0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"),
    (0, "CISCO-CABLE-WIDEBAND-MIB", "ccwbWBCmStatusExtIndex"),
)
if mibBuilder.loadTexts:
    ccwbWBCmStatusExtEntry.setStatus("current")


class _CcwbWBCmStatusExtIndex_Type(Integer32):
    """Custom type ccwbWBCmStatusExtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CcwbWBCmStatusExtIndex_Type.__name__ = "Integer32"
_CcwbWBCmStatusExtIndex_Object = MibTableColumn
ccwbWBCmStatusExtIndex = _CcwbWBCmStatusExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 7, 1, 1),
    _CcwbWBCmStatusExtIndex_Type()
)
ccwbWBCmStatusExtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccwbWBCmStatusExtIndex.setStatus("current")
_CcwbWBCmWBIfindex_Type = InterfaceIndex
_CcwbWBCmWBIfindex_Object = MibTableColumn
ccwbWBCmWBIfindex = _CcwbWBCmWBIfindex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 7, 1, 2),
    _CcwbWBCmWBIfindex_Type()
)
ccwbWBCmWBIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccwbWBCmWBIfindex.setStatus("current")
_CcwbFiberNodeDescrTable_Object = MibTable
ccwbFiberNodeDescrTable = _CcwbFiberNodeDescrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 8)
)
if mibBuilder.loadTexts:
    ccwbFiberNodeDescrTable.setStatus("current")
_CcwbFiberNodeDescrEntry_Object = MibTableRow
ccwbFiberNodeDescrEntry = _CcwbFiberNodeDescrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 8, 1)
)
ccwbFiberNodeDescrEntry.setIndexNames(
    (0, "CISCO-CABLE-WIDEBAND-MIB", "ccwbFiberNodeID"),
)
if mibBuilder.loadTexts:
    ccwbFiberNodeDescrEntry.setStatus("current")


class _CcwbFiberNodeDescription_Type(SnmpAdminString):
    """Custom type ccwbFiberNodeDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CcwbFiberNodeDescription_Type.__name__ = "SnmpAdminString"
_CcwbFiberNodeDescription_Object = MibTableColumn
ccwbFiberNodeDescription = _CcwbFiberNodeDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 8, 1, 1),
    _CcwbFiberNodeDescription_Type()
)
ccwbFiberNodeDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbFiberNodeDescription.setStatus("current")


class _CcwbFiberNodeDescrStorageType_Type(StorageType):
    """Custom type ccwbFiberNodeDescrStorageType based on StorageType"""


_CcwbFiberNodeDescrStorageType_Object = MibTableColumn
ccwbFiberNodeDescrStorageType = _CcwbFiberNodeDescrStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 8, 1, 2),
    _CcwbFiberNodeDescrStorageType_Type()
)
ccwbFiberNodeDescrStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbFiberNodeDescrStorageType.setStatus("current")
_CcwbFiberNodeDescrRowStatus_Type = RowStatus
_CcwbFiberNodeDescrRowStatus_Object = MibTableColumn
ccwbFiberNodeDescrRowStatus = _CcwbFiberNodeDescrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 8, 1, 3),
    _CcwbFiberNodeDescrRowStatus_Type()
)
ccwbFiberNodeDescrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbFiberNodeDescrRowStatus.setStatus("current")
_CcwbFiberNodeTable_Object = MibTable
ccwbFiberNodeTable = _CcwbFiberNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 9)
)
if mibBuilder.loadTexts:
    ccwbFiberNodeTable.setStatus("current")
_CcwbFiberNodeEntry_Object = MibTableRow
ccwbFiberNodeEntry = _CcwbFiberNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 9, 1)
)
ccwbFiberNodeEntry.setIndexNames(
    (0, "CISCO-CABLE-WIDEBAND-MIB", "ccwbFiberNodeID"),
    (0, "CISCO-CABLE-WIDEBAND-MIB", "ccwbFiberNodeGlobRFID"),
)
if mibBuilder.loadTexts:
    ccwbFiberNodeEntry.setStatus("current")


class _CcwbFiberNodeID_Type(Unsigned32):
    """Custom type ccwbFiberNodeID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CcwbFiberNodeID_Type.__name__ = "Unsigned32"
_CcwbFiberNodeID_Object = MibTableColumn
ccwbFiberNodeID = _CcwbFiberNodeID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 9, 1, 1),
    _CcwbFiberNodeID_Type()
)
ccwbFiberNodeID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccwbFiberNodeID.setStatus("current")


class _CcwbFiberNodeGlobRFID_Type(Unsigned32):
    """Custom type ccwbFiberNodeGlobRFID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CcwbFiberNodeGlobRFID_Type.__name__ = "Unsigned32"
_CcwbFiberNodeGlobRFID_Object = MibTableColumn
ccwbFiberNodeGlobRFID = _CcwbFiberNodeGlobRFID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 9, 1, 2),
    _CcwbFiberNodeGlobRFID_Type()
)
ccwbFiberNodeGlobRFID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccwbFiberNodeGlobRFID.setStatus("current")


class _CcwbFiberNodeNBIfIndx_Type(InterfaceIndexOrZero):
    """Custom type ccwbFiberNodeNBIfIndx based on InterfaceIndexOrZero"""
    defaultValue = 0


_CcwbFiberNodeNBIfIndx_Object = MibTableColumn
ccwbFiberNodeNBIfIndx = _CcwbFiberNodeNBIfIndx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 9, 1, 3),
    _CcwbFiberNodeNBIfIndx_Type()
)
ccwbFiberNodeNBIfIndx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbFiberNodeNBIfIndx.setStatus("current")


class _CcwbFiberNodeWBContlrPhyIndx_Type(PhysicalIndexOrZero):
    """Custom type ccwbFiberNodeWBContlrPhyIndx based on PhysicalIndexOrZero"""
    defaultValue = 0


_CcwbFiberNodeWBContlrPhyIndx_Object = MibTableColumn
ccwbFiberNodeWBContlrPhyIndx = _CcwbFiberNodeWBContlrPhyIndx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 9, 1, 4),
    _CcwbFiberNodeWBContlrPhyIndx_Type()
)
ccwbFiberNodeWBContlrPhyIndx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbFiberNodeWBContlrPhyIndx.setStatus("current")


class _CcwbFiberNodeWBRFPort_Type(Integer32):
    """Custom type ccwbFiberNodeWBRFPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CcwbFiberNodeWBRFPort_Type.__name__ = "Integer32"
_CcwbFiberNodeWBRFPort_Object = MibTableColumn
ccwbFiberNodeWBRFPort = _CcwbFiberNodeWBRFPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 9, 1, 5),
    _CcwbFiberNodeWBRFPort_Type()
)
ccwbFiberNodeWBRFPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbFiberNodeWBRFPort.setStatus("current")


class _CcwbFiberNodeStorageType_Type(StorageType):
    """Custom type ccwbFiberNodeStorageType based on StorageType"""


_CcwbFiberNodeStorageType_Object = MibTableColumn
ccwbFiberNodeStorageType = _CcwbFiberNodeStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 9, 1, 6),
    _CcwbFiberNodeStorageType_Type()
)
ccwbFiberNodeStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbFiberNodeStorageType.setStatus("current")
_CcwbFiberNodeRowStatus_Type = RowStatus
_CcwbFiberNodeRowStatus_Object = MibTableColumn
ccwbFiberNodeRowStatus = _CcwbFiberNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 9, 1, 7),
    _CcwbFiberNodeRowStatus_Type()
)
ccwbFiberNodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ccwbFiberNodeRowStatus.setStatus("current")


class _CcwbRFChanUtilInterval_Type(Unsigned32):
    """Custom type ccwbRFChanUtilInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_CcwbRFChanUtilInterval_Type.__name__ = "Unsigned32"
_CcwbRFChanUtilInterval_Object = MibScalar
ccwbRFChanUtilInterval = _CcwbRFChanUtilInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 10),
    _CcwbRFChanUtilInterval_Type()
)
ccwbRFChanUtilInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccwbRFChanUtilInterval.setStatus("current")
if mibBuilder.loadTexts:
    ccwbRFChanUtilInterval.setUnits("seconds")
_CcwbSFPLinkTrapEnable_Type = TruthValue
_CcwbSFPLinkTrapEnable_Object = MibScalar
ccwbSFPLinkTrapEnable = _CcwbSFPLinkTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 1, 11),
    _CcwbSFPLinkTrapEnable_Type()
)
ccwbSFPLinkTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ccwbSFPLinkTrapEnable.setStatus("current")
_CiscoCableWidebandMIBConform_ObjectIdentity = ObjectIdentity
ciscoCableWidebandMIBConform = _CiscoCableWidebandMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 2)
)
_CiscoCableWidebandMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCableWidebandMIBCompliances = _CiscoCableWidebandMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 2, 1)
)
_CiscoCableWidebandMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCableWidebandMIBGroups = _CiscoCableWidebandMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 2, 2)
)
ccwbRFChannelEntry.registerAugmentions(
    ("CISCO-CABLE-WIDEBAND-MIB",
     "ccwbRFChannelQamEntry")
)
ccwbRFChannelQamEntry.setIndexNames(*ccwbRFChannelEntry.getIndexNames())

# Managed Objects groups

ccwbWidebandObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 2, 2, 1)
)
ccwbWidebandObjGroup.setObjects(
      *(("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChannelFrequency"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChannelWidth"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChannelModulation"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChannelAnnex"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChannelStorageType"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChannelRowStatus"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChannelMpegPkts"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChanQamIPAddressType"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChanQamIPAddress"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChanQamMacAddress"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChanQamUdpPort"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChanQamTos"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChanQamVlanId"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChanQamPriorityBits"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbWBtoRFBandwidth"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbWBtoRFStorageType"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbWBtoRFRowStatus"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbWBtoNBStorageType"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbWBtoNBRowStatus"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbWBBondGrpSecondary"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbWBCmStatusValue"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbWBCmWBIfindex"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbFiberNodeDescription"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbFiberNodeDescrStorageType"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbFiberNodeDescrRowStatus"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbFiberNodeNBIfIndx"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbFiberNodeWBContlrPhyIndx"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbFiberNodeWBRFPort"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbFiberNodeStorageType"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbFiberNodeRowStatus"))
)
if mibBuilder.loadTexts:
    ccwbWidebandObjGroup.setStatus("deprecated")

ccwbWidebandObjGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 2, 2, 2)
)
ccwbWidebandObjGroupSup1.setObjects(
      *(("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChannelUtilization"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChanUtilInterval"))
)
if mibBuilder.loadTexts:
    ccwbWidebandObjGroupSup1.setStatus("current")

ccwbWidebandObjGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 2, 2, 3)
)
ccwbWidebandObjGroupRev1.setObjects(
      *(("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChannelFrequencyRev1"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChannelWidth"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChannelModulation"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChannelAnnex"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChannelStorageType"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChannelRowStatus"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChannelMpegPkts"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChanQamIPAddressType"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChanQamIPAddress"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChanQamMacAddress"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChanQamUdpPort"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChanQamTos"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChanQamVlanId"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChanQamPriorityBits"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChanQamDepiRemoteId"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbWBtoRFBandwidth"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbWBtoRFStorageType"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbWBtoRFRowStatus"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbWBtoNBStorageType"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbWBtoNBRowStatus"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbWBBondGrpSecondary"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbWBCmStatusValue"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbWBCmWBIfindex"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbFiberNodeDescription"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbFiberNodeDescrStorageType"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbFiberNodeDescrRowStatus"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbFiberNodeNBIfIndx"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbFiberNodeWBContlrPhyIndx"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbFiberNodeWBRFPort"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbFiberNodeStorageType"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbFiberNodeRowStatus"))
)
if mibBuilder.loadTexts:
    ccwbWidebandObjGroupRev1.setStatus("current")

ccwbWidebandObjGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 2, 2, 4)
)
ccwbWidebandObjGroupSup2.setObjects(
      *(("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChanQamDepiTunnel"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbRFChanQamTsid"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbSFPLinkTrapEnable"))
)
if mibBuilder.loadTexts:
    ccwbWidebandObjGroupSup2.setStatus("current")


# Notification objects

ccwbSFPLinkDownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 0, 1)
)
ccwbSFPLinkDownNotification.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    ccwbSFPLinkDownNotification.setStatus(
        "current"
    )

ccwbSFPLinkUpNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 0, 2)
)
ccwbSFPLinkUpNotification.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    ccwbSFPLinkUpNotification.setStatus(
        "current"
    )


# Notifications groups

ccwbWidebandNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 2, 2, 5)
)
ccwbWidebandNotifGroup.setObjects(
      *(("CISCO-CABLE-WIDEBAND-MIB", "ccwbSFPLinkDownNotification"),
        ("CISCO-CABLE-WIDEBAND-MIB", "ccwbSFPLinkUpNotification"))
)
if mibBuilder.loadTexts:
    ccwbWidebandNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoCableWidebandMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCableWidebandMIBCompliance.setStatus(
        "deprecated"
    )

ciscoCableWidebandMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoCableWidebandMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoCableWidebandMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoCableWidebandMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoCableWidebandMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 479, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoCableWidebandMIBComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CABLE-WIDEBAND-MIB",
    **{"ciscoCableWidebandMIB": ciscoCableWidebandMIB,
       "ciscoCableWidebandMIBNotifs": ciscoCableWidebandMIBNotifs,
       "ccwbSFPLinkDownNotification": ccwbSFPLinkDownNotification,
       "ccwbSFPLinkUpNotification": ccwbSFPLinkUpNotification,
       "ciscoCableWidebandMIBObjects": ciscoCableWidebandMIBObjects,
       "ccwbRFChannelTable": ccwbRFChannelTable,
       "ccwbRFChannelEntry": ccwbRFChannelEntry,
       "ccwbRFChannelNum": ccwbRFChannelNum,
       "ccwbRFChannelFrequency": ccwbRFChannelFrequency,
       "ccwbRFChannelWidth": ccwbRFChannelWidth,
       "ccwbRFChannelModulation": ccwbRFChannelModulation,
       "ccwbRFChannelAnnex": ccwbRFChannelAnnex,
       "ccwbRFChannelMpegPkts": ccwbRFChannelMpegPkts,
       "ccwbRFChannelStorageType": ccwbRFChannelStorageType,
       "ccwbRFChannelRowStatus": ccwbRFChannelRowStatus,
       "ccwbRFChannelUtilization": ccwbRFChannelUtilization,
       "ccwbRFChannelFrequencyRev1": ccwbRFChannelFrequencyRev1,
       "ccwbRFChannelQamTable": ccwbRFChannelQamTable,
       "ccwbRFChannelQamEntry": ccwbRFChannelQamEntry,
       "ccwbRFChanQamIPAddressType": ccwbRFChanQamIPAddressType,
       "ccwbRFChanQamIPAddress": ccwbRFChanQamIPAddress,
       "ccwbRFChanQamMacAddress": ccwbRFChanQamMacAddress,
       "ccwbRFChanQamUdpPort": ccwbRFChanQamUdpPort,
       "ccwbRFChanQamTos": ccwbRFChanQamTos,
       "ccwbRFChanQamVlanId": ccwbRFChanQamVlanId,
       "ccwbRFChanQamPriorityBits": ccwbRFChanQamPriorityBits,
       "ccwbRFChanQamDepiRemoteId": ccwbRFChanQamDepiRemoteId,
       "ccwbRFChanQamDepiTunnel": ccwbRFChanQamDepiTunnel,
       "ccwbRFChanQamTsid": ccwbRFChanQamTsid,
       "ccwbWBtoRFMappingTable": ccwbWBtoRFMappingTable,
       "ccwbWBtoRFMappingEntry": ccwbWBtoRFMappingEntry,
       "ccwbWBtoRFBandwidth": ccwbWBtoRFBandwidth,
       "ccwbWBtoRFStorageType": ccwbWBtoRFStorageType,
       "ccwbWBtoRFRowStatus": ccwbWBtoRFRowStatus,
       "ccwbWBtoNBMappingTable": ccwbWBtoNBMappingTable,
       "ccwbWBtoNBMappingEntry": ccwbWBtoNBMappingEntry,
       "ccwbWBtoNBifIndexForNB": ccwbWBtoNBifIndexForNB,
       "ccwbWBtoNBStorageType": ccwbWBtoNBStorageType,
       "ccwbWBtoNBRowStatus": ccwbWBtoNBRowStatus,
       "ccwbWBBondGrpTable": ccwbWBBondGrpTable,
       "ccwbWBBondGrpEntry": ccwbWBBondGrpEntry,
       "ccwbWBBondGrpSecondary": ccwbWBBondGrpSecondary,
       "ccwbWBCmStatusTable": ccwbWBCmStatusTable,
       "ccwbWBCmStatusEntry": ccwbWBCmStatusEntry,
       "ccwbWBCmStatusValue": ccwbWBCmStatusValue,
       "ccwbWBCmStatusExtTable": ccwbWBCmStatusExtTable,
       "ccwbWBCmStatusExtEntry": ccwbWBCmStatusExtEntry,
       "ccwbWBCmStatusExtIndex": ccwbWBCmStatusExtIndex,
       "ccwbWBCmWBIfindex": ccwbWBCmWBIfindex,
       "ccwbFiberNodeDescrTable": ccwbFiberNodeDescrTable,
       "ccwbFiberNodeDescrEntry": ccwbFiberNodeDescrEntry,
       "ccwbFiberNodeDescription": ccwbFiberNodeDescription,
       "ccwbFiberNodeDescrStorageType": ccwbFiberNodeDescrStorageType,
       "ccwbFiberNodeDescrRowStatus": ccwbFiberNodeDescrRowStatus,
       "ccwbFiberNodeTable": ccwbFiberNodeTable,
       "ccwbFiberNodeEntry": ccwbFiberNodeEntry,
       "ccwbFiberNodeID": ccwbFiberNodeID,
       "ccwbFiberNodeGlobRFID": ccwbFiberNodeGlobRFID,
       "ccwbFiberNodeNBIfIndx": ccwbFiberNodeNBIfIndx,
       "ccwbFiberNodeWBContlrPhyIndx": ccwbFiberNodeWBContlrPhyIndx,
       "ccwbFiberNodeWBRFPort": ccwbFiberNodeWBRFPort,
       "ccwbFiberNodeStorageType": ccwbFiberNodeStorageType,
       "ccwbFiberNodeRowStatus": ccwbFiberNodeRowStatus,
       "ccwbRFChanUtilInterval": ccwbRFChanUtilInterval,
       "ccwbSFPLinkTrapEnable": ccwbSFPLinkTrapEnable,
       "ciscoCableWidebandMIBConform": ciscoCableWidebandMIBConform,
       "ciscoCableWidebandMIBCompliances": ciscoCableWidebandMIBCompliances,
       "ciscoCableWidebandMIBCompliance": ciscoCableWidebandMIBCompliance,
       "ciscoCableWidebandMIBComplianceRev1": ciscoCableWidebandMIBComplianceRev1,
       "ciscoCableWidebandMIBComplianceRev2": ciscoCableWidebandMIBComplianceRev2,
       "ciscoCableWidebandMIBComplianceRev3": ciscoCableWidebandMIBComplianceRev3,
       "ciscoCableWidebandMIBGroups": ciscoCableWidebandMIBGroups,
       "ccwbWidebandObjGroup": ccwbWidebandObjGroup,
       "ccwbWidebandObjGroupSup1": ccwbWidebandObjGroupSup1,
       "ccwbWidebandObjGroupRev1": ccwbWidebandObjGroupRev1,
       "ccwbWidebandObjGroupSup2": ccwbWidebandObjGroupSup2,
       "ccwbWidebandNotifGroup": ccwbWidebandNotifGroup}
)
