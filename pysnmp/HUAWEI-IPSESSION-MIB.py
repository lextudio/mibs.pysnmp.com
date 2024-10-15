# SNMP MIB module (HUAWEI-IPSESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-IPSESSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:10 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwIpSessionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwIpSessionMibObjects_ObjectIdentity = ObjectIdentity
hwIpSessionMibObjects = _HwIpSessionMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1)
)
_HwIpSessIfCfgTable_Object = MibTable
hwIpSessIfCfgTable = _HwIpSessIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1)
)
if mibBuilder.loadTexts:
    hwIpSessIfCfgTable.setStatus("current")
_HwIpSessIfCfgEntry_Object = MibTableRow
hwIpSessIfCfgEntry = _HwIpSessIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1, 1)
)
hwIpSessIfCfgEntry.setIndexNames(
    (0, "HUAWEI-IPSESSION-MIB", "hwIpSessIfCfgIfIndex"),
)
if mibBuilder.loadTexts:
    hwIpSessIfCfgEntry.setStatus("current")
_HwIpSessIfCfgIfIndex_Type = InterfaceIndex
_HwIpSessIfCfgIfIndex_Object = MibTableColumn
hwIpSessIfCfgIfIndex = _HwIpSessIfCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1, 1, 1),
    _HwIpSessIfCfgIfIndex_Type()
)
hwIpSessIfCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIpSessIfCfgIfIndex.setStatus("current")


class _HwIpSessIfCfgAuthDomain_Type(DisplayString):
    """Custom type hwIpSessIfCfgAuthDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwIpSessIfCfgAuthDomain_Type.__name__ = "DisplayString"
_HwIpSessIfCfgAuthDomain_Object = MibTableColumn
hwIpSessIfCfgAuthDomain = _HwIpSessIfCfgAuthDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1, 1, 11),
    _HwIpSessIfCfgAuthDomain_Type()
)
hwIpSessIfCfgAuthDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpSessIfCfgAuthDomain.setStatus("current")


class _HwIpSessIfCfgNasPortType_Type(Integer32):
    """Custom type hwIpSessIfCfgNasPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_HwIpSessIfCfgNasPortType_Type.__name__ = "Integer32"
_HwIpSessIfCfgNasPortType_Object = MibTableColumn
hwIpSessIfCfgNasPortType = _HwIpSessIfCfgNasPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1, 1, 12),
    _HwIpSessIfCfgNasPortType_Type()
)
hwIpSessIfCfgNasPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpSessIfCfgNasPortType.setStatus("current")


class _HwIpSessIfCfgArpInterval_Type(Integer32):
    """Custom type hwIpSessIfCfgArpInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 121),
    )


_HwIpSessIfCfgArpInterval_Type.__name__ = "Integer32"
_HwIpSessIfCfgArpInterval_Object = MibTableColumn
hwIpSessIfCfgArpInterval = _HwIpSessIfCfgArpInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1, 1, 13),
    _HwIpSessIfCfgArpInterval_Type()
)
hwIpSessIfCfgArpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpSessIfCfgArpInterval.setStatus("current")


class _HwIpSessIfCfgArpFailTimes_Type(Integer32):
    """Custom type hwIpSessIfCfgArpFailTimes based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 11),
    )


_HwIpSessIfCfgArpFailTimes_Type.__name__ = "Integer32"
_HwIpSessIfCfgArpFailTimes_Object = MibTableColumn
hwIpSessIfCfgArpFailTimes = _HwIpSessIfCfgArpFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1, 1, 14),
    _HwIpSessIfCfgArpFailTimes_Type()
)
hwIpSessIfCfgArpFailTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpSessIfCfgArpFailTimes.setStatus("current")


class _HwIpSessIfCfgOption82Policy_Type(Integer32):
    """Custom type hwIpSessIfCfgOption82Policy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("insert", 2),
          ("none", 1),
          ("replace", 3))
    )


_HwIpSessIfCfgOption82Policy_Type.__name__ = "Integer32"
_HwIpSessIfCfgOption82Policy_Object = MibTableColumn
hwIpSessIfCfgOption82Policy = _HwIpSessIfCfgOption82Policy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1, 1, 15),
    _HwIpSessIfCfgOption82Policy_Type()
)
hwIpSessIfCfgOption82Policy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpSessIfCfgOption82Policy.setStatus("current")


class _HwIpSessIfCfgServicePolicy_Type(Integer32):
    """Custom type hwIpSessIfCfgServicePolicy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("option60", 2))
    )


_HwIpSessIfCfgServicePolicy_Type.__name__ = "Integer32"
_HwIpSessIfCfgServicePolicy_Object = MibTableColumn
hwIpSessIfCfgServicePolicy = _HwIpSessIfCfgServicePolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1, 1, 16),
    _HwIpSessIfCfgServicePolicy_Type()
)
hwIpSessIfCfgServicePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpSessIfCfgServicePolicy.setStatus("current")


class _HwIpSessIfCfgVpn_Type(DisplayString):
    """Custom type hwIpSessIfCfgVpn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwIpSessIfCfgVpn_Type.__name__ = "DisplayString"
_HwIpSessIfCfgVpn_Object = MibTableColumn
hwIpSessIfCfgVpn = _HwIpSessIfCfgVpn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1, 1, 17),
    _HwIpSessIfCfgVpn_Type()
)
hwIpSessIfCfgVpn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpSessIfCfgVpn.setStatus("current")


class _HwIpSessIfCfgIpSessionEnable_Type(EnabledStatus):
    """Custom type hwIpSessIfCfgIpSessionEnable based on EnabledStatus"""


_HwIpSessIfCfgIpSessionEnable_Object = MibTableColumn
hwIpSessIfCfgIpSessionEnable = _HwIpSessIfCfgIpSessionEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1, 1, 18),
    _HwIpSessIfCfgIpSessionEnable_Type()
)
hwIpSessIfCfgIpSessionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpSessIfCfgIpSessionEnable.setStatus("current")
_HwIpSessIfCfgRowStatus_Type = RowStatus
_HwIpSessIfCfgRowStatus_Object = MibTableColumn
hwIpSessIfCfgRowStatus = _HwIpSessIfCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 1, 1, 51),
    _HwIpSessIfCfgRowStatus_Type()
)
hwIpSessIfCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIpSessIfCfgRowStatus.setStatus("current")
_HwIpSessUserCfgTable_ObjectIdentity = ObjectIdentity
hwIpSessUserCfgTable = _HwIpSessUserCfgTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 2)
)


class _HwIpSessUserPasswordType_Type(Integer32):
    """Custom type hwIpSessUserPasswordType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cipher", 2),
          ("simple", 1))
    )


_HwIpSessUserPasswordType_Type.__name__ = "Integer32"
_HwIpSessUserPasswordType_Object = MibScalar
hwIpSessUserPasswordType = _HwIpSessUserPasswordType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 2, 11),
    _HwIpSessUserPasswordType_Type()
)
hwIpSessUserPasswordType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpSessUserPasswordType.setStatus("current")


class _HwIpSessUserPassword_Type(DisplayString):
    """Custom type hwIpSessUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwIpSessUserPassword_Type.__name__ = "DisplayString"
_HwIpSessUserPassword_Object = MibScalar
hwIpSessUserPassword = _HwIpSessUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 2, 12),
    _HwIpSessUserPassword_Type()
)
hwIpSessUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpSessUserPassword.setStatus("current")


class _HwIpSessUserNameOption82_Type(Integer32):
    """Custom type hwIpSessUserNameOption82 based on Integer32"""
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
        *(("first", 2),
          ("fourth", 5),
          ("none", 1),
          ("second", 3),
          ("third", 4))
    )


_HwIpSessUserNameOption82_Type.__name__ = "Integer32"
_HwIpSessUserNameOption82_Object = MibScalar
hwIpSessUserNameOption82 = _HwIpSessUserNameOption82_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 2, 13),
    _HwIpSessUserNameOption82_Type()
)
hwIpSessUserNameOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpSessUserNameOption82.setStatus("current")


class _HwIpSessUserNameIP_Type(Integer32):
    """Custom type hwIpSessUserNameIP based on Integer32"""
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
        *(("first", 2),
          ("fourth", 5),
          ("none", 1),
          ("second", 3),
          ("third", 4))
    )


_HwIpSessUserNameIP_Type.__name__ = "Integer32"
_HwIpSessUserNameIP_Object = MibScalar
hwIpSessUserNameIP = _HwIpSessUserNameIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 2, 14),
    _HwIpSessUserNameIP_Type()
)
hwIpSessUserNameIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpSessUserNameIP.setStatus("current")


class _HwIpSessUserNameSysName_Type(Integer32):
    """Custom type hwIpSessUserNameSysName based on Integer32"""
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
        *(("first", 2),
          ("fourth", 5),
          ("none", 1),
          ("second", 3),
          ("third", 4))
    )


_HwIpSessUserNameSysName_Type.__name__ = "Integer32"
_HwIpSessUserNameSysName_Object = MibScalar
hwIpSessUserNameSysName = _HwIpSessUserNameSysName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 2, 15),
    _HwIpSessUserNameSysName_Type()
)
hwIpSessUserNameSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpSessUserNameSysName.setStatus("current")


class _HwIpSessUserNameMac_Type(Integer32):
    """Custom type hwIpSessUserNameMac based on Integer32"""
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
        *(("first", 2),
          ("fourth", 5),
          ("none", 1),
          ("second", 3),
          ("third", 4))
    )


_HwIpSessUserNameMac_Type.__name__ = "Integer32"
_HwIpSessUserNameMac_Object = MibScalar
hwIpSessUserNameMac = _HwIpSessUserNameMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 1, 2, 16),
    _HwIpSessUserNameMac_Type()
)
hwIpSessUserNameMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIpSessUserNameMac.setStatus("current")
_HwIpSessionConformance_ObjectIdentity = ObjectIdentity
hwIpSessionConformance = _HwIpSessionConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 3)
)
_HwIpSessionCompliances_ObjectIdentity = ObjectIdentity
hwIpSessionCompliances = _HwIpSessionCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 3, 1)
)
_HwIpSessionGroups_ObjectIdentity = ObjectIdentity
hwIpSessionGroups = _HwIpSessionGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 3, 2)
)

# Managed Objects groups

hwIpSessIfCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 3, 2, 1)
)
hwIpSessIfCfgGroup.setObjects(
      *(("HUAWEI-IPSESSION-MIB", "hwIpSessIfCfgAuthDomain"),
        ("HUAWEI-IPSESSION-MIB", "hwIpSessIfCfgNasPortType"),
        ("HUAWEI-IPSESSION-MIB", "hwIpSessIfCfgArpInterval"),
        ("HUAWEI-IPSESSION-MIB", "hwIpSessIfCfgArpFailTimes"),
        ("HUAWEI-IPSESSION-MIB", "hwIpSessIfCfgOption82Policy"),
        ("HUAWEI-IPSESSION-MIB", "hwIpSessIfCfgServicePolicy"),
        ("HUAWEI-IPSESSION-MIB", "hwIpSessIfCfgVpn"),
        ("HUAWEI-IPSESSION-MIB", "hwIpSessIfCfgIpSessionEnable"),
        ("HUAWEI-IPSESSION-MIB", "hwIpSessIfCfgRowStatus"))
)
if mibBuilder.loadTexts:
    hwIpSessIfCfgGroup.setStatus("current")

hwIpSessUserCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 3, 2, 2)
)
hwIpSessUserCfgGroup.setObjects(
      *(("HUAWEI-IPSESSION-MIB", "hwIpSessUserPasswordType"),
        ("HUAWEI-IPSESSION-MIB", "hwIpSessUserPassword"),
        ("HUAWEI-IPSESSION-MIB", "hwIpSessUserNameOption82"),
        ("HUAWEI-IPSESSION-MIB", "hwIpSessUserNameIP"),
        ("HUAWEI-IPSESSION-MIB", "hwIpSessUserNameSysName"),
        ("HUAWEI-IPSESSION-MIB", "hwIpSessUserNameMac"))
)
if mibBuilder.loadTexts:
    hwIpSessUserCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwIpSessionCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 184, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwIpSessionCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-IPSESSION-MIB",
    **{"hwIpSessionMIB": hwIpSessionMIB,
       "hwIpSessionMibObjects": hwIpSessionMibObjects,
       "hwIpSessIfCfgTable": hwIpSessIfCfgTable,
       "hwIpSessIfCfgEntry": hwIpSessIfCfgEntry,
       "hwIpSessIfCfgIfIndex": hwIpSessIfCfgIfIndex,
       "hwIpSessIfCfgAuthDomain": hwIpSessIfCfgAuthDomain,
       "hwIpSessIfCfgNasPortType": hwIpSessIfCfgNasPortType,
       "hwIpSessIfCfgArpInterval": hwIpSessIfCfgArpInterval,
       "hwIpSessIfCfgArpFailTimes": hwIpSessIfCfgArpFailTimes,
       "hwIpSessIfCfgOption82Policy": hwIpSessIfCfgOption82Policy,
       "hwIpSessIfCfgServicePolicy": hwIpSessIfCfgServicePolicy,
       "hwIpSessIfCfgVpn": hwIpSessIfCfgVpn,
       "hwIpSessIfCfgIpSessionEnable": hwIpSessIfCfgIpSessionEnable,
       "hwIpSessIfCfgRowStatus": hwIpSessIfCfgRowStatus,
       "hwIpSessUserCfgTable": hwIpSessUserCfgTable,
       "hwIpSessUserPasswordType": hwIpSessUserPasswordType,
       "hwIpSessUserPassword": hwIpSessUserPassword,
       "hwIpSessUserNameOption82": hwIpSessUserNameOption82,
       "hwIpSessUserNameIP": hwIpSessUserNameIP,
       "hwIpSessUserNameSysName": hwIpSessUserNameSysName,
       "hwIpSessUserNameMac": hwIpSessUserNameMac,
       "hwIpSessionConformance": hwIpSessionConformance,
       "hwIpSessionCompliances": hwIpSessionCompliances,
       "hwIpSessionCompliance": hwIpSessionCompliance,
       "hwIpSessionGroups": hwIpSessionGroups,
       "hwIpSessIfCfgGroup": hwIpSessIfCfgGroup,
       "hwIpSessUserCfgGroup": hwIpSessUserCfgGroup}
)
