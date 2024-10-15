# SNMP MIB module (HUAWEI-DIE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-DIE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:33 2024
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

(huaweiMgmt,
 hwDatacomm) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "huaweiMgmt",
    "hwDatacomm")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwDIEmib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317)
)
hwDIEmib.setRevisions(
        ("2013-01-10 11:50",
         "2013-06-29 11:50",
         "2013-10-26 11:50")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwDIEMibObjects_ObjectIdentity = ObjectIdentity
hwDIEMibObjects = _HwDIEMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1)
)
_HwDIETable_Object = MibTable
hwDIETable = _HwDIETable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 1)
)
if mibBuilder.loadTexts:
    hwDIETable.setStatus("current")
_HwDIEEntry_Object = MibTableRow
hwDIEEntry = _HwDIEEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 1, 1)
)
hwDIEEntry.setIndexNames(
    (0, "HUAWEI-DIE-MIB", "hwDIEDeviceProfileIndex"),
)
if mibBuilder.loadTexts:
    hwDIEEntry.setStatus("current")


class _HwDIEDeviceProfileIndex_Type(Integer32):
    """Custom type hwDIEDeviceProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwDIEDeviceProfileIndex_Type.__name__ = "Integer32"
_HwDIEDeviceProfileIndex_Object = MibTableColumn
hwDIEDeviceProfileIndex = _HwDIEDeviceProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 1, 1, 1),
    _HwDIEDeviceProfileIndex_Type()
)
hwDIEDeviceProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDIEDeviceProfileIndex.setStatus("current")


class _HwDIEDeviceProfileName_Type(DisplayString):
    """Custom type hwDIEDeviceProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwDIEDeviceProfileName_Type.__name__ = "DisplayString"
_HwDIEDeviceProfileName_Object = MibTableColumn
hwDIEDeviceProfileName = _HwDIEDeviceProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 1, 1, 2),
    _HwDIEDeviceProfileName_Type()
)
hwDIEDeviceProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDIEDeviceProfileName.setStatus("current")


class _HwDIEDeviceProfileDevType_Type(DisplayString):
    """Custom type hwDIEDeviceProfileDevType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwDIEDeviceProfileDevType_Type.__name__ = "DisplayString"
_HwDIEDeviceProfileDevType_Object = MibTableColumn
hwDIEDeviceProfileDevType = _HwDIEDeviceProfileDevType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 1, 1, 3),
    _HwDIEDeviceProfileDevType_Type()
)
hwDIEDeviceProfileDevType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDIEDeviceProfileDevType.setStatus("current")


class _HwDIEDeviceProfileEnable_Type(Integer32):
    """Custom type hwDIEDeviceProfileEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwDIEDeviceProfileEnable_Type.__name__ = "Integer32"
_HwDIEDeviceProfileEnable_Object = MibTableColumn
hwDIEDeviceProfileEnable = _HwDIEDeviceProfileEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 1, 1, 4),
    _HwDIEDeviceProfileEnable_Type()
)
hwDIEDeviceProfileEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDIEDeviceProfileEnable.setStatus("current")


class _HwDIEDeviceProfileRuleLogic_Type(DisplayString):
    """Custom type hwDIEDeviceProfileRuleLogic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HwDIEDeviceProfileRuleLogic_Type.__name__ = "DisplayString"
_HwDIEDeviceProfileRuleLogic_Object = MibTableColumn
hwDIEDeviceProfileRuleLogic = _HwDIEDeviceProfileRuleLogic_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 1, 1, 5),
    _HwDIEDeviceProfileRuleLogic_Type()
)
hwDIEDeviceProfileRuleLogic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDIEDeviceProfileRuleLogic.setStatus("current")
_HwDIEDeviceProfileRowStatus_Type = RowStatus
_HwDIEDeviceProfileRowStatus_Object = MibTableColumn
hwDIEDeviceProfileRowStatus = _HwDIEDeviceProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 1, 1, 6),
    _HwDIEDeviceProfileRowStatus_Type()
)
hwDIEDeviceProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDIEDeviceProfileRowStatus.setStatus("current")
_HwDIERuleTable_Object = MibTable
hwDIERuleTable = _HwDIERuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2)
)
if mibBuilder.loadTexts:
    hwDIERuleTable.setStatus("current")
_HwDIERuleEntry_Object = MibTableRow
hwDIERuleEntry = _HwDIERuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1)
)
hwDIERuleEntry.setIndexNames(
    (0, "HUAWEI-DIE-MIB", "hwDIEDeviceProfileIndex"),
    (0, "HUAWEI-DIE-MIB", "hwDIERuleRuleIndex"),
)
if mibBuilder.loadTexts:
    hwDIERuleEntry.setStatus("current")


class _HwDIERuleRuleIndex_Type(Integer32):
    """Custom type hwDIERuleRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwDIERuleRuleIndex_Type.__name__ = "Integer32"
_HwDIERuleRuleIndex_Object = MibTableColumn
hwDIERuleRuleIndex = _HwDIERuleRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1, 1),
    _HwDIERuleRuleIndex_Type()
)
hwDIERuleRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDIERuleRuleIndex.setStatus("current")
_HwDIERuleMacAddress_Type = MacAddress
_HwDIERuleMacAddress_Object = MibTableColumn
hwDIERuleMacAddress = _HwDIERuleMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1, 2),
    _HwDIERuleMacAddress_Type()
)
hwDIERuleMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDIERuleMacAddress.setStatus("current")


class _HwDIERuleMacMask_Type(Integer32):
    """Custom type hwDIERuleMacMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_HwDIERuleMacMask_Type.__name__ = "Integer32"
_HwDIERuleMacMask_Object = MibTableColumn
hwDIERuleMacMask = _HwDIERuleMacMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1, 3),
    _HwDIERuleMacMask_Type()
)
hwDIERuleMacMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDIERuleMacMask.setStatus("current")


class _HwDIERuleDhcpOptionID_Type(Integer32):
    """Custom type hwDIERuleDhcpOptionID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_HwDIERuleDhcpOptionID_Type.__name__ = "Integer32"
_HwDIERuleDhcpOptionID_Object = MibTableColumn
hwDIERuleDhcpOptionID = _HwDIERuleDhcpOptionID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1, 4),
    _HwDIERuleDhcpOptionID_Type()
)
hwDIERuleDhcpOptionID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDIERuleDhcpOptionID.setStatus("current")


class _HwDIERuleDhcpOptionType_Type(Integer32):
    """Custom type hwDIERuleDhcpOptionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 1),
          ("hex", 2),
          ("invalid", 0))
    )


_HwDIERuleDhcpOptionType_Type.__name__ = "Integer32"
_HwDIERuleDhcpOptionType_Object = MibTableColumn
hwDIERuleDhcpOptionType = _HwDIERuleDhcpOptionType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1, 5),
    _HwDIERuleDhcpOptionType_Type()
)
hwDIERuleDhcpOptionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDIERuleDhcpOptionType.setStatus("current")


class _HwDIERuleDhcpOptionTextAscii_Type(DisplayString):
    """Custom type hwDIERuleDhcpOptionTextAscii based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 247),
    )


_HwDIERuleDhcpOptionTextAscii_Type.__name__ = "DisplayString"
_HwDIERuleDhcpOptionTextAscii_Object = MibTableColumn
hwDIERuleDhcpOptionTextAscii = _HwDIERuleDhcpOptionTextAscii_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1, 6),
    _HwDIERuleDhcpOptionTextAscii_Type()
)
hwDIERuleDhcpOptionTextAscii.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDIERuleDhcpOptionTextAscii.setStatus("current")


class _HwDIERuleDhcpOptionTextHex_Type(DisplayString):
    """Custom type hwDIERuleDhcpOptionTextHex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 765),
    )


_HwDIERuleDhcpOptionTextHex_Type.__name__ = "DisplayString"
_HwDIERuleDhcpOptionTextHex_Object = MibTableColumn
hwDIERuleDhcpOptionTextHex = _HwDIERuleDhcpOptionTextHex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1, 7),
    _HwDIERuleDhcpOptionTextHex_Type()
)
hwDIERuleDhcpOptionTextHex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDIERuleDhcpOptionTextHex.setStatus("current")


class _HwDIERuleDhcpOptionMatch_Type(Integer32):
    """Custom type hwDIERuleDhcpOptionMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allMatch", 2),
          ("invalid", 0),
          ("subMatch", 1))
    )


_HwDIERuleDhcpOptionMatch_Type.__name__ = "Integer32"
_HwDIERuleDhcpOptionMatch_Object = MibTableColumn
hwDIERuleDhcpOptionMatch = _HwDIERuleDhcpOptionMatch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1, 8),
    _HwDIERuleDhcpOptionMatch_Type()
)
hwDIERuleDhcpOptionMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDIERuleDhcpOptionMatch.setStatus("current")


class _HwDIERuleUserAgentText_Type(DisplayString):
    """Custom type hwDIERuleUserAgentText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 247),
    )


_HwDIERuleUserAgentText_Type.__name__ = "DisplayString"
_HwDIERuleUserAgentText_Object = MibTableColumn
hwDIERuleUserAgentText = _HwDIERuleUserAgentText_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1, 9),
    _HwDIERuleUserAgentText_Type()
)
hwDIERuleUserAgentText.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDIERuleUserAgentText.setStatus("current")


class _HwDIERuleUserAgentMatch_Type(Integer32):
    """Custom type hwDIERuleUserAgentMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allMatch", 2),
          ("invalid", 0),
          ("subMatch", 1))
    )


_HwDIERuleUserAgentMatch_Type.__name__ = "Integer32"
_HwDIERuleUserAgentMatch_Object = MibTableColumn
hwDIERuleUserAgentMatch = _HwDIERuleUserAgentMatch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1, 10),
    _HwDIERuleUserAgentMatch_Type()
)
hwDIERuleUserAgentMatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDIERuleUserAgentMatch.setStatus("current")
_HwDIERuleRowStatus_Type = RowStatus
_HwDIERuleRowStatus_Object = MibTableColumn
hwDIERuleRowStatus = _HwDIERuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 2, 1, 11),
    _HwDIERuleRowStatus_Type()
)
hwDIERuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDIERuleRowStatus.setStatus("current")


class _HwDeviceSensorDhcpOption_Type(OctetString):
    """Custom type hwDeviceSensorDhcpOption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwDeviceSensorDhcpOption_Type.__name__ = "OctetString"
_HwDeviceSensorDhcpOption_Object = MibScalar
hwDeviceSensorDhcpOption = _HwDeviceSensorDhcpOption_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 3),
    _HwDeviceSensorDhcpOption_Type()
)
hwDeviceSensorDhcpOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDeviceSensorDhcpOption.setStatus("current")


class _HwDeviceSensorLLDPTlv_Type(OctetString):
    """Custom type hwDeviceSensorLLDPTlv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwDeviceSensorLLDPTlv_Type.__name__ = "OctetString"
_HwDeviceSensorLLDPTlv_Object = MibScalar
hwDeviceSensorLLDPTlv = _HwDeviceSensorLLDPTlv_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 1, 4),
    _HwDeviceSensorLLDPTlv_Type()
)
hwDeviceSensorLLDPTlv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDeviceSensorLLDPTlv.setStatus("current")
_HwDIEConformance_ObjectIdentity = ObjectIdentity
hwDIEConformance = _HwDIEConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 3)
)
_HwDIECompliances_ObjectIdentity = ObjectIdentity
hwDIECompliances = _HwDIECompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 3, 1)
)
_HwDIEObjectGroups_ObjectIdentity = ObjectIdentity
hwDIEObjectGroups = _HwDIEObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 3, 2)
)

# Managed Objects groups

hwDIEGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 3, 2, 1)
)
hwDIEGroup.setObjects(
      *(("HUAWEI-DIE-MIB", "hwDIEDeviceProfileIndex"),
        ("HUAWEI-DIE-MIB", "hwDIEDeviceProfileName"),
        ("HUAWEI-DIE-MIB", "hwDIEDeviceProfileDevType"),
        ("HUAWEI-DIE-MIB", "hwDIEDeviceProfileEnable"),
        ("HUAWEI-DIE-MIB", "hwDIEDeviceProfileRuleLogic"),
        ("HUAWEI-DIE-MIB", "hwDIEDeviceProfileRowStatus"))
)
if mibBuilder.loadTexts:
    hwDIEGroup.setStatus("current")

hwDIERuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 3, 2, 2)
)
hwDIERuleGroup.setObjects(
      *(("HUAWEI-DIE-MIB", "hwDIERuleRuleIndex"),
        ("HUAWEI-DIE-MIB", "hwDIERuleMacAddress"),
        ("HUAWEI-DIE-MIB", "hwDIERuleMacMask"),
        ("HUAWEI-DIE-MIB", "hwDIERuleDhcpOptionID"),
        ("HUAWEI-DIE-MIB", "hwDIERuleDhcpOptionType"),
        ("HUAWEI-DIE-MIB", "hwDIERuleDhcpOptionTextAscii"),
        ("HUAWEI-DIE-MIB", "hwDIERuleDhcpOptionTextHex"),
        ("HUAWEI-DIE-MIB", "hwDIERuleDhcpOptionMatch"),
        ("HUAWEI-DIE-MIB", "hwDIERuleUserAgentText"),
        ("HUAWEI-DIE-MIB", "hwDIERuleUserAgentMatch"),
        ("HUAWEI-DIE-MIB", "hwDIERuleRowStatus"))
)
if mibBuilder.loadTexts:
    hwDIERuleGroup.setStatus("current")

hwDeviceSensorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 3, 2, 3)
)
hwDeviceSensorGroup.setObjects(
      *(("HUAWEI-DIE-MIB", "hwDeviceSensorDhcpOption"),
        ("HUAWEI-DIE-MIB", "hwDeviceSensorLLDPTlv"))
)
if mibBuilder.loadTexts:
    hwDeviceSensorGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwDIECompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 317, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwDIECompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-DIE-MIB",
    **{"hwDIEmib": hwDIEmib,
       "hwDIEMibObjects": hwDIEMibObjects,
       "hwDIETable": hwDIETable,
       "hwDIEEntry": hwDIEEntry,
       "hwDIEDeviceProfileIndex": hwDIEDeviceProfileIndex,
       "hwDIEDeviceProfileName": hwDIEDeviceProfileName,
       "hwDIEDeviceProfileDevType": hwDIEDeviceProfileDevType,
       "hwDIEDeviceProfileEnable": hwDIEDeviceProfileEnable,
       "hwDIEDeviceProfileRuleLogic": hwDIEDeviceProfileRuleLogic,
       "hwDIEDeviceProfileRowStatus": hwDIEDeviceProfileRowStatus,
       "hwDIERuleTable": hwDIERuleTable,
       "hwDIERuleEntry": hwDIERuleEntry,
       "hwDIERuleRuleIndex": hwDIERuleRuleIndex,
       "hwDIERuleMacAddress": hwDIERuleMacAddress,
       "hwDIERuleMacMask": hwDIERuleMacMask,
       "hwDIERuleDhcpOptionID": hwDIERuleDhcpOptionID,
       "hwDIERuleDhcpOptionType": hwDIERuleDhcpOptionType,
       "hwDIERuleDhcpOptionTextAscii": hwDIERuleDhcpOptionTextAscii,
       "hwDIERuleDhcpOptionTextHex": hwDIERuleDhcpOptionTextHex,
       "hwDIERuleDhcpOptionMatch": hwDIERuleDhcpOptionMatch,
       "hwDIERuleUserAgentText": hwDIERuleUserAgentText,
       "hwDIERuleUserAgentMatch": hwDIERuleUserAgentMatch,
       "hwDIERuleRowStatus": hwDIERuleRowStatus,
       "hwDeviceSensorDhcpOption": hwDeviceSensorDhcpOption,
       "hwDeviceSensorLLDPTlv": hwDeviceSensorLLDPTlv,
       "hwDIEConformance": hwDIEConformance,
       "hwDIECompliances": hwDIECompliances,
       "hwDIECompliance": hwDIECompliance,
       "hwDIEObjectGroups": hwDIEObjectGroups,
       "hwDIEGroup": hwDIEGroup,
       "hwDIERuleGroup": hwDIERuleGroup,
       "hwDeviceSensorGroup": hwDeviceSensorGroup}
)
