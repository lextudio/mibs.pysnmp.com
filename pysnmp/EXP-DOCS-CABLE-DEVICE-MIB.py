# SNMP MIB module (EXP-DOCS-CABLE-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXP-DOCS-CABLE-DEVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:09 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(vacmAccessEntry,) = mibBuilder.importSymbols(
    "SNMP-VIEW-BASED-ACM-MIB",
    "vacmAccessEntry")

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
 experimental,
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
    "experimental",
    "iso",
    "mib-2",
    "zeroDotZero")

(DateAndTime,
 DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

docsDev = ModuleIdentity(
    (1, 3, 6, 1, 3, 83)
)
docsDev.setRevisions(
        ("2000-07-07 00:00",
         "1999-08-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceSet(Integer32, TextualConvention):
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
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("all", 9),
          ("allCpe", 2),
          ("allCpeEthernet", 4),
          ("allCpeFirewire", 6),
          ("allCpeUsb", 5),
          ("allExternal", 7),
          ("allInternal", 8),
          ("allNetwork", 3),
          ("application1", 10),
          ("application2", 11),
          ("application3", 12),
          ("application4", 13),
          ("other", 1))
    )



class IpV4orV6Address(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_DocsDevMIBObjects_ObjectIdentity = ObjectIdentity
docsDevMIBObjects = _DocsDevMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 83, 1)
)
_DocsDevBase_ObjectIdentity = ObjectIdentity
docsDevBase = _DocsDevBase_ObjectIdentity(
    (1, 3, 6, 1, 3, 83, 1, 1)
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
    (1, 3, 6, 1, 3, 83, 1, 1, 1),
    _DocsDevRole_Type()
)
docsDevRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevRole.setStatus("current")
_DocsDevDateTime_Type = DateAndTime
_DocsDevDateTime_Object = MibScalar
docsDevDateTime = _DocsDevDateTime_Object(
    (1, 3, 6, 1, 3, 83, 1, 1, 2),
    _DocsDevDateTime_Type()
)
docsDevDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevDateTime.setStatus("current")
_DocsDevResetNow_Type = TruthValue
_DocsDevResetNow_Object = MibScalar
docsDevResetNow = _DocsDevResetNow_Object(
    (1, 3, 6, 1, 3, 83, 1, 1, 3),
    _DocsDevResetNow_Type()
)
docsDevResetNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevResetNow.setStatus("current")
_DocsDevSerialNumber_Type = SnmpAdminString
_DocsDevSerialNumber_Object = MibScalar
docsDevSerialNumber = _DocsDevSerialNumber_Object(
    (1, 3, 6, 1, 3, 83, 1, 1, 4),
    _DocsDevSerialNumber_Type()
)
docsDevSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevSerialNumber.setStatus("current")


class _DocsDevSTPControl_Type(Integer32):
    """Custom type docsDevSTPControl based on Integer32"""
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
    (1, 3, 6, 1, 3, 83, 1, 1, 5),
    _DocsDevSTPControl_Type()
)
docsDevSTPControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevSTPControl.setStatus("current")
_DocsDevNmAccessTable_Object = MibTable
docsDevNmAccessTable = _DocsDevNmAccessTable_Object(
    (1, 3, 6, 1, 3, 83, 1, 2)
)
if mibBuilder.loadTexts:
    docsDevNmAccessTable.setStatus("deprecated")
_DocsDevNmAccessEntry_Object = MibTableRow
docsDevNmAccessEntry = _DocsDevNmAccessEntry_Object(
    (1, 3, 6, 1, 3, 83, 1, 2, 1)
)
docsDevNmAccessEntry.setIndexNames(
    (0, "EXP-DOCS-CABLE-DEVICE-MIB", "docsDevNmAccessIndex"),
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
    (1, 3, 6, 1, 3, 83, 1, 2, 1, 1),
    _DocsDevNmAccessIndex_Type()
)
docsDevNmAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsDevNmAccessIndex.setStatus("deprecated")


class _DocsDevNmAccessIp_Type(IpAddress):
    """Custom type docsDevNmAccessIp based on IpAddress"""
    defaultHexValue = "ffffffff"


_DocsDevNmAccessIp_Object = MibTableColumn
docsDevNmAccessIp = _DocsDevNmAccessIp_Object(
    (1, 3, 6, 1, 3, 83, 1, 2, 1, 2),
    _DocsDevNmAccessIp_Type()
)
docsDevNmAccessIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevNmAccessIp.setStatus("deprecated")


class _DocsDevNmAccessIpMask_Type(IpAddress):
    """Custom type docsDevNmAccessIpMask based on IpAddress"""
    defaultHexValue = "ffffffff"


_DocsDevNmAccessIpMask_Object = MibTableColumn
docsDevNmAccessIpMask = _DocsDevNmAccessIpMask_Object(
    (1, 3, 6, 1, 3, 83, 1, 2, 1, 3),
    _DocsDevNmAccessIpMask_Type()
)
docsDevNmAccessIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevNmAccessIpMask.setStatus("deprecated")


class _DocsDevNmAccessCommunity_Type(OctetString):
    """Custom type docsDevNmAccessCommunity based on OctetString"""
    defaultValue = OctetString("public")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DocsDevNmAccessCommunity_Type.__name__ = "OctetString"
_DocsDevNmAccessCommunity_Object = MibTableColumn
docsDevNmAccessCommunity = _DocsDevNmAccessCommunity_Object(
    (1, 3, 6, 1, 3, 83, 1, 2, 1, 4),
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
    (1, 3, 6, 1, 3, 83, 1, 2, 1, 5),
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
    (1, 3, 6, 1, 3, 83, 1, 2, 1, 6),
    _DocsDevNmAccessInterfaces_Type()
)
docsDevNmAccessInterfaces.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevNmAccessInterfaces.setStatus("deprecated")
_DocsDevNmAccessStatus_Type = RowStatus
_DocsDevNmAccessStatus_Object = MibTableColumn
docsDevNmAccessStatus = _DocsDevNmAccessStatus_Object(
    (1, 3, 6, 1, 3, 83, 1, 2, 1, 7),
    _DocsDevNmAccessStatus_Type()
)
docsDevNmAccessStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevNmAccessStatus.setStatus("deprecated")
_DocsDevSoftware_ObjectIdentity = ObjectIdentity
docsDevSoftware = _DocsDevSoftware_ObjectIdentity(
    (1, 3, 6, 1, 3, 83, 1, 3)
)
_DocsDevSwServer_Type = IpAddress
_DocsDevSwServer_Object = MibScalar
docsDevSwServer = _DocsDevSwServer_Object(
    (1, 3, 6, 1, 3, 83, 1, 3, 1),
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
    (1, 3, 6, 1, 3, 83, 1, 3, 2),
    _DocsDevSwFilename_Type()
)
docsDevSwFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevSwFilename.setStatus("current")


class _DocsDevSwAdminStatus_Type(Integer32):
    """Custom type docsDevSwAdminStatus based on Integer32"""
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
    (1, 3, 6, 1, 3, 83, 1, 3, 3),
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
    (1, 3, 6, 1, 3, 83, 1, 3, 4),
    _DocsDevSwOperStatus_Type()
)
docsDevSwOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevSwOperStatus.setStatus("current")
_DocsDevSwCurrentVers_Type = SnmpAdminString
_DocsDevSwCurrentVers_Object = MibScalar
docsDevSwCurrentVers = _DocsDevSwCurrentVers_Object(
    (1, 3, 6, 1, 3, 83, 1, 3, 5),
    _DocsDevSwCurrentVers_Type()
)
docsDevSwCurrentVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevSwCurrentVers.setStatus("current")
_DocsDevSwServerAddress_Type = IpV4orV6Address
_DocsDevSwServerAddress_Object = MibScalar
docsDevSwServerAddress = _DocsDevSwServerAddress_Object(
    (1, 3, 6, 1, 3, 83, 1, 3, 6),
    _DocsDevSwServerAddress_Type()
)
docsDevSwServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevSwServerAddress.setStatus("current")
_DocsDevServer_ObjectIdentity = ObjectIdentity
docsDevServer = _DocsDevServer_ObjectIdentity(
    (1, 3, 6, 1, 3, 83, 1, 4)
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
    (1, 3, 6, 1, 3, 83, 1, 4, 1),
    _DocsDevServerBootState_Type()
)
docsDevServerBootState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevServerBootState.setStatus("current")
_DocsDevServerDhcp_Type = IpAddress
_DocsDevServerDhcp_Object = MibScalar
docsDevServerDhcp = _DocsDevServerDhcp_Object(
    (1, 3, 6, 1, 3, 83, 1, 4, 2),
    _DocsDevServerDhcp_Type()
)
docsDevServerDhcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevServerDhcp.setStatus("deprecated")
_DocsDevServerTime_Type = IpAddress
_DocsDevServerTime_Object = MibScalar
docsDevServerTime = _DocsDevServerTime_Object(
    (1, 3, 6, 1, 3, 83, 1, 4, 3),
    _DocsDevServerTime_Type()
)
docsDevServerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevServerTime.setStatus("deprecated")
_DocsDevServerTftp_Type = IpAddress
_DocsDevServerTftp_Object = MibScalar
docsDevServerTftp = _DocsDevServerTftp_Object(
    (1, 3, 6, 1, 3, 83, 1, 4, 4),
    _DocsDevServerTftp_Type()
)
docsDevServerTftp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevServerTftp.setStatus("deprecated")
_DocsDevServerConfigFile_Type = SnmpAdminString
_DocsDevServerConfigFile_Object = MibScalar
docsDevServerConfigFile = _DocsDevServerConfigFile_Object(
    (1, 3, 6, 1, 3, 83, 1, 4, 5),
    _DocsDevServerConfigFile_Type()
)
docsDevServerConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevServerConfigFile.setStatus("current")
_DocsDevServerDhcpAddress_Type = IpV4orV6Address
_DocsDevServerDhcpAddress_Object = MibScalar
docsDevServerDhcpAddress = _DocsDevServerDhcpAddress_Object(
    (1, 3, 6, 1, 3, 83, 1, 4, 6),
    _DocsDevServerDhcpAddress_Type()
)
docsDevServerDhcpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevServerDhcpAddress.setStatus("current")
_DocsDevServerTimeAddress_Type = IpV4orV6Address
_DocsDevServerTimeAddress_Object = MibScalar
docsDevServerTimeAddress = _DocsDevServerTimeAddress_Object(
    (1, 3, 6, 1, 3, 83, 1, 4, 7),
    _DocsDevServerTimeAddress_Type()
)
docsDevServerTimeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevServerTimeAddress.setStatus("current")
_DocsDevServerConfigTftpAddress_Type = IpV4orV6Address
_DocsDevServerConfigTftpAddress_Object = MibScalar
docsDevServerConfigTftpAddress = _DocsDevServerConfigTftpAddress_Object(
    (1, 3, 6, 1, 3, 83, 1, 4, 8),
    _DocsDevServerConfigTftpAddress_Type()
)
docsDevServerConfigTftpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevServerConfigTftpAddress.setStatus("current")
_DocsDevEvent_ObjectIdentity = ObjectIdentity
docsDevEvent = _DocsDevEvent_ObjectIdentity(
    (1, 3, 6, 1, 3, 83, 1, 5)
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
    (1, 3, 6, 1, 3, 83, 1, 5, 1),
    _DocsDevEvControl_Type()
)
docsDevEvControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevEvControl.setStatus("current")
_DocsDevEvSyslog_Type = IpAddress
_DocsDevEvSyslog_Object = MibScalar
docsDevEvSyslog = _DocsDevEvSyslog_Object(
    (1, 3, 6, 1, 3, 83, 1, 5, 2),
    _DocsDevEvSyslog_Type()
)
docsDevEvSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevEvSyslog.setStatus("deprecated")


class _DocsDevEvThrottleAdminStatus_Type(Integer32):
    """Custom type docsDevEvThrottleAdminStatus based on Integer32"""
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
    (1, 3, 6, 1, 3, 83, 1, 5, 3),
    _DocsDevEvThrottleAdminStatus_Type()
)
docsDevEvThrottleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevEvThrottleAdminStatus.setStatus("current")
_DocsDevEvThrottleInhibited_Type = TruthValue
_DocsDevEvThrottleInhibited_Object = MibScalar
docsDevEvThrottleInhibited = _DocsDevEvThrottleInhibited_Object(
    (1, 3, 6, 1, 3, 83, 1, 5, 4),
    _DocsDevEvThrottleInhibited_Type()
)
docsDevEvThrottleInhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevEvThrottleInhibited.setStatus("current")
_DocsDevEvThrottleThreshold_Type = Unsigned32
_DocsDevEvThrottleThreshold_Object = MibScalar
docsDevEvThrottleThreshold = _DocsDevEvThrottleThreshold_Object(
    (1, 3, 6, 1, 3, 83, 1, 5, 5),
    _DocsDevEvThrottleThreshold_Type()
)
docsDevEvThrottleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevEvThrottleThreshold.setStatus("current")


class _DocsDevEvThrottleInterval_Type(Integer32):
    """Custom type docsDevEvThrottleInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DocsDevEvThrottleInterval_Type.__name__ = "Integer32"
_DocsDevEvThrottleInterval_Object = MibScalar
docsDevEvThrottleInterval = _DocsDevEvThrottleInterval_Object(
    (1, 3, 6, 1, 3, 83, 1, 5, 6),
    _DocsDevEvThrottleInterval_Type()
)
docsDevEvThrottleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevEvThrottleInterval.setStatus("current")
if mibBuilder.loadTexts:
    docsDevEvThrottleInterval.setUnits("seconds")
_DocsDevEvControlTable_Object = MibTable
docsDevEvControlTable = _DocsDevEvControlTable_Object(
    (1, 3, 6, 1, 3, 83, 1, 5, 7)
)
if mibBuilder.loadTexts:
    docsDevEvControlTable.setStatus("current")
_DocsDevEvControlEntry_Object = MibTableRow
docsDevEvControlEntry = _DocsDevEvControlEntry_Object(
    (1, 3, 6, 1, 3, 83, 1, 5, 7, 1)
)
docsDevEvControlEntry.setIndexNames(
    (0, "EXP-DOCS-CABLE-DEVICE-MIB", "docsDevEvPriority"),
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
    (1, 3, 6, 1, 3, 83, 1, 5, 7, 1, 1),
    _DocsDevEvPriority_Type()
)
docsDevEvPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsDevEvPriority.setStatus("current")


class _DocsDevEvReporting_Type(Bits):
    """Custom type docsDevEvReporting based on Bits"""
    namedValues = NamedValues(
        *(("local", 0),
          ("syslog", 2),
          ("traps", 1))
    )

_DocsDevEvReporting_Type.__name__ = "Bits"
_DocsDevEvReporting_Object = MibTableColumn
docsDevEvReporting = _DocsDevEvReporting_Object(
    (1, 3, 6, 1, 3, 83, 1, 5, 7, 1, 2),
    _DocsDevEvReporting_Type()
)
docsDevEvReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevEvReporting.setStatus("current")
_DocsDevEventTable_Object = MibTable
docsDevEventTable = _DocsDevEventTable_Object(
    (1, 3, 6, 1, 3, 83, 1, 5, 8)
)
if mibBuilder.loadTexts:
    docsDevEventTable.setStatus("current")
_DocsDevEventEntry_Object = MibTableRow
docsDevEventEntry = _DocsDevEventEntry_Object(
    (1, 3, 6, 1, 3, 83, 1, 5, 8, 1)
)
docsDevEventEntry.setIndexNames(
    (0, "EXP-DOCS-CABLE-DEVICE-MIB", "docsDevEvIndex"),
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
    (1, 3, 6, 1, 3, 83, 1, 5, 8, 1, 1),
    _DocsDevEvIndex_Type()
)
docsDevEvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsDevEvIndex.setStatus("current")
_DocsDevEvFirstTime_Type = DateAndTime
_DocsDevEvFirstTime_Object = MibTableColumn
docsDevEvFirstTime = _DocsDevEvFirstTime_Object(
    (1, 3, 6, 1, 3, 83, 1, 5, 8, 1, 2),
    _DocsDevEvFirstTime_Type()
)
docsDevEvFirstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevEvFirstTime.setStatus("current")
_DocsDevEvLastTime_Type = DateAndTime
_DocsDevEvLastTime_Object = MibTableColumn
docsDevEvLastTime = _DocsDevEvLastTime_Object(
    (1, 3, 6, 1, 3, 83, 1, 5, 8, 1, 3),
    _DocsDevEvLastTime_Type()
)
docsDevEvLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevEvLastTime.setStatus("current")
_DocsDevEvCounts_Type = Counter32
_DocsDevEvCounts_Object = MibTableColumn
docsDevEvCounts = _DocsDevEvCounts_Object(
    (1, 3, 6, 1, 3, 83, 1, 5, 8, 1, 4),
    _DocsDevEvCounts_Type()
)
docsDevEvCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevEvCounts.setStatus("current")


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
    (1, 3, 6, 1, 3, 83, 1, 5, 8, 1, 5),
    _DocsDevEvLevel_Type()
)
docsDevEvLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevEvLevel.setStatus("current")
_DocsDevEvId_Type = Unsigned32
_DocsDevEvId_Object = MibTableColumn
docsDevEvId = _DocsDevEvId_Object(
    (1, 3, 6, 1, 3, 83, 1, 5, 8, 1, 6),
    _DocsDevEvId_Type()
)
docsDevEvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevEvId.setStatus("current")
_DocsDevEvText_Type = SnmpAdminString
_DocsDevEvText_Object = MibTableColumn
docsDevEvText = _DocsDevEvText_Object(
    (1, 3, 6, 1, 3, 83, 1, 5, 8, 1, 7),
    _DocsDevEvText_Type()
)
docsDevEvText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevEvText.setStatus("current")
_DocsDevEvSyslogAddress_Type = IpV4orV6Address
_DocsDevEvSyslogAddress_Object = MibScalar
docsDevEvSyslogAddress = _DocsDevEvSyslogAddress_Object(
    (1, 3, 6, 1, 3, 83, 1, 5, 9),
    _DocsDevEvSyslogAddress_Type()
)
docsDevEvSyslogAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevEvSyslogAddress.setStatus("current")
_DocsDevFilter_ObjectIdentity = ObjectIdentity
docsDevFilter = _DocsDevFilter_ObjectIdentity(
    (1, 3, 6, 1, 3, 83, 1, 6)
)


class _DocsDevFilterLLCUnmatchedAction_Type(Integer32):
    """Custom type docsDevFilterLLCUnmatchedAction based on Integer32"""
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
    (1, 3, 6, 1, 3, 83, 1, 6, 1),
    _DocsDevFilterLLCUnmatchedAction_Type()
)
docsDevFilterLLCUnmatchedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevFilterLLCUnmatchedAction.setStatus("current")
_DocsDevFilterLLCTable_Object = MibTable
docsDevFilterLLCTable = _DocsDevFilterLLCTable_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 2)
)
if mibBuilder.loadTexts:
    docsDevFilterLLCTable.setStatus("current")
_DocsDevFilterLLCEntry_Object = MibTableRow
docsDevFilterLLCEntry = _DocsDevFilterLLCEntry_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 2, 1)
)
docsDevFilterLLCEntry.setIndexNames(
    (0, "EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterLLCIndex"),
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
    (1, 3, 6, 1, 3, 83, 1, 6, 2, 1, 1),
    _DocsDevFilterLLCIndex_Type()
)
docsDevFilterLLCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsDevFilterLLCIndex.setStatus("current")
_DocsDevFilterLLCStatus_Type = RowStatus
_DocsDevFilterLLCStatus_Object = MibTableColumn
docsDevFilterLLCStatus = _DocsDevFilterLLCStatus_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 2, 1, 2),
    _DocsDevFilterLLCStatus_Type()
)
docsDevFilterLLCStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterLLCStatus.setStatus("current")
_DocsDevFilterLLCIfIndex_Type = InterfaceIndexOrZero
_DocsDevFilterLLCIfIndex_Object = MibTableColumn
docsDevFilterLLCIfIndex = _DocsDevFilterLLCIfIndex_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 2, 1, 3),
    _DocsDevFilterLLCIfIndex_Type()
)
docsDevFilterLLCIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterLLCIfIndex.setStatus("deprecated")


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
    (1, 3, 6, 1, 3, 83, 1, 6, 2, 1, 4),
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
    (1, 3, 6, 1, 3, 83, 1, 6, 2, 1, 5),
    _DocsDevFilterLLCProtocol_Type()
)
docsDevFilterLLCProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterLLCProtocol.setStatus("current")
_DocsDevFilterLLCMatches_Type = Counter32
_DocsDevFilterLLCMatches_Object = MibTableColumn
docsDevFilterLLCMatches = _DocsDevFilterLLCMatches_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 2, 1, 6),
    _DocsDevFilterLLCMatches_Type()
)
docsDevFilterLLCMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevFilterLLCMatches.setStatus("current")


class _DocsDevFilterLLCInterfaces_Type(OctetString):
    """Custom type docsDevFilterLLCInterfaces based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DocsDevFilterLLCInterfaces_Type.__name__ = "OctetString"
_DocsDevFilterLLCInterfaces_Object = MibTableColumn
docsDevFilterLLCInterfaces = _DocsDevFilterLLCInterfaces_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 2, 1, 7),
    _DocsDevFilterLLCInterfaces_Type()
)
docsDevFilterLLCInterfaces.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterLLCInterfaces.setStatus("current")


class _DocsDevFilterLLCInterfaceSet_Type(InterfaceSet):
    """Custom type docsDevFilterLLCInterfaceSet based on InterfaceSet"""


_DocsDevFilterLLCInterfaceSet_Object = MibTableColumn
docsDevFilterLLCInterfaceSet = _DocsDevFilterLLCInterfaceSet_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 2, 1, 8),
    _DocsDevFilterLLCInterfaceSet_Type()
)
docsDevFilterLLCInterfaceSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterLLCInterfaceSet.setStatus("current")


class _DocsDevFilterIpDefault_Type(Integer32):
    """Custom type docsDevFilterIpDefault based on Integer32"""
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
    (1, 3, 6, 1, 3, 83, 1, 6, 3),
    _DocsDevFilterIpDefault_Type()
)
docsDevFilterIpDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevFilterIpDefault.setStatus("current")
_DocsDevFilterIpTable_Object = MibTable
docsDevFilterIpTable = _DocsDevFilterIpTable_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 4)
)
if mibBuilder.loadTexts:
    docsDevFilterIpTable.setStatus("current")
_DocsDevFilterIpEntry_Object = MibTableRow
docsDevFilterIpEntry = _DocsDevFilterIpEntry_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 4, 1)
)
docsDevFilterIpEntry.setIndexNames(
    (0, "EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpIndex"),
)
if mibBuilder.loadTexts:
    docsDevFilterIpEntry.setStatus("current")


class _DocsDevFilterIpIndex_Type(Integer32):
    """Custom type docsDevFilterIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DocsDevFilterIpIndex_Type.__name__ = "Integer32"
_DocsDevFilterIpIndex_Object = MibTableColumn
docsDevFilterIpIndex = _DocsDevFilterIpIndex_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 4, 1, 1),
    _DocsDevFilterIpIndex_Type()
)
docsDevFilterIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsDevFilterIpIndex.setStatus("current")
_DocsDevFilterIpStatus_Type = RowStatus
_DocsDevFilterIpStatus_Object = MibTableColumn
docsDevFilterIpStatus = _DocsDevFilterIpStatus_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 4, 1, 2),
    _DocsDevFilterIpStatus_Type()
)
docsDevFilterIpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpStatus.setStatus("current")


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
    (1, 3, 6, 1, 3, 83, 1, 6, 4, 1, 3),
    _DocsDevFilterIpControl_Type()
)
docsDevFilterIpControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpControl.setStatus("current")
_DocsDevFilterIpIfIndex_Type = InterfaceIndexOrZero
_DocsDevFilterIpIfIndex_Object = MibTableColumn
docsDevFilterIpIfIndex = _DocsDevFilterIpIfIndex_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 4, 1, 4),
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
    (1, 3, 6, 1, 3, 83, 1, 6, 4, 1, 5),
    _DocsDevFilterIpDirection_Type()
)
docsDevFilterIpDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpDirection.setStatus("current")


class _DocsDevFilterIpBroadcast_Type(TruthValue):
    """Custom type docsDevFilterIpBroadcast based on TruthValue"""


_DocsDevFilterIpBroadcast_Object = MibTableColumn
docsDevFilterIpBroadcast = _DocsDevFilterIpBroadcast_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 4, 1, 6),
    _DocsDevFilterIpBroadcast_Type()
)
docsDevFilterIpBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpBroadcast.setStatus("current")


class _DocsDevFilterIpSaddr_Type(IpAddress):
    """Custom type docsDevFilterIpSaddr based on IpAddress"""
    defaultHexValue = "00000000"


_DocsDevFilterIpSaddr_Object = MibTableColumn
docsDevFilterIpSaddr = _DocsDevFilterIpSaddr_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 4, 1, 7),
    _DocsDevFilterIpSaddr_Type()
)
docsDevFilterIpSaddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpSaddr.setStatus("current")


class _DocsDevFilterIpSmask_Type(IpAddress):
    """Custom type docsDevFilterIpSmask based on IpAddress"""
    defaultHexValue = "00000000"


_DocsDevFilterIpSmask_Object = MibTableColumn
docsDevFilterIpSmask = _DocsDevFilterIpSmask_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 4, 1, 8),
    _DocsDevFilterIpSmask_Type()
)
docsDevFilterIpSmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpSmask.setStatus("current")


class _DocsDevFilterIpDaddr_Type(IpAddress):
    """Custom type docsDevFilterIpDaddr based on IpAddress"""
    defaultHexValue = "00000000"


_DocsDevFilterIpDaddr_Object = MibTableColumn
docsDevFilterIpDaddr = _DocsDevFilterIpDaddr_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 4, 1, 9),
    _DocsDevFilterIpDaddr_Type()
)
docsDevFilterIpDaddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpDaddr.setStatus("current")


class _DocsDevFilterIpDmask_Type(IpAddress):
    """Custom type docsDevFilterIpDmask based on IpAddress"""
    defaultHexValue = "00000000"


_DocsDevFilterIpDmask_Object = MibTableColumn
docsDevFilterIpDmask = _DocsDevFilterIpDmask_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 4, 1, 10),
    _DocsDevFilterIpDmask_Type()
)
docsDevFilterIpDmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpDmask.setStatus("current")


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
    (1, 3, 6, 1, 3, 83, 1, 6, 4, 1, 11),
    _DocsDevFilterIpProtocol_Type()
)
docsDevFilterIpProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpProtocol.setStatus("current")


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
    (1, 3, 6, 1, 3, 83, 1, 6, 4, 1, 12),
    _DocsDevFilterIpSourcePortLow_Type()
)
docsDevFilterIpSourcePortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpSourcePortLow.setStatus("current")


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
    (1, 3, 6, 1, 3, 83, 1, 6, 4, 1, 13),
    _DocsDevFilterIpSourcePortHigh_Type()
)
docsDevFilterIpSourcePortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpSourcePortHigh.setStatus("current")


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
    (1, 3, 6, 1, 3, 83, 1, 6, 4, 1, 14),
    _DocsDevFilterIpDestPortLow_Type()
)
docsDevFilterIpDestPortLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpDestPortLow.setStatus("current")


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
    (1, 3, 6, 1, 3, 83, 1, 6, 4, 1, 15),
    _DocsDevFilterIpDestPortHigh_Type()
)
docsDevFilterIpDestPortHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpDestPortHigh.setStatus("current")
_DocsDevFilterIpMatches_Type = Counter32
_DocsDevFilterIpMatches_Object = MibTableColumn
docsDevFilterIpMatches = _DocsDevFilterIpMatches_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 4, 1, 16),
    _DocsDevFilterIpMatches_Type()
)
docsDevFilterIpMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevFilterIpMatches.setStatus("current")


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
    (1, 3, 6, 1, 3, 83, 1, 6, 4, 1, 17),
    _DocsDevFilterIpTos_Type()
)
docsDevFilterIpTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpTos.setStatus("current")


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
    (1, 3, 6, 1, 3, 83, 1, 6, 4, 1, 18),
    _DocsDevFilterIpTosMask_Type()
)
docsDevFilterIpTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpTosMask.setStatus("current")


class _DocsDevFilterIpContinue_Type(TruthValue):
    """Custom type docsDevFilterIpContinue based on TruthValue"""


_DocsDevFilterIpContinue_Object = MibTableColumn
docsDevFilterIpContinue = _DocsDevFilterIpContinue_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 4, 1, 19),
    _DocsDevFilterIpContinue_Type()
)
docsDevFilterIpContinue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpContinue.setStatus("current")


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
    (1, 3, 6, 1, 3, 83, 1, 6, 4, 1, 20),
    _DocsDevFilterIpPolicyId_Type()
)
docsDevFilterIpPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpPolicyId.setStatus("current")


class _DocsDevFilterIpInterfaces_Type(OctetString):
    """Custom type docsDevFilterIpInterfaces based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DocsDevFilterIpInterfaces_Type.__name__ = "OctetString"
_DocsDevFilterIpInterfaces_Object = MibTableColumn
docsDevFilterIpInterfaces = _DocsDevFilterIpInterfaces_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 4, 1, 21),
    _DocsDevFilterIpInterfaces_Type()
)
docsDevFilterIpInterfaces.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpInterfaces.setStatus("current")


class _DocsDevFilterIpInterfaceSet_Type(InterfaceSet):
    """Custom type docsDevFilterIpInterfaceSet based on InterfaceSet"""


_DocsDevFilterIpInterfaceSet_Object = MibTableColumn
docsDevFilterIpInterfaceSet = _DocsDevFilterIpInterfaceSet_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 4, 1, 22),
    _DocsDevFilterIpInterfaceSet_Type()
)
docsDevFilterIpInterfaceSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpInterfaceSet.setStatus("current")
_DocsDevFilterPolicyTable_Object = MibTable
docsDevFilterPolicyTable = _DocsDevFilterPolicyTable_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 5)
)
if mibBuilder.loadTexts:
    docsDevFilterPolicyTable.setStatus("current")
_DocsDevFilterPolicyEntry_Object = MibTableRow
docsDevFilterPolicyEntry = _DocsDevFilterPolicyEntry_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 5, 1)
)
docsDevFilterPolicyEntry.setIndexNames(
    (0, "EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterPolicyIndex"),
)
if mibBuilder.loadTexts:
    docsDevFilterPolicyEntry.setStatus("current")


class _DocsDevFilterPolicyIndex_Type(Integer32):
    """Custom type docsDevFilterPolicyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DocsDevFilterPolicyIndex_Type.__name__ = "Integer32"
_DocsDevFilterPolicyIndex_Object = MibTableColumn
docsDevFilterPolicyIndex = _DocsDevFilterPolicyIndex_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 5, 1, 1),
    _DocsDevFilterPolicyIndex_Type()
)
docsDevFilterPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsDevFilterPolicyIndex.setStatus("current")


class _DocsDevFilterPolicyId_Type(Integer32):
    """Custom type docsDevFilterPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DocsDevFilterPolicyId_Type.__name__ = "Integer32"
_DocsDevFilterPolicyId_Object = MibTableColumn
docsDevFilterPolicyId = _DocsDevFilterPolicyId_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 5, 1, 2),
    _DocsDevFilterPolicyId_Type()
)
docsDevFilterPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterPolicyId.setStatus("current")
_DocsDevFilterPolicyStatus_Type = RowStatus
_DocsDevFilterPolicyStatus_Object = MibTableColumn
docsDevFilterPolicyStatus = _DocsDevFilterPolicyStatus_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 5, 1, 5),
    _DocsDevFilterPolicyStatus_Type()
)
docsDevFilterPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterPolicyStatus.setStatus("current")


class _DocsDevFilterPolicyPtr_Type(RowPointer):
    """Custom type docsDevFilterPolicyPtr based on RowPointer"""
    defaultValue = (0, 0)


_DocsDevFilterPolicyPtr_Object = MibTableColumn
docsDevFilterPolicyPtr = _DocsDevFilterPolicyPtr_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 5, 1, 6),
    _DocsDevFilterPolicyPtr_Type()
)
docsDevFilterPolicyPtr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterPolicyPtr.setStatus("current")
_DocsDevFilterTosTable_Object = MibTable
docsDevFilterTosTable = _DocsDevFilterTosTable_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 6)
)
if mibBuilder.loadTexts:
    docsDevFilterTosTable.setStatus("current")
_DocsDevFilterTosEntry_Object = MibTableRow
docsDevFilterTosEntry = _DocsDevFilterTosEntry_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 6, 1)
)
docsDevFilterTosEntry.setIndexNames(
    (0, "EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterTosIndex"),
)
if mibBuilder.loadTexts:
    docsDevFilterTosEntry.setStatus("current")


class _DocsDevFilterTosIndex_Type(Integer32):
    """Custom type docsDevFilterTosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DocsDevFilterTosIndex_Type.__name__ = "Integer32"
_DocsDevFilterTosIndex_Object = MibTableColumn
docsDevFilterTosIndex = _DocsDevFilterTosIndex_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 6, 1, 1),
    _DocsDevFilterTosIndex_Type()
)
docsDevFilterTosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsDevFilterTosIndex.setStatus("current")
_DocsDevFilterTosStatus_Type = RowStatus
_DocsDevFilterTosStatus_Object = MibTableColumn
docsDevFilterTosStatus = _DocsDevFilterTosStatus_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 6, 1, 2),
    _DocsDevFilterTosStatus_Type()
)
docsDevFilterTosStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterTosStatus.setStatus("current")


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
    (1, 3, 6, 1, 3, 83, 1, 6, 6, 1, 3),
    _DocsDevFilterTosAndMask_Type()
)
docsDevFilterTosAndMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterTosAndMask.setStatus("current")


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
    (1, 3, 6, 1, 3, 83, 1, 6, 6, 1, 4),
    _DocsDevFilterTosOrMask_Type()
)
docsDevFilterTosOrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterTosOrMask.setStatus("current")
_DocsDevFilterIpV6AuxTable_Object = MibTable
docsDevFilterIpV6AuxTable = _DocsDevFilterIpV6AuxTable_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 7)
)
if mibBuilder.loadTexts:
    docsDevFilterIpV6AuxTable.setStatus("current")
_DocsDevFilterIpV6AuxEntry_Object = MibTableRow
docsDevFilterIpV6AuxEntry = _DocsDevFilterIpV6AuxEntry_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 7, 1)
)
if mibBuilder.loadTexts:
    docsDevFilterIpV6AuxEntry.setStatus("current")


class _DocsDevFilterIpType_Type(Integer32):
    """Custom type docsDevFilterIpType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_DocsDevFilterIpType_Type.__name__ = "Integer32"
_DocsDevFilterIpType_Object = MibTableColumn
docsDevFilterIpType = _DocsDevFilterIpType_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 7, 1, 1),
    _DocsDevFilterIpType_Type()
)
docsDevFilterIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpType.setStatus("current")


class _DocsDevFilterIpV6Saddr_Type(Ipv6Address):
    """Custom type docsDevFilterIpV6Saddr based on Ipv6Address"""
    defaultHexValue = "00000000000000000000000000000000"


_DocsDevFilterIpV6Saddr_Object = MibTableColumn
docsDevFilterIpV6Saddr = _DocsDevFilterIpV6Saddr_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 7, 1, 2),
    _DocsDevFilterIpV6Saddr_Type()
)
docsDevFilterIpV6Saddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpV6Saddr.setStatus("current")


class _DocsDevFilterIpV6Smask_Type(Ipv6Address):
    """Custom type docsDevFilterIpV6Smask based on Ipv6Address"""
    defaultHexValue = "00000000000000000000000000000000"


_DocsDevFilterIpV6Smask_Object = MibTableColumn
docsDevFilterIpV6Smask = _DocsDevFilterIpV6Smask_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 7, 1, 3),
    _DocsDevFilterIpV6Smask_Type()
)
docsDevFilterIpV6Smask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpV6Smask.setStatus("current")


class _DocsDevFilterIpV6Daddr_Type(Ipv6Address):
    """Custom type docsDevFilterIpV6Daddr based on Ipv6Address"""
    defaultHexValue = "00000000000000000000000000000000"


_DocsDevFilterIpV6Daddr_Object = MibTableColumn
docsDevFilterIpV6Daddr = _DocsDevFilterIpV6Daddr_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 7, 1, 4),
    _DocsDevFilterIpV6Daddr_Type()
)
docsDevFilterIpV6Daddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpV6Daddr.setStatus("current")


class _DocsDevFilterIpV6Dmask_Type(Ipv6Address):
    """Custom type docsDevFilterIpV6Dmask based on Ipv6Address"""
    defaultHexValue = "00000000000000000000000000000000"


_DocsDevFilterIpV6Dmask_Object = MibTableColumn
docsDevFilterIpV6Dmask = _DocsDevFilterIpV6Dmask_Object(
    (1, 3, 6, 1, 3, 83, 1, 6, 7, 1, 5),
    _DocsDevFilterIpV6Dmask_Type()
)
docsDevFilterIpV6Dmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevFilterIpV6Dmask.setStatus("current")
_DocsDevCpe_ObjectIdentity = ObjectIdentity
docsDevCpe = _DocsDevCpe_ObjectIdentity(
    (1, 3, 6, 1, 3, 83, 1, 7)
)


class _DocsDevCpeEnroll_Type(Integer32):
    """Custom type docsDevCpeEnroll based on Integer32"""
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
    (1, 3, 6, 1, 3, 83, 1, 7, 1),
    _DocsDevCpeEnroll_Type()
)
docsDevCpeEnroll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevCpeEnroll.setStatus("current")


class _DocsDevCpeIpMax_Type(Integer32):
    """Custom type docsDevCpeIpMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_DocsDevCpeIpMax_Type.__name__ = "Integer32"
_DocsDevCpeIpMax_Object = MibScalar
docsDevCpeIpMax = _DocsDevCpeIpMax_Object(
    (1, 3, 6, 1, 3, 83, 1, 7, 2),
    _DocsDevCpeIpMax_Type()
)
docsDevCpeIpMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsDevCpeIpMax.setStatus("current")
_DocsDevCpeTable_Object = MibTable
docsDevCpeTable = _DocsDevCpeTable_Object(
    (1, 3, 6, 1, 3, 83, 1, 7, 3)
)
if mibBuilder.loadTexts:
    docsDevCpeTable.setStatus("current")
_DocsDevCpeEntry_Object = MibTableRow
docsDevCpeEntry = _DocsDevCpeEntry_Object(
    (1, 3, 6, 1, 3, 83, 1, 7, 3, 1)
)
docsDevCpeEntry.setIndexNames(
    (0, "EXP-DOCS-CABLE-DEVICE-MIB", "docsDevCpeIp"),
)
if mibBuilder.loadTexts:
    docsDevCpeEntry.setStatus("current")
_DocsDevCpeIp_Type = IpAddress
_DocsDevCpeIp_Object = MibTableColumn
docsDevCpeIp = _DocsDevCpeIp_Object(
    (1, 3, 6, 1, 3, 83, 1, 7, 3, 1, 1),
    _DocsDevCpeIp_Type()
)
docsDevCpeIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsDevCpeIp.setStatus("current")


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
    (1, 3, 6, 1, 3, 83, 1, 7, 3, 1, 2),
    _DocsDevCpeSource_Type()
)
docsDevCpeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevCpeSource.setStatus("current")
_DocsDevCpeStatus_Type = RowStatus
_DocsDevCpeStatus_Object = MibTableColumn
docsDevCpeStatus = _DocsDevCpeStatus_Object(
    (1, 3, 6, 1, 3, 83, 1, 7, 3, 1, 3),
    _DocsDevCpeStatus_Type()
)
docsDevCpeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevCpeStatus.setStatus("current")
_DocsDevCpeV6Table_Object = MibTable
docsDevCpeV6Table = _DocsDevCpeV6Table_Object(
    (1, 3, 6, 1, 3, 83, 1, 7, 4)
)
if mibBuilder.loadTexts:
    docsDevCpeV6Table.setStatus("current")
_DocsDevCpeV6Entry_Object = MibTableRow
docsDevCpeV6Entry = _DocsDevCpeV6Entry_Object(
    (1, 3, 6, 1, 3, 83, 1, 7, 4, 1)
)
docsDevCpeV6Entry.setIndexNames(
    (0, "EXP-DOCS-CABLE-DEVICE-MIB", "docsDevCpeV6Ip"),
)
if mibBuilder.loadTexts:
    docsDevCpeV6Entry.setStatus("current")
_DocsDevCpeV6Ip_Type = Ipv6Address
_DocsDevCpeV6Ip_Object = MibTableColumn
docsDevCpeV6Ip = _DocsDevCpeV6Ip_Object(
    (1, 3, 6, 1, 3, 83, 1, 7, 4, 1, 1),
    _DocsDevCpeV6Ip_Type()
)
docsDevCpeV6Ip.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsDevCpeV6Ip.setStatus("current")


class _DocsDevCpeV6Source_Type(Integer32):
    """Custom type docsDevCpeV6Source based on Integer32"""
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


_DocsDevCpeV6Source_Type.__name__ = "Integer32"
_DocsDevCpeV6Source_Object = MibTableColumn
docsDevCpeV6Source = _DocsDevCpeV6Source_Object(
    (1, 3, 6, 1, 3, 83, 1, 7, 4, 1, 2),
    _DocsDevCpeV6Source_Type()
)
docsDevCpeV6Source.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsDevCpeV6Source.setStatus("current")
_DocsDevCpeV6Status_Type = RowStatus
_DocsDevCpeV6Status_Object = MibTableColumn
docsDevCpeV6Status = _DocsDevCpeV6Status_Object(
    (1, 3, 6, 1, 3, 83, 1, 7, 4, 1, 3),
    _DocsDevCpeV6Status_Type()
)
docsDevCpeV6Status.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevCpeV6Status.setStatus("current")
_DocsDevVacmAccessExtTable_Object = MibTable
docsDevVacmAccessExtTable = _DocsDevVacmAccessExtTable_Object(
    (1, 3, 6, 1, 3, 83, 1, 8)
)
if mibBuilder.loadTexts:
    docsDevVacmAccessExtTable.setStatus("current")
_DocsDevVacmAccessExtEntry_Object = MibTableRow
docsDevVacmAccessExtEntry = _DocsDevVacmAccessExtEntry_Object(
    (1, 3, 6, 1, 3, 83, 1, 8, 1)
)
if mibBuilder.loadTexts:
    docsDevVacmAccessExtEntry.setStatus("current")


class _DocsDevVacmAccessInterfaces_Type(OctetString):
    """Custom type docsDevVacmAccessInterfaces based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DocsDevVacmAccessInterfaces_Type.__name__ = "OctetString"
_DocsDevVacmAccessInterfaces_Object = MibTableColumn
docsDevVacmAccessInterfaces = _DocsDevVacmAccessInterfaces_Object(
    (1, 3, 6, 1, 3, 83, 1, 8, 1, 1),
    _DocsDevVacmAccessInterfaces_Type()
)
docsDevVacmAccessInterfaces.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevVacmAccessInterfaces.setStatus("current")


class _DocsDevVacmAccessInterfaceSet_Type(InterfaceSet):
    """Custom type docsDevVacmAccessInterfaceSet based on InterfaceSet"""


_DocsDevVacmAccessInterfaceSet_Object = MibTableColumn
docsDevVacmAccessInterfaceSet = _DocsDevVacmAccessInterfaceSet_Object(
    (1, 3, 6, 1, 3, 83, 1, 8, 1, 2),
    _DocsDevVacmAccessInterfaceSet_Type()
)
docsDevVacmAccessInterfaceSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsDevVacmAccessInterfaceSet.setStatus("current")
_DocsDevNotification_ObjectIdentity = ObjectIdentity
docsDevNotification = _DocsDevNotification_ObjectIdentity(
    (1, 3, 6, 1, 3, 83, 2)
)
_DocsDevConformanceV2_ObjectIdentity = ObjectIdentity
docsDevConformanceV2 = _DocsDevConformanceV2_ObjectIdentity(
    (1, 3, 6, 1, 3, 83, 4)
)
_DocsDevGroupsV2_ObjectIdentity = ObjectIdentity
docsDevGroupsV2 = _DocsDevGroupsV2_ObjectIdentity(
    (1, 3, 6, 1, 3, 83, 4, 1)
)
_DocsDevCompliancesV2_ObjectIdentity = ObjectIdentity
docsDevCompliancesV2 = _DocsDevCompliancesV2_ObjectIdentity(
    (1, 3, 6, 1, 3, 83, 4, 2)
)
docsDevFilterIpEntry.registerAugmentions(
    ("EXP-DOCS-CABLE-DEVICE-MIB",
     "docsDevFilterIpV6AuxEntry")
)
docsDevFilterIpV6AuxEntry.setIndexNames(*docsDevFilterIpEntry.getIndexNames())
vacmAccessEntry.registerAugmentions(
    ("EXP-DOCS-CABLE-DEVICE-MIB",
     "docsDevVacmAccessExtEntry")
)
docsDevVacmAccessExtEntry.setIndexNames(*vacmAccessEntry.getIndexNames())

# Managed Objects groups

docsDevBaseGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 3, 83, 4, 1, 1)
)
docsDevBaseGroupV2.setObjects(
      *(("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevRole"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevDateTime"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevResetNow"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevSerialNumber"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevSTPControl"))
)
if mibBuilder.loadTexts:
    docsDevBaseGroupV2.setStatus("current")

docsDevNmAccessGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 3, 83, 4, 1, 2)
)
docsDevNmAccessGroupV2.setObjects(
      *(("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevNmAccessIp"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevNmAccessIpMask"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevNmAccessCommunity"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevNmAccessControl"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevNmAccessInterfaces"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevNmAccessStatus"))
)
if mibBuilder.loadTexts:
    docsDevNmAccessGroupV2.setStatus("deprecated")

docsDevSoftwareGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 3, 83, 4, 1, 3)
)
docsDevSoftwareGroupV2.setObjects(
      *(("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevSwFilename"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevSwAdminStatus"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevSwOperStatus"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevSwCurrentVers"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevSwServerAddress"))
)
if mibBuilder.loadTexts:
    docsDevSoftwareGroupV2.setStatus("current")

docsDevServerGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 3, 83, 4, 1, 4)
)
docsDevServerGroupV2.setObjects(
      *(("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevServerBootState"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevServerDhcpAddress"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevServerTimeAddress"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevServerConfigTftpAddress"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevServerConfigFile"))
)
if mibBuilder.loadTexts:
    docsDevServerGroupV2.setStatus("current")

docsDevEventGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 3, 83, 4, 1, 5)
)
docsDevEventGroupV2.setObjects(
      *(("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevEvControl"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevEvThrottleAdminStatus"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevEvThrottleInhibited"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevEvThrottleThreshold"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevEvThrottleInterval"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevEvReporting"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevEvFirstTime"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevEvLastTime"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevEvCounts"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevEvSyslogAddress"))
)
if mibBuilder.loadTexts:
    docsDevEventGroupV2.setStatus("current")

docsDevFilterGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 3, 83, 4, 1, 6)
)
docsDevFilterGroupV2.setObjects(
      *(("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterLLCUnmatchedAction"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpDefault"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterLLCStatus"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterLLCProtocolType"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterLLCProtocol"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterLLCMatches"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterLLCInterfaces"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterLLCInterfaceSet"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpControl"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpStatus"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpDirection"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpBroadcast"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpSaddr"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpSmask"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpDaddr"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpDmask"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpProtocol"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpSourcePortLow"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpSourcePortHigh"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpDestPortLow"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpDestPortHigh"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpMatches"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpInterfaces"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpInterfaceSet"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpTos"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpTosMask"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpContinue"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpPolicyId"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterPolicyId"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterPolicyStatus"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterPolicyPtr"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterTosStatus"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterTosAndMask"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterTosOrMask"))
)
if mibBuilder.loadTexts:
    docsDevFilterGroupV2.setStatus("current")

docsDevCpeGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 3, 83, 4, 1, 7)
)
docsDevCpeGroupV2.setObjects(
      *(("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevCpeEnroll"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevCpeIpMax"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevCpeSource"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevCpeStatus"))
)
if mibBuilder.loadTexts:
    docsDevCpeGroupV2.setStatus("current")

docsDevDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 83, 4, 1, 8)
)
docsDevDeprecatedGroup.setObjects(
      *(("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterLLCIfIndex"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpIfIndex"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevSwServer"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevServerDhcp"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevServerTime"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevServerTftp"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevEvSyslog"))
)
if mibBuilder.loadTexts:
    docsDevDeprecatedGroup.setStatus("deprecated")

docsDevIpV6Group = ObjectGroup(
    (1, 3, 6, 1, 3, 83, 4, 1, 9)
)
docsDevIpV6Group.setObjects(
      *(("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpType"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpV6Saddr"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpV6Smask"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpV6Daddr"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevFilterIpV6Dmask"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevCpeV6Source"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevCpeV6Status"))
)
if mibBuilder.loadTexts:
    docsDevIpV6Group.setStatus("current")

docsDevSnmpCoexistGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 83, 4, 1, 10)
)
docsDevSnmpCoexistGroup.setObjects(
      *(("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevVacmAccessInterfaces"),
        ("EXP-DOCS-CABLE-DEVICE-MIB", "docsDevVacmAccessInterfaceSet"))
)
if mibBuilder.loadTexts:
    docsDevSnmpCoexistGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsDevBasicComplianceV2 = ModuleCompliance(
    (1, 3, 6, 1, 3, 83, 4, 2, 1)
)
if mibBuilder.loadTexts:
    docsDevBasicComplianceV2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXP-DOCS-CABLE-DEVICE-MIB",
    **{"InterfaceSet": InterfaceSet,
       "IpV4orV6Address": IpV4orV6Address,
       "docsDev": docsDev,
       "docsDevMIBObjects": docsDevMIBObjects,
       "docsDevBase": docsDevBase,
       "docsDevRole": docsDevRole,
       "docsDevDateTime": docsDevDateTime,
       "docsDevResetNow": docsDevResetNow,
       "docsDevSerialNumber": docsDevSerialNumber,
       "docsDevSTPControl": docsDevSTPControl,
       "docsDevNmAccessTable": docsDevNmAccessTable,
       "docsDevNmAccessEntry": docsDevNmAccessEntry,
       "docsDevNmAccessIndex": docsDevNmAccessIndex,
       "docsDevNmAccessIp": docsDevNmAccessIp,
       "docsDevNmAccessIpMask": docsDevNmAccessIpMask,
       "docsDevNmAccessCommunity": docsDevNmAccessCommunity,
       "docsDevNmAccessControl": docsDevNmAccessControl,
       "docsDevNmAccessInterfaces": docsDevNmAccessInterfaces,
       "docsDevNmAccessStatus": docsDevNmAccessStatus,
       "docsDevSoftware": docsDevSoftware,
       "docsDevSwServer": docsDevSwServer,
       "docsDevSwFilename": docsDevSwFilename,
       "docsDevSwAdminStatus": docsDevSwAdminStatus,
       "docsDevSwOperStatus": docsDevSwOperStatus,
       "docsDevSwCurrentVers": docsDevSwCurrentVers,
       "docsDevSwServerAddress": docsDevSwServerAddress,
       "docsDevServer": docsDevServer,
       "docsDevServerBootState": docsDevServerBootState,
       "docsDevServerDhcp": docsDevServerDhcp,
       "docsDevServerTime": docsDevServerTime,
       "docsDevServerTftp": docsDevServerTftp,
       "docsDevServerConfigFile": docsDevServerConfigFile,
       "docsDevServerDhcpAddress": docsDevServerDhcpAddress,
       "docsDevServerTimeAddress": docsDevServerTimeAddress,
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
       "docsDevEvSyslogAddress": docsDevEvSyslogAddress,
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
       "docsDevFilterLLCInterfaces": docsDevFilterLLCInterfaces,
       "docsDevFilterLLCInterfaceSet": docsDevFilterLLCInterfaceSet,
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
       "docsDevFilterIpInterfaces": docsDevFilterIpInterfaces,
       "docsDevFilterIpInterfaceSet": docsDevFilterIpInterfaceSet,
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
       "docsDevFilterIpV6AuxTable": docsDevFilterIpV6AuxTable,
       "docsDevFilterIpV6AuxEntry": docsDevFilterIpV6AuxEntry,
       "docsDevFilterIpType": docsDevFilterIpType,
       "docsDevFilterIpV6Saddr": docsDevFilterIpV6Saddr,
       "docsDevFilterIpV6Smask": docsDevFilterIpV6Smask,
       "docsDevFilterIpV6Daddr": docsDevFilterIpV6Daddr,
       "docsDevFilterIpV6Dmask": docsDevFilterIpV6Dmask,
       "docsDevCpe": docsDevCpe,
       "docsDevCpeEnroll": docsDevCpeEnroll,
       "docsDevCpeIpMax": docsDevCpeIpMax,
       "docsDevCpeTable": docsDevCpeTable,
       "docsDevCpeEntry": docsDevCpeEntry,
       "docsDevCpeIp": docsDevCpeIp,
       "docsDevCpeSource": docsDevCpeSource,
       "docsDevCpeStatus": docsDevCpeStatus,
       "docsDevCpeV6Table": docsDevCpeV6Table,
       "docsDevCpeV6Entry": docsDevCpeV6Entry,
       "docsDevCpeV6Ip": docsDevCpeV6Ip,
       "docsDevCpeV6Source": docsDevCpeV6Source,
       "docsDevCpeV6Status": docsDevCpeV6Status,
       "docsDevVacmAccessExtTable": docsDevVacmAccessExtTable,
       "docsDevVacmAccessExtEntry": docsDevVacmAccessExtEntry,
       "docsDevVacmAccessInterfaces": docsDevVacmAccessInterfaces,
       "docsDevVacmAccessInterfaceSet": docsDevVacmAccessInterfaceSet,
       "docsDevNotification": docsDevNotification,
       "docsDevConformanceV2": docsDevConformanceV2,
       "docsDevGroupsV2": docsDevGroupsV2,
       "docsDevBaseGroupV2": docsDevBaseGroupV2,
       "docsDevNmAccessGroupV2": docsDevNmAccessGroupV2,
       "docsDevSoftwareGroupV2": docsDevSoftwareGroupV2,
       "docsDevServerGroupV2": docsDevServerGroupV2,
       "docsDevEventGroupV2": docsDevEventGroupV2,
       "docsDevFilterGroupV2": docsDevFilterGroupV2,
       "docsDevCpeGroupV2": docsDevCpeGroupV2,
       "docsDevDeprecatedGroup": docsDevDeprecatedGroup,
       "docsDevIpV6Group": docsDevIpV6Group,
       "docsDevSnmpCoexistGroup": docsDevSnmpCoexistGroup,
       "docsDevCompliancesV2": docsDevCompliancesV2,
       "docsDevBasicComplianceV2": docsDevBasicComplianceV2}
)
