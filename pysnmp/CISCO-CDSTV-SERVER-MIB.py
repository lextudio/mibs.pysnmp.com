# SNMP MIB module (CISCO-CDSTV-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CDSTV-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:20 2024
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

(Dscp,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoCdstvServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 754)
)
ciscoCdstvServerMIB.setRevisions(
        ("2012-12-12 00:00",
         "2010-07-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoCdstvEcn(Integer32, TextualConvention):
    status = "current"
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
        *(("congestion", 3),
          ("disabled", 4),
          ("ect0", 2),
          ("ect1", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCdstvServerMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCdstvServerMIBNotifs = _CiscoCdstvServerMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 0)
)
_CiscoCdstvServerMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCdstvServerMIBObjects = _CiscoCdstvServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1)
)
_CdstvServerCommonObjects_ObjectIdentity = ObjectIdentity
cdstvServerCommonObjects = _CdstvServerCommonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1)
)


class _CdstvServerRole_Type(Integer32):
    """Custom type cdstvServerRole based on Integer32"""
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
        *(("cachingserver", 5),
          ("controller", 4),
          ("isv", 1),
          ("recorder", 6),
          ("streamer", 3),
          ("vault", 2))
    )


_CdstvServerRole_Type.__name__ = "Integer32"
_CdstvServerRole_Object = MibScalar
cdstvServerRole = _CdstvServerRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 1),
    _CdstvServerRole_Type()
)
cdstvServerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvServerRole.setStatus("current")
_CdstvServerPartNo_Type = SnmpAdminString
_CdstvServerPartNo_Object = MibScalar
cdstvServerPartNo = _CdstvServerPartNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 2),
    _CdstvServerPartNo_Type()
)
cdstvServerPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvServerPartNo.setStatus("current")
_CdstvServerID_Type = Unsigned32
_CdstvServerID_Object = MibScalar
cdstvServerID = _CdstvServerID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 3),
    _CdstvServerID_Type()
)
cdstvServerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvServerID.setStatus("current")
_CdstvServerGroupID_Type = Unsigned32
_CdstvServerGroupID_Object = MibScalar
cdstvServerGroupID = _CdstvServerGroupID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 4),
    _CdstvServerGroupID_Type()
)
cdstvServerGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvServerGroupID.setStatus("current")


class _CdstvServerHostname_Type(SnmpAdminString):
    """Custom type cdstvServerHostname based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CdstvServerHostname_Type.__name__ = "SnmpAdminString"
_CdstvServerHostname_Object = MibScalar
cdstvServerHostname = _CdstvServerHostname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 5),
    _CdstvServerHostname_Type()
)
cdstvServerHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvServerHostname.setStatus("current")


class _CdstvServerTTL_Type(Unsigned32):
    """Custom type cdstvServerTTL based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CdstvServerTTL_Type.__name__ = "Unsigned32"
_CdstvServerTTL_Object = MibScalar
cdstvServerTTL = _CdstvServerTTL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 6),
    _CdstvServerTTL_Type()
)
cdstvServerTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvServerTTL.setStatus("current")
if mibBuilder.loadTexts:
    cdstvServerTTL.setUnits("hops")
_CdstvServerDefaultStreamCacheSettings_ObjectIdentity = ObjectIdentity
cdstvServerDefaultStreamCacheSettings = _CdstvServerDefaultStreamCacheSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 7)
)


class _CdstvServerSourceAddressType_Type(InetAddressType):
    """Custom type cdstvServerSourceAddressType based on InetAddressType"""


_CdstvServerSourceAddressType_Object = MibScalar
cdstvServerSourceAddressType = _CdstvServerSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 7, 1),
    _CdstvServerSourceAddressType_Type()
)
cdstvServerSourceAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvServerSourceAddressType.setStatus("current")


class _CdstvServerSourceAddress_Type(InetAddress):
    """Custom type cdstvServerSourceAddress based on InetAddress"""
    defaultValue = OctetString("192.168.207.65")


_CdstvServerSourceAddress_Object = MibScalar
cdstvServerSourceAddress = _CdstvServerSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 7, 2),
    _CdstvServerSourceAddress_Type()
)
cdstvServerSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvServerSourceAddress.setStatus("current")


class _CdstvServerCachePort_Type(InetPortNumber):
    """Custom type cdstvServerCachePort based on InetPortNumber"""
    defaultValue = 48879


_CdstvServerCachePort_Object = MibScalar
cdstvServerCachePort = _CdstvServerCachePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 7, 3),
    _CdstvServerCachePort_Type()
)
cdstvServerCachePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvServerCachePort.setStatus("current")
_CdstvCacheJumboFramesEnable_Type = TruthValue
_CdstvCacheJumboFramesEnable_Object = MibScalar
cdstvCacheJumboFramesEnable = _CdstvCacheJumboFramesEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 8),
    _CdstvCacheJumboFramesEnable_Type()
)
cdstvCacheJumboFramesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvCacheJumboFramesEnable.setStatus("current")
_CdstvServerOffloadEnable_Type = TruthValue
_CdstvServerOffloadEnable_Object = MibScalar
cdstvServerOffloadEnable = _CdstvServerOffloadEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 9),
    _CdstvServerOffloadEnable_Type()
)
cdstvServerOffloadEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvServerOffloadEnable.setStatus("current")
_CdstvServerTransportCacheIPPkts_ObjectIdentity = ObjectIdentity
cdstvServerTransportCacheIPPkts = _CdstvServerTransportCacheIPPkts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 10)
)
_CdstvServerTransportDSCP_Type = Dscp
_CdstvServerTransportDSCP_Object = MibScalar
cdstvServerTransportDSCP = _CdstvServerTransportDSCP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 10, 1),
    _CdstvServerTransportDSCP_Type()
)
cdstvServerTransportDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvServerTransportDSCP.setStatus("current")
_CdstvServerTransportECN_Type = CiscoCdstvEcn
_CdstvServerTransportECN_Object = MibScalar
cdstvServerTransportECN = _CdstvServerTransportECN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 10, 2),
    _CdstvServerTransportECN_Type()
)
cdstvServerTransportECN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvServerTransportECN.setStatus("current")
_CdstvServerCacheDSCP_Type = Dscp
_CdstvServerCacheDSCP_Object = MibScalar
cdstvServerCacheDSCP = _CdstvServerCacheDSCP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 10, 3),
    _CdstvServerCacheDSCP_Type()
)
cdstvServerCacheDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvServerCacheDSCP.setStatus("current")
_CdstvServerCacheECN_Type = CiscoCdstvEcn
_CdstvServerCacheECN_Object = MibScalar
cdstvServerCacheECN = _CdstvServerCacheECN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 10, 4),
    _CdstvServerCacheECN_Type()
)
cdstvServerCacheECN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvServerCacheECN.setStatus("current")
_CdstvServerNullStreamingEnable_Type = TruthValue
_CdstvServerNullStreamingEnable_Object = MibScalar
cdstvServerNullStreamingEnable = _CdstvServerNullStreamingEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 1, 11),
    _CdstvServerNullStreamingEnable_Type()
)
cdstvServerNullStreamingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvServerNullStreamingEnable.setStatus("current")
_CdstvServerStreamingObjects_ObjectIdentity = ObjectIdentity
cdstvServerStreamingObjects = _CdstvServerStreamingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2)
)


class _CdstvServerStartingTransportPort_Type(InetPortNumber):
    """Custom type cdstvServerStartingTransportPort based on InetPortNumber"""
    defaultValue = 48879


_CdstvServerStartingTransportPort_Object = MibScalar
cdstvServerStartingTransportPort = _CdstvServerStartingTransportPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2, 1),
    _CdstvServerStartingTransportPort_Type()
)
cdstvServerStartingTransportPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvServerStartingTransportPort.setStatus("current")
_CdstvServerEndingTransportPort_Type = InetPortNumber
_CdstvServerEndingTransportPort_Object = MibScalar
cdstvServerEndingTransportPort = _CdstvServerEndingTransportPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2, 2),
    _CdstvServerEndingTransportPort_Type()
)
cdstvServerEndingTransportPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvServerEndingTransportPort.setStatus("current")
_CdstvStreamJumboFramesEnable_Type = TruthValue
_CdstvStreamJumboFramesEnable_Object = MibScalar
cdstvStreamJumboFramesEnable = _CdstvStreamJumboFramesEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2, 3),
    _CdstvStreamJumboFramesEnable_Type()
)
cdstvStreamJumboFramesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvStreamJumboFramesEnable.setStatus("current")
_CdstvServerStreamGroupInfo_ObjectIdentity = ObjectIdentity
cdstvServerStreamGroupInfo = _CdstvServerStreamGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2, 4)
)
_CdstvServerStreamGroupName_Type = SnmpAdminString
_CdstvServerStreamGroupName_Object = MibScalar
cdstvServerStreamGroupName = _CdstvServerStreamGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2, 4, 1),
    _CdstvServerStreamGroupName_Type()
)
cdstvServerStreamGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvServerStreamGroupName.setStatus("current")
_CdstvServerStreamGroupID_Type = Unsigned32
_CdstvServerStreamGroupID_Object = MibScalar
cdstvServerStreamGroupID = _CdstvServerStreamGroupID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2, 4, 2),
    _CdstvServerStreamGroupID_Type()
)
cdstvServerStreamGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvServerStreamGroupID.setStatus("current")
_CdstvServerStreamerIsCache_Type = TruthValue
_CdstvServerStreamerIsCache_Object = MibScalar
cdstvServerStreamerIsCache = _CdstvServerStreamerIsCache_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 2, 4, 3),
    _CdstvServerStreamerIsCache_Type()
)
cdstvServerStreamerIsCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvServerStreamerIsCache.setStatus("current")
_CdstvServerStorageObjects_ObjectIdentity = ObjectIdentity
cdstvServerStorageObjects = _CdstvServerStorageObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3)
)


class _CdstvVaultMirrorCopies_Type(Unsigned32):
    """Custom type cdstvVaultMirrorCopies based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CdstvVaultMirrorCopies_Type.__name__ = "Unsigned32"
_CdstvVaultMirrorCopies_Object = MibScalar
cdstvVaultMirrorCopies = _CdstvVaultMirrorCopies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 1),
    _CdstvVaultMirrorCopies_Type()
)
cdstvVaultMirrorCopies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvVaultMirrorCopies.setStatus("current")
if mibBuilder.loadTexts:
    cdstvVaultMirrorCopies.setUnits("copies")


class _CdstvVaultLocalCopies_Type(Unsigned32):
    """Custom type cdstvVaultLocalCopies based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_CdstvVaultLocalCopies_Type.__name__ = "Unsigned32"
_CdstvVaultLocalCopies_Object = MibScalar
cdstvVaultLocalCopies = _CdstvVaultLocalCopies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 2),
    _CdstvVaultLocalCopies_Type()
)
cdstvVaultLocalCopies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvVaultLocalCopies.setStatus("current")
if mibBuilder.loadTexts:
    cdstvVaultLocalCopies.setUnits("copies")
_CdstvServerFTPOutSettings_ObjectIdentity = ObjectIdentity
cdstvServerFTPOutSettings = _CdstvServerFTPOutSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 3)
)


class _CdstvServerFTPOutInterface_Type(Integer32):
    """Custom type cdstvServerFTPOutInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingest", 2),
          ("management", 1))
    )


_CdstvServerFTPOutInterface_Type.__name__ = "Integer32"
_CdstvServerFTPOutInterface_Object = MibScalar
cdstvServerFTPOutInterface = _CdstvServerFTPOutInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 3, 1),
    _CdstvServerFTPOutInterface_Type()
)
cdstvServerFTPOutInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvServerFTPOutInterface.setStatus("current")


class _CdstvServerFTPOutBandwidth_Type(Unsigned32):
    """Custom type cdstvServerFTPOutBandwidth based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CdstvServerFTPOutBandwidth_Type.__name__ = "Unsigned32"
_CdstvServerFTPOutBandwidth_Object = MibScalar
cdstvServerFTPOutBandwidth = _CdstvServerFTPOutBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 3, 2),
    _CdstvServerFTPOutBandwidth_Type()
)
cdstvServerFTPOutBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvServerFTPOutBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    cdstvServerFTPOutBandwidth.setUnits("Mbps")


class _CdstvServerFTPOutSessions_Type(Unsigned32):
    """Custom type cdstvServerFTPOutSessions based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CdstvServerFTPOutSessions_Type.__name__ = "Unsigned32"
_CdstvServerFTPOutSessions_Object = MibScalar
cdstvServerFTPOutSessions = _CdstvServerFTPOutSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 3, 3),
    _CdstvServerFTPOutSessions_Type()
)
cdstvServerFTPOutSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdstvServerFTPOutSessions.setStatus("current")
if mibBuilder.loadTexts:
    cdstvServerFTPOutSessions.setUnits("sessions")
_CdstvServerVaultGroupInformation_ObjectIdentity = ObjectIdentity
cdstvServerVaultGroupInformation = _CdstvServerVaultGroupInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 4)
)
_CdstvServerVaultGroupName_Type = SnmpAdminString
_CdstvServerVaultGroupName_Object = MibScalar
cdstvServerVaultGroupName = _CdstvServerVaultGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 4, 1),
    _CdstvServerVaultGroupName_Type()
)
cdstvServerVaultGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvServerVaultGroupName.setStatus("current")
_CdstvServerVaultGroupID_Type = Unsigned32
_CdstvServerVaultGroupID_Object = MibScalar
cdstvServerVaultGroupID = _CdstvServerVaultGroupID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 3, 4, 2),
    _CdstvServerVaultGroupID_Type()
)
cdstvServerVaultGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvServerVaultGroupID.setStatus("current")
_CdstvServerCachingObjects_ObjectIdentity = ObjectIdentity
cdstvServerCachingObjects = _CdstvServerCachingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 4)
)
_CdstvServerCacheGroupInformation_ObjectIdentity = ObjectIdentity
cdstvServerCacheGroupInformation = _CdstvServerCacheGroupInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 4, 1)
)
_CdstvServerCacheGroupName_Type = SnmpAdminString
_CdstvServerCacheGroupName_Object = MibScalar
cdstvServerCacheGroupName = _CdstvServerCacheGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 4, 1, 1),
    _CdstvServerCacheGroupName_Type()
)
cdstvServerCacheGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvServerCacheGroupName.setStatus("current")
_CdstvServerCacheGroupID_Type = Unsigned32
_CdstvServerCacheGroupID_Object = MibScalar
cdstvServerCacheGroupID = _CdstvServerCacheGroupID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 1, 4, 1, 2),
    _CdstvServerCacheGroupID_Type()
)
cdstvServerCacheGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvServerCacheGroupID.setStatus("current")
_CiscoCdstvServerMIBConform_ObjectIdentity = ObjectIdentity
ciscoCdstvServerMIBConform = _CiscoCdstvServerMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 2)
)
_CiscoCdstvServerMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCdstvServerMIBCompliances = _CiscoCdstvServerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 2, 1)
)
_CiscoCdstvServerMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCdstvServerMIBGroups = _CiscoCdstvServerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 2, 2)
)

# Managed Objects groups

ciscoCdstvServerMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 2, 2, 1)
)
ciscoCdstvServerMIBMainObjectGroup.setObjects(
      *(("CISCO-CDSTV-SERVER-MIB", "cdstvServerRole"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerPartNo"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerID"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerGroupID"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerHostname"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerTTL"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerSourceAddress"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerCachePort"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvCacheJumboFramesEnable"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerOffloadEnable"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerTransportDSCP"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerTransportECN"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerCacheDSCP"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerCacheECN"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerSourceAddressType"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerNullStreamingEnable"))
)
if mibBuilder.loadTexts:
    ciscoCdstvServerMIBMainObjectGroup.setStatus("current")

ciscoCdstvServerMIBStreamingObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 2, 2, 2)
)
ciscoCdstvServerMIBStreamingObjectGroup.setObjects(
      *(("CISCO-CDSTV-SERVER-MIB", "cdstvServerStartingTransportPort"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerEndingTransportPort"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvStreamJumboFramesEnable"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerStreamGroupName"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerStreamGroupID"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerStreamerIsCache"))
)
if mibBuilder.loadTexts:
    ciscoCdstvServerMIBStreamingObjectGroup.setStatus("current")

ciscoCdstvServerMIBStorageObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 2, 2, 3)
)
ciscoCdstvServerMIBStorageObjectGroup.setObjects(
      *(("CISCO-CDSTV-SERVER-MIB", "cdstvVaultMirrorCopies"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvVaultLocalCopies"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerFTPOutInterface"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerFTPOutBandwidth"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerFTPOutSessions"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerVaultGroupName"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerVaultGroupID"))
)
if mibBuilder.loadTexts:
    ciscoCdstvServerMIBStorageObjectGroup.setStatus("current")

ciscoCdstvServerMIBCachingObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 2, 2, 4)
)
ciscoCdstvServerMIBCachingObjectGroup.setObjects(
      *(("CISCO-CDSTV-SERVER-MIB", "cdstvServerCacheGroupName"),
        ("CISCO-CDSTV-SERVER-MIB", "cdstvServerCacheGroupID"))
)
if mibBuilder.loadTexts:
    ciscoCdstvServerMIBCachingObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCdstvServerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 754, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCdstvServerMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CDSTV-SERVER-MIB",
    **{"CiscoCdstvEcn": CiscoCdstvEcn,
       "ciscoCdstvServerMIB": ciscoCdstvServerMIB,
       "ciscoCdstvServerMIBNotifs": ciscoCdstvServerMIBNotifs,
       "ciscoCdstvServerMIBObjects": ciscoCdstvServerMIBObjects,
       "cdstvServerCommonObjects": cdstvServerCommonObjects,
       "cdstvServerRole": cdstvServerRole,
       "cdstvServerPartNo": cdstvServerPartNo,
       "cdstvServerID": cdstvServerID,
       "cdstvServerGroupID": cdstvServerGroupID,
       "cdstvServerHostname": cdstvServerHostname,
       "cdstvServerTTL": cdstvServerTTL,
       "cdstvServerDefaultStreamCacheSettings": cdstvServerDefaultStreamCacheSettings,
       "cdstvServerSourceAddressType": cdstvServerSourceAddressType,
       "cdstvServerSourceAddress": cdstvServerSourceAddress,
       "cdstvServerCachePort": cdstvServerCachePort,
       "cdstvCacheJumboFramesEnable": cdstvCacheJumboFramesEnable,
       "cdstvServerOffloadEnable": cdstvServerOffloadEnable,
       "cdstvServerTransportCacheIPPkts": cdstvServerTransportCacheIPPkts,
       "cdstvServerTransportDSCP": cdstvServerTransportDSCP,
       "cdstvServerTransportECN": cdstvServerTransportECN,
       "cdstvServerCacheDSCP": cdstvServerCacheDSCP,
       "cdstvServerCacheECN": cdstvServerCacheECN,
       "cdstvServerNullStreamingEnable": cdstvServerNullStreamingEnable,
       "cdstvServerStreamingObjects": cdstvServerStreamingObjects,
       "cdstvServerStartingTransportPort": cdstvServerStartingTransportPort,
       "cdstvServerEndingTransportPort": cdstvServerEndingTransportPort,
       "cdstvStreamJumboFramesEnable": cdstvStreamJumboFramesEnable,
       "cdstvServerStreamGroupInfo": cdstvServerStreamGroupInfo,
       "cdstvServerStreamGroupName": cdstvServerStreamGroupName,
       "cdstvServerStreamGroupID": cdstvServerStreamGroupID,
       "cdstvServerStreamerIsCache": cdstvServerStreamerIsCache,
       "cdstvServerStorageObjects": cdstvServerStorageObjects,
       "cdstvVaultMirrorCopies": cdstvVaultMirrorCopies,
       "cdstvVaultLocalCopies": cdstvVaultLocalCopies,
       "cdstvServerFTPOutSettings": cdstvServerFTPOutSettings,
       "cdstvServerFTPOutInterface": cdstvServerFTPOutInterface,
       "cdstvServerFTPOutBandwidth": cdstvServerFTPOutBandwidth,
       "cdstvServerFTPOutSessions": cdstvServerFTPOutSessions,
       "cdstvServerVaultGroupInformation": cdstvServerVaultGroupInformation,
       "cdstvServerVaultGroupName": cdstvServerVaultGroupName,
       "cdstvServerVaultGroupID": cdstvServerVaultGroupID,
       "cdstvServerCachingObjects": cdstvServerCachingObjects,
       "cdstvServerCacheGroupInformation": cdstvServerCacheGroupInformation,
       "cdstvServerCacheGroupName": cdstvServerCacheGroupName,
       "cdstvServerCacheGroupID": cdstvServerCacheGroupID,
       "ciscoCdstvServerMIBConform": ciscoCdstvServerMIBConform,
       "ciscoCdstvServerMIBCompliances": ciscoCdstvServerMIBCompliances,
       "ciscoCdstvServerMIBCompliance": ciscoCdstvServerMIBCompliance,
       "ciscoCdstvServerMIBGroups": ciscoCdstvServerMIBGroups,
       "ciscoCdstvServerMIBMainObjectGroup": ciscoCdstvServerMIBMainObjectGroup,
       "ciscoCdstvServerMIBStreamingObjectGroup": ciscoCdstvServerMIBStreamingObjectGroup,
       "ciscoCdstvServerMIBStorageObjectGroup": ciscoCdstvServerMIBStorageObjectGroup,
       "ciscoCdstvServerMIBCachingObjectGroup": ciscoCdstvServerMIBCachingObjectGroup}
)
