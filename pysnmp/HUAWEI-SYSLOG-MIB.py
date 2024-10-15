# SNMP MIB module (HUAWEI-SYSLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-SYSLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:07 2024
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

(huaweiUtility,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "huaweiUtility")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

syslogMIBObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SyslogEnableAdminStatus_Type = Integer32
_SyslogEnableAdminStatus_Object = MibScalar
syslogEnableAdminStatus = _SyslogEnableAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 1),
    _SyslogEnableAdminStatus_Type()
)
syslogEnableAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogEnableAdminStatus.setStatus("current")
_SyslogServerTable_Object = MibTable
syslogServerTable = _SyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 2)
)
if mibBuilder.loadTexts:
    syslogServerTable.setStatus("current")
_SyslogServerEntry_Object = MibTableRow
syslogServerEntry = _SyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 2, 1)
)
syslogServerEntry.setIndexNames(
    (0, "HUAWEI-SYSLOG-MIB", "syslogServerIpAddress"),
)
if mibBuilder.loadTexts:
    syslogServerEntry.setStatus("current")
_SyslogServerIpAddress_Type = Integer32
_SyslogServerIpAddress_Object = MibTableColumn
syslogServerIpAddress = _SyslogServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 2, 1, 1),
    _SyslogServerIpAddress_Type()
)
syslogServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServerIpAddress.setStatus("current")


class _SyslogPolicyGroupNameSelect_Type(OctetString):
    """Custom type syslogPolicyGroupNameSelect based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SyslogPolicyGroupNameSelect_Type.__name__ = "OctetString"
_SyslogPolicyGroupNameSelect_Object = MibTableColumn
syslogPolicyGroupNameSelect = _SyslogPolicyGroupNameSelect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 2, 1, 2),
    _SyslogPolicyGroupNameSelect_Type()
)
syslogPolicyGroupNameSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogPolicyGroupNameSelect.setStatus("current")
_SyslogServerRowStatus_Type = RowStatus
_SyslogServerRowStatus_Object = MibTableColumn
syslogServerRowStatus = _SyslogServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 2, 1, 4),
    _SyslogServerRowStatus_Type()
)
syslogServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogServerRowStatus.setStatus("current")
_SyslogPolicyGroupTable_Object = MibTable
syslogPolicyGroupTable = _SyslogPolicyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 3)
)
if mibBuilder.loadTexts:
    syslogPolicyGroupTable.setStatus("current")
_SyslogPolicyGroupEntry_Object = MibTableRow
syslogPolicyGroupEntry = _SyslogPolicyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 3, 1)
)
syslogPolicyGroupEntry.setIndexNames(
    (0, "HUAWEI-SYSLOG-MIB", "syslogPolicyGroupName"),
)
if mibBuilder.loadTexts:
    syslogPolicyGroupEntry.setStatus("current")


class _SyslogPolicyGroupName_Type(OctetString):
    """Custom type syslogPolicyGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SyslogPolicyGroupName_Type.__name__ = "OctetString"
_SyslogPolicyGroupName_Object = MibTableColumn
syslogPolicyGroupName = _SyslogPolicyGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 3, 1, 1),
    _SyslogPolicyGroupName_Type()
)
syslogPolicyGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogPolicyGroupName.setStatus("current")
_SyslogPolicyGroupRowStatus_Type = RowStatus
_SyslogPolicyGroupRowStatus_Object = MibTableColumn
syslogPolicyGroupRowStatus = _SyslogPolicyGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 3, 1, 2),
    _SyslogPolicyGroupRowStatus_Type()
)
syslogPolicyGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogPolicyGroupRowStatus.setStatus("current")
_SyslogPolicyConfigTable_Object = MibTable
syslogPolicyConfigTable = _SyslogPolicyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 4)
)
if mibBuilder.loadTexts:
    syslogPolicyConfigTable.setStatus("current")
_SyslogPolicyConfigEntry_Object = MibTableRow
syslogPolicyConfigEntry = _SyslogPolicyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 4, 1)
)
syslogPolicyConfigEntry.setIndexNames(
    (0, "HUAWEI-SYSLOG-MIB", "syslogPolicyConfigIndex"),
)
if mibBuilder.loadTexts:
    syslogPolicyConfigEntry.setStatus("current")


class _SyslogPolicyConfigIndex_Type(Integer32):
    """Custom type syslogPolicyConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SyslogPolicyConfigIndex_Type.__name__ = "Integer32"
_SyslogPolicyConfigIndex_Object = MibTableColumn
syslogPolicyConfigIndex = _SyslogPolicyConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 4, 1, 1),
    _SyslogPolicyConfigIndex_Type()
)
syslogPolicyConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    syslogPolicyConfigIndex.setStatus("current")


class _SyslogPolicyDescr_Type(OctetString):
    """Custom type syslogPolicyDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SyslogPolicyDescr_Type.__name__ = "OctetString"
_SyslogPolicyDescr_Object = MibTableColumn
syslogPolicyDescr = _SyslogPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 4, 1, 2),
    _SyslogPolicyDescr_Type()
)
syslogPolicyDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogPolicyDescr.setStatus("current")


class _SyslogUserType_Type(Integer32):
    """Custom type syslogUserType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              101,
              102,
              200)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("dot1x", 101),
          ("l2dynamic", 4),
          ("l2static", 3),
          ("l2tp", 6),
          ("l3", 5),
          ("others", 200),
          ("portal", 1),
          ("ppp", 2),
          ("telnet", 7),
          ("wlan", 102))
    )


_SyslogUserType_Type.__name__ = "Integer32"
_SyslogUserType_Object = MibTableColumn
syslogUserType = _SyslogUserType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 4, 1, 3),
    _SyslogUserType_Type()
)
syslogUserType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogUserType.setStatus("current")


class _SyslogPolicyBoard_Type(Bits):
    """Custom type syslogPolicyBoard based on Bits"""
    namedValues = NamedValues(
        *(("eighteenth", 18),
          ("eighth", 8),
          ("eleventh", 11),
          ("fifteenth", 15),
          ("fifth", 5),
          ("first", 1),
          ("fourteenth", 14),
          ("fouth", 4),
          ("ninth", 9),
          ("second", 2),
          ("seventennth", 17),
          ("seventh", 7),
          ("sixteenth", 16),
          ("sixth", 6),
          ("tenth", 10),
          ("third", 3),
          ("thirteenth", 13),
          ("twelfth", 12))
    )

_SyslogPolicyBoard_Type.__name__ = "Bits"
_SyslogPolicyBoard_Object = MibTableColumn
syslogPolicyBoard = _SyslogPolicyBoard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 4, 1, 4),
    _SyslogPolicyBoard_Type()
)
syslogPolicyBoard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogPolicyBoard.setStatus("current")
_SyslogPolicyIsp_Type = OctetString
_SyslogPolicyIsp_Object = MibTableColumn
syslogPolicyIsp = _SyslogPolicyIsp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 4, 1, 5),
    _SyslogPolicyIsp_Type()
)
syslogPolicyIsp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogPolicyIsp.setStatus("current")


class _SyslogPolicyType_Type(Integer32):
    """Custom type syslogPolicyType based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("callSyslog", 3),
          ("userOperSyslog", 2))
    )


_SyslogPolicyType_Type.__name__ = "Integer32"
_SyslogPolicyType_Object = MibTableColumn
syslogPolicyType = _SyslogPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 4, 1, 6),
    _SyslogPolicyType_Type()
)
syslogPolicyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogPolicyType.setStatus("current")
_SyslogGroupChoice_Type = OctetString
_SyslogGroupChoice_Object = MibTableColumn
syslogGroupChoice = _SyslogGroupChoice_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 4, 1, 7),
    _SyslogGroupChoice_Type()
)
syslogGroupChoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogGroupChoice.setStatus("current")
_SyslogPolicyRowStatus_Type = RowStatus
_SyslogPolicyRowStatus_Object = MibTableColumn
syslogPolicyRowStatus = _SyslogPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 4, 1, 8),
    _SyslogPolicyRowStatus_Type()
)
syslogPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogPolicyRowStatus.setStatus("current")
_HwSyslogConformance_ObjectIdentity = ObjectIdentity
hwSyslogConformance = _HwSyslogConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 100)
)
_HwSyslogCompliances_ObjectIdentity = ObjectIdentity
hwSyslogCompliances = _HwSyslogCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 100, 1)
)
_HwSyslogObjectGroups_ObjectIdentity = ObjectIdentity
hwSyslogObjectGroups = _HwSyslogObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 100, 2)
)

# Managed Objects groups

hwSyslogAdminStatusObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 100, 2, 1)
)
hwSyslogAdminStatusObjectGroup.setObjects(
    ("HUAWEI-SYSLOG-MIB", "syslogEnableAdminStatus")
)
if mibBuilder.loadTexts:
    hwSyslogAdminStatusObjectGroup.setStatus("current")

hwSyslogServerObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 100, 2, 2)
)
hwSyslogServerObjectGroup.setObjects(
      *(("HUAWEI-SYSLOG-MIB", "syslogServerIpAddress"),
        ("HUAWEI-SYSLOG-MIB", "syslogPolicyGroupNameSelect"),
        ("HUAWEI-SYSLOG-MIB", "syslogServerRowStatus"))
)
if mibBuilder.loadTexts:
    hwSyslogServerObjectGroup.setStatus("current")

hwSyslogPolicyGroupObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 100, 2, 3)
)
hwSyslogPolicyGroupObjectGroup.setObjects(
      *(("HUAWEI-SYSLOG-MIB", "syslogPolicyGroupName"),
        ("HUAWEI-SYSLOG-MIB", "syslogPolicyGroupRowStatus"))
)
if mibBuilder.loadTexts:
    hwSyslogPolicyGroupObjectGroup.setStatus("current")

hwSyslogPolicyConfigObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 100, 2, 4)
)
hwSyslogPolicyConfigObjectGroup.setObjects(
      *(("HUAWEI-SYSLOG-MIB", "syslogPolicyDescr"),
        ("HUAWEI-SYSLOG-MIB", "syslogUserType"),
        ("HUAWEI-SYSLOG-MIB", "syslogPolicyBoard"),
        ("HUAWEI-SYSLOG-MIB", "syslogPolicyIsp"),
        ("HUAWEI-SYSLOG-MIB", "syslogPolicyType"),
        ("HUAWEI-SYSLOG-MIB", "syslogGroupChoice"),
        ("HUAWEI-SYSLOG-MIB", "syslogPolicyRowStatus"))
)
if mibBuilder.loadTexts:
    hwSyslogPolicyConfigObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwSyslogCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 6, 35, 100, 1, 1)
)
if mibBuilder.loadTexts:
    hwSyslogCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SYSLOG-MIB",
    **{"syslogMIBObjects": syslogMIBObjects,
       "syslogEnableAdminStatus": syslogEnableAdminStatus,
       "syslogServerTable": syslogServerTable,
       "syslogServerEntry": syslogServerEntry,
       "syslogServerIpAddress": syslogServerIpAddress,
       "syslogPolicyGroupNameSelect": syslogPolicyGroupNameSelect,
       "syslogServerRowStatus": syslogServerRowStatus,
       "syslogPolicyGroupTable": syslogPolicyGroupTable,
       "syslogPolicyGroupEntry": syslogPolicyGroupEntry,
       "syslogPolicyGroupName": syslogPolicyGroupName,
       "syslogPolicyGroupRowStatus": syslogPolicyGroupRowStatus,
       "syslogPolicyConfigTable": syslogPolicyConfigTable,
       "syslogPolicyConfigEntry": syslogPolicyConfigEntry,
       "syslogPolicyConfigIndex": syslogPolicyConfigIndex,
       "syslogPolicyDescr": syslogPolicyDescr,
       "syslogUserType": syslogUserType,
       "syslogPolicyBoard": syslogPolicyBoard,
       "syslogPolicyIsp": syslogPolicyIsp,
       "syslogPolicyType": syslogPolicyType,
       "syslogGroupChoice": syslogGroupChoice,
       "syslogPolicyRowStatus": syslogPolicyRowStatus,
       "hwSyslogConformance": hwSyslogConformance,
       "hwSyslogCompliances": hwSyslogCompliances,
       "hwSyslogCompliance": hwSyslogCompliance,
       "hwSyslogObjectGroups": hwSyslogObjectGroups,
       "hwSyslogAdminStatusObjectGroup": hwSyslogAdminStatusObjectGroup,
       "hwSyslogServerObjectGroup": hwSyslogServerObjectGroup,
       "hwSyslogPolicyGroupObjectGroup": hwSyslogPolicyGroupObjectGroup,
       "hwSyslogPolicyConfigObjectGroup": hwSyslogPolicyConfigObjectGroup}
)
