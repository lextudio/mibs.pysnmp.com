# SNMP MIB module (HM2-CAM-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-CAM-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:51 2024
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

(HmEnabledStatus,
 hm2ConfigurationMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "hm2ConfigurationMibs")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hm2CamMgmtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 200)
)
hm2CamMgmtMib.setRevisions(
        ("2013-07-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2CamMgmtMibNotifications_ObjectIdentity = ObjectIdentity
hm2CamMgmtMibNotifications = _Hm2CamMgmtMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 0)
)
_Hm2CamMgmtMibObjects_ObjectIdentity = ObjectIdentity
hm2CamMgmtMibObjects = _Hm2CamMgmtMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1)
)
_Hm2CamConfigGroup_ObjectIdentity = ObjectIdentity
hm2CamConfigGroup = _Hm2CamConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 1)
)


class _Hm2CamConfigAdminStatus_Type(HmEnabledStatus):
    """Custom type hm2CamConfigAdminStatus based on HmEnabledStatus"""


_Hm2CamConfigAdminStatus_Object = MibScalar
hm2CamConfigAdminStatus = _Hm2CamConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 1, 1),
    _Hm2CamConfigAdminStatus_Type()
)
hm2CamConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2CamConfigAdminStatus.setStatus("current")


class _Hm2CamConfigLastValidServerindex_Type(Integer32):
    """Custom type hm2CamConfigLastValidServerindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Hm2CamConfigLastValidServerindex_Type.__name__ = "Integer32"
_Hm2CamConfigLastValidServerindex_Object = MibScalar
hm2CamConfigLastValidServerindex = _Hm2CamConfigLastValidServerindex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 1, 2),
    _Hm2CamConfigLastValidServerindex_Type()
)
hm2CamConfigLastValidServerindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2CamConfigLastValidServerindex.setStatus("current")
_Hm2CamClientServerAddrTable_Object = MibTable
hm2CamClientServerAddrTable = _Hm2CamClientServerAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 1, 10)
)
if mibBuilder.loadTexts:
    hm2CamClientServerAddrTable.setStatus("current")
_Hm2CamClientServerAddrEntry_Object = MibTableRow
hm2CamClientServerAddrEntry = _Hm2CamClientServerAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 1, 10, 1)
)
hm2CamClientServerAddrEntry.setIndexNames(
    (0, "HM2-CAM-MGMT-MIB", "hm2CamClientServerIndex"),
)
if mibBuilder.loadTexts:
    hm2CamClientServerAddrEntry.setStatus("current")


class _Hm2CamClientServerIndex_Type(Integer32):
    """Custom type hm2CamClientServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Hm2CamClientServerIndex_Type.__name__ = "Integer32"
_Hm2CamClientServerIndex_Object = MibTableColumn
hm2CamClientServerIndex = _Hm2CamClientServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 1, 10, 1, 1),
    _Hm2CamClientServerIndex_Type()
)
hm2CamClientServerIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hm2CamClientServerIndex.setStatus("current")


class _Hm2CamClientServerAddrType_Type(InetAddressType):
    """Custom type hm2CamClientServerAddrType based on InetAddressType"""


_Hm2CamClientServerAddrType_Object = MibTableColumn
hm2CamClientServerAddrType = _Hm2CamClientServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 1, 10, 1, 2),
    _Hm2CamClientServerAddrType_Type()
)
hm2CamClientServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2CamClientServerAddrType.setStatus("current")


class _Hm2CamClientServerAddr_Type(InetAddress):
    """Custom type hm2CamClientServerAddr based on InetAddress"""
    defaultHexValue = "00000000"


_Hm2CamClientServerAddr_Object = MibTableColumn
hm2CamClientServerAddr = _Hm2CamClientServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 1, 10, 1, 3),
    _Hm2CamClientServerAddr_Type()
)
hm2CamClientServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2CamClientServerAddr.setStatus("current")


class _Hm2CamClientServerPort_Type(InetPortNumber):
    """Custom type hm2CamClientServerPort based on InetPortNumber"""
    defaultValue = 389


_Hm2CamClientServerPort_Object = MibTableColumn
hm2CamClientServerPort = _Hm2CamClientServerPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 1, 10, 1, 4),
    _Hm2CamClientServerPort_Type()
)
hm2CamClientServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2CamClientServerPort.setStatus("current")


class _Hm2CamClientServerDescr_Type(SnmpAdminString):
    """Custom type hm2CamClientServerDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_Hm2CamClientServerDescr_Type.__name__ = "SnmpAdminString"
_Hm2CamClientServerDescr_Object = MibTableColumn
hm2CamClientServerDescr = _Hm2CamClientServerDescr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 1, 10, 1, 5),
    _Hm2CamClientServerDescr_Type()
)
hm2CamClientServerDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2CamClientServerDescr.setStatus("current")


class _Hm2CamClientServerBaseDN_Type(SnmpAdminString):
    """Custom type hm2CamClientServerBaseDN based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_Hm2CamClientServerBaseDN_Type.__name__ = "SnmpAdminString"
_Hm2CamClientServerBaseDN_Object = MibTableColumn
hm2CamClientServerBaseDN = _Hm2CamClientServerBaseDN_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 1, 10, 1, 6),
    _Hm2CamClientServerBaseDN_Type()
)
hm2CamClientServerBaseDN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2CamClientServerBaseDN.setStatus("current")


class _Hm2CamClientServerSearchString_Type(SnmpAdminString):
    """Custom type hm2CamClientServerSearchString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_Hm2CamClientServerSearchString_Type.__name__ = "SnmpAdminString"
_Hm2CamClientServerSearchString_Object = MibTableColumn
hm2CamClientServerSearchString = _Hm2CamClientServerSearchString_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 1, 10, 1, 7),
    _Hm2CamClientServerSearchString_Type()
)
hm2CamClientServerSearchString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2CamClientServerSearchString.setStatus("current")


class _Hm2CamClientServerStatus_Type(Integer32):
    """Custom type hm2CamClientServerStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("other", 3),
          ("unreachable", 2))
    )


_Hm2CamClientServerStatus_Type.__name__ = "Integer32"
_Hm2CamClientServerStatus_Object = MibTableColumn
hm2CamClientServerStatus = _Hm2CamClientServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 1, 10, 1, 8),
    _Hm2CamClientServerStatus_Type()
)
hm2CamClientServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2CamClientServerStatus.setStatus("current")


class _Hm2CamClientServerReplicationInterval_Type(Integer32):
    """Custom type hm2CamClientServerReplicationInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1440),
    )


_Hm2CamClientServerReplicationInterval_Type.__name__ = "Integer32"
_Hm2CamClientServerReplicationInterval_Object = MibTableColumn
hm2CamClientServerReplicationInterval = _Hm2CamClientServerReplicationInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 1, 10, 1, 9),
    _Hm2CamClientServerReplicationInterval_Type()
)
hm2CamClientServerReplicationInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2CamClientServerReplicationInterval.setStatus("current")
if mibBuilder.loadTexts:
    hm2CamClientServerReplicationInterval.setUnits("minutes")


class _Hm2CamClientServerReplicationStatus_Type(Integer32):
    """Custom type hm2CamClientServerReplicationStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("other", 3),
          ("unsuccessful", 2))
    )


_Hm2CamClientServerReplicationStatus_Type.__name__ = "Integer32"
_Hm2CamClientServerReplicationStatus_Object = MibTableColumn
hm2CamClientServerReplicationStatus = _Hm2CamClientServerReplicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 1, 10, 1, 10),
    _Hm2CamClientServerReplicationStatus_Type()
)
hm2CamClientServerReplicationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2CamClientServerReplicationStatus.setStatus("current")
_Hm2CamClientServerRowStatus_Type = RowStatus
_Hm2CamClientServerRowStatus_Object = MibTableColumn
hm2CamClientServerRowStatus = _Hm2CamClientServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 1, 10, 1, 11),
    _Hm2CamClientServerRowStatus_Type()
)
hm2CamClientServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2CamClientServerRowStatus.setStatus("current")
_Hm2CamActionGroup_ObjectIdentity = ObjectIdentity
hm2CamActionGroup = _Hm2CamActionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 10)
)


class _Hm2CamAction_Type(Integer32):
    """Custom type hm2CamAction based on Integer32"""
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
        *(("doReplication", 3),
          ("other", 1),
          ("testConnection", 2))
    )


_Hm2CamAction_Type.__name__ = "Integer32"
_Hm2CamAction_Object = MibScalar
hm2CamAction = _Hm2CamAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 10, 1),
    _Hm2CamAction_Type()
)
hm2CamAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2CamAction.setStatus("current")


class _Hm2CamActionConnectionStatus_Type(Integer32):
    """Custom type hm2CamActionConnectionStatus based on Integer32"""
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
        *(("ok", 1),
          ("other", 4),
          ("pending", 3),
          ("unreachable", 2))
    )


_Hm2CamActionConnectionStatus_Type.__name__ = "Integer32"
_Hm2CamActionConnectionStatus_Object = MibScalar
hm2CamActionConnectionStatus = _Hm2CamActionConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 10, 2),
    _Hm2CamActionConnectionStatus_Type()
)
hm2CamActionConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2CamActionConnectionStatus.setStatus("current")


class _Hm2CamActionReplicationStatus_Type(Integer32):
    """Custom type hm2CamActionReplicationStatus based on Integer32"""
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
        *(("ok", 1),
          ("other", 4),
          ("pending", 3),
          ("unsuccessful", 2))
    )


_Hm2CamActionReplicationStatus_Type.__name__ = "Integer32"
_Hm2CamActionReplicationStatus_Object = MibScalar
hm2CamActionReplicationStatus = _Hm2CamActionReplicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 10, 3),
    _Hm2CamActionReplicationStatus_Type()
)
hm2CamActionReplicationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2CamActionReplicationStatus.setStatus("current")
_Hm2CamPwdChangeGroup_ObjectIdentity = ObjectIdentity
hm2CamPwdChangeGroup = _Hm2CamPwdChangeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 20)
)


class _Hm2CamPwdChangeUserName_Type(SnmpAdminString):
    """Custom type hm2CamPwdChangeUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_Hm2CamPwdChangeUserName_Type.__name__ = "SnmpAdminString"
_Hm2CamPwdChangeUserName_Object = MibScalar
hm2CamPwdChangeUserName = _Hm2CamPwdChangeUserName_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 20, 1),
    _Hm2CamPwdChangeUserName_Type()
)
hm2CamPwdChangeUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2CamPwdChangeUserName.setStatus("current")


class _Hm2CamPwdChangeUserPwOld_Type(SnmpAdminString):
    """Custom type hm2CamPwdChangeUserPwOld based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_Hm2CamPwdChangeUserPwOld_Type.__name__ = "SnmpAdminString"
_Hm2CamPwdChangeUserPwOld_Object = MibScalar
hm2CamPwdChangeUserPwOld = _Hm2CamPwdChangeUserPwOld_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 20, 2),
    _Hm2CamPwdChangeUserPwOld_Type()
)
hm2CamPwdChangeUserPwOld.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2CamPwdChangeUserPwOld.setStatus("current")


class _Hm2CamPwdChangeUserPwNew_Type(SnmpAdminString):
    """Custom type hm2CamPwdChangeUserPwNew based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_Hm2CamPwdChangeUserPwNew_Type.__name__ = "SnmpAdminString"
_Hm2CamPwdChangeUserPwNew_Object = MibScalar
hm2CamPwdChangeUserPwNew = _Hm2CamPwdChangeUserPwNew_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 20, 3),
    _Hm2CamPwdChangeUserPwNew_Type()
)
hm2CamPwdChangeUserPwNew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2CamPwdChangeUserPwNew.setStatus("current")


class _Hm2CamPwdChangeAction_Type(Integer32):
    """Custom type hm2CamPwdChangeAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("changePwd", 2),
          ("other", 1))
    )


_Hm2CamPwdChangeAction_Type.__name__ = "Integer32"
_Hm2CamPwdChangeAction_Object = MibScalar
hm2CamPwdChangeAction = _Hm2CamPwdChangeAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 20, 4),
    _Hm2CamPwdChangeAction_Type()
)
hm2CamPwdChangeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2CamPwdChangeAction.setStatus("current")


class _Hm2CamPwdChangeActionStatus_Type(Integer32):
    """Custom type hm2CamPwdChangeActionStatus based on Integer32"""
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
        *(("ok", 1),
          ("other", 4),
          ("pending", 3),
          ("unsuccessful", 2))
    )


_Hm2CamPwdChangeActionStatus_Type.__name__ = "Integer32"
_Hm2CamPwdChangeActionStatus_Object = MibScalar
hm2CamPwdChangeActionStatus = _Hm2CamPwdChangeActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 20, 5),
    _Hm2CamPwdChangeActionStatus_Type()
)
hm2CamPwdChangeActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2CamPwdChangeActionStatus.setStatus("current")
_Hm2CamCertInfoGroup_ObjectIdentity = ObjectIdentity
hm2CamCertInfoGroup = _Hm2CamCertInfoGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 30)
)
_Hm2CamCertInfoTable_Object = MibTable
hm2CamCertInfoTable = _Hm2CamCertInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 30, 1)
)
if mibBuilder.loadTexts:
    hm2CamCertInfoTable.setStatus("current")
_Hm2CamCertInfoEntry_Object = MibTableRow
hm2CamCertInfoEntry = _Hm2CamCertInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 30, 1, 1)
)
hm2CamCertInfoEntry.setIndexNames(
    (0, "HM2-CAM-MGMT-MIB", "hm2CamCertInfoIndex"),
)
if mibBuilder.loadTexts:
    hm2CamCertInfoEntry.setStatus("current")


class _Hm2CamCertInfoIndex_Type(Integer32):
    """Custom type hm2CamCertInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deviceCert", 2),
          ("rootCert", 1))
    )


_Hm2CamCertInfoIndex_Type.__name__ = "Integer32"
_Hm2CamCertInfoIndex_Object = MibTableColumn
hm2CamCertInfoIndex = _Hm2CamCertInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 30, 1, 1, 1),
    _Hm2CamCertInfoIndex_Type()
)
hm2CamCertInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2CamCertInfoIndex.setStatus("current")
_Hm2CamCertInfoPresent_Type = TruthValue
_Hm2CamCertInfoPresent_Object = MibTableColumn
hm2CamCertInfoPresent = _Hm2CamCertInfoPresent_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 30, 1, 1, 2),
    _Hm2CamCertInfoPresent_Type()
)
hm2CamCertInfoPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2CamCertInfoPresent.setStatus("current")
_Hm2CamCertInfoExpiry_Type = SnmpAdminString
_Hm2CamCertInfoExpiry_Object = MibTableColumn
hm2CamCertInfoExpiry = _Hm2CamCertInfoExpiry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 30, 1, 1, 3),
    _Hm2CamCertInfoExpiry_Type()
)
hm2CamCertInfoExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2CamCertInfoExpiry.setStatus("current")
_Hm2CamCertInfoIssuer_Type = SnmpAdminString
_Hm2CamCertInfoIssuer_Object = MibTableColumn
hm2CamCertInfoIssuer = _Hm2CamCertInfoIssuer_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 30, 1, 1, 4),
    _Hm2CamCertInfoIssuer_Type()
)
hm2CamCertInfoIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2CamCertInfoIssuer.setStatus("current")
_Hm2CamCertInfoSubject_Type = SnmpAdminString
_Hm2CamCertInfoSubject_Object = MibTableColumn
hm2CamCertInfoSubject = _Hm2CamCertInfoSubject_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 30, 1, 1, 5),
    _Hm2CamCertInfoSubject_Type()
)
hm2CamCertInfoSubject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2CamCertInfoSubject.setStatus("current")
_Hm2CamCertInfoSerialNumber_Type = SnmpAdminString
_Hm2CamCertInfoSerialNumber_Object = MibTableColumn
hm2CamCertInfoSerialNumber = _Hm2CamCertInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 1, 30, 1, 1, 6),
    _Hm2CamCertInfoSerialNumber_Type()
)
hm2CamCertInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2CamCertInfoSerialNumber.setStatus("current")

# Managed Objects groups


# Notification objects

hm2CamConfigStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 0, 1)
)
hm2CamConfigStatusTrap.setObjects(
      *(("HM2-CAM-MGMT-MIB", "hm2CamClientServerIndex"),
        ("HM2-CAM-MGMT-MIB", "hm2CamClientServerStatus"))
)
if mibBuilder.loadTexts:
    hm2CamConfigStatusTrap.setStatus(
        "current"
    )

hm2CamReplicationStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 200, 0, 2)
)
hm2CamReplicationStatusTrap.setObjects(
      *(("HM2-CAM-MGMT-MIB", "hm2CamClientServerIndex"),
        ("HM2-CAM-MGMT-MIB", "hm2CamClientServerReplicationStatus"))
)
if mibBuilder.loadTexts:
    hm2CamReplicationStatusTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-CAM-MGMT-MIB",
    **{"hm2CamMgmtMib": hm2CamMgmtMib,
       "hm2CamMgmtMibNotifications": hm2CamMgmtMibNotifications,
       "hm2CamConfigStatusTrap": hm2CamConfigStatusTrap,
       "hm2CamReplicationStatusTrap": hm2CamReplicationStatusTrap,
       "hm2CamMgmtMibObjects": hm2CamMgmtMibObjects,
       "hm2CamConfigGroup": hm2CamConfigGroup,
       "hm2CamConfigAdminStatus": hm2CamConfigAdminStatus,
       "hm2CamConfigLastValidServerindex": hm2CamConfigLastValidServerindex,
       "hm2CamClientServerAddrTable": hm2CamClientServerAddrTable,
       "hm2CamClientServerAddrEntry": hm2CamClientServerAddrEntry,
       "hm2CamClientServerIndex": hm2CamClientServerIndex,
       "hm2CamClientServerAddrType": hm2CamClientServerAddrType,
       "hm2CamClientServerAddr": hm2CamClientServerAddr,
       "hm2CamClientServerPort": hm2CamClientServerPort,
       "hm2CamClientServerDescr": hm2CamClientServerDescr,
       "hm2CamClientServerBaseDN": hm2CamClientServerBaseDN,
       "hm2CamClientServerSearchString": hm2CamClientServerSearchString,
       "hm2CamClientServerStatus": hm2CamClientServerStatus,
       "hm2CamClientServerReplicationInterval": hm2CamClientServerReplicationInterval,
       "hm2CamClientServerReplicationStatus": hm2CamClientServerReplicationStatus,
       "hm2CamClientServerRowStatus": hm2CamClientServerRowStatus,
       "hm2CamActionGroup": hm2CamActionGroup,
       "hm2CamAction": hm2CamAction,
       "hm2CamActionConnectionStatus": hm2CamActionConnectionStatus,
       "hm2CamActionReplicationStatus": hm2CamActionReplicationStatus,
       "hm2CamPwdChangeGroup": hm2CamPwdChangeGroup,
       "hm2CamPwdChangeUserName": hm2CamPwdChangeUserName,
       "hm2CamPwdChangeUserPwOld": hm2CamPwdChangeUserPwOld,
       "hm2CamPwdChangeUserPwNew": hm2CamPwdChangeUserPwNew,
       "hm2CamPwdChangeAction": hm2CamPwdChangeAction,
       "hm2CamPwdChangeActionStatus": hm2CamPwdChangeActionStatus,
       "hm2CamCertInfoGroup": hm2CamCertInfoGroup,
       "hm2CamCertInfoTable": hm2CamCertInfoTable,
       "hm2CamCertInfoEntry": hm2CamCertInfoEntry,
       "hm2CamCertInfoIndex": hm2CamCertInfoIndex,
       "hm2CamCertInfoPresent": hm2CamCertInfoPresent,
       "hm2CamCertInfoExpiry": hm2CamCertInfoExpiry,
       "hm2CamCertInfoIssuer": hm2CamCertInfoIssuer,
       "hm2CamCertInfoSubject": hm2CamCertInfoSubject,
       "hm2CamCertInfoSerialNumber": hm2CamCertInfoSerialNumber}
)
