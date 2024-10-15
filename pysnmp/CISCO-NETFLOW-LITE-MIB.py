# SNMP MIB module (CISCO-NETFLOW-LITE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-NETFLOW-LITE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:07 2024
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

(CiscoVrfName,
 Layer2Cos) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoVrfName",
    "Layer2Cos")

(Dscp,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ciscoNetflowLiteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 776)
)
ciscoNetflowLiteMIB.setRevisions(
        ("2011-09-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoNetflowLiteMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoNetflowLiteMIBNotifs = _CiscoNetflowLiteMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 0)
)
_CiscoNetflowLiteMIBObjects_ObjectIdentity = ObjectIdentity
ciscoNetflowLiteMIBObjects = _CiscoNetflowLiteMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1)
)
_CnlExporter_ObjectIdentity = ObjectIdentity
cnlExporter = _CnlExporter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1)
)
_CnlMaxExporterAllowed_Type = Unsigned32
_CnlMaxExporterAllowed_Object = MibScalar
cnlMaxExporterAllowed = _CnlMaxExporterAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 1),
    _CnlMaxExporterAllowed_Type()
)
cnlMaxExporterAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnlMaxExporterAllowed.setStatus("current")
_CnlExporterTable_Object = MibTable
cnlExporterTable = _CnlExporterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cnlExporterTable.setStatus("current")
_CnlExporterEntry_Object = MibTableRow
cnlExporterEntry = _CnlExporterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1)
)
cnlExporterEntry.setIndexNames(
    (1, "CISCO-NETFLOW-LITE-MIB", "cnlExporterName"),
)
if mibBuilder.loadTexts:
    cnlExporterEntry.setStatus("current")


class _CnlExporterName_Type(SnmpAdminString):
    """Custom type cnlExporterName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CnlExporterName_Type.__name__ = "SnmpAdminString"
_CnlExporterName_Object = MibTableColumn
cnlExporterName = _CnlExporterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 1),
    _CnlExporterName_Type()
)
cnlExporterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnlExporterName.setStatus("current")


class _CnlExportAddrType_Type(InetAddressType):
    """Custom type cnlExportAddrType based on InetAddressType"""


_CnlExportAddrType_Object = MibTableColumn
cnlExportAddrType = _CnlExportAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 2),
    _CnlExportAddrType_Type()
)
cnlExportAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlExportAddrType.setStatus("current")
_CnlExportDestinationAddr_Type = InetAddress
_CnlExportDestinationAddr_Object = MibTableColumn
cnlExportDestinationAddr = _CnlExportDestinationAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 3),
    _CnlExportDestinationAddr_Type()
)
cnlExportDestinationAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlExportDestinationAddr.setStatus("current")


class _CnlExportDestinationUdpPort_Type(InetPortNumber):
    """Custom type cnlExportDestinationUdpPort based on InetPortNumber"""
    defaultValue = 0


_CnlExportDestinationUdpPort_Object = MibTableColumn
cnlExportDestinationUdpPort = _CnlExportDestinationUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 4),
    _CnlExportDestinationUdpPort_Type()
)
cnlExportDestinationUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlExportDestinationUdpPort.setStatus("current")


class _CnlExportDestinationUdpLoadShare_Type(Unsigned32):
    """Custom type cnlExportDestinationUdpLoadShare based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CnlExportDestinationUdpLoadShare_Type.__name__ = "Unsigned32"
_CnlExportDestinationUdpLoadShare_Object = MibTableColumn
cnlExportDestinationUdpLoadShare = _CnlExportDestinationUdpLoadShare_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 5),
    _CnlExportDestinationUdpLoadShare_Type()
)
cnlExportDestinationUdpLoadShare.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlExportDestinationUdpLoadShare.setStatus("current")
_CnlExportSourceAddr_Type = InetAddress
_CnlExportSourceAddr_Object = MibTableColumn
cnlExportSourceAddr = _CnlExportSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 6),
    _CnlExportSourceAddr_Type()
)
cnlExportSourceAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlExportSourceAddr.setStatus("current")
_CnlExportSourceUdpPort_Type = InetPortNumber
_CnlExportSourceUdpPort_Object = MibTableColumn
cnlExportSourceUdpPort = _CnlExportSourceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 7),
    _CnlExportSourceUdpPort_Type()
)
cnlExportSourceUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlExportSourceUdpPort.setStatus("current")
_CnlExportVrf_Type = CiscoVrfName
_CnlExportVrf_Object = MibTableColumn
cnlExportVrf = _CnlExportVrf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 8),
    _CnlExportVrf_Type()
)
cnlExportVrf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlExportVrf.setStatus("current")


class _CnlExportTtl_Type(Unsigned32):
    """Custom type cnlExportTtl based on Unsigned32"""
    defaultValue = 254

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_CnlExportTtl_Type.__name__ = "Unsigned32"
_CnlExportTtl_Object = MibTableColumn
cnlExportTtl = _CnlExportTtl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 9),
    _CnlExportTtl_Type()
)
cnlExportTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlExportTtl.setStatus("current")


class _CnlExportCos_Type(Layer2Cos):
    """Custom type cnlExportCos based on Layer2Cos"""
    defaultValue = 0


_CnlExportCos_Object = MibTableColumn
cnlExportCos = _CnlExportCos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 10),
    _CnlExportCos_Type()
)
cnlExportCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlExportCos.setStatus("current")


class _CnlExportDscp_Type(Dscp):
    """Custom type cnlExportDscp based on Dscp"""
    defaultValue = 0


_CnlExportDscp_Object = MibTableColumn
cnlExportDscp = _CnlExportDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 11),
    _CnlExportDscp_Type()
)
cnlExportDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlExportDscp.setStatus("current")


class _CnlExportTemplateTimeout_Type(Unsigned32):
    """Custom type cnlExportTemplateTimeout based on Unsigned32"""
    defaultValue = 1800


_CnlExportTemplateTimeout_Object = MibTableColumn
cnlExportTemplateTimeout = _CnlExportTemplateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 12),
    _CnlExportTemplateTimeout_Type()
)
cnlExportTemplateTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlExportTemplateTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cnlExportTemplateTimeout.setUnits("seconds")


class _CnlExportSamplerTableTimeout_Type(Unsigned32):
    """Custom type cnlExportSamplerTableTimeout based on Unsigned32"""
    defaultValue = 1800


_CnlExportSamplerTableTimeout_Object = MibTableColumn
cnlExportSamplerTableTimeout = _CnlExportSamplerTableTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 13),
    _CnlExportSamplerTableTimeout_Type()
)
cnlExportSamplerTableTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlExportSamplerTableTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cnlExportSamplerTableTimeout.setUnits("seconds")


class _CnlExportInterfaceTableTimeout_Type(Unsigned32):
    """Custom type cnlExportInterfaceTableTimeout based on Unsigned32"""
    defaultValue = 1800


_CnlExportInterfaceTableTimeout_Object = MibTableColumn
cnlExportInterfaceTableTimeout = _CnlExportInterfaceTableTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 14),
    _CnlExportInterfaceTableTimeout_Type()
)
cnlExportInterfaceTableTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlExportInterfaceTableTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cnlExportInterfaceTableTimeout.setUnits("seconds")


class _CnlExportProtocol_Type(Integer32):
    """Custom type cnlExportProtocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipFix", 1),
          ("netflowV9", 2))
    )


_CnlExportProtocol_Type.__name__ = "Integer32"
_CnlExportProtocol_Object = MibTableColumn
cnlExportProtocol = _CnlExportProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 15),
    _CnlExportProtocol_Type()
)
cnlExportProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlExportProtocol.setStatus("current")
_CnlPacketExported_Type = Counter64
_CnlPacketExported_Object = MibTableColumn
cnlPacketExported = _CnlPacketExported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 16),
    _CnlPacketExported_Type()
)
cnlPacketExported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnlPacketExported.setStatus("current")


class _CnlExporterStorageType_Type(StorageType):
    """Custom type cnlExporterStorageType based on StorageType"""


_CnlExporterStorageType_Object = MibTableColumn
cnlExporterStorageType = _CnlExporterStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 17),
    _CnlExporterStorageType_Type()
)
cnlExporterStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlExporterStorageType.setStatus("current")
_CnlExporterRowStatus_Type = RowStatus
_CnlExporterRowStatus_Object = MibTableColumn
cnlExporterRowStatus = _CnlExporterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 1, 2, 1, 18),
    _CnlExporterRowStatus_Type()
)
cnlExporterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlExporterRowStatus.setStatus("current")
_CnlSampler_ObjectIdentity = ObjectIdentity
cnlSampler = _CnlSampler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 2)
)
_CnlMaxSamplerAllowed_Type = Unsigned32
_CnlMaxSamplerAllowed_Object = MibScalar
cnlMaxSamplerAllowed = _CnlMaxSamplerAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 2, 1),
    _CnlMaxSamplerAllowed_Type()
)
cnlMaxSamplerAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnlMaxSamplerAllowed.setStatus("current")
_CnlSamplerTable_Object = MibTable
cnlSamplerTable = _CnlSamplerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cnlSamplerTable.setStatus("current")
_CnlSamplerEntry_Object = MibTableRow
cnlSamplerEntry = _CnlSamplerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 2, 2, 1)
)
cnlSamplerEntry.setIndexNames(
    (1, "CISCO-NETFLOW-LITE-MIB", "cnlSamplerName"),
)
if mibBuilder.loadTexts:
    cnlSamplerEntry.setStatus("current")


class _CnlSamplerName_Type(SnmpAdminString):
    """Custom type cnlSamplerName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CnlSamplerName_Type.__name__ = "SnmpAdminString"
_CnlSamplerName_Object = MibTableColumn
cnlSamplerName = _CnlSamplerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 2, 2, 1, 1),
    _CnlSamplerName_Type()
)
cnlSamplerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnlSamplerName.setStatus("current")


class _CnlSamplerPacketRate_Type(Unsigned32):
    """Custom type cnlSamplerPacketRate based on Unsigned32"""
    defaultValue = 1


_CnlSamplerPacketRate_Object = MibTableColumn
cnlSamplerPacketRate = _CnlSamplerPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 2, 2, 1, 2),
    _CnlSamplerPacketRate_Type()
)
cnlSamplerPacketRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlSamplerPacketRate.setStatus("current")


class _CnlSamplerPacketSectionSize_Type(Unsigned32):
    """Custom type cnlSamplerPacketSectionSize based on Unsigned32"""
    defaultValue = 64


_CnlSamplerPacketSectionSize_Object = MibTableColumn
cnlSamplerPacketSectionSize = _CnlSamplerPacketSectionSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 2, 2, 1, 3),
    _CnlSamplerPacketSectionSize_Type()
)
cnlSamplerPacketSectionSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlSamplerPacketSectionSize.setStatus("current")
if mibBuilder.loadTexts:
    cnlSamplerPacketSectionSize.setUnits("bytes")


class _CnlSamplerPacketOffset_Type(Unsigned32):
    """Custom type cnlSamplerPacketOffset based on Unsigned32"""
    defaultValue = 0


_CnlSamplerPacketOffset_Object = MibTableColumn
cnlSamplerPacketOffset = _CnlSamplerPacketOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 2, 2, 1, 4),
    _CnlSamplerPacketOffset_Type()
)
cnlSamplerPacketOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlSamplerPacketOffset.setStatus("current")


class _CnlSamplerStorageType_Type(StorageType):
    """Custom type cnlSamplerStorageType based on StorageType"""


_CnlSamplerStorageType_Object = MibTableColumn
cnlSamplerStorageType = _CnlSamplerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 2, 2, 1, 5),
    _CnlSamplerStorageType_Type()
)
cnlSamplerStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlSamplerStorageType.setStatus("current")
_CnlSamplerRowStatus_Type = RowStatus
_CnlSamplerRowStatus_Object = MibTableColumn
cnlSamplerRowStatus = _CnlSamplerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 2, 2, 1, 6),
    _CnlSamplerRowStatus_Type()
)
cnlSamplerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlSamplerRowStatus.setStatus("current")
_CnlMonitor_ObjectIdentity = ObjectIdentity
cnlMonitor = _CnlMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3)
)
_CnlIfMonitorTable_Object = MibTable
cnlIfMonitorTable = _CnlIfMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cnlIfMonitorTable.setStatus("current")
_CnlIfMonitorEntry_Object = MibTableRow
cnlIfMonitorEntry = _CnlIfMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1)
)
cnlIfMonitorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (1, "CISCO-NETFLOW-LITE-MIB", "cnlIfMonitorSessionName"),
)
if mibBuilder.loadTexts:
    cnlIfMonitorEntry.setStatus("current")


class _CnlIfMonitorSessionName_Type(SnmpAdminString):
    """Custom type cnlIfMonitorSessionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CnlIfMonitorSessionName_Type.__name__ = "SnmpAdminString"
_CnlIfMonitorSessionName_Object = MibTableColumn
cnlIfMonitorSessionName = _CnlIfMonitorSessionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 1),
    _CnlIfMonitorSessionName_Type()
)
cnlIfMonitorSessionName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnlIfMonitorSessionName.setStatus("current")


class _CnlIfMonitorActiveStatus_Type(Integer32):
    """Custom type cnlIfMonitorActiveStatus based on Integer32"""
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


_CnlIfMonitorActiveStatus_Type.__name__ = "Integer32"
_CnlIfMonitorActiveStatus_Object = MibTableColumn
cnlIfMonitorActiveStatus = _CnlIfMonitorActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 2),
    _CnlIfMonitorActiveStatus_Type()
)
cnlIfMonitorActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnlIfMonitorActiveStatus.setStatus("current")
_CnlIfSamplerName_Type = SnmpAdminString
_CnlIfSamplerName_Object = MibTableColumn
cnlIfSamplerName = _CnlIfSamplerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 3),
    _CnlIfSamplerName_Type()
)
cnlIfSamplerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlIfSamplerName.setStatus("current")
_CnlIfExporterName_Type = SnmpAdminString
_CnlIfExporterName_Object = MibTableColumn
cnlIfExporterName = _CnlIfExporterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 4),
    _CnlIfExporterName_Type()
)
cnlIfExporterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlIfExporterName.setStatus("current")


class _CnlIfAveragePacketSize_Type(Unsigned32):
    """Custom type cnlIfAveragePacketSize based on Unsigned32"""
    defaultValue = 0


_CnlIfAveragePacketSize_Object = MibTableColumn
cnlIfAveragePacketSize = _CnlIfAveragePacketSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 5),
    _CnlIfAveragePacketSize_Type()
)
cnlIfAveragePacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlIfAveragePacketSize.setStatus("current")
_CnlIfAveragePacketSizeObserved_Type = Unsigned32
_CnlIfAveragePacketSizeObserved_Object = MibTableColumn
cnlIfAveragePacketSizeObserved = _CnlIfAveragePacketSizeObserved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 6),
    _CnlIfAveragePacketSizeObserved_Type()
)
cnlIfAveragePacketSizeObserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnlIfAveragePacketSizeObserved.setStatus("current")
_CnlIfAveragePacketSizeUsed_Type = Unsigned32
_CnlIfAveragePacketSizeUsed_Object = MibTableColumn
cnlIfAveragePacketSizeUsed = _CnlIfAveragePacketSizeUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 7),
    _CnlIfAveragePacketSizeUsed_Type()
)
cnlIfAveragePacketSizeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnlIfAveragePacketSizeUsed.setStatus("current")
_CnlIfMonitorPktsObserved_Type = Counter64
_CnlIfMonitorPktsObserved_Object = MibTableColumn
cnlIfMonitorPktsObserved = _CnlIfMonitorPktsObserved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 8),
    _CnlIfMonitorPktsObserved_Type()
)
cnlIfMonitorPktsObserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnlIfMonitorPktsObserved.setStatus("current")
_CnlIfMonitorPktsExported_Type = Counter64
_CnlIfMonitorPktsExported_Object = MibTableColumn
cnlIfMonitorPktsExported = _CnlIfMonitorPktsExported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 9),
    _CnlIfMonitorPktsExported_Type()
)
cnlIfMonitorPktsExported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnlIfMonitorPktsExported.setStatus("current")
_CnlIfMonitorPktsDropped_Type = Counter64
_CnlIfMonitorPktsDropped_Object = MibTableColumn
cnlIfMonitorPktsDropped = _CnlIfMonitorPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 10),
    _CnlIfMonitorPktsDropped_Type()
)
cnlIfMonitorPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnlIfMonitorPktsDropped.setStatus("current")


class _CnlIfMonitorStorageType_Type(StorageType):
    """Custom type cnlIfMonitorStorageType based on StorageType"""


_CnlIfMonitorStorageType_Object = MibTableColumn
cnlIfMonitorStorageType = _CnlIfMonitorStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 11),
    _CnlIfMonitorStorageType_Type()
)
cnlIfMonitorStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlIfMonitorStorageType.setStatus("current")
_CnlIfMonitorRowStatus_Type = RowStatus
_CnlIfMonitorRowStatus_Object = MibTableColumn
cnlIfMonitorRowStatus = _CnlIfMonitorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 1, 3, 1, 1, 12),
    _CnlIfMonitorRowStatus_Type()
)
cnlIfMonitorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cnlIfMonitorRowStatus.setStatus("current")
_CiscoNetflowLiteMIBConform_ObjectIdentity = ObjectIdentity
ciscoNetflowLiteMIBConform = _CiscoNetflowLiteMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 2)
)
_CiscoNetflowLiteMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoNetflowLiteMIBCompliances = _CiscoNetflowLiteMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 2, 1)
)
_CiscoNetflowLiteMIBGroups_ObjectIdentity = ObjectIdentity
ciscoNetflowLiteMIBGroups = _CiscoNetflowLiteMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 2, 2)
)

# Managed Objects groups

cnlExporterInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 2, 2, 1)
)
cnlExporterInfoGroup.setObjects(
      *(("CISCO-NETFLOW-LITE-MIB", "cnlMaxExporterAllowed"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlExportAddrType"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlExportDestinationAddr"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlExportDestinationUdpPort"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlExportDestinationUdpLoadShare"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlExportSourceAddr"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlExportSourceUdpPort"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlExportVrf"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlExportTtl"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlExportCos"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlExportDscp"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlExportTemplateTimeout"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlExportSamplerTableTimeout"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlExportInterfaceTableTimeout"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlExportProtocol"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlPacketExported"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlExporterStorageType"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlExporterRowStatus"))
)
if mibBuilder.loadTexts:
    cnlExporterInfoGroup.setStatus("current")

cnlSamplerInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 2, 2, 2)
)
cnlSamplerInfoGroup.setObjects(
      *(("CISCO-NETFLOW-LITE-MIB", "cnlMaxSamplerAllowed"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlSamplerPacketRate"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlSamplerPacketSectionSize"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlSamplerPacketOffset"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlSamplerStorageType"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlSamplerRowStatus"))
)
if mibBuilder.loadTexts:
    cnlSamplerInfoGroup.setStatus("current")

cnlIfMonitorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 2, 2, 3)
)
cnlIfMonitorInfoGroup.setObjects(
      *(("CISCO-NETFLOW-LITE-MIB", "cnlIfMonitorActiveStatus"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlIfSamplerName"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlIfExporterName"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlIfAveragePacketSize"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlIfAveragePacketSizeObserved"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlIfAveragePacketSizeUsed"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlIfMonitorPktsObserved"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlIfMonitorPktsExported"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlIfMonitorPktsDropped"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlIfMonitorStorageType"),
        ("CISCO-NETFLOW-LITE-MIB", "cnlIfMonitorRowStatus"))
)
if mibBuilder.loadTexts:
    cnlIfMonitorInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoNetflowLiteMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 776, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoNetflowLiteMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-NETFLOW-LITE-MIB",
    **{"ciscoNetflowLiteMIB": ciscoNetflowLiteMIB,
       "ciscoNetflowLiteMIBNotifs": ciscoNetflowLiteMIBNotifs,
       "ciscoNetflowLiteMIBObjects": ciscoNetflowLiteMIBObjects,
       "cnlExporter": cnlExporter,
       "cnlMaxExporterAllowed": cnlMaxExporterAllowed,
       "cnlExporterTable": cnlExporterTable,
       "cnlExporterEntry": cnlExporterEntry,
       "cnlExporterName": cnlExporterName,
       "cnlExportAddrType": cnlExportAddrType,
       "cnlExportDestinationAddr": cnlExportDestinationAddr,
       "cnlExportDestinationUdpPort": cnlExportDestinationUdpPort,
       "cnlExportDestinationUdpLoadShare": cnlExportDestinationUdpLoadShare,
       "cnlExportSourceAddr": cnlExportSourceAddr,
       "cnlExportSourceUdpPort": cnlExportSourceUdpPort,
       "cnlExportVrf": cnlExportVrf,
       "cnlExportTtl": cnlExportTtl,
       "cnlExportCos": cnlExportCos,
       "cnlExportDscp": cnlExportDscp,
       "cnlExportTemplateTimeout": cnlExportTemplateTimeout,
       "cnlExportSamplerTableTimeout": cnlExportSamplerTableTimeout,
       "cnlExportInterfaceTableTimeout": cnlExportInterfaceTableTimeout,
       "cnlExportProtocol": cnlExportProtocol,
       "cnlPacketExported": cnlPacketExported,
       "cnlExporterStorageType": cnlExporterStorageType,
       "cnlExporterRowStatus": cnlExporterRowStatus,
       "cnlSampler": cnlSampler,
       "cnlMaxSamplerAllowed": cnlMaxSamplerAllowed,
       "cnlSamplerTable": cnlSamplerTable,
       "cnlSamplerEntry": cnlSamplerEntry,
       "cnlSamplerName": cnlSamplerName,
       "cnlSamplerPacketRate": cnlSamplerPacketRate,
       "cnlSamplerPacketSectionSize": cnlSamplerPacketSectionSize,
       "cnlSamplerPacketOffset": cnlSamplerPacketOffset,
       "cnlSamplerStorageType": cnlSamplerStorageType,
       "cnlSamplerRowStatus": cnlSamplerRowStatus,
       "cnlMonitor": cnlMonitor,
       "cnlIfMonitorTable": cnlIfMonitorTable,
       "cnlIfMonitorEntry": cnlIfMonitorEntry,
       "cnlIfMonitorSessionName": cnlIfMonitorSessionName,
       "cnlIfMonitorActiveStatus": cnlIfMonitorActiveStatus,
       "cnlIfSamplerName": cnlIfSamplerName,
       "cnlIfExporterName": cnlIfExporterName,
       "cnlIfAveragePacketSize": cnlIfAveragePacketSize,
       "cnlIfAveragePacketSizeObserved": cnlIfAveragePacketSizeObserved,
       "cnlIfAveragePacketSizeUsed": cnlIfAveragePacketSizeUsed,
       "cnlIfMonitorPktsObserved": cnlIfMonitorPktsObserved,
       "cnlIfMonitorPktsExported": cnlIfMonitorPktsExported,
       "cnlIfMonitorPktsDropped": cnlIfMonitorPktsDropped,
       "cnlIfMonitorStorageType": cnlIfMonitorStorageType,
       "cnlIfMonitorRowStatus": cnlIfMonitorRowStatus,
       "ciscoNetflowLiteMIBConform": ciscoNetflowLiteMIBConform,
       "ciscoNetflowLiteMIBCompliances": ciscoNetflowLiteMIBCompliances,
       "ciscoNetflowLiteMIBCompliance": ciscoNetflowLiteMIBCompliance,
       "ciscoNetflowLiteMIBGroups": ciscoNetflowLiteMIBGroups,
       "cnlExporterInfoGroup": cnlExporterInfoGroup,
       "cnlSamplerInfoGroup": cnlSamplerInfoGroup,
       "cnlIfMonitorInfoGroup": cnlIfMonitorInfoGroup}
)
