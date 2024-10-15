# SNMP MIB module (CISCO-VPN-LIC-USAGE-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VPN-LIC-USAGE-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:35 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoVpnLicUsageMonitorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 816)
)
ciscoVpnLicUsageMonitorMIB.setRevisions(
        ("2013-09-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VPNLicType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("anyconnectpremium", 2),
          ("other", 1))
    )



class VPNLicDeviceRole(Integer32, TextualConvention):
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
        *(("bkpserver", 2),
          ("client", 3),
          ("server", 1))
    )



class LicServerStatus(Integer32, TextualConvention):
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
        *(("active", 1),
          ("expired", 3),
          ("inactive", 2))
    )



class LicServerRegistered(Integer32, TextualConvention):
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
        *(("invalid", 3),
          ("no", 1),
          ("yes", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoVpnLicUsageMonitorMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVpnLicUsageMonitorMIBObjects = _CiscoVpnLicUsageMonitorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0)
)
_CvpnLicDeviceRole_Type = VPNLicDeviceRole
_CvpnLicDeviceRole_Object = MibScalar
cvpnLicDeviceRole = _CvpnLicDeviceRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 1),
    _CvpnLicDeviceRole_Type()
)
cvpnLicDeviceRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicDeviceRole.setStatus("current")
_CvpnLicServer_ObjectIdentity = ObjectIdentity
cvpnLicServer = _CvpnLicServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 2)
)
_CvpnLicServerAddrType_Type = InetAddressType
_CvpnLicServerAddrType_Object = MibScalar
cvpnLicServerAddrType = _CvpnLicServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 2, 1),
    _CvpnLicServerAddrType_Type()
)
cvpnLicServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicServerAddrType.setStatus("current")
_CvpnLicServerAddr_Type = InetAddress
_CvpnLicServerAddr_Object = MibScalar
cvpnLicServerAddr = _CvpnLicServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 2, 2),
    _CvpnLicServerAddr_Type()
)
cvpnLicServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicServerAddr.setStatus("current")
_CvpnLicBkpSerAddrType_Type = InetAddressType
_CvpnLicBkpSerAddrType_Object = MibScalar
cvpnLicBkpSerAddrType = _CvpnLicBkpSerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 2, 3),
    _CvpnLicBkpSerAddrType_Type()
)
cvpnLicBkpSerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicBkpSerAddrType.setStatus("current")
_CvpnLicBkpSerAddr_Type = InetAddress
_CvpnLicBkpSerAddr_Object = MibScalar
cvpnLicBkpSerAddr = _CvpnLicBkpSerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 2, 4),
    _CvpnLicBkpSerAddr_Type()
)
cvpnLicBkpSerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicBkpSerAddr.setStatus("current")


class _CvpnLicServerVer_Type(Integer32):
    """Custom type cvpnLicServerVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CvpnLicServerVer_Type.__name__ = "Integer32"
_CvpnLicServerVer_Object = MibScalar
cvpnLicServerVer = _CvpnLicServerVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 2, 5),
    _CvpnLicServerVer_Type()
)
cvpnLicServerVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicServerVer.setStatus("current")
_CvpnLicServerStatus_Type = LicServerStatus
_CvpnLicServerStatus_Object = MibScalar
cvpnLicServerStatus = _CvpnLicServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 2, 6),
    _CvpnLicServerStatus_Type()
)
cvpnLicServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicServerStatus.setStatus("current")
_CvpnLicServerTable_Object = MibTable
cvpnLicServerTable = _CvpnLicServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 2, 7)
)
if mibBuilder.loadTexts:
    cvpnLicServerTable.setStatus("current")
_CvpnLicServerEntry_Object = MibTableRow
cvpnLicServerEntry = _CvpnLicServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 2, 7, 1)
)
cvpnLicServerEntry.setIndexNames(
    (0, "CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicServerVPNLicType"),
)
if mibBuilder.loadTexts:
    cvpnLicServerEntry.setStatus("current")
_CvpnLicServerVPNLicType_Type = VPNLicType
_CvpnLicServerVPNLicType_Object = MibTableColumn
cvpnLicServerVPNLicType = _CvpnLicServerVPNLicType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 2, 7, 1, 1),
    _CvpnLicServerVPNLicType_Type()
)
cvpnLicServerVPNLicType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvpnLicServerVPNLicType.setStatus("current")


class _CvpnLicServerNumLicCapacity_Type(Unsigned32):
    """Custom type cvpnLicServerNumLicCapacity based on Unsigned32"""
    defaultValue = 0


_CvpnLicServerNumLicCapacity_Object = MibTableColumn
cvpnLicServerNumLicCapacity = _CvpnLicServerNumLicCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 2, 7, 1, 2),
    _CvpnLicServerNumLicCapacity_Type()
)
cvpnLicServerNumLicCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicServerNumLicCapacity.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicServerNumLicCapacity.setUnits("license")


class _CvpnLicServerNumLicAvail_Type(Unsigned32):
    """Custom type cvpnLicServerNumLicAvail based on Unsigned32"""
    defaultValue = 0


_CvpnLicServerNumLicAvail_Object = MibTableColumn
cvpnLicServerNumLicAvail = _CvpnLicServerNumLicAvail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 2, 7, 1, 3),
    _CvpnLicServerNumLicAvail_Type()
)
cvpnLicServerNumLicAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicServerNumLicAvail.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicServerNumLicAvail.setUnits("license")


class _CvpnLicServerUtilized_Type(Unsigned32):
    """Custom type cvpnLicServerUtilized based on Unsigned32"""
    defaultValue = 0


_CvpnLicServerUtilized_Object = MibTableColumn
cvpnLicServerUtilized = _CvpnLicServerUtilized_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 2, 7, 1, 4),
    _CvpnLicServerUtilized_Type()
)
cvpnLicServerUtilized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicServerUtilized.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicServerUtilized.setUnits("license")
_CvpnLicBkpServer_ObjectIdentity = ObjectIdentity
cvpnLicBkpServer = _CvpnLicBkpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 3)
)
_CvpnLicBkpServerAddrType_Type = InetAddressType
_CvpnLicBkpServerAddrType_Object = MibScalar
cvpnLicBkpServerAddrType = _CvpnLicBkpServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 3, 1),
    _CvpnLicBkpServerAddrType_Type()
)
cvpnLicBkpServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicBkpServerAddrType.setStatus("current")
_CvpnLicBkpServerAddr_Type = InetAddress
_CvpnLicBkpServerAddr_Object = MibScalar
cvpnLicBkpServerAddr = _CvpnLicBkpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 3, 2),
    _CvpnLicBkpServerAddr_Type()
)
cvpnLicBkpServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicBkpServerAddr.setStatus("current")


class _CvpnLicBkpServerDevID_Type(SnmpAdminString):
    """Custom type cvpnLicBkpServerDevID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CvpnLicBkpServerDevID_Type.__name__ = "SnmpAdminString"
_CvpnLicBkpServerDevID_Object = MibScalar
cvpnLicBkpServerDevID = _CvpnLicBkpServerDevID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 3, 3),
    _CvpnLicBkpServerDevID_Type()
)
cvpnLicBkpServerDevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicBkpServerDevID.setStatus("current")
_CvpnLicBkpServerVer_Type = Unsigned32
_CvpnLicBkpServerVer_Object = MibScalar
cvpnLicBkpServerVer = _CvpnLicBkpServerVer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 3, 4),
    _CvpnLicBkpServerVer_Type()
)
cvpnLicBkpServerVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicBkpServerVer.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicBkpServerVer.setUnits("license")
_CvpnLicBkpServerRegd_Type = LicServerRegistered
_CvpnLicBkpServerRegd_Object = MibScalar
cvpnLicBkpServerRegd = _CvpnLicBkpServerRegd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 3, 5),
    _CvpnLicBkpServerRegd_Type()
)
cvpnLicBkpServerRegd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicBkpServerRegd.setStatus("current")


class _CvpnLicBkpServerHAPeerDevID_Type(SnmpAdminString):
    """Custom type cvpnLicBkpServerHAPeerDevID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CvpnLicBkpServerHAPeerDevID_Type.__name__ = "SnmpAdminString"
_CvpnLicBkpServerHAPeerDevID_Object = MibScalar
cvpnLicBkpServerHAPeerDevID = _CvpnLicBkpServerHAPeerDevID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 3, 6),
    _CvpnLicBkpServerHAPeerDevID_Type()
)
cvpnLicBkpServerHAPeerDevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicBkpServerHAPeerDevID.setStatus("current")
_CvpnLicBkpServerHAPeerRegd_Type = LicServerRegistered
_CvpnLicBkpServerHAPeerRegd_Object = MibScalar
cvpnLicBkpServerHAPeerRegd = _CvpnLicBkpServerHAPeerRegd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 3, 7),
    _CvpnLicBkpServerHAPeerRegd_Type()
)
cvpnLicBkpServerHAPeerRegd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicBkpServerHAPeerRegd.setStatus("current")
_CvpnLicBkpServerStatus_Type = LicServerStatus
_CvpnLicBkpServerStatus_Object = MibScalar
cvpnLicBkpServerStatus = _CvpnLicBkpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 3, 8),
    _CvpnLicBkpServerStatus_Type()
)
cvpnLicBkpServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicBkpServerStatus.setStatus("current")
_CvpnLicServerHelloTx_Type = Counter32
_CvpnLicServerHelloTx_Object = MibScalar
cvpnLicServerHelloTx = _CvpnLicServerHelloTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 3, 9),
    _CvpnLicServerHelloTx_Type()
)
cvpnLicServerHelloTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicServerHelloTx.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicServerHelloTx.setUnits("packets")
_CvpnLicServerHelloRx_Type = Counter32
_CvpnLicServerHelloRx_Object = MibScalar
cvpnLicServerHelloRx = _CvpnLicServerHelloRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 3, 10),
    _CvpnLicServerHelloRx_Type()
)
cvpnLicServerHelloRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicServerHelloRx.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicServerHelloRx.setUnits("packets")
_CvpnLicServerHelloError_Type = Counter32
_CvpnLicServerHelloError_Object = MibScalar
cvpnLicServerHelloError = _CvpnLicServerHelloError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 3, 11),
    _CvpnLicServerHelloError_Type()
)
cvpnLicServerHelloError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicServerHelloError.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicServerHelloError.setUnits("packets")
_CvpnLicServerSyncTx_Type = Counter32
_CvpnLicServerSyncTx_Object = MibScalar
cvpnLicServerSyncTx = _CvpnLicServerSyncTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 3, 12),
    _CvpnLicServerSyncTx_Type()
)
cvpnLicServerSyncTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicServerSyncTx.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicServerSyncTx.setUnits("packets")
_CvpnLicServerSyncRx_Type = Counter32
_CvpnLicServerSyncRx_Object = MibScalar
cvpnLicServerSyncRx = _CvpnLicServerSyncRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 3, 13),
    _CvpnLicServerSyncRx_Type()
)
cvpnLicServerSyncRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicServerSyncRx.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicServerSyncRx.setUnits("packets")
_CvpnLicServerSyncError_Type = Counter32
_CvpnLicServerSyncError_Object = MibScalar
cvpnLicServerSyncError = _CvpnLicServerSyncError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 3, 14),
    _CvpnLicServerSyncError_Type()
)
cvpnLicServerSyncError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicServerSyncError.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicServerSyncError.setUnits("packets")
_CvpnLicServerUpdateTx_Type = Counter32
_CvpnLicServerUpdateTx_Object = MibScalar
cvpnLicServerUpdateTx = _CvpnLicServerUpdateTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 3, 15),
    _CvpnLicServerUpdateTx_Type()
)
cvpnLicServerUpdateTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicServerUpdateTx.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicServerUpdateTx.setUnits("packets")
_CvpnLicServerUpdateRx_Type = Counter32
_CvpnLicServerUpdateRx_Object = MibScalar
cvpnLicServerUpdateRx = _CvpnLicServerUpdateRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 3, 16),
    _CvpnLicServerUpdateRx_Type()
)
cvpnLicServerUpdateRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicServerUpdateRx.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicServerUpdateRx.setUnits("packets")
_CvpnLicServerUpdateError_Type = Counter32
_CvpnLicServerUpdateError_Object = MibScalar
cvpnLicServerUpdateError = _CvpnLicServerUpdateError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 3, 17),
    _CvpnLicServerUpdateError_Type()
)
cvpnLicServerUpdateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicServerUpdateError.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicServerUpdateError.setUnits("packets")
_CvpnLicClient_ObjectIdentity = ObjectIdentity
cvpnLicClient = _CvpnLicClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 4)
)
_CvpnLicClntInfoTable_Object = MibTable
cvpnLicClntInfoTable = _CvpnLicClntInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 4, 1)
)
if mibBuilder.loadTexts:
    cvpnLicClntInfoTable.setStatus("current")
_CvpnLicClntInfoEntry_Object = MibTableRow
cvpnLicClntInfoEntry = _CvpnLicClntInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 4, 1, 1)
)
cvpnLicClntInfoEntry.setIndexNames(
    (0, "CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicClntVPNLicType"),
    (0, "CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicClntInfoDeviceID"),
)
if mibBuilder.loadTexts:
    cvpnLicClntInfoEntry.setStatus("current")
_CvpnLicClntVPNLicType_Type = VPNLicType
_CvpnLicClntVPNLicType_Object = MibTableColumn
cvpnLicClntVPNLicType = _CvpnLicClntVPNLicType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 4, 1, 1, 1),
    _CvpnLicClntVPNLicType_Type()
)
cvpnLicClntVPNLicType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvpnLicClntVPNLicType.setStatus("current")


class _CvpnLicClntInfoDeviceID_Type(SnmpAdminString):
    """Custom type cvpnLicClntInfoDeviceID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CvpnLicClntInfoDeviceID_Type.__name__ = "SnmpAdminString"
_CvpnLicClntInfoDeviceID_Object = MibTableColumn
cvpnLicClntInfoDeviceID = _CvpnLicClntInfoDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 4, 1, 1, 2),
    _CvpnLicClntInfoDeviceID_Type()
)
cvpnLicClntInfoDeviceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvpnLicClntInfoDeviceID.setStatus("current")


class _CvpnLicClntInfoHostName_Type(SnmpAdminString):
    """Custom type cvpnLicClntInfoHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CvpnLicClntInfoHostName_Type.__name__ = "SnmpAdminString"
_CvpnLicClntInfoHostName_Object = MibTableColumn
cvpnLicClntInfoHostName = _CvpnLicClntInfoHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 4, 1, 1, 3),
    _CvpnLicClntInfoHostName_Type()
)
cvpnLicClntInfoHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicClntInfoHostName.setStatus("current")
_CvpnLicClntInfoPlatLmt_Type = Unsigned32
_CvpnLicClntInfoPlatLmt_Object = MibTableColumn
cvpnLicClntInfoPlatLmt = _CvpnLicClntInfoPlatLmt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 4, 1, 1, 4),
    _CvpnLicClntInfoPlatLmt_Type()
)
cvpnLicClntInfoPlatLmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicClntInfoPlatLmt.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicClntInfoPlatLmt.setUnits("license")
_CvpnLicClntInfoCurUsage_Type = Unsigned32
_CvpnLicClntInfoCurUsage_Object = MibTableColumn
cvpnLicClntInfoCurUsage = _CvpnLicClntInfoCurUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 4, 1, 1, 5),
    _CvpnLicClntInfoCurUsage_Type()
)
cvpnLicClntInfoCurUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicClntInfoCurUsage.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicClntInfoCurUsage.setUnits("license")
_CvpnLicClntInfoHigh_Type = Unsigned32
_CvpnLicClntInfoHigh_Object = MibTableColumn
cvpnLicClntInfoHigh = _CvpnLicClntInfoHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 4, 1, 1, 6),
    _CvpnLicClntInfoHigh_Type()
)
cvpnLicClntInfoHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicClntInfoHigh.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicClntInfoHigh.setUnits("license")
_CvpnLicClntInfoRegReqTx_Type = Counter32
_CvpnLicClntInfoRegReqTx_Object = MibTableColumn
cvpnLicClntInfoRegReqTx = _CvpnLicClntInfoRegReqTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 4, 1, 1, 7),
    _CvpnLicClntInfoRegReqTx_Type()
)
cvpnLicClntInfoRegReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicClntInfoRegReqTx.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicClntInfoRegReqTx.setUnits("packets")
_CvpnLicClntInfoRegReqRx_Type = Counter32
_CvpnLicClntInfoRegReqRx_Object = MibTableColumn
cvpnLicClntInfoRegReqRx = _CvpnLicClntInfoRegReqRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 4, 1, 1, 8),
    _CvpnLicClntInfoRegReqRx_Type()
)
cvpnLicClntInfoRegReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicClntInfoRegReqRx.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicClntInfoRegReqRx.setUnits("packets")
_CvpnLicClntInfoRegReqError_Type = Counter32
_CvpnLicClntInfoRegReqError_Object = MibTableColumn
cvpnLicClntInfoRegReqError = _CvpnLicClntInfoRegReqError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 4, 1, 1, 9),
    _CvpnLicClntInfoRegReqError_Type()
)
cvpnLicClntInfoRegReqError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicClntInfoRegReqError.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicClntInfoRegReqError.setUnits("packets")
_CvpnLicClntInfoGetReqTx_Type = Counter32
_CvpnLicClntInfoGetReqTx_Object = MibTableColumn
cvpnLicClntInfoGetReqTx = _CvpnLicClntInfoGetReqTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 4, 1, 1, 10),
    _CvpnLicClntInfoGetReqTx_Type()
)
cvpnLicClntInfoGetReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicClntInfoGetReqTx.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicClntInfoGetReqTx.setUnits("packets")
_CvpnLicClntInfoGetReqRx_Type = Counter32
_CvpnLicClntInfoGetReqRx_Object = MibTableColumn
cvpnLicClntInfoGetReqRx = _CvpnLicClntInfoGetReqRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 4, 1, 1, 11),
    _CvpnLicClntInfoGetReqRx_Type()
)
cvpnLicClntInfoGetReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicClntInfoGetReqRx.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicClntInfoGetReqRx.setUnits("packets")
_CvpnLicClntInfoGetReqError_Type = Counter32
_CvpnLicClntInfoGetReqError_Object = MibTableColumn
cvpnLicClntInfoGetReqError = _CvpnLicClntInfoGetReqError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 4, 1, 1, 12),
    _CvpnLicClntInfoGetReqError_Type()
)
cvpnLicClntInfoGetReqError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicClntInfoGetReqError.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicClntInfoGetReqError.setUnits("packets")
_CvpnLicClntInfoRelReqTx_Type = Counter32
_CvpnLicClntInfoRelReqTx_Object = MibTableColumn
cvpnLicClntInfoRelReqTx = _CvpnLicClntInfoRelReqTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 4, 1, 1, 13),
    _CvpnLicClntInfoRelReqTx_Type()
)
cvpnLicClntInfoRelReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicClntInfoRelReqTx.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicClntInfoRelReqTx.setUnits("packets")
_CvpnLicClntInfoRelReqRx_Type = Counter32
_CvpnLicClntInfoRelReqRx_Object = MibTableColumn
cvpnLicClntInfoRelReqRx = _CvpnLicClntInfoRelReqRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 4, 1, 1, 14),
    _CvpnLicClntInfoRelReqRx_Type()
)
cvpnLicClntInfoRelReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicClntInfoRelReqRx.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicClntInfoRelReqRx.setUnits("packets")
_CvpnLicClntInfoRelReqError_Type = Counter32
_CvpnLicClntInfoRelReqError_Object = MibTableColumn
cvpnLicClntInfoRelReqError = _CvpnLicClntInfoRelReqError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 4, 1, 1, 15),
    _CvpnLicClntInfoRelReqError_Type()
)
cvpnLicClntInfoRelReqError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicClntInfoRelReqError.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicClntInfoRelReqError.setUnits("packets")
_CvpnLicClntInfoTransferReqTx_Type = Counter32
_CvpnLicClntInfoTransferReqTx_Object = MibTableColumn
cvpnLicClntInfoTransferReqTx = _CvpnLicClntInfoTransferReqTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 4, 1, 1, 16),
    _CvpnLicClntInfoTransferReqTx_Type()
)
cvpnLicClntInfoTransferReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicClntInfoTransferReqTx.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicClntInfoTransferReqTx.setUnits("packets")
_CvpnLicClntInfoTransferReqRx_Type = Counter32
_CvpnLicClntInfoTransferReqRx_Object = MibTableColumn
cvpnLicClntInfoTransferReqRx = _CvpnLicClntInfoTransferReqRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 4, 1, 1, 17),
    _CvpnLicClntInfoTransferReqRx_Type()
)
cvpnLicClntInfoTransferReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicClntInfoTransferReqRx.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicClntInfoTransferReqRx.setUnits("packets")
_CvpnLicClntInfoTransferReqError_Type = Counter32
_CvpnLicClntInfoTransferReqError_Object = MibTableColumn
cvpnLicClntInfoTransferReqError = _CvpnLicClntInfoTransferReqError_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 0, 4, 1, 1, 18),
    _CvpnLicClntInfoTransferReqError_Type()
)
cvpnLicClntInfoTransferReqError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvpnLicClntInfoTransferReqError.setStatus("current")
if mibBuilder.loadTexts:
    cvpnLicClntInfoTransferReqError.setUnits("packets")
_CiscoVpnLicUsageMonitorMIBConform_ObjectIdentity = ObjectIdentity
ciscoVpnLicUsageMonitorMIBConform = _CiscoVpnLicUsageMonitorMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 1)
)
_CiscoVpnLicUsageMonitorMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVpnLicUsageMonitorMIBCompliances = _CiscoVpnLicUsageMonitorMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 1, 1)
)
_CiscoVpnLicUsageMonitorMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVpnLicUsageMonitorMIBGroups = _CiscoVpnLicUsageMonitorMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 1, 2)
)

# Managed Objects groups

ciscoVPNSharedLicUsageMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 1, 2, 1)
)
ciscoVPNSharedLicUsageMandatoryGroup.setObjects(
      *(("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicDeviceRole"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicServerAddrType"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicServerAddr"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicBkpSerAddrType"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicBkpSerAddr"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicServerVer"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicServerStatus"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicServerNumLicCapacity"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicServerNumLicAvail"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicServerUtilized"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicClntInfoHostName"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicClntInfoPlatLmt"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicClntInfoCurUsage"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicClntInfoHigh"))
)
if mibBuilder.loadTexts:
    ciscoVPNSharedLicUsageMandatoryGroup.setStatus("current")

ciscoVPNSharedLicOptUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 1, 2, 2)
)
ciscoVPNSharedLicOptUsageGroup.setObjects(
      *(("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicBkpServerAddrType"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicBkpServerAddr"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicBkpServerDevID"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicBkpServerVer"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicBkpServerRegd"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicBkpServerHAPeerDevID"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicBkpServerHAPeerRegd"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicBkpServerStatus"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicServerHelloTx"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicServerHelloRx"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicServerHelloError"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicServerSyncTx"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicServerSyncRx"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicServerSyncError"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicServerUpdateTx"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicServerUpdateRx"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicServerUpdateError"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicClntInfoRegReqTx"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicClntInfoRegReqRx"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicClntInfoRegReqError"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicClntInfoGetReqTx"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicClntInfoGetReqRx"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicClntInfoGetReqError"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicClntInfoRelReqTx"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicClntInfoRelReqRx"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicClntInfoRelReqError"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicClntInfoTransferReqTx"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicClntInfoTransferReqRx"),
        ("CISCO-VPN-LIC-USAGE-MONITOR-MIB", "cvpnLicClntInfoTransferReqError"))
)
if mibBuilder.loadTexts:
    ciscoVPNSharedLicOptUsageGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVpnLicUsageMonitorMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 816, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoVpnLicUsageMonitorMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VPN-LIC-USAGE-MONITOR-MIB",
    **{"VPNLicType": VPNLicType,
       "VPNLicDeviceRole": VPNLicDeviceRole,
       "LicServerStatus": LicServerStatus,
       "LicServerRegistered": LicServerRegistered,
       "ciscoVpnLicUsageMonitorMIB": ciscoVpnLicUsageMonitorMIB,
       "ciscoVpnLicUsageMonitorMIBObjects": ciscoVpnLicUsageMonitorMIBObjects,
       "cvpnLicDeviceRole": cvpnLicDeviceRole,
       "cvpnLicServer": cvpnLicServer,
       "cvpnLicServerAddrType": cvpnLicServerAddrType,
       "cvpnLicServerAddr": cvpnLicServerAddr,
       "cvpnLicBkpSerAddrType": cvpnLicBkpSerAddrType,
       "cvpnLicBkpSerAddr": cvpnLicBkpSerAddr,
       "cvpnLicServerVer": cvpnLicServerVer,
       "cvpnLicServerStatus": cvpnLicServerStatus,
       "cvpnLicServerTable": cvpnLicServerTable,
       "cvpnLicServerEntry": cvpnLicServerEntry,
       "cvpnLicServerVPNLicType": cvpnLicServerVPNLicType,
       "cvpnLicServerNumLicCapacity": cvpnLicServerNumLicCapacity,
       "cvpnLicServerNumLicAvail": cvpnLicServerNumLicAvail,
       "cvpnLicServerUtilized": cvpnLicServerUtilized,
       "cvpnLicBkpServer": cvpnLicBkpServer,
       "cvpnLicBkpServerAddrType": cvpnLicBkpServerAddrType,
       "cvpnLicBkpServerAddr": cvpnLicBkpServerAddr,
       "cvpnLicBkpServerDevID": cvpnLicBkpServerDevID,
       "cvpnLicBkpServerVer": cvpnLicBkpServerVer,
       "cvpnLicBkpServerRegd": cvpnLicBkpServerRegd,
       "cvpnLicBkpServerHAPeerDevID": cvpnLicBkpServerHAPeerDevID,
       "cvpnLicBkpServerHAPeerRegd": cvpnLicBkpServerHAPeerRegd,
       "cvpnLicBkpServerStatus": cvpnLicBkpServerStatus,
       "cvpnLicServerHelloTx": cvpnLicServerHelloTx,
       "cvpnLicServerHelloRx": cvpnLicServerHelloRx,
       "cvpnLicServerHelloError": cvpnLicServerHelloError,
       "cvpnLicServerSyncTx": cvpnLicServerSyncTx,
       "cvpnLicServerSyncRx": cvpnLicServerSyncRx,
       "cvpnLicServerSyncError": cvpnLicServerSyncError,
       "cvpnLicServerUpdateTx": cvpnLicServerUpdateTx,
       "cvpnLicServerUpdateRx": cvpnLicServerUpdateRx,
       "cvpnLicServerUpdateError": cvpnLicServerUpdateError,
       "cvpnLicClient": cvpnLicClient,
       "cvpnLicClntInfoTable": cvpnLicClntInfoTable,
       "cvpnLicClntInfoEntry": cvpnLicClntInfoEntry,
       "cvpnLicClntVPNLicType": cvpnLicClntVPNLicType,
       "cvpnLicClntInfoDeviceID": cvpnLicClntInfoDeviceID,
       "cvpnLicClntInfoHostName": cvpnLicClntInfoHostName,
       "cvpnLicClntInfoPlatLmt": cvpnLicClntInfoPlatLmt,
       "cvpnLicClntInfoCurUsage": cvpnLicClntInfoCurUsage,
       "cvpnLicClntInfoHigh": cvpnLicClntInfoHigh,
       "cvpnLicClntInfoRegReqTx": cvpnLicClntInfoRegReqTx,
       "cvpnLicClntInfoRegReqRx": cvpnLicClntInfoRegReqRx,
       "cvpnLicClntInfoRegReqError": cvpnLicClntInfoRegReqError,
       "cvpnLicClntInfoGetReqTx": cvpnLicClntInfoGetReqTx,
       "cvpnLicClntInfoGetReqRx": cvpnLicClntInfoGetReqRx,
       "cvpnLicClntInfoGetReqError": cvpnLicClntInfoGetReqError,
       "cvpnLicClntInfoRelReqTx": cvpnLicClntInfoRelReqTx,
       "cvpnLicClntInfoRelReqRx": cvpnLicClntInfoRelReqRx,
       "cvpnLicClntInfoRelReqError": cvpnLicClntInfoRelReqError,
       "cvpnLicClntInfoTransferReqTx": cvpnLicClntInfoTransferReqTx,
       "cvpnLicClntInfoTransferReqRx": cvpnLicClntInfoTransferReqRx,
       "cvpnLicClntInfoTransferReqError": cvpnLicClntInfoTransferReqError,
       "ciscoVpnLicUsageMonitorMIBConform": ciscoVpnLicUsageMonitorMIBConform,
       "ciscoVpnLicUsageMonitorMIBCompliances": ciscoVpnLicUsageMonitorMIBCompliances,
       "ciscoVpnLicUsageMonitorMIBCompliance": ciscoVpnLicUsageMonitorMIBCompliance,
       "ciscoVpnLicUsageMonitorMIBGroups": ciscoVpnLicUsageMonitorMIBGroups,
       "ciscoVPNSharedLicUsageMandatoryGroup": ciscoVPNSharedLicUsageMandatoryGroup,
       "ciscoVPNSharedLicOptUsageGroup": ciscoVPNSharedLicOptUsageGroup}
)
