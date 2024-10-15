# SNMP MIB module (DOCS-CABLE-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-CABLE-DEVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:08 2024
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

(diffServActionStorage,
 diffServAlgDropStatus,
 diffServAlgDropStorage,
 diffServAlgDropType,
 diffServClfrElementStatus,
 diffServClfrElementStorage,
 diffServClfrStatus,
 diffServClfrStorage,
 diffServCountActStorage,
 diffServDataPathStatus,
 diffServDataPathStorage,
 diffServMIBActionGroup,
 diffServMIBAlgDropGroup,
 diffServMIBClfrElementGroup,
 diffServMIBClfrGroup,
 diffServMIBCounterGroup,
 diffServMIBDataPathGroup,
 diffServMIBDscpMarkActGroup,
 diffServMIBMultiFieldClfrGroup,
 diffServMultiFieldClfrAddrType,
 diffServMultiFieldClfrDstAddr,
 diffServMultiFieldClfrSrcAddr,
 diffServMultiFieldClfrStorage) = mibBuilder.importSymbols(
    "DIFFSERV-MIB",
    "diffServActionStorage",
    "diffServAlgDropStatus",
    "diffServAlgDropStorage",
    "diffServAlgDropType",
    "diffServClfrElementStatus",
    "diffServClfrElementStorage",
    "diffServClfrStatus",
    "diffServClfrStorage",
    "diffServCountActStorage",
    "diffServDataPathStatus",
    "diffServDataPathStorage",
    "diffServMIBActionGroup",
    "diffServMIBAlgDropGroup",
    "diffServMIBClfrElementGroup",
    "diffServMIBClfrGroup",
    "diffServMIBCounterGroup",
    "diffServMIBDataPathGroup",
    "diffServMIBDscpMarkActGroup",
    "diffServMIBMultiFieldClfrGroup",
    "diffServMultiFieldClfrAddrType",
    "diffServMultiFieldClfrDstAddr",
    "diffServMultiFieldClfrSrcAddr",
    "diffServMultiFieldClfrStorage")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ZeroBasedCounter32,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32")

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
 iso,
 mib_2,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2",
    "zeroDotZero")

(DateAndTime,
 DisplayString,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

docsDev = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 69)
)
docsDev.setRevisions(
        ("2006-12-20 00:00",
         "1999-08-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DocsDevNotifications_ObjectIdentity = ObjectIdentity
docsDevNotifications = _DocsDevNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 69, 0)
)
_DocsDevMIBObjects_ObjectIdentity = ObjectIdentity
docsDevMIBObjects = _DocsDevMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 69, 1)
)
_DocsDevBase_ObjectIdentity = ObjectIdentity
docsDevBase = _DocsDevBase_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 69, 1, 1)
)


class _DocsDevRole_Type(Integer32):
    """Custom type docsDevRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cm", 1),
          ("cmtsActive", 2),
          ("cmtsBackup", 3))
    )


_DocsDevRole_Type.__name__ = "Integer32"
_DocsDevRole_Object = MibScalar
docsDevRole = _DocsDevRole_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 1, 1),
    _DocsDevRole_Type()
)
docsDevRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevRole.setStatus("current")
_DocsDevDateTime_Type = DateAndTime
_DocsDevDateTime_Object = MibScalar
docsDevDateTime = _DocsDevDateTime_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 1, 2),
    _DocsDevDateTime_Type()
)
docsDevDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevDateTime.setStatus("current")
_DocsDevResetNow_Type = TruthValue
_DocsDevResetNow_Object = MibScalar
docsDevResetNow = _DocsDevResetNow_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 1, 3),
    _DocsDevResetNow_Type()
)
docsDevResetNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevResetNow.setStatus("current")
_DocsDevSerialNumber_Type = SnmpAdminString
_DocsDevSerialNumber_Object = MibScalar
docsDevSerialNumber = _DocsDevSerialNumber_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 1, 4),
    _DocsDevSerialNumber_Type()
)
docsDevSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevSerialNumber.setStatus("current")


class _DocsDevSTPControl_Type(Integer32):
    """Custom type docsDevSTPControl based on Integer32"""
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
        *(("noStFilterBpdu", 2),
          ("noStPassBpdu", 3),
          ("stEnabled", 1))
    )


_DocsDevSTPControl_Type.__name__ = "Integer32"
_DocsDevSTPControl_Object = MibScalar
docsDevSTPControl = _DocsDevSTPControl_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 1, 5),
    _DocsDevSTPControl_Type()
)
docsDevSTPControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevSTPControl.setStatus("current")


class _DocsDevIgmpModeControl_Type(Integer32):
    """Custom type docsDevIgmpModeControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("passive", 1))
    )


_DocsDevIgmpModeControl_Type.__name__ = "Integer32"
_DocsDevIgmpModeControl_Object = MibScalar
docsDevIgmpModeControl = _DocsDevIgmpModeControl_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 1, 6),
    _DocsDevIgmpModeControl_Type()
)
docsDevIgmpModeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevIgmpModeControl.setStatus("current")


class _DocsDevMaxCpe_Type(Unsigned32):
    """Custom type docsDevMaxCpe based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DocsDevMaxCpe_Type.__name__ = "Unsigned32"
_DocsDevMaxCpe_Object = MibScalar
docsDevMaxCpe = _DocsDevMaxCpe_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 1, 7),
    _DocsDevMaxCpe_Type()
)
docsDevMaxCpe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevMaxCpe.setStatus("current")
if mibBuilder.loadTexts:
    docsDevMaxCpe.setUnits("CPEs")
_DocsDevNmAccessTable_Object = MibTable
docsDevNmAccessTable = _DocsDevNmAccessTable_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 2)
)
if mibBuilder.loadTexts:
    docsDevNmAccessTable.setStatus("deprecated")
_DocsDevNmAccessEntry_Object = MibTableRow
docsDevNmAccessEntry = _DocsDevNmAccessEntry_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 2, 1)
)
docsDevNmAccessEntry.setIndexNames(
    (0, "DOCS-CABLE-DEVICE-MIB", "docsDevNmAccessIndex"),
)
if mibBuilder.loadTexts:
    docsDevNmAccessEntry.setStatus("deprecated")


class _DocsDevNmAccessIndex_Type(Integer32):
    """Custom type docsDevNmAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DocsDevNmAccessIndex_Type.__name__ = "Integer32"
_DocsDevNmAccessIndex_Object = MibTableColumn
docsDevNmAccessIndex = _DocsDevNmAccessIndex_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 2, 1, 1),
    _DocsDevNmAccessIndex_Type()
)
docsDevNmAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsDevNmAccessIndex.setStatus("deprecated")


class _DocsDevNmAccessIp_Type(IpAddress):
    """Custom type docsDevNmAccessIp based on IpAddress"""
    defaultHexValue = "00000000"


_DocsDevNmAccessIp_Object = MibTableColumn
docsDevNmAccessIp = _DocsDevNmAccessIp_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 2, 1, 2),
    _DocsDevNmAccessIp_Type()
)
docsDevNmAccessIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevNmAccessIp.setStatus("deprecated")


class _DocsDevNmAccessIpMask_Type(IpAddress):
    """Custom type docsDevNmAccessIpMask based on IpAddress"""
    defaultHexValue = "00000000"


_DocsDevNmAccessIpMask_Object = MibTableColumn
docsDevNmAccessIpMask = _DocsDevNmAccessIpMask_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 2, 1, 3),
    _DocsDevNmAccessIpMask_Type()
)
docsDevNmAccessIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevNmAccessIpMask.setStatus("deprecated")


class _DocsDevNmAccessCommunity_Type(OctetString):
    """Custom type docsDevNmAccessCommunity based on OctetString"""
    defaultValue = OctetString("public")


_DocsDevNmAccessCommunity_Object = MibTableColumn
docsDevNmAccessCommunity = _DocsDevNmAccessCommunity_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 2, 1, 4),
    _DocsDevNmAccessCommunity_Type()
)
docsDevNmAccessCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevNmAccessCommunity.setStatus("deprecated")


class _DocsDevNmAccessControl_Type(Integer32):
    """Custom type docsDevNmAccessControl based on Integer32"""
    defaultValue = 2

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
        *(("none", 1),
          ("read", 2),
          ("readWrite", 3),
          ("roWithTraps", 4),
          ("rwWithTraps", 5),
          ("trapsOnly", 6))
    )


_DocsDevNmAccessControl_Type.__name__ = "Integer32"
_DocsDevNmAccessControl_Object = MibTableColumn
docsDevNmAccessControl = _DocsDevNmAccessControl_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 2, 1, 5),
    _DocsDevNmAccessControl_Type()
)
docsDevNmAccessControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevNmAccessControl.setStatus("deprecated")


class _DocsDevNmAccessInterfaces_Type(OctetString):
    """Custom type docsDevNmAccessInterfaces based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DocsDevNmAccessInterfaces_Type.__name__ = "OctetString"
_DocsDevNmAccessInterfaces_Object = MibTableColumn
docsDevNmAccessInterfaces = _DocsDevNmAccessInterfaces_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 2, 1, 6),
    _DocsDevNmAccessInterfaces_Type()
)
docsDevNmAccessInterfaces.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevNmAccessInterfaces.setStatus("deprecated")
_DocsDevNmAccessStatus_Type = RowStatus
_DocsDevNmAccessStatus_Object = MibTableColumn
docsDevNmAccessStatus = _DocsDevNmAccessStatus_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 2, 1, 7),
    _DocsDevNmAccessStatus_Type()
)
docsDevNmAccessStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevNmAccessStatus.setStatus("deprecated")


class _DocsDevNmAccessTrapVersion_Type(Integer32):
    """Custom type docsDevNmAccessTrapVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableSNMPv2trap", 1),
          ("enableSNMPv2trap", 2))
    )


_DocsDevNmAccessTrapVersion_Type.__name__ = "Integer32"
_DocsDevNmAccessTrapVersion_Object = MibTableColumn
docsDevNmAccessTrapVersion = _DocsDevNmAccessTrapVersion_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 2, 1, 8),
    _DocsDevNmAccessTrapVersion_Type()
)
docsDevNmAccessTrapVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevNmAccessTrapVersion.setStatus("deprecated")
_DocsDevSoftware_ObjectIdentity = ObjectIdentity
docsDevSoftware = _DocsDevSoftware_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 69, 1, 3)
)
_DocsDevSwServer_Type = IpAddress
_DocsDevSwServer_Object = MibScalar
docsDevSwServer = _DocsDevSwServer_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 3, 1),
    _DocsDevSwServer_Type()
)
docsDevSwServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevSwServer.setStatus("deprecated")


class _DocsDevSwFilename_Type(SnmpAdminString):
    """Custom type docsDevSwFilename based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DocsDevSwFilename_Type.__name__ = "SnmpAdminString"
_DocsDevSwFilename_Object = MibScalar
docsDevSwFilename = _DocsDevSwFilename_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 3, 2),
    _DocsDevSwFilename_Type()
)
docsDevSwFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevSwFilename.setStatus("current")


class _DocsDevSwAdminStatus_Type(Integer32):
    """Custom type docsDevSwAdminStatus based on Integer32"""
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
        *(("allowProvisioningUpgrade", 2),
          ("ignoreProvisioningUpgrade", 3),
          ("upgradeFromMgt", 1))
    )


_DocsDevSwAdminStatus_Type.__name__ = "Integer32"
_DocsDevSwAdminStatus_Object = MibScalar
docsDevSwAdminStatus = _DocsDevSwAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 3, 3),
    _DocsDevSwAdminStatus_Type()
)
docsDevSwAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevSwAdminStatus.setStatus("current")


class _DocsDevSwOperStatus_Type(Integer32):
    """Custom type docsDevSwOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("completeFromMgt", 3),
          ("completeFromProvisioning", 2),
          ("failed", 4),
          ("inProgress", 1),
          ("other", 5))
    )


_DocsDevSwOperStatus_Type.__name__ = "Integer32"
_DocsDevSwOperStatus_Object = MibScalar
docsDevSwOperStatus = _DocsDevSwOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 3, 4),
    _DocsDevSwOperStatus_Type()
)
docsDevSwOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevSwOperStatus.setStatus("current")
_DocsDevSwCurrentVers_Type = SnmpAdminString
_DocsDevSwCurrentVers_Object = MibScalar
docsDevSwCurrentVers = _DocsDevSwCurrentVers_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 3, 5),
    _DocsDevSwCurrentVers_Type()
)
docsDevSwCurrentVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevSwCurrentVers.setStatus("current")
_DocsDevSwServerAddressType_Type = InetAddressType
_DocsDevSwServerAddressType_Object = MibScalar
docsDevSwServerAddressType = _DocsDevSwServerAddressType_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 3, 6),
    _DocsDevSwServerAddressType_Type()
)
docsDevSwServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevSwServerAddressType.setStatus("current")
_DocsDevSwServerAddress_Type = InetAddress
_DocsDevSwServerAddress_Object = MibScalar
docsDevSwServerAddress = _DocsDevSwServerAddress_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 3, 7),
    _DocsDevSwServerAddress_Type()
)
docsDevSwServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevSwServerAddress.setStatus("current")


class _DocsDevSwServerTransportProtocol_Type(Integer32):
    """Custom type docsDevSwServerTransportProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("http", 2),
          ("tftp", 1))
    )


_DocsDevSwServerTransportProtocol_Type.__name__ = "Integer32"
_DocsDevSwServerTransportProtocol_Object = MibScalar
docsDevSwServerTransportProtocol = _DocsDevSwServerTransportProtocol_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 3, 8),
    _DocsDevSwServerTransportProtocol_Type()
)
docsDevSwServerTransportProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevSwServerTransportProtocol.setStatus("current")
_DocsDevServer_ObjectIdentity = ObjectIdentity
docsDevServer = _DocsDevServer_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 69, 1, 4)
)


class _DocsDevServerBootState_Type(Integer32):
    """Custom type docsDevServerBootState based on Integer32"""
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
        *(("disabled", 2),
          ("forwardingDenied", 8),
          ("operational", 1),
          ("other", 9),
          ("refusedByCmts", 7),
          ("unknown", 10),
          ("waitingForDhcpOffer", 3),
          ("waitingForDhcpResponse", 4),
          ("waitingForTftp", 6),
          ("waitingForTimeServer", 5))
    )


_DocsDevServerBootState_Type.__name__ = "Integer32"
_DocsDevServerBootState_Object = MibScalar
docsDevServerBootState = _DocsDevServerBootState_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 4, 1),
    _DocsDevServerBootState_Type()
)
docsDevServerBootState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevServerBootState.setStatus("current")
_DocsDevServerDhcp_Type = IpAddress
_DocsDevServerDhcp_Object = MibScalar
docsDevServerDhcp = _DocsDevServerDhcp_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 4, 2),
    _DocsDevServerDhcp_Type()
)
docsDevServerDhcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevServerDhcp.setStatus("deprecated")
_DocsDevServerTime_Type = IpAddress
_DocsDevServerTime_Object = MibScalar
docsDevServerTime = _DocsDevServerTime_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 4, 3),
    _DocsDevServerTime_Type()
)
docsDevServerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevServerTime.setStatus("deprecated")
_DocsDevServerTftp_Type = IpAddress
_DocsDevServerTftp_Object = MibScalar
docsDevServerTftp = _DocsDevServerTftp_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 4, 4),
    _DocsDevServerTftp_Type()
)
docsDevServerTftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevServerTftp.setStatus("deprecated")
_DocsDevServerConfigFile_Type = SnmpAdminString
_DocsDevServerConfigFile_Object = MibScalar
docsDevServerConfigFile = _DocsDevServerConfigFile_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 4, 5),
    _DocsDevServerConfigFile_Type()
)
docsDevServerConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevServerConfigFile.setStatus("current")
_DocsDevServerDhcpAddressType_Type = InetAddressType
_DocsDevServerDhcpAddressType_Object = MibScalar
docsDevServerDhcpAddressType = _DocsDevServerDhcpAddressType_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 4, 6),
    _DocsDevServerDhcpAddressType_Type()
)
docsDevServerDhcpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevServerDhcpAddressType.setStatus("current")
_DocsDevServerDhcpAddress_Type = InetAddress
_DocsDevServerDhcpAddress_Object = MibScalar
docsDevServerDhcpAddress = _DocsDevServerDhcpAddress_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 4, 7),
    _DocsDevServerDhcpAddress_Type()
)
docsDevServerDhcpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevServerDhcpAddress.setStatus("current")
_DocsDevServerTimeAddressType_Type = InetAddressType
_DocsDevServerTimeAddressType_Object = MibScalar
docsDevServerTimeAddressType = _DocsDevServerTimeAddressType_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 4, 8),
    _DocsDevServerTimeAddressType_Type()
)
docsDevServerTimeAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevServerTimeAddressType.setStatus("current")
_DocsDevServerTimeAddress_Type = InetAddress
_DocsDevServerTimeAddress_Object = MibScalar
docsDevServerTimeAddress = _DocsDevServerTimeAddress_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 4, 9),
    _DocsDevServerTimeAddress_Type()
)
docsDevServerTimeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevServerTimeAddress.setStatus("current")
_DocsDevServerConfigTftpAddressType_Type = InetAddressType
_DocsDevServerConfigTftpAddressType_Object = MibScalar
docsDevServerConfigTftpAddressType = _DocsDevServerConfigTftpAddressType_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 4, 10),
    _DocsDevServerConfigTftpAddressType_Type()
)
docsDevServerConfigTftpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevServerConfigTftpAddressType.setStatus("current")
_DocsDevServerConfigTftpAddress_Type = InetAddress
_DocsDevServerConfigTftpAddress_Object = MibScalar
docsDevServerConfigTftpAddress = _DocsDevServerConfigTftpAddress_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 4, 11),
    _DocsDevServerConfigTftpAddress_Type()
)
docsDevServerConfigTftpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevServerConfigTftpAddress.setStatus("current")
_DocsDevEvent_ObjectIdentity = ObjectIdentity
docsDevEvent = _DocsDevEvent_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 69, 1, 5)
)


class _DocsDevEvControl_Type(Integer32):
    """Custom type docsDevEvControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("resetLog", 1),
          ("useDefaultReporting", 2))
    )


_DocsDevEvControl_Type.__name__ = "Integer32"
_DocsDevEvControl_Object = MibScalar
docsDevEvControl = _DocsDevEvControl_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 5, 1),
    _DocsDevEvControl_Type()
)
docsDevEvControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevEvControl.setStatus("current")
_DocsDevEvSyslog_Type = IpAddress
_DocsDevEvSyslog_Object = MibScalar
docsDevEvSyslog = _DocsDevEvSyslog_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 5, 2),
    _DocsDevEvSyslog_Type()
)
docsDevEvSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevEvSyslog.setStatus("deprecated")


class _DocsDevEvThrottleAdminStatus_Type(Integer32):
    """Custom type docsDevEvThrottleAdminStatus based on Integer32"""
    defaultValue = 1

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
        *(("inhibited", 4),
          ("maintainBelowThreshold", 2),
          ("stopAtThreshold", 3),
          ("unconstrained", 1))
    )


_DocsDevEvThrottleAdminStatus_Type.__name__ = "Integer32"
_DocsDevEvThrottleAdminStatus_Object = MibScalar
docsDevEvThrottleAdminStatus = _DocsDevEvThrottleAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 5, 3),
    _DocsDevEvThrottleAdminStatus_Type()
)
docsDevEvThrottleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevEvThrottleAdminStatus.setStatus("current")
_DocsDevEvThrottleInhibited_Type = TruthValue
_DocsDevEvThrottleInhibited_Object = MibScalar
docsDevEvThrottleInhibited = _DocsDevEvThrottleInhibited_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 5, 4),
    _DocsDevEvThrottleInhibited_Type()
)
docsDevEvThrottleInhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevEvThrottleInhibited.setStatus("deprecated")


class _DocsDevEvThrottleThreshold_Type(Unsigned32):
    """Custom type docsDevEvThrottleThreshold based on Unsigned32"""
    defaultValue = 0


_DocsDevEvThrottleThreshold_Object = MibScalar
docsDevEvThrottleThreshold = _DocsDevEvThrottleThreshold_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 5, 5),
    _DocsDevEvThrottleThreshold_Type()
)
docsDevEvThrottleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevEvThrottleThreshold.setStatus("current")
if mibBuilder.loadTexts:
    docsDevEvThrottleThreshold.setUnits("events")


class _DocsDevEvThrottleInterval_Type(Integer32):
    """Custom type docsDevEvThrottleInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DocsDevEvThrottleInterval_Type.__name__ = "Integer32"
_DocsDevEvThrottleInterval_Object = MibScalar
docsDevEvThrottleInterval = _DocsDevEvThrottleInterval_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 5, 6),
    _DocsDevEvThrottleInterval_Type()
)
docsDevEvThrottleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevEvThrottleInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsDevEvThrottleInterval.setUnits("seconds")
_DocsDevEvControlTable_Object = MibTable
docsDevEvControlTable = _DocsDevEvControlTable_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 5, 7)
)
if mibBuilder.loadTexts:
    docsDevEvControlTable.setStatus("current")
_DocsDevEvControlEntry_Object = MibTableRow
docsDevEvControlEntry = _DocsDevEvControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 5, 7, 1)
)
docsDevEvControlEntry.setIndexNames(
    (0, "DOCS-CABLE-DEVICE-MIB", "docsDevEvPriority"),
)
if mibBuilder.loadTexts:
    docsDevEvControlEntry.setStatus("current")


class _DocsDevEvPriority_Type(Integer32):
    """Custom type docsDevEvPriority based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("information", 7),
          ("notice", 6),
          ("warning", 5))
    )


_DocsDevEvPriority_Type.__name__ = "Integer32"
_DocsDevEvPriority_Object = MibTableColumn
docsDevEvPriority = _DocsDevEvPriority_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 5, 7, 1, 1),
    _DocsDevEvPriority_Type()
)
docsDevEvPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsDevEvPriority.setStatus("current")


class _DocsDevEvReporting_Type(Bits):
    """Custom type docsDevEvReporting based on Bits"""
    namedValues = NamedValues(
        *(("local", 0),
          ("localVolatile", 8),
          ("stdInterface", 9),
          ("syslog", 2),
          ("traps", 1))
    )

_DocsDevEvReporting_Type.__name__ = "Bits"
_DocsDevEvReporting_Object = MibTableColumn
docsDevEvReporting = _DocsDevEvReporting_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 5, 7, 1, 2),
    _DocsDevEvReporting_Type()
)
docsDevEvReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevEvReporting.setStatus("current")
_DocsDevEventTable_Object = MibTable
docsDevEventTable = _DocsDevEventTable_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 5, 8)
)
if mibBuilder.loadTexts:
    docsDevEventTable.setStatus("current")
_DocsDevEventEntry_Object = MibTableRow
docsDevEventEntry = _DocsDevEventEntry_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 5, 8, 1)
)
docsDevEventEntry.setIndexNames(
    (0, "DOCS-CABLE-DEVICE-MIB", "docsDevEvIndex"),
)
if mibBuilder.loadTexts:
    docsDevEventEntry.setStatus("current")


class _DocsDevEvIndex_Type(Integer32):
    """Custom type docsDevEvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DocsDevEvIndex_Type.__name__ = "Integer32"
_DocsDevEvIndex_Object = MibTableColumn
docsDevEvIndex = _DocsDevEvIndex_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 5, 8, 1, 1),
    _DocsDevEvIndex_Type()
)
docsDevEvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsDevEvIndex.setStatus("current")
_DocsDevEvFirstTime_Type = DateAndTime
_DocsDevEvFirstTime_Object = MibTableColumn
docsDevEvFirstTime = _DocsDevEvFirstTime_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 5, 8, 1, 2),
    _DocsDevEvFirstTime_Type()
)
docsDevEvFirstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevEvFirstTime.setStatus("current")
_DocsDevEvLastTime_Type = DateAndTime
_DocsDevEvLastTime_Object = MibTableColumn
docsDevEvLastTime = _DocsDevEvLastTime_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 5, 8, 1, 3),
    _DocsDevEvLastTime_Type()
)
docsDevEvLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevEvLastTime.setStatus("current")
_DocsDevEvCounts_Type = Counter32
_DocsDevEvCounts_Object = MibTableColumn
docsDevEvCounts = _DocsDevEvCounts_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 5, 8, 1, 4),
    _DocsDevEvCounts_Type()
)
docsDevEvCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevEvCounts.setStatus("current")
if mibBuilder.loadTexts:
    docsDevEvCounts.setUnits("events")


class _DocsDevEvLevel_Type(Integer32):
    """Custom type docsDevEvLevel based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("information", 7),
          ("notice", 6),
          ("warning", 5))
    )


_DocsDevEvLevel_Type.__name__ = "Integer32"
_DocsDevEvLevel_Object = MibTableColumn
docsDevEvLevel = _DocsDevEvLevel_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 5, 8, 1, 5),
    _DocsDevEvLevel_Type()
)
docsDevEvLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevEvLevel.setStatus("current")
_DocsDevEvId_Type = Unsigned32
_DocsDevEvId_Object = MibTableColumn
docsDevEvId = _DocsDevEvId_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 5, 8, 1, 6),
    _DocsDevEvId_Type()
)
docsDevEvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevEvId.setStatus("current")
_DocsDevEvText_Type = SnmpAdminString
_DocsDevEvText_Object = MibTableColumn
docsDevEvText = _DocsDevEvText_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 5, 8, 1, 7),
    _DocsDevEvText_Type()
)
docsDevEvText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevEvText.setStatus("current")


class _DocsDevEvSyslogAddressType_Type(InetAddressType):
    """Custom type docsDevEvSyslogAddressType based on InetAddressType"""


_DocsDevEvSyslogAddressType_Object = MibScalar
docsDevEvSyslogAddressType = _DocsDevEvSyslogAddressType_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 5, 9),
    _DocsDevEvSyslogAddressType_Type()
)
docsDevEvSyslogAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevEvSyslogAddressType.setStatus("current")
_DocsDevEvSyslogAddress_Type = InetAddress
_DocsDevEvSyslogAddress_Object = MibScalar
docsDevEvSyslogAddress = _DocsDevEvSyslogAddress_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 5, 10),
    _DocsDevEvSyslogAddress_Type()
)
docsDevEvSyslogAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevEvSyslogAddress.setStatus("current")
_DocsDevEvThrottleThresholdExceeded_Type = TruthValue
_DocsDevEvThrottleThresholdExceeded_Object = MibScalar
docsDevEvThrottleThresholdExceeded = _DocsDevEvThrottleThresholdExceeded_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 5, 11),
    _DocsDevEvThrottleThresholdExceeded_Type()
)
docsDevEvThrottleThresholdExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevEvThrottleThresholdExceeded.setStatus("current")
_DocsDevFilter_ObjectIdentity = ObjectIdentity
docsDevFilter = _DocsDevFilter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 69, 1, 6)
)


class _DocsDevFilterLLCUnmatchedAction_Type(Integer32):
    """Custom type docsDevFilterLLCUnmatchedAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("discard", 1))
    )


_DocsDevFilterLLCUnmatchedAction_Type.__name__ = "Integer32"
_DocsDevFilterLLCUnmatchedAction_Object = MibScalar
docsDevFilterLLCUnmatchedAction = _DocsDevFilterLLCUnmatchedAction_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 1),
    _DocsDevFilterLLCUnmatchedAction_Type()
)
docsDevFilterLLCUnmatchedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevFilterLLCUnmatchedAction.setStatus("current")
_DocsDevFilterLLCTable_Object = MibTable
docsDevFilterLLCTable = _DocsDevFilterLLCTable_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 2)
)
if mibBuilder.loadTexts:
    docsDevFilterLLCTable.setStatus("current")
_DocsDevFilterLLCEntry_Object = MibTableRow
docsDevFilterLLCEntry = _DocsDevFilterLLCEntry_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 2, 1)
)
docsDevFilterLLCEntry.setIndexNames(
    (0, "DOCS-CABLE-DEVICE-MIB", "docsDevFilterLLCIndex"),
)
if mibBuilder.loadTexts:
    docsDevFilterLLCEntry.setStatus("current")


class _DocsDevFilterLLCIndex_Type(Integer32):
    """Custom type docsDevFilterLLCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DocsDevFilterLLCIndex_Type.__name__ = "Integer32"
_DocsDevFilterLLCIndex_Object = MibTableColumn
docsDevFilterLLCIndex = _DocsDevFilterLLCIndex_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 2, 1, 1),
    _DocsDevFilterLLCIndex_Type()
)
docsDevFilterLLCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsDevFilterLLCIndex.setStatus("current")
_DocsDevFilterLLCStatus_Type = RowStatus
_DocsDevFilterLLCStatus_Object = MibTableColumn
docsDevFilterLLCStatus = _DocsDevFilterLLCStatus_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 2, 1, 2),
    _DocsDevFilterLLCStatus_Type()
)
docsDevFilterLLCStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterLLCStatus.setStatus("current")
_DocsDevFilterLLCIfIndex_Type = InterfaceIndexOrZero
_DocsDevFilterLLCIfIndex_Object = MibTableColumn
docsDevFilterLLCIfIndex = _DocsDevFilterLLCIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 2, 1, 3),
    _DocsDevFilterLLCIfIndex_Type()
)
docsDevFilterLLCIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterLLCIfIndex.setStatus("current")


class _DocsDevFilterLLCProtocolType_Type(Integer32):
    """Custom type docsDevFilterLLCProtocolType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dsap", 2),
          ("ethertype", 1))
    )


_DocsDevFilterLLCProtocolType_Type.__name__ = "Integer32"
_DocsDevFilterLLCProtocolType_Object = MibTableColumn
docsDevFilterLLCProtocolType = _DocsDevFilterLLCProtocolType_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 2, 1, 4),
    _DocsDevFilterLLCProtocolType_Type()
)
docsDevFilterLLCProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterLLCProtocolType.setStatus("current")


class _DocsDevFilterLLCProtocol_Type(Integer32):
    """Custom type docsDevFilterLLCProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsDevFilterLLCProtocol_Type.__name__ = "Integer32"
_DocsDevFilterLLCProtocol_Object = MibTableColumn
docsDevFilterLLCProtocol = _DocsDevFilterLLCProtocol_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 2, 1, 5),
    _DocsDevFilterLLCProtocol_Type()
)
docsDevFilterLLCProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterLLCProtocol.setStatus("current")
_DocsDevFilterLLCMatches_Type = Counter32
_DocsDevFilterLLCMatches_Object = MibTableColumn
docsDevFilterLLCMatches = _DocsDevFilterLLCMatches_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 2, 1, 6),
    _DocsDevFilterLLCMatches_Type()
)
docsDevFilterLLCMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevFilterLLCMatches.setStatus("current")
if mibBuilder.loadTexts:
    docsDevFilterLLCMatches.setUnits("matches")


class _DocsDevFilterIpDefault_Type(Integer32):
    """Custom type docsDevFilterIpDefault based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("discard", 1))
    )


_DocsDevFilterIpDefault_Type.__name__ = "Integer32"
_DocsDevFilterIpDefault_Object = MibScalar
docsDevFilterIpDefault = _DocsDevFilterIpDefault_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 3),
    _DocsDevFilterIpDefault_Type()
)
docsDevFilterIpDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevFilterIpDefault.setStatus("deprecated")
_DocsDevFilterIpTable_Object = MibTable
docsDevFilterIpTable = _DocsDevFilterIpTable_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 4)
)
if mibBuilder.loadTexts:
    docsDevFilterIpTable.setStatus("deprecated")
_DocsDevFilterIpEntry_Object = MibTableRow
docsDevFilterIpEntry = _DocsDevFilterIpEntry_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 4, 1)
)
docsDevFilterIpEntry.setIndexNames(
    (0, "DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpIndex"),
)
if mibBuilder.loadTexts:
    docsDevFilterIpEntry.setStatus("deprecated")


class _DocsDevFilterIpIndex_Type(Integer32):
    """Custom type docsDevFilterIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DocsDevFilterIpIndex_Type.__name__ = "Integer32"
_DocsDevFilterIpIndex_Object = MibTableColumn
docsDevFilterIpIndex = _DocsDevFilterIpIndex_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 4, 1, 1),
    _DocsDevFilterIpIndex_Type()
)
docsDevFilterIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsDevFilterIpIndex.setStatus("deprecated")
_DocsDevFilterIpStatus_Type = RowStatus
_DocsDevFilterIpStatus_Object = MibTableColumn
docsDevFilterIpStatus = _DocsDevFilterIpStatus_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 4, 1, 2),
    _DocsDevFilterIpStatus_Type()
)
docsDevFilterIpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpStatus.setStatus("deprecated")


class _DocsDevFilterIpControl_Type(Integer32):
    """Custom type docsDevFilterIpControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accept", 2),
          ("discard", 1),
          ("policy", 3))
    )


_DocsDevFilterIpControl_Type.__name__ = "Integer32"
_DocsDevFilterIpControl_Object = MibTableColumn
docsDevFilterIpControl = _DocsDevFilterIpControl_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 4, 1, 3),
    _DocsDevFilterIpControl_Type()
)
docsDevFilterIpControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpControl.setStatus("deprecated")
_DocsDevFilterIpIfIndex_Type = InterfaceIndexOrZero
_DocsDevFilterIpIfIndex_Object = MibTableColumn
docsDevFilterIpIfIndex = _DocsDevFilterIpIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 4, 1, 4),
    _DocsDevFilterIpIfIndex_Type()
)
docsDevFilterIpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpIfIndex.setStatus("deprecated")


class _DocsDevFilterIpDirection_Type(Integer32):
    """Custom type docsDevFilterIpDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("inbound", 1),
          ("outbound", 2))
    )


_DocsDevFilterIpDirection_Type.__name__ = "Integer32"
_DocsDevFilterIpDirection_Object = MibTableColumn
docsDevFilterIpDirection = _DocsDevFilterIpDirection_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 4, 1, 5),
    _DocsDevFilterIpDirection_Type()
)
docsDevFilterIpDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpDirection.setStatus("deprecated")


class _DocsDevFilterIpBroadcast_Type(TruthValue):
    """Custom type docsDevFilterIpBroadcast based on TruthValue"""


_DocsDevFilterIpBroadcast_Object = MibTableColumn
docsDevFilterIpBroadcast = _DocsDevFilterIpBroadcast_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 4, 1, 6),
    _DocsDevFilterIpBroadcast_Type()
)
docsDevFilterIpBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpBroadcast.setStatus("deprecated")


class _DocsDevFilterIpSaddr_Type(IpAddress):
    """Custom type docsDevFilterIpSaddr based on IpAddress"""
    defaultHexValue = "00000000"


_DocsDevFilterIpSaddr_Object = MibTableColumn
docsDevFilterIpSaddr = _DocsDevFilterIpSaddr_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 4, 1, 7),
    _DocsDevFilterIpSaddr_Type()
)
docsDevFilterIpSaddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpSaddr.setStatus("deprecated")


class _DocsDevFilterIpSmask_Type(IpAddress):
    """Custom type docsDevFilterIpSmask based on IpAddress"""
    defaultHexValue = "00000000"


_DocsDevFilterIpSmask_Object = MibTableColumn
docsDevFilterIpSmask = _DocsDevFilterIpSmask_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 4, 1, 8),
    _DocsDevFilterIpSmask_Type()
)
docsDevFilterIpSmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpSmask.setStatus("deprecated")


class _DocsDevFilterIpDaddr_Type(IpAddress):
    """Custom type docsDevFilterIpDaddr based on IpAddress"""
    defaultHexValue = "00000000"


_DocsDevFilterIpDaddr_Object = MibTableColumn
docsDevFilterIpDaddr = _DocsDevFilterIpDaddr_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 4, 1, 9),
    _DocsDevFilterIpDaddr_Type()
)
docsDevFilterIpDaddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpDaddr.setStatus("deprecated")


class _DocsDevFilterIpDmask_Type(IpAddress):
    """Custom type docsDevFilterIpDmask based on IpAddress"""
    defaultHexValue = "00000000"


_DocsDevFilterIpDmask_Object = MibTableColumn
docsDevFilterIpDmask = _DocsDevFilterIpDmask_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 4, 1, 10),
    _DocsDevFilterIpDmask_Type()
)
docsDevFilterIpDmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpDmask.setStatus("deprecated")


class _DocsDevFilterIpProtocol_Type(Integer32):
    """Custom type docsDevFilterIpProtocol based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_DocsDevFilterIpProtocol_Type.__name__ = "Integer32"
_DocsDevFilterIpProtocol_Object = MibTableColumn
docsDevFilterIpProtocol = _DocsDevFilterIpProtocol_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 4, 1, 11),
    _DocsDevFilterIpProtocol_Type()
)
docsDevFilterIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpProtocol.setStatus("deprecated")


class _DocsDevFilterIpSourcePortLow_Type(Integer32):
    """Custom type docsDevFilterIpSourcePortLow based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsDevFilterIpSourcePortLow_Type.__name__ = "Integer32"
_DocsDevFilterIpSourcePortLow_Object = MibTableColumn
docsDevFilterIpSourcePortLow = _DocsDevFilterIpSourcePortLow_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 4, 1, 12),
    _DocsDevFilterIpSourcePortLow_Type()
)
docsDevFilterIpSourcePortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpSourcePortLow.setStatus("deprecated")


class _DocsDevFilterIpSourcePortHigh_Type(Integer32):
    """Custom type docsDevFilterIpSourcePortHigh based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsDevFilterIpSourcePortHigh_Type.__name__ = "Integer32"
_DocsDevFilterIpSourcePortHigh_Object = MibTableColumn
docsDevFilterIpSourcePortHigh = _DocsDevFilterIpSourcePortHigh_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 4, 1, 13),
    _DocsDevFilterIpSourcePortHigh_Type()
)
docsDevFilterIpSourcePortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpSourcePortHigh.setStatus("deprecated")


class _DocsDevFilterIpDestPortLow_Type(Integer32):
    """Custom type docsDevFilterIpDestPortLow based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsDevFilterIpDestPortLow_Type.__name__ = "Integer32"
_DocsDevFilterIpDestPortLow_Object = MibTableColumn
docsDevFilterIpDestPortLow = _DocsDevFilterIpDestPortLow_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 4, 1, 14),
    _DocsDevFilterIpDestPortLow_Type()
)
docsDevFilterIpDestPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpDestPortLow.setStatus("deprecated")


class _DocsDevFilterIpDestPortHigh_Type(Integer32):
    """Custom type docsDevFilterIpDestPortHigh based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DocsDevFilterIpDestPortHigh_Type.__name__ = "Integer32"
_DocsDevFilterIpDestPortHigh_Object = MibTableColumn
docsDevFilterIpDestPortHigh = _DocsDevFilterIpDestPortHigh_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 4, 1, 15),
    _DocsDevFilterIpDestPortHigh_Type()
)
docsDevFilterIpDestPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpDestPortHigh.setStatus("deprecated")
_DocsDevFilterIpMatches_Type = ZeroBasedCounter32
_DocsDevFilterIpMatches_Object = MibTableColumn
docsDevFilterIpMatches = _DocsDevFilterIpMatches_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 4, 1, 16),
    _DocsDevFilterIpMatches_Type()
)
docsDevFilterIpMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevFilterIpMatches.setStatus("deprecated")
if mibBuilder.loadTexts:
    docsDevFilterIpMatches.setUnits("matches")


class _DocsDevFilterIpTos_Type(OctetString):
    """Custom type docsDevFilterIpTos based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsDevFilterIpTos_Type.__name__ = "OctetString"
_DocsDevFilterIpTos_Object = MibTableColumn
docsDevFilterIpTos = _DocsDevFilterIpTos_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 4, 1, 17),
    _DocsDevFilterIpTos_Type()
)
docsDevFilterIpTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpTos.setStatus("deprecated")


class _DocsDevFilterIpTosMask_Type(OctetString):
    """Custom type docsDevFilterIpTosMask based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsDevFilterIpTosMask_Type.__name__ = "OctetString"
_DocsDevFilterIpTosMask_Object = MibTableColumn
docsDevFilterIpTosMask = _DocsDevFilterIpTosMask_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 4, 1, 18),
    _DocsDevFilterIpTosMask_Type()
)
docsDevFilterIpTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpTosMask.setStatus("deprecated")


class _DocsDevFilterIpContinue_Type(TruthValue):
    """Custom type docsDevFilterIpContinue based on TruthValue"""


_DocsDevFilterIpContinue_Object = MibTableColumn
docsDevFilterIpContinue = _DocsDevFilterIpContinue_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 4, 1, 19),
    _DocsDevFilterIpContinue_Type()
)
docsDevFilterIpContinue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpContinue.setStatus("deprecated")


class _DocsDevFilterIpPolicyId_Type(Integer32):
    """Custom type docsDevFilterIpPolicyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DocsDevFilterIpPolicyId_Type.__name__ = "Integer32"
_DocsDevFilterIpPolicyId_Object = MibTableColumn
docsDevFilterIpPolicyId = _DocsDevFilterIpPolicyId_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 4, 1, 20),
    _DocsDevFilterIpPolicyId_Type()
)
docsDevFilterIpPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpPolicyId.setStatus("deprecated")
_DocsDevFilterPolicyTable_Object = MibTable
docsDevFilterPolicyTable = _DocsDevFilterPolicyTable_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 5)
)
if mibBuilder.loadTexts:
    docsDevFilterPolicyTable.setStatus("deprecated")
_DocsDevFilterPolicyEntry_Object = MibTableRow
docsDevFilterPolicyEntry = _DocsDevFilterPolicyEntry_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 5, 1)
)
docsDevFilterPolicyEntry.setIndexNames(
    (0, "DOCS-CABLE-DEVICE-MIB", "docsDevFilterPolicyIndex"),
)
if mibBuilder.loadTexts:
    docsDevFilterPolicyEntry.setStatus("deprecated")


class _DocsDevFilterPolicyIndex_Type(Integer32):
    """Custom type docsDevFilterPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DocsDevFilterPolicyIndex_Type.__name__ = "Integer32"
_DocsDevFilterPolicyIndex_Object = MibTableColumn
docsDevFilterPolicyIndex = _DocsDevFilterPolicyIndex_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 5, 1, 1),
    _DocsDevFilterPolicyIndex_Type()
)
docsDevFilterPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsDevFilterPolicyIndex.setStatus("deprecated")


class _DocsDevFilterPolicyId_Type(Integer32):
    """Custom type docsDevFilterPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DocsDevFilterPolicyId_Type.__name__ = "Integer32"
_DocsDevFilterPolicyId_Object = MibTableColumn
docsDevFilterPolicyId = _DocsDevFilterPolicyId_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 5, 1, 2),
    _DocsDevFilterPolicyId_Type()
)
docsDevFilterPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterPolicyId.setStatus("deprecated")
_DocsDevFilterPolicyStatus_Type = RowStatus
_DocsDevFilterPolicyStatus_Object = MibTableColumn
docsDevFilterPolicyStatus = _DocsDevFilterPolicyStatus_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 5, 1, 5),
    _DocsDevFilterPolicyStatus_Type()
)
docsDevFilterPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterPolicyStatus.setStatus("deprecated")


class _DocsDevFilterPolicyPtr_Type(RowPointer):
    """Custom type docsDevFilterPolicyPtr based on RowPointer"""
    defaultValue = (0, 0)


_DocsDevFilterPolicyPtr_Object = MibTableColumn
docsDevFilterPolicyPtr = _DocsDevFilterPolicyPtr_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 5, 1, 6),
    _DocsDevFilterPolicyPtr_Type()
)
docsDevFilterPolicyPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterPolicyPtr.setStatus("deprecated")
_DocsDevFilterTosTable_Object = MibTable
docsDevFilterTosTable = _DocsDevFilterTosTable_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 6)
)
if mibBuilder.loadTexts:
    docsDevFilterTosTable.setStatus("deprecated")
_DocsDevFilterTosEntry_Object = MibTableRow
docsDevFilterTosEntry = _DocsDevFilterTosEntry_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 6, 1)
)
docsDevFilterTosEntry.setIndexNames(
    (0, "DOCS-CABLE-DEVICE-MIB", "docsDevFilterTosIndex"),
)
if mibBuilder.loadTexts:
    docsDevFilterTosEntry.setStatus("deprecated")


class _DocsDevFilterTosIndex_Type(Integer32):
    """Custom type docsDevFilterTosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DocsDevFilterTosIndex_Type.__name__ = "Integer32"
_DocsDevFilterTosIndex_Object = MibTableColumn
docsDevFilterTosIndex = _DocsDevFilterTosIndex_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 6, 1, 1),
    _DocsDevFilterTosIndex_Type()
)
docsDevFilterTosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsDevFilterTosIndex.setStatus("deprecated")
_DocsDevFilterTosStatus_Type = RowStatus
_DocsDevFilterTosStatus_Object = MibTableColumn
docsDevFilterTosStatus = _DocsDevFilterTosStatus_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 6, 1, 2),
    _DocsDevFilterTosStatus_Type()
)
docsDevFilterTosStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterTosStatus.setStatus("deprecated")


class _DocsDevFilterTosAndMask_Type(OctetString):
    """Custom type docsDevFilterTosAndMask based on OctetString"""
    defaultHexValue = "ff"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsDevFilterTosAndMask_Type.__name__ = "OctetString"
_DocsDevFilterTosAndMask_Object = MibTableColumn
docsDevFilterTosAndMask = _DocsDevFilterTosAndMask_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 6, 1, 3),
    _DocsDevFilterTosAndMask_Type()
)
docsDevFilterTosAndMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterTosAndMask.setStatus("deprecated")


class _DocsDevFilterTosOrMask_Type(OctetString):
    """Custom type docsDevFilterTosOrMask based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DocsDevFilterTosOrMask_Type.__name__ = "OctetString"
_DocsDevFilterTosOrMask_Object = MibTableColumn
docsDevFilterTosOrMask = _DocsDevFilterTosOrMask_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 6, 6, 1, 4),
    _DocsDevFilterTosOrMask_Type()
)
docsDevFilterTosOrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterTosOrMask.setStatus("deprecated")
_DocsDevCpe_ObjectIdentity = ObjectIdentity
docsDevCpe = _DocsDevCpe_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 69, 1, 7)
)


class _DocsDevCpeEnroll_Type(Integer32):
    """Custom type docsDevCpeEnroll based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 2),
          ("none", 1))
    )


_DocsDevCpeEnroll_Type.__name__ = "Integer32"
_DocsDevCpeEnroll_Object = MibScalar
docsDevCpeEnroll = _DocsDevCpeEnroll_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 7, 1),
    _DocsDevCpeEnroll_Type()
)
docsDevCpeEnroll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevCpeEnroll.setStatus("current")


class _DocsDevCpeIpMax_Type(Integer32):
    """Custom type docsDevCpeIpMax based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_DocsDevCpeIpMax_Type.__name__ = "Integer32"
_DocsDevCpeIpMax_Object = MibScalar
docsDevCpeIpMax = _DocsDevCpeIpMax_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 7, 2),
    _DocsDevCpeIpMax_Type()
)
docsDevCpeIpMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevCpeIpMax.setStatus("current")
_DocsDevCpeTable_Object = MibTable
docsDevCpeTable = _DocsDevCpeTable_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 7, 3)
)
if mibBuilder.loadTexts:
    docsDevCpeTable.setStatus("deprecated")
_DocsDevCpeEntry_Object = MibTableRow
docsDevCpeEntry = _DocsDevCpeEntry_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 7, 3, 1)
)
docsDevCpeEntry.setIndexNames(
    (0, "DOCS-CABLE-DEVICE-MIB", "docsDevCpeIp"),
)
if mibBuilder.loadTexts:
    docsDevCpeEntry.setStatus("deprecated")
_DocsDevCpeIp_Type = IpAddress
_DocsDevCpeIp_Object = MibTableColumn
docsDevCpeIp = _DocsDevCpeIp_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 7, 3, 1, 1),
    _DocsDevCpeIp_Type()
)
docsDevCpeIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsDevCpeIp.setStatus("deprecated")


class _DocsDevCpeSource_Type(Integer32):
    """Custom type docsDevCpeSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("learned", 3),
          ("manual", 2),
          ("other", 1))
    )


_DocsDevCpeSource_Type.__name__ = "Integer32"
_DocsDevCpeSource_Object = MibTableColumn
docsDevCpeSource = _DocsDevCpeSource_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 7, 3, 1, 2),
    _DocsDevCpeSource_Type()
)
docsDevCpeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevCpeSource.setStatus("deprecated")
_DocsDevCpeStatus_Type = RowStatus
_DocsDevCpeStatus_Object = MibTableColumn
docsDevCpeStatus = _DocsDevCpeStatus_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 7, 3, 1, 3),
    _DocsDevCpeStatus_Type()
)
docsDevCpeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevCpeStatus.setStatus("deprecated")
_DocsDevCpeInetTable_Object = MibTable
docsDevCpeInetTable = _DocsDevCpeInetTable_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 7, 4)
)
if mibBuilder.loadTexts:
    docsDevCpeInetTable.setStatus("current")
_DocsDevCpeInetEntry_Object = MibTableRow
docsDevCpeInetEntry = _DocsDevCpeInetEntry_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 7, 4, 1)
)
docsDevCpeInetEntry.setIndexNames(
    (0, "DOCS-CABLE-DEVICE-MIB", "docsDevCpeInetType"),
    (0, "DOCS-CABLE-DEVICE-MIB", "docsDevCpeInetAddr"),
)
if mibBuilder.loadTexts:
    docsDevCpeInetEntry.setStatus("current")
_DocsDevCpeInetType_Type = InetAddressType
_DocsDevCpeInetType_Object = MibTableColumn
docsDevCpeInetType = _DocsDevCpeInetType_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 7, 4, 1, 1),
    _DocsDevCpeInetType_Type()
)
docsDevCpeInetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsDevCpeInetType.setStatus("current")
_DocsDevCpeInetAddr_Type = InetAddress
_DocsDevCpeInetAddr_Object = MibTableColumn
docsDevCpeInetAddr = _DocsDevCpeInetAddr_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 7, 4, 1, 2),
    _DocsDevCpeInetAddr_Type()
)
docsDevCpeInetAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsDevCpeInetAddr.setStatus("current")


class _DocsDevCpeInetSource_Type(Integer32):
    """Custom type docsDevCpeInetSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("learned", 3),
          ("manual", 2))
    )


_DocsDevCpeInetSource_Type.__name__ = "Integer32"
_DocsDevCpeInetSource_Object = MibTableColumn
docsDevCpeInetSource = _DocsDevCpeInetSource_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 7, 4, 1, 3),
    _DocsDevCpeInetSource_Type()
)
docsDevCpeInetSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevCpeInetSource.setStatus("current")
_DocsDevCpeInetRowStatus_Type = RowStatus
_DocsDevCpeInetRowStatus_Object = MibTableColumn
docsDevCpeInetRowStatus = _DocsDevCpeInetRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 69, 1, 7, 4, 1, 4),
    _DocsDevCpeInetRowStatus_Type()
)
docsDevCpeInetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevCpeInetRowStatus.setStatus("current")
_DocsDevNotification_ObjectIdentity = ObjectIdentity
docsDevNotification = _DocsDevNotification_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 69, 2)
)
_DocsDevConformance_ObjectIdentity = ObjectIdentity
docsDevConformance = _DocsDevConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 69, 3)
)
_DocsDevGroups_ObjectIdentity = ObjectIdentity
docsDevGroups = _DocsDevGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 69, 3, 1)
)
_DocsDevCompliances_ObjectIdentity = ObjectIdentity
docsDevCompliances = _DocsDevCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 69, 3, 2)
)
_DocsDevGroupsV2_ObjectIdentity = ObjectIdentity
docsDevGroupsV2 = _DocsDevGroupsV2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 69, 3, 3)
)
_DocsDevCompliancesV2_ObjectIdentity = ObjectIdentity
docsDevCompliancesV2 = _DocsDevCompliancesV2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 69, 3, 4)
)

# Managed Objects groups

docsDevBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 69, 3, 1, 1)
)
docsDevBaseGroup.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevRole"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevDateTime"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevResetNow"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSerialNumber"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSTPControl"))
)
if mibBuilder.loadTexts:
    docsDevBaseGroup.setStatus("current")

docsDevNmAccessGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 69, 3, 1, 2)
)
docsDevNmAccessGroup.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevNmAccessIp"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevNmAccessIpMask"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevNmAccessCommunity"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevNmAccessControl"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevNmAccessInterfaces"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevNmAccessStatus"))
)
if mibBuilder.loadTexts:
    docsDevNmAccessGroup.setStatus("deprecated")

docsDevSoftwareGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 69, 3, 1, 3)
)
docsDevSoftwareGroup.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevSwServer"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwFilename"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwAdminStatus"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwOperStatus"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwCurrentVers"))
)
if mibBuilder.loadTexts:
    docsDevSoftwareGroup.setStatus("deprecated")

docsDevServerGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 69, 3, 1, 4)
)
docsDevServerGroup.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevServerBootState"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevServerDhcp"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevServerTime"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevServerTftp"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevServerConfigFile"))
)
if mibBuilder.loadTexts:
    docsDevServerGroup.setStatus("deprecated")

docsDevEventGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 69, 3, 1, 5)
)
docsDevEventGroup.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvControl"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvSyslog"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvThrottleAdminStatus"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvThrottleInhibited"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvThrottleThreshold"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvThrottleInterval"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvReporting"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvFirstTime"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvLastTime"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvCounts"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"))
)
if mibBuilder.loadTexts:
    docsDevEventGroup.setStatus("deprecated")

docsDevFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 69, 3, 1, 6)
)
docsDevFilterGroup.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevFilterLLCUnmatchedAction"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpDefault"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterLLCStatus"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterLLCIfIndex"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterLLCProtocolType"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterLLCProtocol"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterLLCMatches"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpControl"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpIfIndex"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpStatus"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpDirection"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpBroadcast"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpSaddr"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpSmask"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpDaddr"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpDmask"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpProtocol"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpSourcePortLow"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpSourcePortHigh"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpDestPortLow"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpDestPortHigh"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpMatches"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpTos"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpTosMask"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpContinue"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpPolicyId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterPolicyId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterPolicyStatus"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterPolicyPtr"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterTosStatus"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterTosAndMask"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterTosOrMask"))
)
if mibBuilder.loadTexts:
    docsDevFilterGroup.setStatus("deprecated")

docsDevCpeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 69, 3, 1, 7)
)
docsDevCpeGroup.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevCpeEnroll"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevCpeIpMax"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevCpeSource"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevCpeStatus"))
)
if mibBuilder.loadTexts:
    docsDevCpeGroup.setStatus("deprecated")

docsDevBaseIgmpGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 69, 3, 3, 1)
)
docsDevBaseIgmpGroup.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevIgmpModeControl")
)
if mibBuilder.loadTexts:
    docsDevBaseIgmpGroup.setStatus("current")

docsDevBaseMaxCpeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 69, 3, 3, 2)
)
docsDevBaseMaxCpeGroup.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevMaxCpe")
)
if mibBuilder.loadTexts:
    docsDevBaseMaxCpeGroup.setStatus("current")

docsDevNmAccessExtGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 69, 3, 3, 3)
)
docsDevNmAccessExtGroup.setObjects(
    ("DOCS-CABLE-DEVICE-MIB", "docsDevNmAccessTrapVersion")
)
if mibBuilder.loadTexts:
    docsDevNmAccessExtGroup.setStatus("deprecated")

docsDevSoftwareGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 69, 3, 3, 4)
)
docsDevSoftwareGroupV2.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevSwFilename"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwAdminStatus"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwOperStatus"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwCurrentVers"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwServerAddressType"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwServerAddress"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwServerTransportProtocol"))
)
if mibBuilder.loadTexts:
    docsDevSoftwareGroupV2.setStatus("current")

docsDevServerGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 69, 3, 3, 5)
)
docsDevServerGroupV2.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevServerBootState"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevServerDhcpAddressType"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevServerDhcpAddress"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevServerTimeAddressType"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevServerTimeAddress"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevServerConfigTftpAddressType"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevServerConfigTftpAddress"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevServerConfigFile"))
)
if mibBuilder.loadTexts:
    docsDevServerGroupV2.setStatus("current")

docsDevEventGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 69, 3, 3, 6)
)
docsDevEventGroupV2.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvControl"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvThrottleAdminStatus"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvThrottleThreshold"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvThrottleInterval"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvReporting"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvFirstTime"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvLastTime"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvCounts"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvSyslogAddressType"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvSyslogAddress"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvThrottleThresholdExceeded"))
)
if mibBuilder.loadTexts:
    docsDevEventGroupV2.setStatus("current")

docsDevFilterLLCGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 69, 3, 3, 7)
)
docsDevFilterLLCGroup.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevFilterLLCUnmatchedAction"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterLLCStatus"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterLLCIfIndex"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterLLCProtocolType"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterLLCProtocol"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevFilterLLCMatches"))
)
if mibBuilder.loadTexts:
    docsDevFilterLLCGroup.setStatus("current")

docsDevInetCpeGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 69, 3, 3, 8)
)
docsDevInetCpeGroup.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevCpeEnroll"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevCpeIpMax"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevCpeInetSource"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevCpeInetRowStatus"))
)
if mibBuilder.loadTexts:
    docsDevInetCpeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsDevBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 69, 3, 2, 1)
)
if mibBuilder.loadTexts:
    docsDevBasicCompliance.setStatus(
        "deprecated"
    )

docsDevCmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 69, 3, 4, 1)
)
if mibBuilder.loadTexts:
    docsDevCmCompliance.setStatus(
        "current"
    )

docsDevCmtsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 69, 3, 4, 2)
)
if mibBuilder.loadTexts:
    docsDevCmtsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-CABLE-DEVICE-MIB",
    **{"docsDev": docsDev,
       "docsDevNotifications": docsDevNotifications,
       "docsDevMIBObjects": docsDevMIBObjects,
       "docsDevBase": docsDevBase,
       "docsDevRole": docsDevRole,
       "docsDevDateTime": docsDevDateTime,
       "docsDevResetNow": docsDevResetNow,
       "docsDevSerialNumber": docsDevSerialNumber,
       "docsDevSTPControl": docsDevSTPControl,
       "docsDevIgmpModeControl": docsDevIgmpModeControl,
       "docsDevMaxCpe": docsDevMaxCpe,
       "docsDevNmAccessTable": docsDevNmAccessTable,
       "docsDevNmAccessEntry": docsDevNmAccessEntry,
       "docsDevNmAccessIndex": docsDevNmAccessIndex,
       "docsDevNmAccessIp": docsDevNmAccessIp,
       "docsDevNmAccessIpMask": docsDevNmAccessIpMask,
       "docsDevNmAccessCommunity": docsDevNmAccessCommunity,
       "docsDevNmAccessControl": docsDevNmAccessControl,
       "docsDevNmAccessInterfaces": docsDevNmAccessInterfaces,
       "docsDevNmAccessStatus": docsDevNmAccessStatus,
       "docsDevNmAccessTrapVersion": docsDevNmAccessTrapVersion,
       "docsDevSoftware": docsDevSoftware,
       "docsDevSwServer": docsDevSwServer,
       "docsDevSwFilename": docsDevSwFilename,
       "docsDevSwAdminStatus": docsDevSwAdminStatus,
       "docsDevSwOperStatus": docsDevSwOperStatus,
       "docsDevSwCurrentVers": docsDevSwCurrentVers,
       "docsDevSwServerAddressType": docsDevSwServerAddressType,
       "docsDevSwServerAddress": docsDevSwServerAddress,
       "docsDevSwServerTransportProtocol": docsDevSwServerTransportProtocol,
       "docsDevServer": docsDevServer,
       "docsDevServerBootState": docsDevServerBootState,
       "docsDevServerDhcp": docsDevServerDhcp,
       "docsDevServerTime": docsDevServerTime,
       "docsDevServerTftp": docsDevServerTftp,
       "docsDevServerConfigFile": docsDevServerConfigFile,
       "docsDevServerDhcpAddressType": docsDevServerDhcpAddressType,
       "docsDevServerDhcpAddress": docsDevServerDhcpAddress,
       "docsDevServerTimeAddressType": docsDevServerTimeAddressType,
       "docsDevServerTimeAddress": docsDevServerTimeAddress,
       "docsDevServerConfigTftpAddressType": docsDevServerConfigTftpAddressType,
       "docsDevServerConfigTftpAddress": docsDevServerConfigTftpAddress,
       "docsDevEvent": docsDevEvent,
       "docsDevEvControl": docsDevEvControl,
       "docsDevEvSyslog": docsDevEvSyslog,
       "docsDevEvThrottleAdminStatus": docsDevEvThrottleAdminStatus,
       "docsDevEvThrottleInhibited": docsDevEvThrottleInhibited,
       "docsDevEvThrottleThreshold": docsDevEvThrottleThreshold,
       "docsDevEvThrottleInterval": docsDevEvThrottleInterval,
       "docsDevEvControlTable": docsDevEvControlTable,
       "docsDevEvControlEntry": docsDevEvControlEntry,
       "docsDevEvPriority": docsDevEvPriority,
       "docsDevEvReporting": docsDevEvReporting,
       "docsDevEventTable": docsDevEventTable,
       "docsDevEventEntry": docsDevEventEntry,
       "docsDevEvIndex": docsDevEvIndex,
       "docsDevEvFirstTime": docsDevEvFirstTime,
       "docsDevEvLastTime": docsDevEvLastTime,
       "docsDevEvCounts": docsDevEvCounts,
       "docsDevEvLevel": docsDevEvLevel,
       "docsDevEvId": docsDevEvId,
       "docsDevEvText": docsDevEvText,
       "docsDevEvSyslogAddressType": docsDevEvSyslogAddressType,
       "docsDevEvSyslogAddress": docsDevEvSyslogAddress,
       "docsDevEvThrottleThresholdExceeded": docsDevEvThrottleThresholdExceeded,
       "docsDevFilter": docsDevFilter,
       "docsDevFilterLLCUnmatchedAction": docsDevFilterLLCUnmatchedAction,
       "docsDevFilterLLCTable": docsDevFilterLLCTable,
       "docsDevFilterLLCEntry": docsDevFilterLLCEntry,
       "docsDevFilterLLCIndex": docsDevFilterLLCIndex,
       "docsDevFilterLLCStatus": docsDevFilterLLCStatus,
       "docsDevFilterLLCIfIndex": docsDevFilterLLCIfIndex,
       "docsDevFilterLLCProtocolType": docsDevFilterLLCProtocolType,
       "docsDevFilterLLCProtocol": docsDevFilterLLCProtocol,
       "docsDevFilterLLCMatches": docsDevFilterLLCMatches,
       "docsDevFilterIpDefault": docsDevFilterIpDefault,
       "docsDevFilterIpTable": docsDevFilterIpTable,
       "docsDevFilterIpEntry": docsDevFilterIpEntry,
       "docsDevFilterIpIndex": docsDevFilterIpIndex,
       "docsDevFilterIpStatus": docsDevFilterIpStatus,
       "docsDevFilterIpControl": docsDevFilterIpControl,
       "docsDevFilterIpIfIndex": docsDevFilterIpIfIndex,
       "docsDevFilterIpDirection": docsDevFilterIpDirection,
       "docsDevFilterIpBroadcast": docsDevFilterIpBroadcast,
       "docsDevFilterIpSaddr": docsDevFilterIpSaddr,
       "docsDevFilterIpSmask": docsDevFilterIpSmask,
       "docsDevFilterIpDaddr": docsDevFilterIpDaddr,
       "docsDevFilterIpDmask": docsDevFilterIpDmask,
       "docsDevFilterIpProtocol": docsDevFilterIpProtocol,
       "docsDevFilterIpSourcePortLow": docsDevFilterIpSourcePortLow,
       "docsDevFilterIpSourcePortHigh": docsDevFilterIpSourcePortHigh,
       "docsDevFilterIpDestPortLow": docsDevFilterIpDestPortLow,
       "docsDevFilterIpDestPortHigh": docsDevFilterIpDestPortHigh,
       "docsDevFilterIpMatches": docsDevFilterIpMatches,
       "docsDevFilterIpTos": docsDevFilterIpTos,
       "docsDevFilterIpTosMask": docsDevFilterIpTosMask,
       "docsDevFilterIpContinue": docsDevFilterIpContinue,
       "docsDevFilterIpPolicyId": docsDevFilterIpPolicyId,
       "docsDevFilterPolicyTable": docsDevFilterPolicyTable,
       "docsDevFilterPolicyEntry": docsDevFilterPolicyEntry,
       "docsDevFilterPolicyIndex": docsDevFilterPolicyIndex,
       "docsDevFilterPolicyId": docsDevFilterPolicyId,
       "docsDevFilterPolicyStatus": docsDevFilterPolicyStatus,
       "docsDevFilterPolicyPtr": docsDevFilterPolicyPtr,
       "docsDevFilterTosTable": docsDevFilterTosTable,
       "docsDevFilterTosEntry": docsDevFilterTosEntry,
       "docsDevFilterTosIndex": docsDevFilterTosIndex,
       "docsDevFilterTosStatus": docsDevFilterTosStatus,
       "docsDevFilterTosAndMask": docsDevFilterTosAndMask,
       "docsDevFilterTosOrMask": docsDevFilterTosOrMask,
       "docsDevCpe": docsDevCpe,
       "docsDevCpeEnroll": docsDevCpeEnroll,
       "docsDevCpeIpMax": docsDevCpeIpMax,
       "docsDevCpeTable": docsDevCpeTable,
       "docsDevCpeEntry": docsDevCpeEntry,
       "docsDevCpeIp": docsDevCpeIp,
       "docsDevCpeSource": docsDevCpeSource,
       "docsDevCpeStatus": docsDevCpeStatus,
       "docsDevCpeInetTable": docsDevCpeInetTable,
       "docsDevCpeInetEntry": docsDevCpeInetEntry,
       "docsDevCpeInetType": docsDevCpeInetType,
       "docsDevCpeInetAddr": docsDevCpeInetAddr,
       "docsDevCpeInetSource": docsDevCpeInetSource,
       "docsDevCpeInetRowStatus": docsDevCpeInetRowStatus,
       "docsDevNotification": docsDevNotification,
       "docsDevConformance": docsDevConformance,
       "docsDevGroups": docsDevGroups,
       "docsDevBaseGroup": docsDevBaseGroup,
       "docsDevNmAccessGroup": docsDevNmAccessGroup,
       "docsDevSoftwareGroup": docsDevSoftwareGroup,
       "docsDevServerGroup": docsDevServerGroup,
       "docsDevEventGroup": docsDevEventGroup,
       "docsDevFilterGroup": docsDevFilterGroup,
       "docsDevCpeGroup": docsDevCpeGroup,
       "docsDevCompliances": docsDevCompliances,
       "docsDevBasicCompliance": docsDevBasicCompliance,
       "docsDevGroupsV2": docsDevGroupsV2,
       "docsDevBaseIgmpGroup": docsDevBaseIgmpGroup,
       "docsDevBaseMaxCpeGroup": docsDevBaseMaxCpeGroup,
       "docsDevNmAccessExtGroup": docsDevNmAccessExtGroup,
       "docsDevSoftwareGroupV2": docsDevSoftwareGroupV2,
       "docsDevServerGroupV2": docsDevServerGroupV2,
       "docsDevEventGroupV2": docsDevEventGroupV2,
       "docsDevFilterLLCGroup": docsDevFilterLLCGroup,
       "docsDevInetCpeGroup": docsDevInetCpeGroup,
       "docsDevCompliancesV2": docsDevCompliancesV2,
       "docsDevCmCompliance": docsDevCmCompliance,
       "docsDevCmtsCompliance": docsDevCmtsCompliance}
)
