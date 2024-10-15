# SNMP MIB module (CISCO-VTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:12 2024
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

(Cisco2KVlanList,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "Cisco2KVlanList")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoVtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 46)
)
ciscoVtpMIB.setRevisions(
        ("2013-10-14 00:00",
         "2010-05-12 00:00",
         "2009-12-03 00:00",
         "2008-03-07 00:00",
         "2007-10-04 00:00",
         "2006-02-17 00:00",
         "2004-02-11 00:00",
         "2003-11-21 00:00",
         "2003-08-08 00:00",
         "2003-07-11 00:00",
         "2003-04-16 00:00",
         "2002-04-10 00:00",
         "2002-02-28 00:00",
         "2001-08-03 00:00",
         "2001-02-26 00:00",
         "2001-02-12 00:00",
         "2000-09-19 00:00",
         "2000-04-10 00:00",
         "2000-01-06 00:00",
         "1999-02-25 11:30",
         "1999-01-05 11:30",
         "1998-05-19 11:30",
         "1997-08-08 11:38",
         "1997-05-09 11:30",
         "1997-02-24 11:15",
         "1997-01-27 17:30",
         "1996-09-16 12:30",
         "1996-07-17 12:30",
         "1996-01-18 18:20")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class ManagementDomainIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class VlanType(Integer32, TextualConvention):
    status = "current"
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
        *(("deprecated", 6),
          ("ethernet", 1),
          ("fddi", 2),
          ("fddiNet", 4),
          ("tokenRing", 3),
          ("trNet", 5))
    )



class VlanTypeExt(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_VtpMIBObjects_ObjectIdentity = ObjectIdentity
vtpMIBObjects = _VtpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1)
)
_VtpStatus_ObjectIdentity = ObjectIdentity
vtpStatus = _VtpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 1)
)


class _VtpVersion_Type(Integer32):
    """Custom type vtpVersion based on Integer32"""
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
        *(("none", 3),
          ("one", 1),
          ("three", 4),
          ("two", 2))
    )


_VtpVersion_Type.__name__ = "Integer32"
_VtpVersion_Object = MibScalar
vtpVersion = _VtpVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 1, 1),
    _VtpVersion_Type()
)
vtpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpVersion.setStatus("current")


class _VtpMaxVlanStorage_Type(Integer32):
    """Custom type vtpMaxVlanStorage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1023),
    )


_VtpMaxVlanStorage_Type.__name__ = "Integer32"
_VtpMaxVlanStorage_Object = MibScalar
vtpMaxVlanStorage = _VtpMaxVlanStorage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 1, 2),
    _VtpMaxVlanStorage_Type()
)
vtpMaxVlanStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpMaxVlanStorage.setStatus("current")
_VtpNotificationsEnabled_Type = TruthValue
_VtpNotificationsEnabled_Object = MibScalar
vtpNotificationsEnabled = _VtpNotificationsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 1, 3),
    _VtpNotificationsEnabled_Type()
)
vtpNotificationsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtpNotificationsEnabled.setStatus("current")
_VtpVlanCreatedNotifEnabled_Type = TruthValue
_VtpVlanCreatedNotifEnabled_Object = MibScalar
vtpVlanCreatedNotifEnabled = _VtpVlanCreatedNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 1, 4),
    _VtpVlanCreatedNotifEnabled_Type()
)
vtpVlanCreatedNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtpVlanCreatedNotifEnabled.setStatus("current")
_VtpVlanDeletedNotifEnabled_Type = TruthValue
_VtpVlanDeletedNotifEnabled_Object = MibScalar
vtpVlanDeletedNotifEnabled = _VtpVlanDeletedNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 1, 5),
    _VtpVlanDeletedNotifEnabled_Type()
)
vtpVlanDeletedNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtpVlanDeletedNotifEnabled.setStatus("current")
_VlanManagementDomains_ObjectIdentity = ObjectIdentity
vlanManagementDomains = _VlanManagementDomains_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2)
)
_ManagementDomainTable_Object = MibTable
managementDomainTable = _ManagementDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1)
)
if mibBuilder.loadTexts:
    managementDomainTable.setStatus("current")
_ManagementDomainEntry_Object = MibTableRow
managementDomainEntry = _ManagementDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1)
)
managementDomainEntry.setIndexNames(
    (0, "CISCO-VTP-MIB", "managementDomainIndex"),
)
if mibBuilder.loadTexts:
    managementDomainEntry.setStatus("current")
_ManagementDomainIndex_Type = ManagementDomainIndex
_ManagementDomainIndex_Object = MibTableColumn
managementDomainIndex = _ManagementDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 1),
    _ManagementDomainIndex_Type()
)
managementDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    managementDomainIndex.setStatus("current")


class _ManagementDomainName_Type(DisplayString):
    """Custom type managementDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ManagementDomainName_Type.__name__ = "DisplayString"
_ManagementDomainName_Object = MibTableColumn
managementDomainName = _ManagementDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 2),
    _ManagementDomainName_Type()
)
managementDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    managementDomainName.setStatus("current")


class _ManagementDomainLocalMode_Type(Integer32):
    """Custom type managementDomainLocalMode based on Integer32"""
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
        *(("client", 1),
          ("off", 4),
          ("server", 2),
          ("transparent", 3))
    )


_ManagementDomainLocalMode_Type.__name__ = "Integer32"
_ManagementDomainLocalMode_Object = MibTableColumn
managementDomainLocalMode = _ManagementDomainLocalMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 3),
    _ManagementDomainLocalMode_Type()
)
managementDomainLocalMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    managementDomainLocalMode.setStatus("current")
_ManagementDomainConfigRevNumber_Type = Gauge32
_ManagementDomainConfigRevNumber_Object = MibTableColumn
managementDomainConfigRevNumber = _ManagementDomainConfigRevNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 4),
    _ManagementDomainConfigRevNumber_Type()
)
managementDomainConfigRevNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementDomainConfigRevNumber.setStatus("current")
_ManagementDomainLastUpdater_Type = IpAddress
_ManagementDomainLastUpdater_Object = MibTableColumn
managementDomainLastUpdater = _ManagementDomainLastUpdater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 5),
    _ManagementDomainLastUpdater_Type()
)
managementDomainLastUpdater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementDomainLastUpdater.setStatus("current")
_ManagementDomainLastChange_Type = DateAndTime
_ManagementDomainLastChange_Object = MibTableColumn
managementDomainLastChange = _ManagementDomainLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 6),
    _ManagementDomainLastChange_Type()
)
managementDomainLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementDomainLastChange.setStatus("current")
_ManagementDomainRowStatus_Type = RowStatus
_ManagementDomainRowStatus_Object = MibTableColumn
managementDomainRowStatus = _ManagementDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 7),
    _ManagementDomainRowStatus_Type()
)
managementDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    managementDomainRowStatus.setStatus("current")
_ManagementDomainTftpServer_Type = IpAddress
_ManagementDomainTftpServer_Object = MibTableColumn
managementDomainTftpServer = _ManagementDomainTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 8),
    _ManagementDomainTftpServer_Type()
)
managementDomainTftpServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    managementDomainTftpServer.setStatus("current")
_ManagementDomainTftpPathname_Type = DisplayString
_ManagementDomainTftpPathname_Object = MibTableColumn
managementDomainTftpPathname = _ManagementDomainTftpPathname_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 9),
    _ManagementDomainTftpPathname_Type()
)
managementDomainTftpPathname.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    managementDomainTftpPathname.setStatus("current")


class _ManagementDomainPruningState_Type(Integer32):
    """Custom type managementDomainPruningState based on Integer32"""
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


_ManagementDomainPruningState_Type.__name__ = "Integer32"
_ManagementDomainPruningState_Object = MibTableColumn
managementDomainPruningState = _ManagementDomainPruningState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 10),
    _ManagementDomainPruningState_Type()
)
managementDomainPruningState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    managementDomainPruningState.setStatus("current")


class _ManagementDomainVersionInUse_Type(Integer32):
    """Custom type managementDomainVersionInUse based on Integer32"""
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
        *(("none", 3),
          ("version1", 1),
          ("version2", 2),
          ("version3", 4))
    )


_ManagementDomainVersionInUse_Type.__name__ = "Integer32"
_ManagementDomainVersionInUse_Object = MibTableColumn
managementDomainVersionInUse = _ManagementDomainVersionInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 11),
    _ManagementDomainVersionInUse_Type()
)
managementDomainVersionInUse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    managementDomainVersionInUse.setStatus("current")


class _ManagementDomainPruningStateOper_Type(Integer32):
    """Custom type managementDomainPruningStateOper based on Integer32"""
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


_ManagementDomainPruningStateOper_Type.__name__ = "Integer32"
_ManagementDomainPruningStateOper_Object = MibTableColumn
managementDomainPruningStateOper = _ManagementDomainPruningStateOper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 12),
    _ManagementDomainPruningStateOper_Type()
)
managementDomainPruningStateOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementDomainPruningStateOper.setStatus("current")
_ManagementDomainAdminSrcIf_Type = SnmpAdminString
_ManagementDomainAdminSrcIf_Object = MibTableColumn
managementDomainAdminSrcIf = _ManagementDomainAdminSrcIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 13),
    _ManagementDomainAdminSrcIf_Type()
)
managementDomainAdminSrcIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    managementDomainAdminSrcIf.setStatus("current")


class _ManagementDomainSourceOnlyMode_Type(TruthValue):
    """Custom type managementDomainSourceOnlyMode based on TruthValue"""


_ManagementDomainSourceOnlyMode_Object = MibTableColumn
managementDomainSourceOnlyMode = _ManagementDomainSourceOnlyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 14),
    _ManagementDomainSourceOnlyMode_Type()
)
managementDomainSourceOnlyMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    managementDomainSourceOnlyMode.setStatus("current")
_ManagementDomainOperSrcIf_Type = SnmpAdminString
_ManagementDomainOperSrcIf_Object = MibTableColumn
managementDomainOperSrcIf = _ManagementDomainOperSrcIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 15),
    _ManagementDomainOperSrcIf_Type()
)
managementDomainOperSrcIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementDomainOperSrcIf.setStatus("current")
_ManagementDomainConfigFile_Type = SnmpAdminString
_ManagementDomainConfigFile_Object = MibTableColumn
managementDomainConfigFile = _ManagementDomainConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 16),
    _ManagementDomainConfigFile_Type()
)
managementDomainConfigFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    managementDomainConfigFile.setStatus("current")
_ManagementDomainLocalUpdaterType_Type = InetAddressType
_ManagementDomainLocalUpdaterType_Object = MibTableColumn
managementDomainLocalUpdaterType = _ManagementDomainLocalUpdaterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 17),
    _ManagementDomainLocalUpdaterType_Type()
)
managementDomainLocalUpdaterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementDomainLocalUpdaterType.setStatus("current")
_ManagementDomainLocalUpdater_Type = InetAddress
_ManagementDomainLocalUpdater_Object = MibTableColumn
managementDomainLocalUpdater = _ManagementDomainLocalUpdater_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 18),
    _ManagementDomainLocalUpdater_Type()
)
managementDomainLocalUpdater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementDomainLocalUpdater.setStatus("current")
_ManagementDomainDeviceID_Type = SnmpAdminString
_ManagementDomainDeviceID_Object = MibTableColumn
managementDomainDeviceID = _ManagementDomainDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 2, 1, 1, 19),
    _ManagementDomainDeviceID_Type()
)
managementDomainDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    managementDomainDeviceID.setStatus("current")
_VlanInfo_ObjectIdentity = ObjectIdentity
vlanInfo = _VlanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3)
)
_VtpVlanTable_Object = MibTable
vtpVlanTable = _VtpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1)
)
if mibBuilder.loadTexts:
    vtpVlanTable.setStatus("current")
_VtpVlanEntry_Object = MibTableRow
vtpVlanEntry = _VtpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1)
)
vtpVlanEntry.setIndexNames(
    (0, "CISCO-VTP-MIB", "managementDomainIndex"),
    (0, "CISCO-VTP-MIB", "vtpVlanIndex"),
)
if mibBuilder.loadTexts:
    vtpVlanEntry.setStatus("current")
_VtpVlanIndex_Type = VlanIndex
_VtpVlanIndex_Object = MibTableColumn
vtpVlanIndex = _VtpVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 1),
    _VtpVlanIndex_Type()
)
vtpVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vtpVlanIndex.setStatus("current")


class _VtpVlanState_Type(Integer32):
    """Custom type vtpVlanState based on Integer32"""
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
        *(("mtuTooBigForDevice", 3),
          ("mtuTooBigForTrunk", 4),
          ("operational", 1),
          ("suspended", 2))
    )


_VtpVlanState_Type.__name__ = "Integer32"
_VtpVlanState_Object = MibTableColumn
vtpVlanState = _VtpVlanState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 2),
    _VtpVlanState_Type()
)
vtpVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpVlanState.setStatus("current")
_VtpVlanType_Type = VlanType
_VtpVlanType_Object = MibTableColumn
vtpVlanType = _VtpVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 3),
    _VtpVlanType_Type()
)
vtpVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpVlanType.setStatus("current")


class _VtpVlanName_Type(DisplayString):
    """Custom type vtpVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VtpVlanName_Type.__name__ = "DisplayString"
_VtpVlanName_Object = MibTableColumn
vtpVlanName = _VtpVlanName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 4),
    _VtpVlanName_Type()
)
vtpVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpVlanName.setStatus("current")


class _VtpVlanMtu_Type(Integer32):
    """Custom type vtpVlanMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 18190),
    )


_VtpVlanMtu_Type.__name__ = "Integer32"
_VtpVlanMtu_Object = MibTableColumn
vtpVlanMtu = _VtpVlanMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 5),
    _VtpVlanMtu_Type()
)
vtpVlanMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpVlanMtu.setStatus("current")


class _VtpVlanDot10Said_Type(OctetString):
    """Custom type vtpVlanDot10Said based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_VtpVlanDot10Said_Type.__name__ = "OctetString"
_VtpVlanDot10Said_Object = MibTableColumn
vtpVlanDot10Said = _VtpVlanDot10Said_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 6),
    _VtpVlanDot10Said_Type()
)
vtpVlanDot10Said.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpVlanDot10Said.setStatus("current")


class _VtpVlanRingNumber_Type(Integer32):
    """Custom type vtpVlanRingNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VtpVlanRingNumber_Type.__name__ = "Integer32"
_VtpVlanRingNumber_Object = MibTableColumn
vtpVlanRingNumber = _VtpVlanRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 7),
    _VtpVlanRingNumber_Type()
)
vtpVlanRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpVlanRingNumber.setStatus("current")


class _VtpVlanBridgeNumber_Type(Integer32):
    """Custom type vtpVlanBridgeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_VtpVlanBridgeNumber_Type.__name__ = "Integer32"
_VtpVlanBridgeNumber_Object = MibTableColumn
vtpVlanBridgeNumber = _VtpVlanBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 8),
    _VtpVlanBridgeNumber_Type()
)
vtpVlanBridgeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpVlanBridgeNumber.setStatus("current")


class _VtpVlanStpType_Type(Integer32):
    """Custom type vtpVlanStpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hybrid", 3),
          ("ibm", 2),
          ("ieee", 1))
    )


_VtpVlanStpType_Type.__name__ = "Integer32"
_VtpVlanStpType_Object = MibTableColumn
vtpVlanStpType = _VtpVlanStpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 9),
    _VtpVlanStpType_Type()
)
vtpVlanStpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpVlanStpType.setStatus("current")
_VtpVlanParentVlan_Type = VlanIndex
_VtpVlanParentVlan_Object = MibTableColumn
vtpVlanParentVlan = _VtpVlanParentVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 10),
    _VtpVlanParentVlan_Type()
)
vtpVlanParentVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpVlanParentVlan.setStatus("current")
_VtpVlanTranslationalVlan1_Type = VlanIndex
_VtpVlanTranslationalVlan1_Object = MibTableColumn
vtpVlanTranslationalVlan1 = _VtpVlanTranslationalVlan1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 11),
    _VtpVlanTranslationalVlan1_Type()
)
vtpVlanTranslationalVlan1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpVlanTranslationalVlan1.setStatus("current")
_VtpVlanTranslationalVlan2_Type = VlanIndex
_VtpVlanTranslationalVlan2_Object = MibTableColumn
vtpVlanTranslationalVlan2 = _VtpVlanTranslationalVlan2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 12),
    _VtpVlanTranslationalVlan2_Type()
)
vtpVlanTranslationalVlan2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpVlanTranslationalVlan2.setStatus("current")


class _VtpVlanBridgeType_Type(Integer32):
    """Custom type vtpVlanBridgeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("srb", 2),
          ("srt", 1))
    )


_VtpVlanBridgeType_Type.__name__ = "Integer32"
_VtpVlanBridgeType_Object = MibTableColumn
vtpVlanBridgeType = _VtpVlanBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 13),
    _VtpVlanBridgeType_Type()
)
vtpVlanBridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpVlanBridgeType.setStatus("current")


class _VtpVlanAreHopCount_Type(Integer32):
    """Custom type vtpVlanAreHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_VtpVlanAreHopCount_Type.__name__ = "Integer32"
_VtpVlanAreHopCount_Object = MibTableColumn
vtpVlanAreHopCount = _VtpVlanAreHopCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 14),
    _VtpVlanAreHopCount_Type()
)
vtpVlanAreHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpVlanAreHopCount.setStatus("current")


class _VtpVlanSteHopCount_Type(Integer32):
    """Custom type vtpVlanSteHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_VtpVlanSteHopCount_Type.__name__ = "Integer32"
_VtpVlanSteHopCount_Object = MibTableColumn
vtpVlanSteHopCount = _VtpVlanSteHopCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 15),
    _VtpVlanSteHopCount_Type()
)
vtpVlanSteHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpVlanSteHopCount.setStatus("current")
_VtpVlanIsCRFBackup_Type = TruthValue
_VtpVlanIsCRFBackup_Object = MibTableColumn
vtpVlanIsCRFBackup = _VtpVlanIsCRFBackup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 16),
    _VtpVlanIsCRFBackup_Type()
)
vtpVlanIsCRFBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpVlanIsCRFBackup.setStatus("current")
_VtpVlanTypeExt_Type = VlanTypeExt
_VtpVlanTypeExt_Object = MibTableColumn
vtpVlanTypeExt = _VtpVlanTypeExt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 17),
    _VtpVlanTypeExt_Type()
)
vtpVlanTypeExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpVlanTypeExt.setStatus("current")
_VtpVlanIfIndex_Type = InterfaceIndexOrZero
_VtpVlanIfIndex_Object = MibTableColumn
vtpVlanIfIndex = _VtpVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 1, 1, 18),
    _VtpVlanIfIndex_Type()
)
vtpVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpVlanIfIndex.setStatus("current")
_InternalVlanInfo_ObjectIdentity = ObjectIdentity
internalVlanInfo = _InternalVlanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 2)
)


class _VtpInternalVlanAllocPolicy_Type(Integer32):
    """Custom type vtpInternalVlanAllocPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascending", 1),
          ("descending", 2))
    )


_VtpInternalVlanAllocPolicy_Type.__name__ = "Integer32"
_VtpInternalVlanAllocPolicy_Object = MibScalar
vtpInternalVlanAllocPolicy = _VtpInternalVlanAllocPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 2, 1),
    _VtpInternalVlanAllocPolicy_Type()
)
vtpInternalVlanAllocPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtpInternalVlanAllocPolicy.setStatus("current")
_VtpInternalVlanTable_Object = MibTable
vtpInternalVlanTable = _VtpInternalVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    vtpInternalVlanTable.setStatus("current")
_VtpInternalVlanEntry_Object = MibTableRow
vtpInternalVlanEntry = _VtpInternalVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 2, 2, 1)
)
vtpInternalVlanEntry.setIndexNames(
    (0, "CISCO-VTP-MIB", "managementDomainIndex"),
    (0, "CISCO-VTP-MIB", "vtpVlanIndex"),
)
if mibBuilder.loadTexts:
    vtpInternalVlanEntry.setStatus("current")
_VtpInternalVlanOwner_Type = SnmpAdminString
_VtpInternalVlanOwner_Object = MibTableColumn
vtpInternalVlanOwner = _VtpInternalVlanOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 3, 2, 2, 1, 1),
    _VtpInternalVlanOwner_Type()
)
vtpInternalVlanOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpInternalVlanOwner.setStatus("current")
_VlanEdit_ObjectIdentity = ObjectIdentity
vlanEdit = _VlanEdit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4)
)
_VtpEditControlTable_Object = MibTable
vtpEditControlTable = _VtpEditControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 1)
)
if mibBuilder.loadTexts:
    vtpEditControlTable.setStatus("current")
_VtpEditControlEntry_Object = MibTableRow
vtpEditControlEntry = _VtpEditControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    vtpEditControlEntry.setStatus("current")


class _VtpVlanEditOperation_Type(Integer32):
    """Custom type vtpVlanEditOperation based on Integer32"""
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
        *(("apply", 3),
          ("copy", 2),
          ("none", 1),
          ("release", 4),
          ("restartTimer", 5))
    )


_VtpVlanEditOperation_Type.__name__ = "Integer32"
_VtpVlanEditOperation_Object = MibTableColumn
vtpVlanEditOperation = _VtpVlanEditOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 1, 1, 1),
    _VtpVlanEditOperation_Type()
)
vtpVlanEditOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vtpVlanEditOperation.setStatus("current")


class _VtpVlanApplyStatus_Type(Integer32):
    """Custom type vtpVlanApplyStatus based on Integer32"""
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
        *(("configNumberError", 3),
          ("editBufferEmpty", 8),
          ("inProgress", 1),
          ("inconsistentEdit", 4),
          ("localNVStoreFail", 6),
          ("notPrimaryServer", 10),
          ("remoteNVStoreFail", 7),
          ("someOtherError", 9),
          ("succeeded", 2),
          ("tooBig", 5))
    )


_VtpVlanApplyStatus_Type.__name__ = "Integer32"
_VtpVlanApplyStatus_Object = MibTableColumn
vtpVlanApplyStatus = _VtpVlanApplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 1, 1, 2),
    _VtpVlanApplyStatus_Type()
)
vtpVlanApplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpVlanApplyStatus.setStatus("current")
_VtpVlanEditBufferOwner_Type = OwnerString
_VtpVlanEditBufferOwner_Object = MibTableColumn
vtpVlanEditBufferOwner = _VtpVlanEditBufferOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 1, 1, 3),
    _VtpVlanEditBufferOwner_Type()
)
vtpVlanEditBufferOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vtpVlanEditBufferOwner.setStatus("current")
_VtpVlanEditConfigRevNumber_Type = Gauge32
_VtpVlanEditConfigRevNumber_Object = MibTableColumn
vtpVlanEditConfigRevNumber = _VtpVlanEditConfigRevNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 1, 1, 4),
    _VtpVlanEditConfigRevNumber_Type()
)
vtpVlanEditConfigRevNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vtpVlanEditConfigRevNumber.setStatus("current")
_VtpVlanEditModifiedVlan_Type = VlanIndex
_VtpVlanEditModifiedVlan_Object = MibTableColumn
vtpVlanEditModifiedVlan = _VtpVlanEditModifiedVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 1, 1, 5),
    _VtpVlanEditModifiedVlan_Type()
)
vtpVlanEditModifiedVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpVlanEditModifiedVlan.setStatus("current")
_VtpVlanEditTable_Object = MibTable
vtpVlanEditTable = _VtpVlanEditTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2)
)
if mibBuilder.loadTexts:
    vtpVlanEditTable.setStatus("current")
_VtpVlanEditEntry_Object = MibTableRow
vtpVlanEditEntry = _VtpVlanEditEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1)
)
vtpVlanEditEntry.setIndexNames(
    (0, "CISCO-VTP-MIB", "managementDomainIndex"),
    (0, "CISCO-VTP-MIB", "vtpVlanEditIndex"),
)
if mibBuilder.loadTexts:
    vtpVlanEditEntry.setStatus("current")
_VtpVlanEditIndex_Type = VlanIndex
_VtpVlanEditIndex_Object = MibTableColumn
vtpVlanEditIndex = _VtpVlanEditIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 1),
    _VtpVlanEditIndex_Type()
)
vtpVlanEditIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vtpVlanEditIndex.setStatus("current")


class _VtpVlanEditState_Type(Integer32):
    """Custom type vtpVlanEditState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("suspended", 2))
    )


_VtpVlanEditState_Type.__name__ = "Integer32"
_VtpVlanEditState_Object = MibTableColumn
vtpVlanEditState = _VtpVlanEditState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 2),
    _VtpVlanEditState_Type()
)
vtpVlanEditState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vtpVlanEditState.setStatus("current")


class _VtpVlanEditType_Type(VlanType):
    """Custom type vtpVlanEditType based on VlanType"""


_VtpVlanEditType_Object = MibTableColumn
vtpVlanEditType = _VtpVlanEditType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 3),
    _VtpVlanEditType_Type()
)
vtpVlanEditType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vtpVlanEditType.setStatus("current")


class _VtpVlanEditName_Type(DisplayString):
    """Custom type vtpVlanEditName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_VtpVlanEditName_Type.__name__ = "DisplayString"
_VtpVlanEditName_Object = MibTableColumn
vtpVlanEditName = _VtpVlanEditName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 4),
    _VtpVlanEditName_Type()
)
vtpVlanEditName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vtpVlanEditName.setStatus("current")


class _VtpVlanEditMtu_Type(Integer32):
    """Custom type vtpVlanEditMtu based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1500, 18190),
    )


_VtpVlanEditMtu_Type.__name__ = "Integer32"
_VtpVlanEditMtu_Object = MibTableColumn
vtpVlanEditMtu = _VtpVlanEditMtu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 5),
    _VtpVlanEditMtu_Type()
)
vtpVlanEditMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vtpVlanEditMtu.setStatus("current")


class _VtpVlanEditDot10Said_Type(OctetString):
    """Custom type vtpVlanEditDot10Said based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_VtpVlanEditDot10Said_Type.__name__ = "OctetString"
_VtpVlanEditDot10Said_Object = MibTableColumn
vtpVlanEditDot10Said = _VtpVlanEditDot10Said_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 6),
    _VtpVlanEditDot10Said_Type()
)
vtpVlanEditDot10Said.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vtpVlanEditDot10Said.setStatus("current")


class _VtpVlanEditRingNumber_Type(Integer32):
    """Custom type vtpVlanEditRingNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_VtpVlanEditRingNumber_Type.__name__ = "Integer32"
_VtpVlanEditRingNumber_Object = MibTableColumn
vtpVlanEditRingNumber = _VtpVlanEditRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 7),
    _VtpVlanEditRingNumber_Type()
)
vtpVlanEditRingNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vtpVlanEditRingNumber.setStatus("current")


class _VtpVlanEditBridgeNumber_Type(Integer32):
    """Custom type vtpVlanEditBridgeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_VtpVlanEditBridgeNumber_Type.__name__ = "Integer32"
_VtpVlanEditBridgeNumber_Object = MibTableColumn
vtpVlanEditBridgeNumber = _VtpVlanEditBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 8),
    _VtpVlanEditBridgeNumber_Type()
)
vtpVlanEditBridgeNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vtpVlanEditBridgeNumber.setStatus("current")


class _VtpVlanEditStpType_Type(Integer32):
    """Custom type vtpVlanEditStpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("ibm", 2),
          ("ieee", 1))
    )


_VtpVlanEditStpType_Type.__name__ = "Integer32"
_VtpVlanEditStpType_Object = MibTableColumn
vtpVlanEditStpType = _VtpVlanEditStpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 9),
    _VtpVlanEditStpType_Type()
)
vtpVlanEditStpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vtpVlanEditStpType.setStatus("current")
_VtpVlanEditParentVlan_Type = VlanIndex
_VtpVlanEditParentVlan_Object = MibTableColumn
vtpVlanEditParentVlan = _VtpVlanEditParentVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 10),
    _VtpVlanEditParentVlan_Type()
)
vtpVlanEditParentVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vtpVlanEditParentVlan.setStatus("current")
_VtpVlanEditRowStatus_Type = RowStatus
_VtpVlanEditRowStatus_Object = MibTableColumn
vtpVlanEditRowStatus = _VtpVlanEditRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 11),
    _VtpVlanEditRowStatus_Type()
)
vtpVlanEditRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vtpVlanEditRowStatus.setStatus("current")


class _VtpVlanEditTranslationalVlan1_Type(VlanIndex):
    """Custom type vtpVlanEditTranslationalVlan1 based on VlanIndex"""
    defaultValue = 0


_VtpVlanEditTranslationalVlan1_Object = MibTableColumn
vtpVlanEditTranslationalVlan1 = _VtpVlanEditTranslationalVlan1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 12),
    _VtpVlanEditTranslationalVlan1_Type()
)
vtpVlanEditTranslationalVlan1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vtpVlanEditTranslationalVlan1.setStatus("current")


class _VtpVlanEditTranslationalVlan2_Type(VlanIndex):
    """Custom type vtpVlanEditTranslationalVlan2 based on VlanIndex"""
    defaultValue = 0


_VtpVlanEditTranslationalVlan2_Object = MibTableColumn
vtpVlanEditTranslationalVlan2 = _VtpVlanEditTranslationalVlan2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 13),
    _VtpVlanEditTranslationalVlan2_Type()
)
vtpVlanEditTranslationalVlan2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vtpVlanEditTranslationalVlan2.setStatus("current")


class _VtpVlanEditBridgeType_Type(Integer32):
    """Custom type vtpVlanEditBridgeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("srb", 2),
          ("srt", 1))
    )


_VtpVlanEditBridgeType_Type.__name__ = "Integer32"
_VtpVlanEditBridgeType_Object = MibTableColumn
vtpVlanEditBridgeType = _VtpVlanEditBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 14),
    _VtpVlanEditBridgeType_Type()
)
vtpVlanEditBridgeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vtpVlanEditBridgeType.setStatus("current")


class _VtpVlanEditAreHopCount_Type(Integer32):
    """Custom type vtpVlanEditAreHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_VtpVlanEditAreHopCount_Type.__name__ = "Integer32"
_VtpVlanEditAreHopCount_Object = MibTableColumn
vtpVlanEditAreHopCount = _VtpVlanEditAreHopCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 15),
    _VtpVlanEditAreHopCount_Type()
)
vtpVlanEditAreHopCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vtpVlanEditAreHopCount.setStatus("current")


class _VtpVlanEditSteHopCount_Type(Integer32):
    """Custom type vtpVlanEditSteHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_VtpVlanEditSteHopCount_Type.__name__ = "Integer32"
_VtpVlanEditSteHopCount_Object = MibTableColumn
vtpVlanEditSteHopCount = _VtpVlanEditSteHopCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 16),
    _VtpVlanEditSteHopCount_Type()
)
vtpVlanEditSteHopCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vtpVlanEditSteHopCount.setStatus("current")
_VtpVlanEditIsCRFBackup_Type = TruthValue
_VtpVlanEditIsCRFBackup_Object = MibTableColumn
vtpVlanEditIsCRFBackup = _VtpVlanEditIsCRFBackup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 17),
    _VtpVlanEditIsCRFBackup_Type()
)
vtpVlanEditIsCRFBackup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vtpVlanEditIsCRFBackup.setStatus("current")
_VtpVlanEditTypeExt_Type = VlanTypeExt
_VtpVlanEditTypeExt_Object = MibTableColumn
vtpVlanEditTypeExt = _VtpVlanEditTypeExt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 18),
    _VtpVlanEditTypeExt_Type()
)
vtpVlanEditTypeExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpVlanEditTypeExt.setStatus("deprecated")
_VtpVlanEditTypeExt2_Type = VlanTypeExt
_VtpVlanEditTypeExt2_Object = MibTableColumn
vtpVlanEditTypeExt2 = _VtpVlanEditTypeExt2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 2, 1, 19),
    _VtpVlanEditTypeExt2_Type()
)
vtpVlanEditTypeExt2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vtpVlanEditTypeExt2.setStatus("current")
_VtpVlanLocalShutdownTable_Object = MibTable
vtpVlanLocalShutdownTable = _VtpVlanLocalShutdownTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 3)
)
if mibBuilder.loadTexts:
    vtpVlanLocalShutdownTable.setStatus("current")
_VtpVlanLocalShutdownEntry_Object = MibTableRow
vtpVlanLocalShutdownEntry = _VtpVlanLocalShutdownEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 3, 1)
)
vtpVlanLocalShutdownEntry.setIndexNames(
    (0, "CISCO-VTP-MIB", "managementDomainIndex"),
    (0, "CISCO-VTP-MIB", "vtpVlanIndex"),
)
if mibBuilder.loadTexts:
    vtpVlanLocalShutdownEntry.setStatus("current")


class _VtpVlanLocalShutdown_Type(Integer32):
    """Custom type vtpVlanLocalShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_VtpVlanLocalShutdown_Type.__name__ = "Integer32"
_VtpVlanLocalShutdown_Object = MibTableColumn
vtpVlanLocalShutdown = _VtpVlanLocalShutdown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 4, 3, 1, 1),
    _VtpVlanLocalShutdown_Type()
)
vtpVlanLocalShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtpVlanLocalShutdown.setStatus("current")
_VtpStats_ObjectIdentity = ObjectIdentity
vtpStats = _VtpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 5)
)
_VtpStatsTable_Object = MibTable
vtpStatsTable = _VtpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 5, 1)
)
if mibBuilder.loadTexts:
    vtpStatsTable.setStatus("current")
_VtpStatsEntry_Object = MibTableRow
vtpStatsEntry = _VtpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    vtpStatsEntry.setStatus("current")
_VtpInSummaryAdverts_Type = Counter32
_VtpInSummaryAdverts_Object = MibTableColumn
vtpInSummaryAdverts = _VtpInSummaryAdverts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 5, 1, 1, 1),
    _VtpInSummaryAdverts_Type()
)
vtpInSummaryAdverts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpInSummaryAdverts.setStatus("current")
_VtpInSubsetAdverts_Type = Counter32
_VtpInSubsetAdverts_Object = MibTableColumn
vtpInSubsetAdverts = _VtpInSubsetAdverts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 5, 1, 1, 2),
    _VtpInSubsetAdverts_Type()
)
vtpInSubsetAdverts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpInSubsetAdverts.setStatus("current")
_VtpInAdvertRequests_Type = Counter32
_VtpInAdvertRequests_Object = MibTableColumn
vtpInAdvertRequests = _VtpInAdvertRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 5, 1, 1, 3),
    _VtpInAdvertRequests_Type()
)
vtpInAdvertRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpInAdvertRequests.setStatus("current")
_VtpOutSummaryAdverts_Type = Counter32
_VtpOutSummaryAdverts_Object = MibTableColumn
vtpOutSummaryAdverts = _VtpOutSummaryAdverts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 5, 1, 1, 4),
    _VtpOutSummaryAdverts_Type()
)
vtpOutSummaryAdverts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpOutSummaryAdverts.setStatus("current")
_VtpOutSubsetAdverts_Type = Counter32
_VtpOutSubsetAdverts_Object = MibTableColumn
vtpOutSubsetAdverts = _VtpOutSubsetAdverts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 5, 1, 1, 5),
    _VtpOutSubsetAdverts_Type()
)
vtpOutSubsetAdverts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpOutSubsetAdverts.setStatus("current")
_VtpOutAdvertRequests_Type = Counter32
_VtpOutAdvertRequests_Object = MibTableColumn
vtpOutAdvertRequests = _VtpOutAdvertRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 5, 1, 1, 6),
    _VtpOutAdvertRequests_Type()
)
vtpOutAdvertRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpOutAdvertRequests.setStatus("current")
_VtpConfigRevNumberErrors_Type = Counter32
_VtpConfigRevNumberErrors_Object = MibTableColumn
vtpConfigRevNumberErrors = _VtpConfigRevNumberErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 5, 1, 1, 7),
    _VtpConfigRevNumberErrors_Type()
)
vtpConfigRevNumberErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpConfigRevNumberErrors.setStatus("current")
_VtpConfigDigestErrors_Type = Counter32
_VtpConfigDigestErrors_Object = MibTableColumn
vtpConfigDigestErrors = _VtpConfigDigestErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 5, 1, 1, 8),
    _VtpConfigDigestErrors_Type()
)
vtpConfigDigestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpConfigDigestErrors.setStatus("current")
_VlanTrunkPorts_ObjectIdentity = ObjectIdentity
vlanTrunkPorts = _VlanTrunkPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6)
)
_VlanTrunkPortTable_Object = MibTable
vlanTrunkPortTable = _VlanTrunkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1)
)
if mibBuilder.loadTexts:
    vlanTrunkPortTable.setStatus("current")
_VlanTrunkPortEntry_Object = MibTableRow
vlanTrunkPortEntry = _VlanTrunkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1)
)
vlanTrunkPortEntry.setIndexNames(
    (0, "CISCO-VTP-MIB", "vlanTrunkPortIfIndex"),
)
if mibBuilder.loadTexts:
    vlanTrunkPortEntry.setStatus("current")
_VlanTrunkPortIfIndex_Type = InterfaceIndex
_VlanTrunkPortIfIndex_Object = MibTableColumn
vlanTrunkPortIfIndex = _VlanTrunkPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 1),
    _VlanTrunkPortIfIndex_Type()
)
vlanTrunkPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanTrunkPortIfIndex.setStatus("current")
_VlanTrunkPortManagementDomain_Type = ManagementDomainIndex
_VlanTrunkPortManagementDomain_Object = MibTableColumn
vlanTrunkPortManagementDomain = _VlanTrunkPortManagementDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 2),
    _VlanTrunkPortManagementDomain_Type()
)
vlanTrunkPortManagementDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkPortManagementDomain.setStatus("current")


class _VlanTrunkPortEncapsulationType_Type(Integer32):
    """Custom type vlanTrunkPortEncapsulationType based on Integer32"""
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
        *(("dot10", 2),
          ("dot1Q", 4),
          ("isl", 1),
          ("lane", 3),
          ("negotiate", 5))
    )


_VlanTrunkPortEncapsulationType_Type.__name__ = "Integer32"
_VlanTrunkPortEncapsulationType_Object = MibTableColumn
vlanTrunkPortEncapsulationType = _VlanTrunkPortEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 3),
    _VlanTrunkPortEncapsulationType_Type()
)
vlanTrunkPortEncapsulationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkPortEncapsulationType.setStatus("current")


class _VlanTrunkPortVlansEnabled_Type(OctetString):
    """Custom type vlanTrunkPortVlansEnabled based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_VlanTrunkPortVlansEnabled_Type.__name__ = "OctetString"
_VlanTrunkPortVlansEnabled_Object = MibTableColumn
vlanTrunkPortVlansEnabled = _VlanTrunkPortVlansEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 4),
    _VlanTrunkPortVlansEnabled_Type()
)
vlanTrunkPortVlansEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansEnabled.setStatus("current")
_VlanTrunkPortNativeVlan_Type = VlanIndex
_VlanTrunkPortNativeVlan_Object = MibTableColumn
vlanTrunkPortNativeVlan = _VlanTrunkPortNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 5),
    _VlanTrunkPortNativeVlan_Type()
)
vlanTrunkPortNativeVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkPortNativeVlan.setStatus("current")
_VlanTrunkPortRowStatus_Type = RowStatus
_VlanTrunkPortRowStatus_Object = MibTableColumn
vlanTrunkPortRowStatus = _VlanTrunkPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 6),
    _VlanTrunkPortRowStatus_Type()
)
vlanTrunkPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkPortRowStatus.setStatus("current")
_VlanTrunkPortInJoins_Type = Counter32
_VlanTrunkPortInJoins_Object = MibTableColumn
vlanTrunkPortInJoins = _VlanTrunkPortInJoins_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 7),
    _VlanTrunkPortInJoins_Type()
)
vlanTrunkPortInJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTrunkPortInJoins.setStatus("current")
_VlanTrunkPortOutJoins_Type = Counter32
_VlanTrunkPortOutJoins_Object = MibTableColumn
vlanTrunkPortOutJoins = _VlanTrunkPortOutJoins_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 8),
    _VlanTrunkPortOutJoins_Type()
)
vlanTrunkPortOutJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTrunkPortOutJoins.setStatus("current")
_VlanTrunkPortOldAdverts_Type = Counter32
_VlanTrunkPortOldAdverts_Object = MibTableColumn
vlanTrunkPortOldAdverts = _VlanTrunkPortOldAdverts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 9),
    _VlanTrunkPortOldAdverts_Type()
)
vlanTrunkPortOldAdverts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTrunkPortOldAdverts.setStatus("current")


class _VlanTrunkPortVlansPruningEligible_Type(OctetString):
    """Custom type vlanTrunkPortVlansPruningEligible based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_VlanTrunkPortVlansPruningEligible_Type.__name__ = "OctetString"
_VlanTrunkPortVlansPruningEligible_Object = MibTableColumn
vlanTrunkPortVlansPruningEligible = _VlanTrunkPortVlansPruningEligible_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 10),
    _VlanTrunkPortVlansPruningEligible_Type()
)
vlanTrunkPortVlansPruningEligible.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansPruningEligible.setStatus("current")


class _VlanTrunkPortVlansXmitJoined_Type(OctetString):
    """Custom type vlanTrunkPortVlansXmitJoined based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_VlanTrunkPortVlansXmitJoined_Type.__name__ = "OctetString"
_VlanTrunkPortVlansXmitJoined_Object = MibTableColumn
vlanTrunkPortVlansXmitJoined = _VlanTrunkPortVlansXmitJoined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 11),
    _VlanTrunkPortVlansXmitJoined_Type()
)
vlanTrunkPortVlansXmitJoined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansXmitJoined.setStatus("current")


class _VlanTrunkPortVlansRcvJoined_Type(OctetString):
    """Custom type vlanTrunkPortVlansRcvJoined based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_VlanTrunkPortVlansRcvJoined_Type.__name__ = "OctetString"
_VlanTrunkPortVlansRcvJoined_Object = MibTableColumn
vlanTrunkPortVlansRcvJoined = _VlanTrunkPortVlansRcvJoined_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 12),
    _VlanTrunkPortVlansRcvJoined_Type()
)
vlanTrunkPortVlansRcvJoined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansRcvJoined.setStatus("current")


class _VlanTrunkPortDynamicState_Type(Integer32):
    """Custom type vlanTrunkPortDynamicState based on Integer32"""
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
        *(("auto", 4),
          ("desirable", 3),
          ("off", 2),
          ("on", 1),
          ("onNoNegotiate", 5))
    )


_VlanTrunkPortDynamicState_Type.__name__ = "Integer32"
_VlanTrunkPortDynamicState_Object = MibTableColumn
vlanTrunkPortDynamicState = _VlanTrunkPortDynamicState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 13),
    _VlanTrunkPortDynamicState_Type()
)
vlanTrunkPortDynamicState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkPortDynamicState.setStatus("current")


class _VlanTrunkPortDynamicStatus_Type(Integer32):
    """Custom type vlanTrunkPortDynamicStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notTrunking", 2),
          ("trunking", 1))
    )


_VlanTrunkPortDynamicStatus_Type.__name__ = "Integer32"
_VlanTrunkPortDynamicStatus_Object = MibTableColumn
vlanTrunkPortDynamicStatus = _VlanTrunkPortDynamicStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 14),
    _VlanTrunkPortDynamicStatus_Type()
)
vlanTrunkPortDynamicStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTrunkPortDynamicStatus.setStatus("current")
_VlanTrunkPortVtpEnabled_Type = TruthValue
_VlanTrunkPortVtpEnabled_Object = MibTableColumn
vlanTrunkPortVtpEnabled = _VlanTrunkPortVtpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 15),
    _VlanTrunkPortVtpEnabled_Type()
)
vlanTrunkPortVtpEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkPortVtpEnabled.setStatus("current")


class _VlanTrunkPortEncapsulationOperType_Type(Integer32):
    """Custom type vlanTrunkPortEncapsulationOperType based on Integer32"""
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
        *(("dot10", 2),
          ("dot1Q", 4),
          ("isl", 1),
          ("lane", 3),
          ("negotiating", 5),
          ("notApplicable", 6))
    )


_VlanTrunkPortEncapsulationOperType_Type.__name__ = "Integer32"
_VlanTrunkPortEncapsulationOperType_Object = MibTableColumn
vlanTrunkPortEncapsulationOperType = _VlanTrunkPortEncapsulationOperType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 16),
    _VlanTrunkPortEncapsulationOperType_Type()
)
vlanTrunkPortEncapsulationOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTrunkPortEncapsulationOperType.setStatus("current")


class _VlanTrunkPortVlansEnabled2k_Type(OctetString):
    """Custom type vlanTrunkPortVlansEnabled2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VlanTrunkPortVlansEnabled2k_Type.__name__ = "OctetString"
_VlanTrunkPortVlansEnabled2k_Object = MibTableColumn
vlanTrunkPortVlansEnabled2k = _VlanTrunkPortVlansEnabled2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 17),
    _VlanTrunkPortVlansEnabled2k_Type()
)
vlanTrunkPortVlansEnabled2k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansEnabled2k.setStatus("current")


class _VlanTrunkPortVlansEnabled3k_Type(OctetString):
    """Custom type vlanTrunkPortVlansEnabled3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VlanTrunkPortVlansEnabled3k_Type.__name__ = "OctetString"
_VlanTrunkPortVlansEnabled3k_Object = MibTableColumn
vlanTrunkPortVlansEnabled3k = _VlanTrunkPortVlansEnabled3k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 18),
    _VlanTrunkPortVlansEnabled3k_Type()
)
vlanTrunkPortVlansEnabled3k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansEnabled3k.setStatus("current")


class _VlanTrunkPortVlansEnabled4k_Type(OctetString):
    """Custom type vlanTrunkPortVlansEnabled4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VlanTrunkPortVlansEnabled4k_Type.__name__ = "OctetString"
_VlanTrunkPortVlansEnabled4k_Object = MibTableColumn
vlanTrunkPortVlansEnabled4k = _VlanTrunkPortVlansEnabled4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 19),
    _VlanTrunkPortVlansEnabled4k_Type()
)
vlanTrunkPortVlansEnabled4k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansEnabled4k.setStatus("current")


class _VtpVlansPruningEligible2k_Type(OctetString):
    """Custom type vtpVlansPruningEligible2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VtpVlansPruningEligible2k_Type.__name__ = "OctetString"
_VtpVlansPruningEligible2k_Object = MibTableColumn
vtpVlansPruningEligible2k = _VtpVlansPruningEligible2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 20),
    _VtpVlansPruningEligible2k_Type()
)
vtpVlansPruningEligible2k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vtpVlansPruningEligible2k.setStatus("current")


class _VtpVlansPruningEligible3k_Type(OctetString):
    """Custom type vtpVlansPruningEligible3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VtpVlansPruningEligible3k_Type.__name__ = "OctetString"
_VtpVlansPruningEligible3k_Object = MibTableColumn
vtpVlansPruningEligible3k = _VtpVlansPruningEligible3k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 21),
    _VtpVlansPruningEligible3k_Type()
)
vtpVlansPruningEligible3k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vtpVlansPruningEligible3k.setStatus("current")


class _VtpVlansPruningEligible4k_Type(OctetString):
    """Custom type vtpVlansPruningEligible4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VtpVlansPruningEligible4k_Type.__name__ = "OctetString"
_VtpVlansPruningEligible4k_Object = MibTableColumn
vtpVlansPruningEligible4k = _VtpVlansPruningEligible4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 22),
    _VtpVlansPruningEligible4k_Type()
)
vtpVlansPruningEligible4k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vtpVlansPruningEligible4k.setStatus("current")


class _VlanTrunkPortVlansXmitJoined2k_Type(OctetString):
    """Custom type vlanTrunkPortVlansXmitJoined2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VlanTrunkPortVlansXmitJoined2k_Type.__name__ = "OctetString"
_VlanTrunkPortVlansXmitJoined2k_Object = MibTableColumn
vlanTrunkPortVlansXmitJoined2k = _VlanTrunkPortVlansXmitJoined2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 23),
    _VlanTrunkPortVlansXmitJoined2k_Type()
)
vlanTrunkPortVlansXmitJoined2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansXmitJoined2k.setStatus("current")


class _VlanTrunkPortVlansXmitJoined3k_Type(OctetString):
    """Custom type vlanTrunkPortVlansXmitJoined3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VlanTrunkPortVlansXmitJoined3k_Type.__name__ = "OctetString"
_VlanTrunkPortVlansXmitJoined3k_Object = MibTableColumn
vlanTrunkPortVlansXmitJoined3k = _VlanTrunkPortVlansXmitJoined3k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 24),
    _VlanTrunkPortVlansXmitJoined3k_Type()
)
vlanTrunkPortVlansXmitJoined3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansXmitJoined3k.setStatus("current")


class _VlanTrunkPortVlansXmitJoined4k_Type(OctetString):
    """Custom type vlanTrunkPortVlansXmitJoined4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VlanTrunkPortVlansXmitJoined4k_Type.__name__ = "OctetString"
_VlanTrunkPortVlansXmitJoined4k_Object = MibTableColumn
vlanTrunkPortVlansXmitJoined4k = _VlanTrunkPortVlansXmitJoined4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 25),
    _VlanTrunkPortVlansXmitJoined4k_Type()
)
vlanTrunkPortVlansXmitJoined4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansXmitJoined4k.setStatus("current")


class _VlanTrunkPortVlansRcvJoined2k_Type(OctetString):
    """Custom type vlanTrunkPortVlansRcvJoined2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VlanTrunkPortVlansRcvJoined2k_Type.__name__ = "OctetString"
_VlanTrunkPortVlansRcvJoined2k_Object = MibTableColumn
vlanTrunkPortVlansRcvJoined2k = _VlanTrunkPortVlansRcvJoined2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 26),
    _VlanTrunkPortVlansRcvJoined2k_Type()
)
vlanTrunkPortVlansRcvJoined2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansRcvJoined2k.setStatus("current")


class _VlanTrunkPortVlansRcvJoined3k_Type(OctetString):
    """Custom type vlanTrunkPortVlansRcvJoined3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VlanTrunkPortVlansRcvJoined3k_Type.__name__ = "OctetString"
_VlanTrunkPortVlansRcvJoined3k_Object = MibTableColumn
vlanTrunkPortVlansRcvJoined3k = _VlanTrunkPortVlansRcvJoined3k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 27),
    _VlanTrunkPortVlansRcvJoined3k_Type()
)
vlanTrunkPortVlansRcvJoined3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansRcvJoined3k.setStatus("current")


class _VlanTrunkPortVlansRcvJoined4k_Type(OctetString):
    """Custom type vlanTrunkPortVlansRcvJoined4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VlanTrunkPortVlansRcvJoined4k_Type.__name__ = "OctetString"
_VlanTrunkPortVlansRcvJoined4k_Object = MibTableColumn
vlanTrunkPortVlansRcvJoined4k = _VlanTrunkPortVlansRcvJoined4k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 28),
    _VlanTrunkPortVlansRcvJoined4k_Type()
)
vlanTrunkPortVlansRcvJoined4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansRcvJoined4k.setStatus("current")


class _VlanTrunkPortDot1qTunnel_Type(Integer32):
    """Custom type vlanTrunkPortDot1qTunnel based on Integer32"""
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
        *(("access", 2),
          ("disabled", 3),
          ("trunk", 1))
    )


_VlanTrunkPortDot1qTunnel_Type.__name__ = "Integer32"
_VlanTrunkPortDot1qTunnel_Object = MibTableColumn
vlanTrunkPortDot1qTunnel = _VlanTrunkPortDot1qTunnel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 29),
    _VlanTrunkPortDot1qTunnel_Type()
)
vlanTrunkPortDot1qTunnel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkPortDot1qTunnel.setStatus("deprecated")
_VlanTrunkPortVlansActiveFirst2k_Type = Cisco2KVlanList
_VlanTrunkPortVlansActiveFirst2k_Object = MibTableColumn
vlanTrunkPortVlansActiveFirst2k = _VlanTrunkPortVlansActiveFirst2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 30),
    _VlanTrunkPortVlansActiveFirst2k_Type()
)
vlanTrunkPortVlansActiveFirst2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansActiveFirst2k.setStatus("current")
_VlanTrunkPortVlansActiveSecond2k_Type = Cisco2KVlanList
_VlanTrunkPortVlansActiveSecond2k_Object = MibTableColumn
vlanTrunkPortVlansActiveSecond2k = _VlanTrunkPortVlansActiveSecond2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 1, 1, 31),
    _VlanTrunkPortVlansActiveSecond2k_Type()
)
vlanTrunkPortVlansActiveSecond2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTrunkPortVlansActiveSecond2k.setStatus("current")
_VlanTrunkPortSetSerialNo_Type = TestAndIncr
_VlanTrunkPortSetSerialNo_Object = MibScalar
vlanTrunkPortSetSerialNo = _VlanTrunkPortSetSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 2),
    _VlanTrunkPortSetSerialNo_Type()
)
vlanTrunkPortSetSerialNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTrunkPortSetSerialNo.setStatus("current")


class _VlanTrunkPortsDot1qTag_Type(TruthValue):
    """Custom type vlanTrunkPortsDot1qTag based on TruthValue"""


_VlanTrunkPortsDot1qTag_Object = MibScalar
vlanTrunkPortsDot1qTag = _VlanTrunkPortsDot1qTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 6, 3),
    _VlanTrunkPortsDot1qTag_Type()
)
vlanTrunkPortsDot1qTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTrunkPortsDot1qTag.setStatus("deprecated")
_VtpDiscover_ObjectIdentity = ObjectIdentity
vtpDiscover = _VtpDiscover_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7)
)
_VtpDiscoverTable_Object = MibTable
vtpDiscoverTable = _VtpDiscoverTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 1)
)
if mibBuilder.loadTexts:
    vtpDiscoverTable.setStatus("current")
_VtpDiscoverEntry_Object = MibTableRow
vtpDiscoverEntry = _VtpDiscoverEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 1, 1)
)
vtpDiscoverEntry.setIndexNames(
    (0, "CISCO-VTP-MIB", "managementDomainIndex"),
)
if mibBuilder.loadTexts:
    vtpDiscoverEntry.setStatus("current")


class _VtpDiscoverAction_Type(Integer32):
    """Custom type vtpDiscoverAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discover", 1),
          ("noOperation", 2),
          ("purgeResult", 3))
    )


_VtpDiscoverAction_Type.__name__ = "Integer32"
_VtpDiscoverAction_Object = MibTableColumn
vtpDiscoverAction = _VtpDiscoverAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 1, 1, 1),
    _VtpDiscoverAction_Type()
)
vtpDiscoverAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtpDiscoverAction.setStatus("current")


class _VtpDiscoverStatus_Type(Integer32):
    """Custom type vtpDiscoverStatus based on Integer32"""
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
        *(("inProgress", 1),
          ("resourceUnavailable", 3),
          ("someOtherError", 4),
          ("succeeded", 2))
    )


_VtpDiscoverStatus_Type.__name__ = "Integer32"
_VtpDiscoverStatus_Object = MibTableColumn
vtpDiscoverStatus = _VtpDiscoverStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 1, 1, 2),
    _VtpDiscoverStatus_Type()
)
vtpDiscoverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpDiscoverStatus.setStatus("current")
_VtpLastDiscoverTime_Type = TimeStamp
_VtpLastDiscoverTime_Object = MibTableColumn
vtpLastDiscoverTime = _VtpLastDiscoverTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 1, 1, 3),
    _VtpLastDiscoverTime_Type()
)
vtpLastDiscoverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpLastDiscoverTime.setStatus("current")
_VtpDiscoverResultTable_Object = MibTable
vtpDiscoverResultTable = _VtpDiscoverResultTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 2)
)
if mibBuilder.loadTexts:
    vtpDiscoverResultTable.setStatus("current")
_VtpDiscoverResultEntry_Object = MibTableRow
vtpDiscoverResultEntry = _VtpDiscoverResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 2, 1)
)
vtpDiscoverResultEntry.setIndexNames(
    (0, "CISCO-VTP-MIB", "managementDomainIndex"),
    (0, "CISCO-VTP-MIB", "vtpDiscoverResultIndex"),
)
if mibBuilder.loadTexts:
    vtpDiscoverResultEntry.setStatus("current")
_VtpDiscoverResultIndex_Type = Unsigned32
_VtpDiscoverResultIndex_Object = MibTableColumn
vtpDiscoverResultIndex = _VtpDiscoverResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 2, 1, 1),
    _VtpDiscoverResultIndex_Type()
)
vtpDiscoverResultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpDiscoverResultIndex.setStatus("current")


class _VtpDiscoverResultDatabaseName_Type(SnmpAdminString):
    """Custom type vtpDiscoverResultDatabaseName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VtpDiscoverResultDatabaseName_Type.__name__ = "SnmpAdminString"
_VtpDiscoverResultDatabaseName_Object = MibTableColumn
vtpDiscoverResultDatabaseName = _VtpDiscoverResultDatabaseName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 2, 1, 2),
    _VtpDiscoverResultDatabaseName_Type()
)
vtpDiscoverResultDatabaseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpDiscoverResultDatabaseName.setStatus("current")
_VtpDiscoverResultConflicting_Type = TruthValue
_VtpDiscoverResultConflicting_Object = MibTableColumn
vtpDiscoverResultConflicting = _VtpDiscoverResultConflicting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 2, 1, 3),
    _VtpDiscoverResultConflicting_Type()
)
vtpDiscoverResultConflicting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpDiscoverResultConflicting.setStatus("current")


class _VtpDiscoverResultDeviceId_Type(SnmpAdminString):
    """Custom type vtpDiscoverResultDeviceId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VtpDiscoverResultDeviceId_Type.__name__ = "SnmpAdminString"
_VtpDiscoverResultDeviceId_Object = MibTableColumn
vtpDiscoverResultDeviceId = _VtpDiscoverResultDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 2, 1, 4),
    _VtpDiscoverResultDeviceId_Type()
)
vtpDiscoverResultDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpDiscoverResultDeviceId.setStatus("current")


class _VtpDiscoverResultPrimaryServer_Type(SnmpAdminString):
    """Custom type vtpDiscoverResultPrimaryServer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VtpDiscoverResultPrimaryServer_Type.__name__ = "SnmpAdminString"
_VtpDiscoverResultPrimaryServer_Object = MibTableColumn
vtpDiscoverResultPrimaryServer = _VtpDiscoverResultPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 2, 1, 5),
    _VtpDiscoverResultPrimaryServer_Type()
)
vtpDiscoverResultPrimaryServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpDiscoverResultPrimaryServer.setStatus("current")
_VtpDiscoverResultRevNumber_Type = Gauge32
_VtpDiscoverResultRevNumber_Object = MibTableColumn
vtpDiscoverResultRevNumber = _VtpDiscoverResultRevNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 2, 1, 6),
    _VtpDiscoverResultRevNumber_Type()
)
vtpDiscoverResultRevNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpDiscoverResultRevNumber.setStatus("current")


class _VtpDiscoverResultSystemName_Type(SnmpAdminString):
    """Custom type vtpDiscoverResultSystemName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VtpDiscoverResultSystemName_Type.__name__ = "SnmpAdminString"
_VtpDiscoverResultSystemName_Object = MibTableColumn
vtpDiscoverResultSystemName = _VtpDiscoverResultSystemName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 7, 2, 1, 7),
    _VtpDiscoverResultSystemName_Type()
)
vtpDiscoverResultSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpDiscoverResultSystemName.setStatus("current")
_VtpDatabase_ObjectIdentity = ObjectIdentity
vtpDatabase = _VtpDatabase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 8)
)
_VtpDatabaseTable_Object = MibTable
vtpDatabaseTable = _VtpDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 8, 1)
)
if mibBuilder.loadTexts:
    vtpDatabaseTable.setStatus("current")
_VtpDatabaseEntry_Object = MibTableRow
vtpDatabaseEntry = _VtpDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 8, 1, 1)
)
vtpDatabaseEntry.setIndexNames(
    (0, "CISCO-VTP-MIB", "managementDomainIndex"),
    (0, "CISCO-VTP-MIB", "vtpDatabaseIndex"),
)
if mibBuilder.loadTexts:
    vtpDatabaseEntry.setStatus("current")
_VtpDatabaseIndex_Type = Unsigned32
_VtpDatabaseIndex_Object = MibTableColumn
vtpDatabaseIndex = _VtpDatabaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 8, 1, 1, 1),
    _VtpDatabaseIndex_Type()
)
vtpDatabaseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vtpDatabaseIndex.setStatus("current")


class _VtpDatabaseName_Type(SnmpAdminString):
    """Custom type vtpDatabaseName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VtpDatabaseName_Type.__name__ = "SnmpAdminString"
_VtpDatabaseName_Object = MibTableColumn
vtpDatabaseName = _VtpDatabaseName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 8, 1, 1, 2),
    _VtpDatabaseName_Type()
)
vtpDatabaseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpDatabaseName.setStatus("current")


class _VtpDatabaseLocalMode_Type(Integer32):
    """Custom type vtpDatabaseLocalMode based on Integer32"""
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
        *(("client", 1),
          ("off", 4),
          ("server", 2),
          ("transparent", 3))
    )


_VtpDatabaseLocalMode_Type.__name__ = "Integer32"
_VtpDatabaseLocalMode_Object = MibTableColumn
vtpDatabaseLocalMode = _VtpDatabaseLocalMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 8, 1, 1, 3),
    _VtpDatabaseLocalMode_Type()
)
vtpDatabaseLocalMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtpDatabaseLocalMode.setStatus("current")
_VtpDatabaseRevNumber_Type = Gauge32
_VtpDatabaseRevNumber_Object = MibTableColumn
vtpDatabaseRevNumber = _VtpDatabaseRevNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 8, 1, 1, 4),
    _VtpDatabaseRevNumber_Type()
)
vtpDatabaseRevNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpDatabaseRevNumber.setStatus("current")
_VtpDatabasePrimaryServer_Type = TruthValue
_VtpDatabasePrimaryServer_Object = MibTableColumn
vtpDatabasePrimaryServer = _VtpDatabasePrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 8, 1, 1, 5),
    _VtpDatabasePrimaryServer_Type()
)
vtpDatabasePrimaryServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpDatabasePrimaryServer.setStatus("current")


class _VtpDatabasePrimaryServerId_Type(SnmpAdminString):
    """Custom type vtpDatabasePrimaryServerId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VtpDatabasePrimaryServerId_Type.__name__ = "SnmpAdminString"
_VtpDatabasePrimaryServerId_Object = MibTableColumn
vtpDatabasePrimaryServerId = _VtpDatabasePrimaryServerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 8, 1, 1, 6),
    _VtpDatabasePrimaryServerId_Type()
)
vtpDatabasePrimaryServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vtpDatabasePrimaryServerId.setStatus("current")
_VtpDatabaseTakeOverPrimary_Type = TruthValue
_VtpDatabaseTakeOverPrimary_Object = MibTableColumn
vtpDatabaseTakeOverPrimary = _VtpDatabaseTakeOverPrimary_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 8, 1, 1, 7),
    _VtpDatabaseTakeOverPrimary_Type()
)
vtpDatabaseTakeOverPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtpDatabaseTakeOverPrimary.setStatus("current")


class _VtpDatabaseTakeOverPassword_Type(SnmpAdminString):
    """Custom type vtpDatabaseTakeOverPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VtpDatabaseTakeOverPassword_Type.__name__ = "SnmpAdminString"
_VtpDatabaseTakeOverPassword_Object = MibTableColumn
vtpDatabaseTakeOverPassword = _VtpDatabaseTakeOverPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 8, 1, 1, 8),
    _VtpDatabaseTakeOverPassword_Type()
)
vtpDatabaseTakeOverPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtpDatabaseTakeOverPassword.setStatus("current")
_VtpAuthentication_ObjectIdentity = ObjectIdentity
vtpAuthentication = _VtpAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 9)
)
_VtpAuthenticationTable_Object = MibTable
vtpAuthenticationTable = _VtpAuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 9, 1)
)
if mibBuilder.loadTexts:
    vtpAuthenticationTable.setStatus("current")
_VtpAuthEntry_Object = MibTableRow
vtpAuthEntry = _VtpAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 9, 1, 1)
)
vtpAuthEntry.setIndexNames(
    (0, "CISCO-VTP-MIB", "managementDomainIndex"),
)
if mibBuilder.loadTexts:
    vtpAuthEntry.setStatus("current")


class _VtpAuthPassword_Type(SnmpAdminString):
    """Custom type vtpAuthPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VtpAuthPassword_Type.__name__ = "SnmpAdminString"
_VtpAuthPassword_Object = MibTableColumn
vtpAuthPassword = _VtpAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 9, 1, 1, 1),
    _VtpAuthPassword_Type()
)
vtpAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtpAuthPassword.setStatus("current")


class _VtpAuthPasswordType_Type(Integer32):
    """Custom type vtpAuthPasswordType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hidden", 2),
          ("plaintext", 1))
    )


_VtpAuthPasswordType_Type.__name__ = "Integer32"
_VtpAuthPasswordType_Object = MibTableColumn
vtpAuthPasswordType = _VtpAuthPasswordType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 9, 1, 1, 2),
    _VtpAuthPasswordType_Type()
)
vtpAuthPasswordType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtpAuthPasswordType.setStatus("current")


class _VtpAuthSecretKey_Type(OctetString):
    """Custom type vtpAuthSecretKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_VtpAuthSecretKey_Type.__name__ = "OctetString"
_VtpAuthSecretKey_Object = MibTableColumn
vtpAuthSecretKey = _VtpAuthSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 9, 1, 1, 3),
    _VtpAuthSecretKey_Type()
)
vtpAuthSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vtpAuthSecretKey.setStatus("current")
_VlanStatistics_ObjectIdentity = ObjectIdentity
vlanStatistics = _VlanStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 10)
)
_VlanStatsVlans_Type = Unsigned32
_VlanStatsVlans_Object = MibScalar
vlanStatsVlans = _VlanStatsVlans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 10, 1),
    _VlanStatsVlans_Type()
)
vlanStatsVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanStatsVlans.setStatus("current")
_VlanStatsExtendedVlans_Type = Unsigned32
_VlanStatsExtendedVlans_Object = MibScalar
vlanStatsExtendedVlans = _VlanStatsExtendedVlans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 10, 2),
    _VlanStatsExtendedVlans_Type()
)
vlanStatsExtendedVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanStatsExtendedVlans.setStatus("current")
_VlanStatsInternalVlans_Type = Unsigned32
_VlanStatsInternalVlans_Object = MibScalar
vlanStatsInternalVlans = _VlanStatsInternalVlans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 10, 3),
    _VlanStatsInternalVlans_Type()
)
vlanStatsInternalVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanStatsInternalVlans.setStatus("current")
_VlanStatsFreeVlans_Type = Unsigned32
_VlanStatsFreeVlans_Object = MibScalar
vlanStatsFreeVlans = _VlanStatsFreeVlans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 1, 10, 4),
    _VlanStatsFreeVlans_Type()
)
vlanStatsFreeVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanStatsFreeVlans.setStatus("current")
_VtpNotifications_ObjectIdentity = ObjectIdentity
vtpNotifications = _VtpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2)
)
_VtpNotificationsPrefix_ObjectIdentity = ObjectIdentity
vtpNotificationsPrefix = _VtpNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0)
)
_VtpNotificationsObjects_ObjectIdentity = ObjectIdentity
vtpNotificationsObjects = _VtpNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 1)
)


class _VtpVlanPortLocalSegment_Type(Integer32):
    """Custom type vtpVlanPortLocalSegment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VtpVlanPortLocalSegment_Type.__name__ = "Integer32"
_VtpVlanPortLocalSegment_Object = MibScalar
vtpVlanPortLocalSegment = _VtpVlanPortLocalSegment_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 1, 1),
    _VtpVlanPortLocalSegment_Type()
)
vtpVlanPortLocalSegment.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vtpVlanPortLocalSegment.setStatus("current")
_VtpMIBConformance_ObjectIdentity = ObjectIdentity
vtpMIBConformance = _VtpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3)
)
_VtpMIBCompliances_ObjectIdentity = ObjectIdentity
vtpMIBCompliances = _VtpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1)
)
_VtpMIBGroups_ObjectIdentity = ObjectIdentity
vtpMIBGroups = _VtpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2)
)
managementDomainEntry.registerAugmentions(
    ("CISCO-VTP-MIB",
     "vtpEditControlEntry")
)
vtpEditControlEntry.setIndexNames(*managementDomainEntry.getIndexNames())
managementDomainEntry.registerAugmentions(
    ("CISCO-VTP-MIB",
     "vtpStatsEntry")
)
vtpStatsEntry.setIndexNames(*managementDomainEntry.getIndexNames())

# Managed Objects groups

vtpBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 1)
)
vtpBasicGroup.setObjects(
      *(("CISCO-VTP-MIB", "vtpVersion"),
        ("CISCO-VTP-MIB", "vtpMaxVlanStorage"),
        ("CISCO-VTP-MIB", "vtpNotificationsEnabled"),
        ("CISCO-VTP-MIB", "managementDomainName"),
        ("CISCO-VTP-MIB", "managementDomainLocalMode"),
        ("CISCO-VTP-MIB", "managementDomainConfigRevNumber"),
        ("CISCO-VTP-MIB", "managementDomainLastUpdater"),
        ("CISCO-VTP-MIB", "managementDomainLastChange"),
        ("CISCO-VTP-MIB", "managementDomainTftpServer"),
        ("CISCO-VTP-MIB", "managementDomainTftpPathname"),
        ("CISCO-VTP-MIB", "managementDomainRowStatus"))
)
if mibBuilder.loadTexts:
    vtpBasicGroup.setStatus("current")

vtpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 4)
)
vtpStatsGroup.setObjects(
      *(("CISCO-VTP-MIB", "vtpInSummaryAdverts"),
        ("CISCO-VTP-MIB", "vtpInSubsetAdverts"),
        ("CISCO-VTP-MIB", "vtpInAdvertRequests"),
        ("CISCO-VTP-MIB", "vtpOutSummaryAdverts"),
        ("CISCO-VTP-MIB", "vtpOutSubsetAdverts"),
        ("CISCO-VTP-MIB", "vtpOutAdvertRequests"),
        ("CISCO-VTP-MIB", "vtpConfigRevNumberErrors"),
        ("CISCO-VTP-MIB", "vtpConfigDigestErrors"))
)
if mibBuilder.loadTexts:
    vtpStatsGroup.setStatus("current")

vtpTrunkPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 5)
)
vtpTrunkPortGroup.setObjects(
      *(("CISCO-VTP-MIB", "vlanTrunkPortManagementDomain"),
        ("CISCO-VTP-MIB", "vlanTrunkPortEncapsulationType"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVlansEnabled"),
        ("CISCO-VTP-MIB", "vlanTrunkPortNativeVlan"),
        ("CISCO-VTP-MIB", "vlanTrunkPortRowStatus"),
        ("CISCO-VTP-MIB", "vlanTrunkPortSetSerialNo"))
)
if mibBuilder.loadTexts:
    vtpTrunkPortGroup.setStatus("current")

vtpTrunkPruningGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 7)
)
vtpTrunkPruningGroup.setObjects(
      *(("CISCO-VTP-MIB", "vlanTrunkPortInJoins"),
        ("CISCO-VTP-MIB", "vlanTrunkPortOutJoins"),
        ("CISCO-VTP-MIB", "vlanTrunkPortOldAdverts"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVlansPruningEligible"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVlansXmitJoined"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVlansRcvJoined"))
)
if mibBuilder.loadTexts:
    vtpTrunkPruningGroup.setStatus("current")

vtpTrunkPruningGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 10)
)
vtpTrunkPruningGroup2.setObjects(
    ("CISCO-VTP-MIB", "managementDomainPruningState")
)
if mibBuilder.loadTexts:
    vtpTrunkPruningGroup2.setStatus("current")

vtpTrunkPortGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 11)
)
vtpTrunkPortGroup2.setObjects(
      *(("CISCO-VTP-MIB", "vlanTrunkPortDynamicState"),
        ("CISCO-VTP-MIB", "vlanTrunkPortDynamicStatus"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVtpEnabled"))
)
if mibBuilder.loadTexts:
    vtpTrunkPortGroup2.setStatus("current")

vtpVersion2BasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 12)
)
vtpVersion2BasicGroup.setObjects(
    ("CISCO-VTP-MIB", "managementDomainVersionInUse")
)
if mibBuilder.loadTexts:
    vtpVersion2BasicGroup.setStatus("current")

vtpVlanInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 13)
)
vtpVlanInfoGroup.setObjects(
      *(("CISCO-VTP-MIB", "vtpVlanState"),
        ("CISCO-VTP-MIB", "vtpVlanType"),
        ("CISCO-VTP-MIB", "vtpVlanName"),
        ("CISCO-VTP-MIB", "vtpVlanMtu"),
        ("CISCO-VTP-MIB", "vtpVlanDot10Said"),
        ("CISCO-VTP-MIB", "vtpVlanRingNumber"),
        ("CISCO-VTP-MIB", "vtpVlanBridgeNumber"),
        ("CISCO-VTP-MIB", "vtpVlanStpType"),
        ("CISCO-VTP-MIB", "vtpVlanParentVlan"),
        ("CISCO-VTP-MIB", "vtpVlanTranslationalVlan1"),
        ("CISCO-VTP-MIB", "vtpVlanTranslationalVlan2"),
        ("CISCO-VTP-MIB", "vtpVlanBridgeType"),
        ("CISCO-VTP-MIB", "vtpVlanAreHopCount"),
        ("CISCO-VTP-MIB", "vtpVlanSteHopCount"),
        ("CISCO-VTP-MIB", "vtpVlanIsCRFBackup"))
)
if mibBuilder.loadTexts:
    vtpVlanInfoGroup.setStatus("current")

vtpVlanInfoEditGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 14)
)
vtpVlanInfoEditGroup.setObjects(
      *(("CISCO-VTP-MIB", "vtpVlanEditOperation"),
        ("CISCO-VTP-MIB", "vtpVlanApplyStatus"),
        ("CISCO-VTP-MIB", "vtpVlanEditBufferOwner"),
        ("CISCO-VTP-MIB", "vtpVlanEditConfigRevNumber"),
        ("CISCO-VTP-MIB", "vtpVlanEditState"),
        ("CISCO-VTP-MIB", "vtpVlanEditType"),
        ("CISCO-VTP-MIB", "vtpVlanEditName"),
        ("CISCO-VTP-MIB", "vtpVlanEditMtu"),
        ("CISCO-VTP-MIB", "vtpVlanEditDot10Said"),
        ("CISCO-VTP-MIB", "vtpVlanEditRingNumber"),
        ("CISCO-VTP-MIB", "vtpVlanEditBridgeNumber"),
        ("CISCO-VTP-MIB", "vtpVlanEditStpType"),
        ("CISCO-VTP-MIB", "vtpVlanEditParentVlan"),
        ("CISCO-VTP-MIB", "vtpVlanEditRowStatus"),
        ("CISCO-VTP-MIB", "vtpVlanEditTranslationalVlan1"),
        ("CISCO-VTP-MIB", "vtpVlanEditTranslationalVlan2"),
        ("CISCO-VTP-MIB", "vtpVlanEditBridgeType"),
        ("CISCO-VTP-MIB", "vtpVlanEditAreHopCount"),
        ("CISCO-VTP-MIB", "vtpVlanEditSteHopCount"),
        ("CISCO-VTP-MIB", "vtpVlanEditIsCRFBackup"))
)
if mibBuilder.loadTexts:
    vtpVlanInfoEditGroup.setStatus("current")

vtpTrunkPortGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 15)
)
vtpTrunkPortGroup3.setObjects(
    ("CISCO-VTP-MIB", "vlanTrunkPortEncapsulationOperType")
)
if mibBuilder.loadTexts:
    vtpTrunkPortGroup3.setStatus("current")

vtp4kVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 16)
)
vtp4kVlanGroup.setObjects(
      *(("CISCO-VTP-MIB", "vtpVlanTypeExt"),
        ("CISCO-VTP-MIB", "vtpVlanEditTypeExt"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVlansEnabled2k"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVlansEnabled3k"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVlansEnabled4k"),
        ("CISCO-VTP-MIB", "vtpVlansPruningEligible2k"),
        ("CISCO-VTP-MIB", "vtpVlansPruningEligible3k"),
        ("CISCO-VTP-MIB", "vtpVlansPruningEligible4k"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVlansXmitJoined2k"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVlansXmitJoined3k"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVlansXmitJoined4k"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVlansRcvJoined2k"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVlansRcvJoined3k"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVlansRcvJoined4k"))
)
if mibBuilder.loadTexts:
    vtp4kVlanGroup.setStatus("deprecated")

vtpDot1qTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 17)
)
vtpDot1qTunnelGroup.setObjects(
      *(("CISCO-VTP-MIB", "vlanTrunkPortsDot1qTag"),
        ("CISCO-VTP-MIB", "vlanTrunkPortDot1qTunnel"))
)
if mibBuilder.loadTexts:
    vtpDot1qTunnelGroup.setStatus("deprecated")

vtpVlanIfIndexGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 18)
)
vtpVlanIfIndexGroup.setObjects(
    ("CISCO-VTP-MIB", "vtpVlanIfIndex")
)
if mibBuilder.loadTexts:
    vtpVlanIfIndexGroup.setStatus("current")

vtpVlanInfoEditGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 19)
)
vtpVlanInfoEditGroup2.setObjects(
    ("CISCO-VTP-MIB", "vtpVlanEditModifiedVlan")
)
if mibBuilder.loadTexts:
    vtpVlanInfoEditGroup2.setStatus("current")

vtp4kVlanGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 20)
)
vtp4kVlanGroupRev1.setObjects(
      *(("CISCO-VTP-MIB", "vtpVlanTypeExt"),
        ("CISCO-VTP-MIB", "vtpVlanEditTypeExt2"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVlansEnabled2k"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVlansEnabled3k"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVlansEnabled4k"),
        ("CISCO-VTP-MIB", "vtpVlansPruningEligible2k"),
        ("CISCO-VTP-MIB", "vtpVlansPruningEligible3k"),
        ("CISCO-VTP-MIB", "vtpVlansPruningEligible4k"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVlansXmitJoined2k"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVlansXmitJoined3k"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVlansXmitJoined4k"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVlansRcvJoined2k"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVlansRcvJoined3k"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVlansRcvJoined4k"))
)
if mibBuilder.loadTexts:
    vtp4kVlanGroupRev1.setStatus("current")

vtpNotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 21)
)
vtpNotificationObjectsGroup.setObjects(
    ("CISCO-VTP-MIB", "vtpVlanPortLocalSegment")
)
if mibBuilder.loadTexts:
    vtpNotificationObjectsGroup.setStatus("current")

vtpDot1qTunnelGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 22)
)
vtpDot1qTunnelGroup2.setObjects(
    ("CISCO-VTP-MIB", "vlanTrunkPortsDot1qTag")
)
if mibBuilder.loadTexts:
    vtpDot1qTunnelGroup2.setStatus("deprecated")

vtpVlanNotifEnabledGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 24)
)
vtpVlanNotifEnabledGroup.setObjects(
      *(("CISCO-VTP-MIB", "vtpVlanCreatedNotifEnabled"),
        ("CISCO-VTP-MIB", "vtpVlanDeletedNotifEnabled"))
)
if mibBuilder.loadTexts:
    vtpVlanNotifEnabledGroup.setStatus("current")

vtpDiscoverGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 27)
)
vtpDiscoverGroup.setObjects(
      *(("CISCO-VTP-MIB", "vtpDiscoverAction"),
        ("CISCO-VTP-MIB", "vtpDiscoverStatus"),
        ("CISCO-VTP-MIB", "vtpLastDiscoverTime"),
        ("CISCO-VTP-MIB", "vtpDiscoverResultIndex"),
        ("CISCO-VTP-MIB", "vtpDiscoverResultDatabaseName"),
        ("CISCO-VTP-MIB", "vtpDiscoverResultConflicting"),
        ("CISCO-VTP-MIB", "vtpDiscoverResultDeviceId"),
        ("CISCO-VTP-MIB", "vtpDiscoverResultPrimaryServer"),
        ("CISCO-VTP-MIB", "vtpDiscoverResultRevNumber"),
        ("CISCO-VTP-MIB", "vtpDiscoverResultSystemName"))
)
if mibBuilder.loadTexts:
    vtpDiscoverGroup.setStatus("current")

vtpDatabaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 28)
)
vtpDatabaseGroup.setObjects(
      *(("CISCO-VTP-MIB", "vtpDatabaseName"),
        ("CISCO-VTP-MIB", "vtpDatabaseLocalMode"),
        ("CISCO-VTP-MIB", "vtpDatabaseRevNumber"),
        ("CISCO-VTP-MIB", "vtpDatabasePrimaryServer"),
        ("CISCO-VTP-MIB", "vtpDatabasePrimaryServerId"),
        ("CISCO-VTP-MIB", "vtpDatabaseTakeOverPrimary"),
        ("CISCO-VTP-MIB", "vtpDatabaseTakeOverPassword"))
)
if mibBuilder.loadTexts:
    vtpDatabaseGroup.setStatus("current")

vtpAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 29)
)
vtpAuthGroup.setObjects(
      *(("CISCO-VTP-MIB", "vtpAuthPassword"),
        ("CISCO-VTP-MIB", "vtpAuthPasswordType"),
        ("CISCO-VTP-MIB", "vtpAuthSecretKey"))
)
if mibBuilder.loadTexts:
    vtpAuthGroup.setStatus("current")

vtpInternalVlanGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 32)
)
vtpInternalVlanGrp.setObjects(
      *(("CISCO-VTP-MIB", "vtpInternalVlanAllocPolicy"),
        ("CISCO-VTP-MIB", "vtpInternalVlanOwner"))
)
if mibBuilder.loadTexts:
    vtpInternalVlanGrp.setStatus("current")

vlanStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 33)
)
vlanStatsGroup.setObjects(
      *(("CISCO-VTP-MIB", "vlanStatsVlans"),
        ("CISCO-VTP-MIB", "vlanStatsExtendedVlans"),
        ("CISCO-VTP-MIB", "vlanStatsInternalVlans"),
        ("CISCO-VTP-MIB", "vlanStatsFreeVlans"))
)
if mibBuilder.loadTexts:
    vlanStatsGroup.setStatus("current")

vtpTrunkPruningGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 36)
)
vtpTrunkPruningGroup3.setObjects(
    ("CISCO-VTP-MIB", "managementDomainPruningStateOper")
)
if mibBuilder.loadTexts:
    vtpTrunkPruningGroup3.setStatus("current")

vlanTrunkPortActiveVlansGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 38)
)
vlanTrunkPortActiveVlansGroup.setObjects(
      *(("CISCO-VTP-MIB", "vlanTrunkPortVlansActiveFirst2k"),
        ("CISCO-VTP-MIB", "vlanTrunkPortVlansActiveSecond2k"))
)
if mibBuilder.loadTexts:
    vlanTrunkPortActiveVlansGroup.setStatus("current")

vtpSourceInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 39)
)
vtpSourceInterfaceGroup.setObjects(
      *(("CISCO-VTP-MIB", "managementDomainAdminSrcIf"),
        ("CISCO-VTP-MIB", "managementDomainSourceOnlyMode"),
        ("CISCO-VTP-MIB", "managementDomainOperSrcIf"))
)
if mibBuilder.loadTexts:
    vtpSourceInterfaceGroup.setStatus("current")

vtpConfigFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 40)
)
vtpConfigFileGroup.setObjects(
    ("CISCO-VTP-MIB", "managementDomainConfigFile")
)
if mibBuilder.loadTexts:
    vtpConfigFileGroup.setStatus("current")

vtpVlanLocalShutdownGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 41)
)
vtpVlanLocalShutdownGroup.setObjects(
    ("CISCO-VTP-MIB", "vtpVlanLocalShutdown")
)
if mibBuilder.loadTexts:
    vtpVlanLocalShutdownGroup.setStatus("current")

vtpLocalUpdaterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 42)
)
vtpLocalUpdaterGroup.setObjects(
      *(("CISCO-VTP-MIB", "managementDomainLocalUpdaterType"),
        ("CISCO-VTP-MIB", "managementDomainLocalUpdater"))
)
if mibBuilder.loadTexts:
    vtpLocalUpdaterGroup.setStatus("current")

vtpDeviceIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 43)
)
vtpDeviceIdGroup.setObjects(
    ("CISCO-VTP-MIB", "managementDomainDeviceID")
)
if mibBuilder.loadTexts:
    vtpDeviceIdGroup.setStatus("current")


# Notification objects

vtpConfigRevNumberError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 1)
)
vtpConfigRevNumberError.setObjects(
    ("CISCO-VTP-MIB", "managementDomainConfigRevNumber")
)
if mibBuilder.loadTexts:
    vtpConfigRevNumberError.setStatus(
        "current"
    )

vtpConfigDigestError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 2)
)
vtpConfigDigestError.setObjects(
    ("CISCO-VTP-MIB", "managementDomainConfigRevNumber")
)
if mibBuilder.loadTexts:
    vtpConfigDigestError.setStatus(
        "current"
    )

vtpServerDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 3)
)
vtpServerDisabled.setObjects(
      *(("CISCO-VTP-MIB", "managementDomainConfigRevNumber"),
        ("CISCO-VTP-MIB", "vtpMaxVlanStorage"))
)
if mibBuilder.loadTexts:
    vtpServerDisabled.setStatus(
        "current"
    )

vtpMtuTooBig = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 4)
)
vtpMtuTooBig.setObjects(
      *(("CISCO-VTP-MIB", "vlanTrunkPortManagementDomain"),
        ("CISCO-VTP-MIB", "vtpVlanState"))
)
if mibBuilder.loadTexts:
    vtpMtuTooBig.setStatus(
        "current"
    )

vtpVersionOneDeviceDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 6)
)
vtpVersionOneDeviceDetected.setObjects(
    ("CISCO-VTP-MIB", "vlanTrunkPortManagementDomain")
)
if mibBuilder.loadTexts:
    vtpVersionOneDeviceDetected.setStatus(
        "current"
    )

vlanTrunkPortDynamicStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 7)
)
vlanTrunkPortDynamicStatusChange.setObjects(
    ("CISCO-VTP-MIB", "vlanTrunkPortDynamicStatus")
)
if mibBuilder.loadTexts:
    vlanTrunkPortDynamicStatusChange.setStatus(
        "current"
    )

vtpLocalModeChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 8)
)
vtpLocalModeChanged.setObjects(
    ("CISCO-VTP-MIB", "managementDomainLocalMode")
)
if mibBuilder.loadTexts:
    vtpLocalModeChanged.setStatus(
        "current"
    )

vtpVersionInUseChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 9)
)
vtpVersionInUseChanged.setObjects(
    ("CISCO-VTP-MIB", "managementDomainVersionInUse")
)
if mibBuilder.loadTexts:
    vtpVersionInUseChanged.setStatus(
        "current"
    )

vtpVlanCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 10)
)
vtpVlanCreated.setObjects(
    ("CISCO-VTP-MIB", "vtpVlanName")
)
if mibBuilder.loadTexts:
    vtpVlanCreated.setStatus(
        "current"
    )

vtpVlanDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 11)
)
vtpVlanDeleted.setObjects(
    ("CISCO-VTP-MIB", "vtpVlanName")
)
if mibBuilder.loadTexts:
    vtpVlanDeleted.setStatus(
        "current"
    )

vtpVlanRingNumberConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 12)
)
vtpVlanRingNumberConflict.setObjects(
      *(("CISCO-VTP-MIB", "vtpVlanRingNumber"),
        ("IF-MIB", "ifIndex"),
        ("CISCO-VTP-MIB", "vtpVlanPortLocalSegment"))
)
if mibBuilder.loadTexts:
    vtpVlanRingNumberConflict.setStatus(
        "current"
    )

vtpPruningStateOperChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 2, 0, 13)
)
vtpPruningStateOperChange.setObjects(
    ("CISCO-VTP-MIB", "managementDomainPruningStateOper")
)
if mibBuilder.loadTexts:
    vtpPruningStateOperChange.setStatus(
        "current"
    )


# Notifications groups

vtpConfigNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 6)
)
vtpConfigNotificationsGroup.setObjects(
      *(("CISCO-VTP-MIB", "vtpConfigDigestError"),
        ("CISCO-VTP-MIB", "vtpConfigRevNumberError"),
        ("CISCO-VTP-MIB", "vtpServerDisabled"),
        ("CISCO-VTP-MIB", "vtpMtuTooBig"),
        ("CISCO-VTP-MIB", "vtpVersionOneDeviceDetected"),
        ("CISCO-VTP-MIB", "vlanTrunkPortDynamicStatusChange"))
)
if mibBuilder.loadTexts:
    vtpConfigNotificationsGroup.setStatus(
        "deprecated"
    )

vtpConfigNotificationsGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 23)
)
vtpConfigNotificationsGroup2.setObjects(
      *(("CISCO-VTP-MIB", "vtpLocalModeChanged"),
        ("CISCO-VTP-MIB", "vtpVersionInUseChanged"))
)
if mibBuilder.loadTexts:
    vtpConfigNotificationsGroup2.setStatus(
        "current"
    )

vtpConfigNotificationsGroup3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 25)
)
vtpConfigNotificationsGroup3.setObjects(
      *(("CISCO-VTP-MIB", "vtpVlanCreated"),
        ("CISCO-VTP-MIB", "vtpVlanDeleted"))
)
if mibBuilder.loadTexts:
    vtpConfigNotificationsGroup3.setStatus(
        "current"
    )

vtpConfigNotificationsGroup4 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 26)
)
vtpConfigNotificationsGroup4.setObjects(
    ("CISCO-VTP-MIB", "vtpVlanRingNumberConflict")
)
if mibBuilder.loadTexts:
    vtpConfigNotificationsGroup4.setStatus(
        "current"
    )

vtpConfigNotificationsGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 30)
)
vtpConfigNotificationsGroupRev1.setObjects(
      *(("CISCO-VTP-MIB", "vtpConfigDigestError"),
        ("CISCO-VTP-MIB", "vtpConfigRevNumberError"),
        ("CISCO-VTP-MIB", "vtpVersionOneDeviceDetected"),
        ("CISCO-VTP-MIB", "vlanTrunkPortDynamicStatusChange"))
)
if mibBuilder.loadTexts:
    vtpConfigNotificationsGroupRev1.setStatus(
        "current"
    )

vtpConfigNotificationsGroup5 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 31)
)
vtpConfigNotificationsGroup5.setObjects(
      *(("CISCO-VTP-MIB", "vtpServerDisabled"),
        ("CISCO-VTP-MIB", "vtpMtuTooBig"))
)
if mibBuilder.loadTexts:
    vtpConfigNotificationsGroup5.setStatus(
        "deprecated"
    )

vtpConfigNotificationsGroup6 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 34)
)
vtpConfigNotificationsGroup6.setObjects(
    ("CISCO-VTP-MIB", "vtpServerDisabled")
)
if mibBuilder.loadTexts:
    vtpConfigNotificationsGroup6.setStatus(
        "current"
    )

vtpConfigNotificationsGroup7 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 35)
)
vtpConfigNotificationsGroup7.setObjects(
    ("CISCO-VTP-MIB", "vtpMtuTooBig")
)
if mibBuilder.loadTexts:
    vtpConfigNotificationsGroup7.setStatus(
        "current"
    )

vtpConfigNotificationsGroup8 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 2, 37)
)
vtpConfigNotificationsGroup8.setObjects(
    ("CISCO-VTP-MIB", "vtpPruningStateOperChange")
)
if mibBuilder.loadTexts:
    vtpConfigNotificationsGroup8.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vtpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 1)
)
if mibBuilder.loadTexts:
    vtpMIBCompliance.setStatus(
        "deprecated"
    )

vtpMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 2)
)
if mibBuilder.loadTexts:
    vtpMIBCompliance2.setStatus(
        "deprecated"
    )

vtpMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 3)
)
if mibBuilder.loadTexts:
    vtpMIBCompliance3.setStatus(
        "deprecated"
    )

vtpMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 4)
)
if mibBuilder.loadTexts:
    vtpMIBCompliance4.setStatus(
        "deprecated"
    )

vtpMIBCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 5)
)
if mibBuilder.loadTexts:
    vtpMIBCompliance5.setStatus(
        "deprecated"
    )

vtpMIBCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 6)
)
if mibBuilder.loadTexts:
    vtpMIBCompliance6.setStatus(
        "deprecated"
    )

vtpMIBCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 7)
)
if mibBuilder.loadTexts:
    vtpMIBCompliance7.setStatus(
        "deprecated"
    )

vtpMIBCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 8)
)
if mibBuilder.loadTexts:
    vtpMIBCompliance8.setStatus(
        "deprecated"
    )

vtpMIBCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 9)
)
if mibBuilder.loadTexts:
    vtpMIBCompliance9.setStatus(
        "deprecated"
    )

vtpMIBCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 10)
)
if mibBuilder.loadTexts:
    vtpMIBCompliance10.setStatus(
        "deprecated"
    )

vtpMIBCompliance11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 11)
)
if mibBuilder.loadTexts:
    vtpMIBCompliance11.setStatus(
        "deprecated"
    )

vtpMIBCompliance12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 12)
)
if mibBuilder.loadTexts:
    vtpMIBCompliance12.setStatus(
        "deprecated"
    )

vtpMIBCompliance13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 13)
)
if mibBuilder.loadTexts:
    vtpMIBCompliance13.setStatus(
        "deprecated"
    )

vtpMIBCompliance14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 14)
)
if mibBuilder.loadTexts:
    vtpMIBCompliance14.setStatus(
        "deprecated"
    )

vtpMIBCompliance15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 15)
)
if mibBuilder.loadTexts:
    vtpMIBCompliance15.setStatus(
        "deprecated"
    )

vtpMIBCompliance16 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 46, 3, 1, 16)
)
if mibBuilder.loadTexts:
    vtpMIBCompliance16.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VTP-MIB",
    **{"VlanIndex": VlanIndex,
       "ManagementDomainIndex": ManagementDomainIndex,
       "VlanType": VlanType,
       "VlanTypeExt": VlanTypeExt,
       "ciscoVtpMIB": ciscoVtpMIB,
       "vtpMIBObjects": vtpMIBObjects,
       "vtpStatus": vtpStatus,
       "vtpVersion": vtpVersion,
       "vtpMaxVlanStorage": vtpMaxVlanStorage,
       "vtpNotificationsEnabled": vtpNotificationsEnabled,
       "vtpVlanCreatedNotifEnabled": vtpVlanCreatedNotifEnabled,
       "vtpVlanDeletedNotifEnabled": vtpVlanDeletedNotifEnabled,
       "vlanManagementDomains": vlanManagementDomains,
       "managementDomainTable": managementDomainTable,
       "managementDomainEntry": managementDomainEntry,
       "managementDomainIndex": managementDomainIndex,
       "managementDomainName": managementDomainName,
       "managementDomainLocalMode": managementDomainLocalMode,
       "managementDomainConfigRevNumber": managementDomainConfigRevNumber,
       "managementDomainLastUpdater": managementDomainLastUpdater,
       "managementDomainLastChange": managementDomainLastChange,
       "managementDomainRowStatus": managementDomainRowStatus,
       "managementDomainTftpServer": managementDomainTftpServer,
       "managementDomainTftpPathname": managementDomainTftpPathname,
       "managementDomainPruningState": managementDomainPruningState,
       "managementDomainVersionInUse": managementDomainVersionInUse,
       "managementDomainPruningStateOper": managementDomainPruningStateOper,
       "managementDomainAdminSrcIf": managementDomainAdminSrcIf,
       "managementDomainSourceOnlyMode": managementDomainSourceOnlyMode,
       "managementDomainOperSrcIf": managementDomainOperSrcIf,
       "managementDomainConfigFile": managementDomainConfigFile,
       "managementDomainLocalUpdaterType": managementDomainLocalUpdaterType,
       "managementDomainLocalUpdater": managementDomainLocalUpdater,
       "managementDomainDeviceID": managementDomainDeviceID,
       "vlanInfo": vlanInfo,
       "vtpVlanTable": vtpVlanTable,
       "vtpVlanEntry": vtpVlanEntry,
       "vtpVlanIndex": vtpVlanIndex,
       "vtpVlanState": vtpVlanState,
       "vtpVlanType": vtpVlanType,
       "vtpVlanName": vtpVlanName,
       "vtpVlanMtu": vtpVlanMtu,
       "vtpVlanDot10Said": vtpVlanDot10Said,
       "vtpVlanRingNumber": vtpVlanRingNumber,
       "vtpVlanBridgeNumber": vtpVlanBridgeNumber,
       "vtpVlanStpType": vtpVlanStpType,
       "vtpVlanParentVlan": vtpVlanParentVlan,
       "vtpVlanTranslationalVlan1": vtpVlanTranslationalVlan1,
       "vtpVlanTranslationalVlan2": vtpVlanTranslationalVlan2,
       "vtpVlanBridgeType": vtpVlanBridgeType,
       "vtpVlanAreHopCount": vtpVlanAreHopCount,
       "vtpVlanSteHopCount": vtpVlanSteHopCount,
       "vtpVlanIsCRFBackup": vtpVlanIsCRFBackup,
       "vtpVlanTypeExt": vtpVlanTypeExt,
       "vtpVlanIfIndex": vtpVlanIfIndex,
       "internalVlanInfo": internalVlanInfo,
       "vtpInternalVlanAllocPolicy": vtpInternalVlanAllocPolicy,
       "vtpInternalVlanTable": vtpInternalVlanTable,
       "vtpInternalVlanEntry": vtpInternalVlanEntry,
       "vtpInternalVlanOwner": vtpInternalVlanOwner,
       "vlanEdit": vlanEdit,
       "vtpEditControlTable": vtpEditControlTable,
       "vtpEditControlEntry": vtpEditControlEntry,
       "vtpVlanEditOperation": vtpVlanEditOperation,
       "vtpVlanApplyStatus": vtpVlanApplyStatus,
       "vtpVlanEditBufferOwner": vtpVlanEditBufferOwner,
       "vtpVlanEditConfigRevNumber": vtpVlanEditConfigRevNumber,
       "vtpVlanEditModifiedVlan": vtpVlanEditModifiedVlan,
       "vtpVlanEditTable": vtpVlanEditTable,
       "vtpVlanEditEntry": vtpVlanEditEntry,
       "vtpVlanEditIndex": vtpVlanEditIndex,
       "vtpVlanEditState": vtpVlanEditState,
       "vtpVlanEditType": vtpVlanEditType,
       "vtpVlanEditName": vtpVlanEditName,
       "vtpVlanEditMtu": vtpVlanEditMtu,
       "vtpVlanEditDot10Said": vtpVlanEditDot10Said,
       "vtpVlanEditRingNumber": vtpVlanEditRingNumber,
       "vtpVlanEditBridgeNumber": vtpVlanEditBridgeNumber,
       "vtpVlanEditStpType": vtpVlanEditStpType,
       "vtpVlanEditParentVlan": vtpVlanEditParentVlan,
       "vtpVlanEditRowStatus": vtpVlanEditRowStatus,
       "vtpVlanEditTranslationalVlan1": vtpVlanEditTranslationalVlan1,
       "vtpVlanEditTranslationalVlan2": vtpVlanEditTranslationalVlan2,
       "vtpVlanEditBridgeType": vtpVlanEditBridgeType,
       "vtpVlanEditAreHopCount": vtpVlanEditAreHopCount,
       "vtpVlanEditSteHopCount": vtpVlanEditSteHopCount,
       "vtpVlanEditIsCRFBackup": vtpVlanEditIsCRFBackup,
       "vtpVlanEditTypeExt": vtpVlanEditTypeExt,
       "vtpVlanEditTypeExt2": vtpVlanEditTypeExt2,
       "vtpVlanLocalShutdownTable": vtpVlanLocalShutdownTable,
       "vtpVlanLocalShutdownEntry": vtpVlanLocalShutdownEntry,
       "vtpVlanLocalShutdown": vtpVlanLocalShutdown,
       "vtpStats": vtpStats,
       "vtpStatsTable": vtpStatsTable,
       "vtpStatsEntry": vtpStatsEntry,
       "vtpInSummaryAdverts": vtpInSummaryAdverts,
       "vtpInSubsetAdverts": vtpInSubsetAdverts,
       "vtpInAdvertRequests": vtpInAdvertRequests,
       "vtpOutSummaryAdverts": vtpOutSummaryAdverts,
       "vtpOutSubsetAdverts": vtpOutSubsetAdverts,
       "vtpOutAdvertRequests": vtpOutAdvertRequests,
       "vtpConfigRevNumberErrors": vtpConfigRevNumberErrors,
       "vtpConfigDigestErrors": vtpConfigDigestErrors,
       "vlanTrunkPorts": vlanTrunkPorts,
       "vlanTrunkPortTable": vlanTrunkPortTable,
       "vlanTrunkPortEntry": vlanTrunkPortEntry,
       "vlanTrunkPortIfIndex": vlanTrunkPortIfIndex,
       "vlanTrunkPortManagementDomain": vlanTrunkPortManagementDomain,
       "vlanTrunkPortEncapsulationType": vlanTrunkPortEncapsulationType,
       "vlanTrunkPortVlansEnabled": vlanTrunkPortVlansEnabled,
       "vlanTrunkPortNativeVlan": vlanTrunkPortNativeVlan,
       "vlanTrunkPortRowStatus": vlanTrunkPortRowStatus,
       "vlanTrunkPortInJoins": vlanTrunkPortInJoins,
       "vlanTrunkPortOutJoins": vlanTrunkPortOutJoins,
       "vlanTrunkPortOldAdverts": vlanTrunkPortOldAdverts,
       "vlanTrunkPortVlansPruningEligible": vlanTrunkPortVlansPruningEligible,
       "vlanTrunkPortVlansXmitJoined": vlanTrunkPortVlansXmitJoined,
       "vlanTrunkPortVlansRcvJoined": vlanTrunkPortVlansRcvJoined,
       "vlanTrunkPortDynamicState": vlanTrunkPortDynamicState,
       "vlanTrunkPortDynamicStatus": vlanTrunkPortDynamicStatus,
       "vlanTrunkPortVtpEnabled": vlanTrunkPortVtpEnabled,
       "vlanTrunkPortEncapsulationOperType": vlanTrunkPortEncapsulationOperType,
       "vlanTrunkPortVlansEnabled2k": vlanTrunkPortVlansEnabled2k,
       "vlanTrunkPortVlansEnabled3k": vlanTrunkPortVlansEnabled3k,
       "vlanTrunkPortVlansEnabled4k": vlanTrunkPortVlansEnabled4k,
       "vtpVlansPruningEligible2k": vtpVlansPruningEligible2k,
       "vtpVlansPruningEligible3k": vtpVlansPruningEligible3k,
       "vtpVlansPruningEligible4k": vtpVlansPruningEligible4k,
       "vlanTrunkPortVlansXmitJoined2k": vlanTrunkPortVlansXmitJoined2k,
       "vlanTrunkPortVlansXmitJoined3k": vlanTrunkPortVlansXmitJoined3k,
       "vlanTrunkPortVlansXmitJoined4k": vlanTrunkPortVlansXmitJoined4k,
       "vlanTrunkPortVlansRcvJoined2k": vlanTrunkPortVlansRcvJoined2k,
       "vlanTrunkPortVlansRcvJoined3k": vlanTrunkPortVlansRcvJoined3k,
       "vlanTrunkPortVlansRcvJoined4k": vlanTrunkPortVlansRcvJoined4k,
       "vlanTrunkPortDot1qTunnel": vlanTrunkPortDot1qTunnel,
       "vlanTrunkPortVlansActiveFirst2k": vlanTrunkPortVlansActiveFirst2k,
       "vlanTrunkPortVlansActiveSecond2k": vlanTrunkPortVlansActiveSecond2k,
       "vlanTrunkPortSetSerialNo": vlanTrunkPortSetSerialNo,
       "vlanTrunkPortsDot1qTag": vlanTrunkPortsDot1qTag,
       "vtpDiscover": vtpDiscover,
       "vtpDiscoverTable": vtpDiscoverTable,
       "vtpDiscoverEntry": vtpDiscoverEntry,
       "vtpDiscoverAction": vtpDiscoverAction,
       "vtpDiscoverStatus": vtpDiscoverStatus,
       "vtpLastDiscoverTime": vtpLastDiscoverTime,
       "vtpDiscoverResultTable": vtpDiscoverResultTable,
       "vtpDiscoverResultEntry": vtpDiscoverResultEntry,
       "vtpDiscoverResultIndex": vtpDiscoverResultIndex,
       "vtpDiscoverResultDatabaseName": vtpDiscoverResultDatabaseName,
       "vtpDiscoverResultConflicting": vtpDiscoverResultConflicting,
       "vtpDiscoverResultDeviceId": vtpDiscoverResultDeviceId,
       "vtpDiscoverResultPrimaryServer": vtpDiscoverResultPrimaryServer,
       "vtpDiscoverResultRevNumber": vtpDiscoverResultRevNumber,
       "vtpDiscoverResultSystemName": vtpDiscoverResultSystemName,
       "vtpDatabase": vtpDatabase,
       "vtpDatabaseTable": vtpDatabaseTable,
       "vtpDatabaseEntry": vtpDatabaseEntry,
       "vtpDatabaseIndex": vtpDatabaseIndex,
       "vtpDatabaseName": vtpDatabaseName,
       "vtpDatabaseLocalMode": vtpDatabaseLocalMode,
       "vtpDatabaseRevNumber": vtpDatabaseRevNumber,
       "vtpDatabasePrimaryServer": vtpDatabasePrimaryServer,
       "vtpDatabasePrimaryServerId": vtpDatabasePrimaryServerId,
       "vtpDatabaseTakeOverPrimary": vtpDatabaseTakeOverPrimary,
       "vtpDatabaseTakeOverPassword": vtpDatabaseTakeOverPassword,
       "vtpAuthentication": vtpAuthentication,
       "vtpAuthenticationTable": vtpAuthenticationTable,
       "vtpAuthEntry": vtpAuthEntry,
       "vtpAuthPassword": vtpAuthPassword,
       "vtpAuthPasswordType": vtpAuthPasswordType,
       "vtpAuthSecretKey": vtpAuthSecretKey,
       "vlanStatistics": vlanStatistics,
       "vlanStatsVlans": vlanStatsVlans,
       "vlanStatsExtendedVlans": vlanStatsExtendedVlans,
       "vlanStatsInternalVlans": vlanStatsInternalVlans,
       "vlanStatsFreeVlans": vlanStatsFreeVlans,
       "vtpNotifications": vtpNotifications,
       "vtpNotificationsPrefix": vtpNotificationsPrefix,
       "vtpConfigRevNumberError": vtpConfigRevNumberError,
       "vtpConfigDigestError": vtpConfigDigestError,
       "vtpServerDisabled": vtpServerDisabled,
       "vtpMtuTooBig": vtpMtuTooBig,
       "vtpVersionOneDeviceDetected": vtpVersionOneDeviceDetected,
       "vlanTrunkPortDynamicStatusChange": vlanTrunkPortDynamicStatusChange,
       "vtpLocalModeChanged": vtpLocalModeChanged,
       "vtpVersionInUseChanged": vtpVersionInUseChanged,
       "vtpVlanCreated": vtpVlanCreated,
       "vtpVlanDeleted": vtpVlanDeleted,
       "vtpVlanRingNumberConflict": vtpVlanRingNumberConflict,
       "vtpPruningStateOperChange": vtpPruningStateOperChange,
       "vtpNotificationsObjects": vtpNotificationsObjects,
       "vtpVlanPortLocalSegment": vtpVlanPortLocalSegment,
       "vtpMIBConformance": vtpMIBConformance,
       "vtpMIBCompliances": vtpMIBCompliances,
       "vtpMIBCompliance": vtpMIBCompliance,
       "vtpMIBCompliance2": vtpMIBCompliance2,
       "vtpMIBCompliance3": vtpMIBCompliance3,
       "vtpMIBCompliance4": vtpMIBCompliance4,
       "vtpMIBCompliance5": vtpMIBCompliance5,
       "vtpMIBCompliance6": vtpMIBCompliance6,
       "vtpMIBCompliance7": vtpMIBCompliance7,
       "vtpMIBCompliance8": vtpMIBCompliance8,
       "vtpMIBCompliance9": vtpMIBCompliance9,
       "vtpMIBCompliance10": vtpMIBCompliance10,
       "vtpMIBCompliance11": vtpMIBCompliance11,
       "vtpMIBCompliance12": vtpMIBCompliance12,
       "vtpMIBCompliance13": vtpMIBCompliance13,
       "vtpMIBCompliance14": vtpMIBCompliance14,
       "vtpMIBCompliance15": vtpMIBCompliance15,
       "vtpMIBCompliance16": vtpMIBCompliance16,
       "vtpMIBGroups": vtpMIBGroups,
       "vtpBasicGroup": vtpBasicGroup,
       "vtpStatsGroup": vtpStatsGroup,
       "vtpTrunkPortGroup": vtpTrunkPortGroup,
       "vtpConfigNotificationsGroup": vtpConfigNotificationsGroup,
       "vtpTrunkPruningGroup": vtpTrunkPruningGroup,
       "vtpTrunkPruningGroup2": vtpTrunkPruningGroup2,
       "vtpTrunkPortGroup2": vtpTrunkPortGroup2,
       "vtpVersion2BasicGroup": vtpVersion2BasicGroup,
       "vtpVlanInfoGroup": vtpVlanInfoGroup,
       "vtpVlanInfoEditGroup": vtpVlanInfoEditGroup,
       "vtpTrunkPortGroup3": vtpTrunkPortGroup3,
       "vtp4kVlanGroup": vtp4kVlanGroup,
       "vtpDot1qTunnelGroup": vtpDot1qTunnelGroup,
       "vtpVlanIfIndexGroup": vtpVlanIfIndexGroup,
       "vtpVlanInfoEditGroup2": vtpVlanInfoEditGroup2,
       "vtp4kVlanGroupRev1": vtp4kVlanGroupRev1,
       "vtpNotificationObjectsGroup": vtpNotificationObjectsGroup,
       "vtpDot1qTunnelGroup2": vtpDot1qTunnelGroup2,
       "vtpConfigNotificationsGroup2": vtpConfigNotificationsGroup2,
       "vtpVlanNotifEnabledGroup": vtpVlanNotifEnabledGroup,
       "vtpConfigNotificationsGroup3": vtpConfigNotificationsGroup3,
       "vtpConfigNotificationsGroup4": vtpConfigNotificationsGroup4,
       "vtpDiscoverGroup": vtpDiscoverGroup,
       "vtpDatabaseGroup": vtpDatabaseGroup,
       "vtpAuthGroup": vtpAuthGroup,
       "vtpConfigNotificationsGroupRev1": vtpConfigNotificationsGroupRev1,
       "vtpConfigNotificationsGroup5": vtpConfigNotificationsGroup5,
       "vtpInternalVlanGrp": vtpInternalVlanGrp,
       "vlanStatsGroup": vlanStatsGroup,
       "vtpConfigNotificationsGroup6": vtpConfigNotificationsGroup6,
       "vtpConfigNotificationsGroup7": vtpConfigNotificationsGroup7,
       "vtpTrunkPruningGroup3": vtpTrunkPruningGroup3,
       "vtpConfigNotificationsGroup8": vtpConfigNotificationsGroup8,
       "vlanTrunkPortActiveVlansGroup": vlanTrunkPortActiveVlansGroup,
       "vtpSourceInterfaceGroup": vtpSourceInterfaceGroup,
       "vtpConfigFileGroup": vtpConfigFileGroup,
       "vtpVlanLocalShutdownGroup": vtpVlanLocalShutdownGroup,
       "vtpLocalUpdaterGroup": vtpLocalUpdaterGroup,
       "vtpDeviceIdGroup": vtpDeviceIdGroup}
)
