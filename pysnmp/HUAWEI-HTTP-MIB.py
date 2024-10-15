# SNMP MIB module (HUAWEI-HTTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-HTTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:57 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwHttpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 192)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwHttpObjects_ObjectIdentity = ObjectIdentity
hwHttpObjects = _HwHttpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 192, 1)
)
_HwHttpConfiguration_ObjectIdentity = ObjectIdentity
hwHttpConfiguration = _HwHttpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 192, 1, 1)
)


class _HwHttpEnable_Type(EnabledStatus):
    """Custom type hwHttpEnable based on EnabledStatus"""
    defaultValue = 1

    subtypeSpec = EnabledStatus.subtypeSpec
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


_HwHttpEnable_Type.__name__ = "EnabledStatus"
_HwHttpEnable_Object = MibScalar
hwHttpEnable = _HwHttpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 192, 1, 1, 1),
    _HwHttpEnable_Type()
)
hwHttpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwHttpEnable.setStatus("current")


class _HwHttpPortNum_Type(Integer32):
    """Custom type hwHttpPortNum based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 80),
        ValueRangeConstraint(1025, 55535),
    )


_HwHttpPortNum_Type.__name__ = "Integer32"
_HwHttpPortNum_Object = MibScalar
hwHttpPortNum = _HwHttpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 192, 1, 1, 2),
    _HwHttpPortNum_Type()
)
hwHttpPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwHttpPortNum.setStatus("current")


class _HwHttpAclNum_Type(Integer32):
    """Custom type hwHttpAclNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2999),
    )


_HwHttpAclNum_Type.__name__ = "Integer32"
_HwHttpAclNum_Object = MibScalar
hwHttpAclNum = _HwHttpAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 192, 1, 1, 3),
    _HwHttpAclNum_Type()
)
hwHttpAclNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwHttpAclNum.setStatus("current")


class _HwHttpTimeOut_Type(Integer32):
    """Custom type hwHttpTimeOut based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 35791),
    )


_HwHttpTimeOut_Type.__name__ = "Integer32"
_HwHttpTimeOut_Object = MibScalar
hwHttpTimeOut = _HwHttpTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 192, 1, 1, 4),
    _HwHttpTimeOut_Type()
)
hwHttpTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwHttpTimeOut.setStatus("current")


class _HwHttpOnlineUserNum_Type(Integer32):
    """Custom type hwHttpOnlineUserNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_HwHttpOnlineUserNum_Type.__name__ = "Integer32"
_HwHttpOnlineUserNum_Object = MibScalar
hwHttpOnlineUserNum = _HwHttpOnlineUserNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 192, 1, 1, 5),
    _HwHttpOnlineUserNum_Type()
)
hwHttpOnlineUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwHttpOnlineUserNum.setStatus("current")
_HwHttpMaxUserNum_Type = Integer32
_HwHttpMaxUserNum_Object = MibScalar
hwHttpMaxUserNum = _HwHttpMaxUserNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 192, 1, 1, 6),
    _HwHttpMaxUserNum_Type()
)
hwHttpMaxUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwHttpMaxUserNum.setStatus("current")
_HwHttpUserInfoTable_Object = MibTable
hwHttpUserInfoTable = _HwHttpUserInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 192, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hwHttpUserInfoTable.setStatus("current")
_HwHttpUserInfoEntry_Object = MibTableRow
hwHttpUserInfoEntry = _HwHttpUserInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 192, 1, 1, 7, 1)
)
hwHttpUserInfoEntry.setIndexNames(
    (0, "HUAWEI-HTTP-MIB", "hwHttpUserIndex"),
)
if mibBuilder.loadTexts:
    hwHttpUserInfoEntry.setStatus("current")


class _HwHttpUserIndex_Type(Integer32):
    """Custom type hwHttpUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HwHttpUserIndex_Type.__name__ = "Integer32"
_HwHttpUserIndex_Object = MibTableColumn
hwHttpUserIndex = _HwHttpUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 192, 1, 1, 7, 1, 1),
    _HwHttpUserIndex_Type()
)
hwHttpUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwHttpUserIndex.setStatus("current")


class _HwHttpUserName_Type(OctetString):
    """Custom type hwHttpUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwHttpUserName_Type.__name__ = "OctetString"
_HwHttpUserName_Object = MibTableColumn
hwHttpUserName = _HwHttpUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 192, 1, 1, 7, 1, 2),
    _HwHttpUserName_Type()
)
hwHttpUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwHttpUserName.setStatus("current")
_HwHttpUserIpAddr_Type = IpAddress
_HwHttpUserIpAddr_Object = MibTableColumn
hwHttpUserIpAddr = _HwHttpUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 192, 1, 1, 7, 1, 3),
    _HwHttpUserIpAddr_Type()
)
hwHttpUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwHttpUserIpAddr.setStatus("current")
_HwHttpUserLoginTime_Type = DateAndTime
_HwHttpUserLoginTime_Object = MibTableColumn
hwHttpUserLoginTime = _HwHttpUserLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 192, 1, 1, 7, 1, 4),
    _HwHttpUserLoginTime_Type()
)
hwHttpUserLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwHttpUserLoginTime.setStatus("current")
_HwHttpUserTimeOut_Type = Integer32
_HwHttpUserTimeOut_Object = MibTableColumn
hwHttpUserTimeOut = _HwHttpUserTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 192, 1, 1, 7, 1, 5),
    _HwHttpUserTimeOut_Type()
)
hwHttpUserTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwHttpUserTimeOut.setStatus("current")
_HwHttpConformance_ObjectIdentity = ObjectIdentity
hwHttpConformance = _HwHttpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 192, 2)
)
_HwHttpCompliances_ObjectIdentity = ObjectIdentity
hwHttpCompliances = _HwHttpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 192, 2, 1)
)
_HwHttpGroups_ObjectIdentity = ObjectIdentity
hwHttpGroups = _HwHttpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 192, 2, 2)
)

# Managed Objects groups

hwHttpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 192, 2, 2, 1)
)
hwHttpConfigGroup.setObjects(
      *(("HUAWEI-HTTP-MIB", "hwHttpEnable"),
        ("HUAWEI-HTTP-MIB", "hwHttpPortNum"),
        ("HUAWEI-HTTP-MIB", "hwHttpAclNum"),
        ("HUAWEI-HTTP-MIB", "hwHttpTimeOut"))
)
if mibBuilder.loadTexts:
    hwHttpConfigGroup.setStatus("current")

hwHttpInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 192, 2, 2, 2)
)
hwHttpInfoGroup.setObjects(
      *(("HUAWEI-HTTP-MIB", "hwHttpOnlineUserNum"),
        ("HUAWEI-HTTP-MIB", "hwHttpMaxUserNum"),
        ("HUAWEI-HTTP-MIB", "hwHttpUserName"),
        ("HUAWEI-HTTP-MIB", "hwHttpUserIpAddr"),
        ("HUAWEI-HTTP-MIB", "hwHttpUserLoginTime"),
        ("HUAWEI-HTTP-MIB", "hwHttpUserTimeOut"))
)
if mibBuilder.loadTexts:
    hwHttpInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwHttpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 192, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwHttpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-HTTP-MIB",
    **{"hwHttpMIB": hwHttpMIB,
       "hwHttpObjects": hwHttpObjects,
       "hwHttpConfiguration": hwHttpConfiguration,
       "hwHttpEnable": hwHttpEnable,
       "hwHttpPortNum": hwHttpPortNum,
       "hwHttpAclNum": hwHttpAclNum,
       "hwHttpTimeOut": hwHttpTimeOut,
       "hwHttpOnlineUserNum": hwHttpOnlineUserNum,
       "hwHttpMaxUserNum": hwHttpMaxUserNum,
       "hwHttpUserInfoTable": hwHttpUserInfoTable,
       "hwHttpUserInfoEntry": hwHttpUserInfoEntry,
       "hwHttpUserIndex": hwHttpUserIndex,
       "hwHttpUserName": hwHttpUserName,
       "hwHttpUserIpAddr": hwHttpUserIpAddr,
       "hwHttpUserLoginTime": hwHttpUserLoginTime,
       "hwHttpUserTimeOut": hwHttpUserTimeOut,
       "hwHttpConformance": hwHttpConformance,
       "hwHttpCompliances": hwHttpCompliances,
       "hwHttpCompliance": hwHttpCompliance,
       "hwHttpGroups": hwHttpGroups,
       "hwHttpConfigGroup": hwHttpConfigGroup,
       "hwHttpInfoGroup": hwHttpInfoGroup}
)
