# SNMP MIB module (HUAWEI-BRAS-VSM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BRAS-VSM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:14 2024
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

(hwBRASMib,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwBRASMib")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

hwBRASVsm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwVsmSetFlowQryTLenTable_ObjectIdentity = ObjectIdentity
hwVsmSetFlowQryTLenTable = _HwVsmSetFlowQryTLenTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 1)
)


class _HwVsmSetTimeLen_Type(Integer32):
    """Custom type hwVsmSetTimeLen based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_HwVsmSetTimeLen_Type.__name__ = "Integer32"
_HwVsmSetTimeLen_Object = MibScalar
hwVsmSetTimeLen = _HwVsmSetTimeLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 1, 1),
    _HwVsmSetTimeLen_Type()
)
hwVsmSetTimeLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmSetTimeLen.setStatus("current")
_HwVsmServicePolicyTable_Object = MibTable
hwVsmServicePolicyTable = _HwVsmServicePolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2)
)
if mibBuilder.loadTexts:
    hwVsmServicePolicyTable.setStatus("current")
_HwVsmServicePolicyEntry_Object = MibTableRow
hwVsmServicePolicyEntry = _HwVsmServicePolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1)
)
hwVsmServicePolicyEntry.setIndexNames(
    (0, "HUAWEI-BRAS-VSM-MIB", "hwVsmServicePolicyName"),
)
if mibBuilder.loadTexts:
    hwVsmServicePolicyEntry.setStatus("current")


class _HwVsmServicePolicyName_Type(DisplayString):
    """Custom type hwVsmServicePolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVsmServicePolicyName_Type.__name__ = "DisplayString"
_HwVsmServicePolicyName_Object = MibTableColumn
hwVsmServicePolicyName = _HwVsmServicePolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 1),
    _HwVsmServicePolicyName_Type()
)
hwVsmServicePolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVsmServicePolicyName.setStatus("current")


class _HwVsmAcctSchemeName_Type(DisplayString):
    """Custom type hwVsmAcctSchemeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVsmAcctSchemeName_Type.__name__ = "DisplayString"
_HwVsmAcctSchemeName_Object = MibTableColumn
hwVsmAcctSchemeName = _HwVsmAcctSchemeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 2),
    _HwVsmAcctSchemeName_Type()
)
hwVsmAcctSchemeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmAcctSchemeName.setStatus("current")


class _HwVsmTrafficPolicyName_Type(DisplayString):
    """Custom type hwVsmTrafficPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVsmTrafficPolicyName_Type.__name__ = "DisplayString"
_HwVsmTrafficPolicyName_Object = MibTableColumn
hwVsmTrafficPolicyName = _HwVsmTrafficPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 3),
    _HwVsmTrafficPolicyName_Type()
)
hwVsmTrafficPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmTrafficPolicyName.setStatus("current")


class _HwVsmSetIdleCutTime_Type(Integer32):
    """Custom type hwVsmSetIdleCutTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_HwVsmSetIdleCutTime_Type.__name__ = "Integer32"
_HwVsmSetIdleCutTime_Object = MibTableColumn
hwVsmSetIdleCutTime = _HwVsmSetIdleCutTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 4),
    _HwVsmSetIdleCutTime_Type()
)
hwVsmSetIdleCutTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmSetIdleCutTime.setStatus("current")


class _HwVsmSetIdleCutFlow_Type(Integer32):
    """Custom type hwVsmSetIdleCutFlow based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 768000),
    )


_HwVsmSetIdleCutFlow_Type.__name__ = "Integer32"
_HwVsmSetIdleCutFlow_Object = MibTableColumn
hwVsmSetIdleCutFlow = _HwVsmSetIdleCutFlow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 5),
    _HwVsmSetIdleCutFlow_Type()
)
hwVsmSetIdleCutFlow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmSetIdleCutFlow.setStatus("current")
_HwVsmSevicePolicyRowStatus_Type = RowStatus
_HwVsmSevicePolicyRowStatus_Object = MibTableColumn
hwVsmSevicePolicyRowStatus = _HwVsmSevicePolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 6),
    _HwVsmSevicePolicyRowStatus_Type()
)
hwVsmSevicePolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmSevicePolicyRowStatus.setStatus("current")


class _HwVsmOutTrafficPolicyName_Type(DisplayString):
    """Custom type hwVsmOutTrafficPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVsmOutTrafficPolicyName_Type.__name__ = "DisplayString"
_HwVsmOutTrafficPolicyName_Object = MibTableColumn
hwVsmOutTrafficPolicyName = _HwVsmOutTrafficPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 7),
    _HwVsmOutTrafficPolicyName_Type()
)
hwVsmOutTrafficPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmOutTrafficPolicyName.setStatus("current")


class _HwVsmDaaPolicyFlag_Type(Integer32):
    """Custom type hwVsmDaaPolicyFlag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("daa", 1),
          ("vas", 0))
    )


_HwVsmDaaPolicyFlag_Type.__name__ = "Integer32"
_HwVsmDaaPolicyFlag_Object = MibTableColumn
hwVsmDaaPolicyFlag = _HwVsmDaaPolicyFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 8),
    _HwVsmDaaPolicyFlag_Type()
)
hwVsmDaaPolicyFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmDaaPolicyFlag.setStatus("current")


class _HwVsmSetTariffLevel1_Type(DisplayString):
    """Custom type hwVsmSetTariffLevel1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVsmSetTariffLevel1_Type.__name__ = "DisplayString"
_HwVsmSetTariffLevel1_Object = MibTableColumn
hwVsmSetTariffLevel1 = _HwVsmSetTariffLevel1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 9),
    _HwVsmSetTariffLevel1_Type()
)
hwVsmSetTariffLevel1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmSetTariffLevel1.setStatus("current")


class _HwVsmSetTariffLevel2_Type(DisplayString):
    """Custom type hwVsmSetTariffLevel2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVsmSetTariffLevel2_Type.__name__ = "DisplayString"
_HwVsmSetTariffLevel2_Object = MibTableColumn
hwVsmSetTariffLevel2 = _HwVsmSetTariffLevel2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 10),
    _HwVsmSetTariffLevel2_Type()
)
hwVsmSetTariffLevel2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmSetTariffLevel2.setStatus("current")


class _HwVsmSetTariffLevel3_Type(DisplayString):
    """Custom type hwVsmSetTariffLevel3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVsmSetTariffLevel3_Type.__name__ = "DisplayString"
_HwVsmSetTariffLevel3_Object = MibTableColumn
hwVsmSetTariffLevel3 = _HwVsmSetTariffLevel3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 11),
    _HwVsmSetTariffLevel3_Type()
)
hwVsmSetTariffLevel3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmSetTariffLevel3.setStatus("current")


class _HwVsmSetTariffLevel4_Type(DisplayString):
    """Custom type hwVsmSetTariffLevel4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVsmSetTariffLevel4_Type.__name__ = "DisplayString"
_HwVsmSetTariffLevel4_Object = MibTableColumn
hwVsmSetTariffLevel4 = _HwVsmSetTariffLevel4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 12),
    _HwVsmSetTariffLevel4_Type()
)
hwVsmSetTariffLevel4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmSetTariffLevel4.setStatus("current")


class _HwVsmSetTariffLevel5_Type(DisplayString):
    """Custom type hwVsmSetTariffLevel5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVsmSetTariffLevel5_Type.__name__ = "DisplayString"
_HwVsmSetTariffLevel5_Object = MibTableColumn
hwVsmSetTariffLevel5 = _HwVsmSetTariffLevel5_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 13),
    _HwVsmSetTariffLevel5_Type()
)
hwVsmSetTariffLevel5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmSetTariffLevel5.setStatus("current")


class _HwVsmSetTariffLevel6_Type(DisplayString):
    """Custom type hwVsmSetTariffLevel6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVsmSetTariffLevel6_Type.__name__ = "DisplayString"
_HwVsmSetTariffLevel6_Object = MibTableColumn
hwVsmSetTariffLevel6 = _HwVsmSetTariffLevel6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 14),
    _HwVsmSetTariffLevel6_Type()
)
hwVsmSetTariffLevel6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmSetTariffLevel6.setStatus("current")


class _HwVsmSetTariffLevel7_Type(DisplayString):
    """Custom type hwVsmSetTariffLevel7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVsmSetTariffLevel7_Type.__name__ = "DisplayString"
_HwVsmSetTariffLevel7_Object = MibTableColumn
hwVsmSetTariffLevel7 = _HwVsmSetTariffLevel7_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 15),
    _HwVsmSetTariffLevel7_Type()
)
hwVsmSetTariffLevel7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmSetTariffLevel7.setStatus("current")


class _HwVsmSetTariffLevel8_Type(DisplayString):
    """Custom type hwVsmSetTariffLevel8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVsmSetTariffLevel8_Type.__name__ = "DisplayString"
_HwVsmSetTariffLevel8_Object = MibTableColumn
hwVsmSetTariffLevel8 = _HwVsmSetTariffLevel8_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 16),
    _HwVsmSetTariffLevel8_Type()
)
hwVsmSetTariffLevel8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmSetTariffLevel8.setStatus("current")


class _HwVsmTariffLevel1AcctSwitch_Type(EnabledStatus):
    """Custom type hwVsmTariffLevel1AcctSwitch based on EnabledStatus"""
    defaultValue = 1


_HwVsmTariffLevel1AcctSwitch_Object = MibTableColumn
hwVsmTariffLevel1AcctSwitch = _HwVsmTariffLevel1AcctSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 17),
    _HwVsmTariffLevel1AcctSwitch_Type()
)
hwVsmTariffLevel1AcctSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmTariffLevel1AcctSwitch.setStatus("current")


class _HwVsmTariffLevel2AcctSwitch_Type(EnabledStatus):
    """Custom type hwVsmTariffLevel2AcctSwitch based on EnabledStatus"""
    defaultValue = 1


_HwVsmTariffLevel2AcctSwitch_Object = MibTableColumn
hwVsmTariffLevel2AcctSwitch = _HwVsmTariffLevel2AcctSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 18),
    _HwVsmTariffLevel2AcctSwitch_Type()
)
hwVsmTariffLevel2AcctSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmTariffLevel2AcctSwitch.setStatus("current")


class _HwVsmTariffLevel3AcctSwitch_Type(EnabledStatus):
    """Custom type hwVsmTariffLevel3AcctSwitch based on EnabledStatus"""
    defaultValue = 1


_HwVsmTariffLevel3AcctSwitch_Object = MibTableColumn
hwVsmTariffLevel3AcctSwitch = _HwVsmTariffLevel3AcctSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 19),
    _HwVsmTariffLevel3AcctSwitch_Type()
)
hwVsmTariffLevel3AcctSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmTariffLevel3AcctSwitch.setStatus("current")


class _HwVsmTariffLevel4AcctSwitch_Type(EnabledStatus):
    """Custom type hwVsmTariffLevel4AcctSwitch based on EnabledStatus"""
    defaultValue = 1


_HwVsmTariffLevel4AcctSwitch_Object = MibTableColumn
hwVsmTariffLevel4AcctSwitch = _HwVsmTariffLevel4AcctSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 20),
    _HwVsmTariffLevel4AcctSwitch_Type()
)
hwVsmTariffLevel4AcctSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmTariffLevel4AcctSwitch.setStatus("current")


class _HwVsmTariffLevel5AcctSwitch_Type(EnabledStatus):
    """Custom type hwVsmTariffLevel5AcctSwitch based on EnabledStatus"""
    defaultValue = 1


_HwVsmTariffLevel5AcctSwitch_Object = MibTableColumn
hwVsmTariffLevel5AcctSwitch = _HwVsmTariffLevel5AcctSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 21),
    _HwVsmTariffLevel5AcctSwitch_Type()
)
hwVsmTariffLevel5AcctSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmTariffLevel5AcctSwitch.setStatus("current")


class _HwVsmTariffLevel6AcctSwitch_Type(EnabledStatus):
    """Custom type hwVsmTariffLevel6AcctSwitch based on EnabledStatus"""
    defaultValue = 1


_HwVsmTariffLevel6AcctSwitch_Object = MibTableColumn
hwVsmTariffLevel6AcctSwitch = _HwVsmTariffLevel6AcctSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 22),
    _HwVsmTariffLevel6AcctSwitch_Type()
)
hwVsmTariffLevel6AcctSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmTariffLevel6AcctSwitch.setStatus("current")


class _HwVsmTariffLevel7AcctSwitch_Type(EnabledStatus):
    """Custom type hwVsmTariffLevel7AcctSwitch based on EnabledStatus"""
    defaultValue = 1


_HwVsmTariffLevel7AcctSwitch_Object = MibTableColumn
hwVsmTariffLevel7AcctSwitch = _HwVsmTariffLevel7AcctSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 23),
    _HwVsmTariffLevel7AcctSwitch_Type()
)
hwVsmTariffLevel7AcctSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmTariffLevel7AcctSwitch.setStatus("current")


class _HwVsmTariffLevel8AcctSwitch_Type(EnabledStatus):
    """Custom type hwVsmTariffLevel8AcctSwitch based on EnabledStatus"""
    defaultValue = 1


_HwVsmTariffLevel8AcctSwitch_Object = MibTableColumn
hwVsmTariffLevel8AcctSwitch = _HwVsmTariffLevel8AcctSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 2, 1, 24),
    _HwVsmTariffLevel8AcctSwitch_Type()
)
hwVsmTariffLevel8AcctSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmTariffLevel8AcctSwitch.setStatus("current")
_HwVsmValServiceTable_Object = MibTable
hwVsmValServiceTable = _HwVsmValServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3)
)
if mibBuilder.loadTexts:
    hwVsmValServiceTable.setStatus("current")
_HwVsmValServiceEntry_Object = MibTableRow
hwVsmValServiceEntry = _HwVsmValServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1)
)
hwVsmValServiceEntry.setIndexNames(
    (0, "HUAWEI-BRAS-VSM-MIB", "hwVsmServiceID"),
    (0, "HUAWEI-BRAS-VSM-MIB", "hwVsmServiceSlot"),
)
if mibBuilder.loadTexts:
    hwVsmValServiceEntry.setStatus("current")


class _HwVsmServiceID_Type(Integer32):
    """Custom type hwVsmServiceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_HwVsmServiceID_Type.__name__ = "Integer32"
_HwVsmServiceID_Object = MibTableColumn
hwVsmServiceID = _HwVsmServiceID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 1),
    _HwVsmServiceID_Type()
)
hwVsmServiceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVsmServiceID.setStatus("current")


class _HwVsmUserID_Type(Integer32):
    """Custom type hwVsmUserID based on Integer32"""
    defaultValue = 4294967295

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwVsmUserID_Type.__name__ = "Integer32"
_HwVsmUserID_Object = MibTableColumn
hwVsmUserID = _HwVsmUserID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 2),
    _HwVsmUserID_Type()
)
hwVsmUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVsmUserID.setStatus("current")


class _HwVsmFlowNum_Type(Integer32):
    """Custom type hwVsmFlowNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HwVsmFlowNum_Type.__name__ = "Integer32"
_HwVsmFlowNum_Object = MibTableColumn
hwVsmFlowNum = _HwVsmFlowNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 3),
    _HwVsmFlowNum_Type()
)
hwVsmFlowNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVsmFlowNum.setStatus("current")


class _HwVsmServiceSource_Type(Integer32):
    """Custom type hwVsmServiceSource based on Integer32"""
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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("vsmSourceBmi", 9),
          ("vsmSourceBod", 4),
          ("vsmSourceCopsNet", 5),
          ("vsmSourceCopsNetPm", 6),
          ("vsmSourceCopsPm", 8),
          ("vsmSourceCopsUser", 7),
          ("vsmSourceDefault", 0),
          ("vsmSourceIpBod", 10),
          ("vsmSourceIptn", 2),
          ("vsmSourceRadius", 3),
          ("vsmSourceSig", 1))
    )


_HwVsmServiceSource_Type.__name__ = "Integer32"
_HwVsmServiceSource_Object = MibTableColumn
hwVsmServiceSource = _HwVsmServiceSource_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 4),
    _HwVsmServiceSource_Type()
)
hwVsmServiceSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVsmServiceSource.setStatus("current")


class _HwVsmServiceSlot_Type(Integer32):
    """Custom type hwVsmServiceSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwVsmServiceSlot_Type.__name__ = "Integer32"
_HwVsmServiceSlot_Object = MibTableColumn
hwVsmServiceSlot = _HwVsmServiceSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 5),
    _HwVsmServiceSlot_Type()
)
hwVsmServiceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVsmServiceSlot.setStatus("current")


class _HwVsmValServicePolicy_Type(DisplayString):
    """Custom type hwVsmValServicePolicy based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVsmValServicePolicy_Type.__name__ = "DisplayString"
_HwVsmValServicePolicy_Object = MibTableColumn
hwVsmValServicePolicy = _HwVsmValServicePolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 6),
    _HwVsmValServicePolicy_Type()
)
hwVsmValServicePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVsmValServicePolicy.setStatus("current")


class _HwVsmAcctMethod_Type(Integer32):
    """Custom type hwVsmAcctMethod based on Integer32"""
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
        *(("cops", 4),
          ("local", 1),
          ("none", 2),
          ("radius", 3))
    )


_HwVsmAcctMethod_Type.__name__ = "Integer32"
_HwVsmAcctMethod_Object = MibTableColumn
hwVsmAcctMethod = _HwVsmAcctMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 7),
    _HwVsmAcctMethod_Type()
)
hwVsmAcctMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVsmAcctMethod.setStatus("current")


class _HwVsmAcctStartTime_Type(DisplayString):
    """Custom type hwVsmAcctStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVsmAcctStartTime_Type.__name__ = "DisplayString"
_HwVsmAcctStartTime_Object = MibTableColumn
hwVsmAcctStartTime = _HwVsmAcctStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 8),
    _HwVsmAcctStartTime_Type()
)
hwVsmAcctStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVsmAcctStartTime.setStatus("current")


class _HwVsmAcctServerName_Type(DisplayString):
    """Custom type hwVsmAcctServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVsmAcctServerName_Type.__name__ = "DisplayString"
_HwVsmAcctServerName_Object = MibTableColumn
hwVsmAcctServerName = _HwVsmAcctServerName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 9),
    _HwVsmAcctServerName_Type()
)
hwVsmAcctServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVsmAcctServerName.setStatus("current")


class _HwVsmTwoLevelAcctServerName_Type(DisplayString):
    """Custom type hwVsmTwoLevelAcctServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVsmTwoLevelAcctServerName_Type.__name__ = "DisplayString"
_HwVsmTwoLevelAcctServerName_Object = MibTableColumn
hwVsmTwoLevelAcctServerName = _HwVsmTwoLevelAcctServerName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 10),
    _HwVsmTwoLevelAcctServerName_Type()
)
hwVsmTwoLevelAcctServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVsmTwoLevelAcctServerName.setStatus("current")


class _HwVsmPhyInfoAcctServerName_Type(DisplayString):
    """Custom type hwVsmPhyInfoAcctServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVsmPhyInfoAcctServerName_Type.__name__ = "DisplayString"
_HwVsmPhyInfoAcctServerName_Object = MibTableColumn
hwVsmPhyInfoAcctServerName = _HwVsmPhyInfoAcctServerName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 11),
    _HwVsmPhyInfoAcctServerName_Type()
)
hwVsmPhyInfoAcctServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVsmPhyInfoAcctServerName.setStatus("current")


class _HwVsmServiceIdleCutTime_Type(Integer32):
    """Custom type hwVsmServiceIdleCutTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_HwVsmServiceIdleCutTime_Type.__name__ = "Integer32"
_HwVsmServiceIdleCutTime_Object = MibTableColumn
hwVsmServiceIdleCutTime = _HwVsmServiceIdleCutTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 12),
    _HwVsmServiceIdleCutTime_Type()
)
hwVsmServiceIdleCutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVsmServiceIdleCutTime.setStatus("current")


class _HwVsmServiceIdleCutFlow_Type(Integer32):
    """Custom type hwVsmServiceIdleCutFlow based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 768000),
    )


_HwVsmServiceIdleCutFlow_Type.__name__ = "Integer32"
_HwVsmServiceIdleCutFlow_Object = MibTableColumn
hwVsmServiceIdleCutFlow = _HwVsmServiceIdleCutFlow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 13),
    _HwVsmServiceIdleCutFlow_Type()
)
hwVsmServiceIdleCutFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVsmServiceIdleCutFlow.setStatus("current")
_HwVsmUpPacketNum_Type = Counter64
_HwVsmUpPacketNum_Object = MibTableColumn
hwVsmUpPacketNum = _HwVsmUpPacketNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 14),
    _HwVsmUpPacketNum_Type()
)
hwVsmUpPacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVsmUpPacketNum.setStatus("current")
_HwVsmUpByteNum_Type = Counter64
_HwVsmUpByteNum_Object = MibTableColumn
hwVsmUpByteNum = _HwVsmUpByteNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 15),
    _HwVsmUpByteNum_Type()
)
hwVsmUpByteNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVsmUpByteNum.setStatus("current")
_HwVsmDownPacketNum_Type = Counter64
_HwVsmDownPacketNum_Object = MibTableColumn
hwVsmDownPacketNum = _HwVsmDownPacketNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 16),
    _HwVsmDownPacketNum_Type()
)
hwVsmDownPacketNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVsmDownPacketNum.setStatus("current")
_HwVsmDownByteNum_Type = Counter64
_HwVsmDownByteNum_Object = MibTableColumn
hwVsmDownByteNum = _HwVsmDownByteNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 17),
    _HwVsmDownByteNum_Type()
)
hwVsmDownByteNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVsmDownByteNum.setStatus("current")


class _HwVsmDownloadServerName_Type(DisplayString):
    """Custom type hwVsmDownloadServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVsmDownloadServerName_Type.__name__ = "DisplayString"
_HwVsmDownloadServerName_Object = MibTableColumn
hwVsmDownloadServerName = _HwVsmDownloadServerName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 18),
    _HwVsmDownloadServerName_Type()
)
hwVsmDownloadServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVsmDownloadServerName.setStatus("current")


class _HwVsmAcctServerType_Type(DisplayString):
    """Custom type hwVsmAcctServerType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_HwVsmAcctServerType_Type.__name__ = "DisplayString"
_HwVsmAcctServerType_Object = MibTableColumn
hwVsmAcctServerType = _HwVsmAcctServerType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 3, 1, 19),
    _HwVsmAcctServerType_Type()
)
hwVsmAcctServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVsmAcctServerType.setStatus("current")
_HwVsmConformance_ObjectIdentity = ObjectIdentity
hwVsmConformance = _HwVsmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 4)
)
_HwVsmCompliances_ObjectIdentity = ObjectIdentity
hwVsmCompliances = _HwVsmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 4, 1)
)
_HwVsmObjectGroups_ObjectIdentity = ObjectIdentity
hwVsmObjectGroups = _HwVsmObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 4, 2)
)
_HwVsmAcctServicePolicyEnableTable_ObjectIdentity = ObjectIdentity
hwVsmAcctServicePolicyEnableTable = _HwVsmAcctServicePolicyEnableTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 5)
)


class _HwVsmAcctServicePolicyEnable_Type(DisplayString):
    """Custom type hwVsmAcctServicePolicyEnable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwVsmAcctServicePolicyEnable_Type.__name__ = "DisplayString"
_HwVsmAcctServicePolicyEnable_Object = MibScalar
hwVsmAcctServicePolicyEnable = _HwVsmAcctServicePolicyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 5, 1),
    _HwVsmAcctServicePolicyEnable_Type()
)
hwVsmAcctServicePolicyEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmAcctServicePolicyEnable.setStatus("current")


class _HwVsmAcctServicePolicyDisable_Type(Integer32):
    """Custom type hwVsmAcctServicePolicyDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HwVsmAcctServicePolicyDisable_Type.__name__ = "Integer32"
_HwVsmAcctServicePolicyDisable_Object = MibScalar
hwVsmAcctServicePolicyDisable = _HwVsmAcctServicePolicyDisable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 5, 2),
    _HwVsmAcctServicePolicyDisable_Type()
)
hwVsmAcctServicePolicyDisable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVsmAcctServicePolicyDisable.setStatus("current")

# Managed Objects groups

hwVsmSetFlowQryTLenObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 4, 2, 1)
)
hwVsmSetFlowQryTLenObjectGroup.setObjects(
    ("HUAWEI-BRAS-VSM-MIB", "hwVsmSetTimeLen")
)
if mibBuilder.loadTexts:
    hwVsmSetFlowQryTLenObjectGroup.setStatus("current")

hwVsmServicePolicyObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 4, 2, 2)
)
hwVsmServicePolicyObjectGroup.setObjects(
      *(("HUAWEI-BRAS-VSM-MIB", "hwVsmServicePolicyName"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmAcctSchemeName"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmTrafficPolicyName"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmSetIdleCutTime"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmSetIdleCutFlow"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmSevicePolicyRowStatus"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmOutTrafficPolicyName"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmDaaPolicyFlag"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmSetTariffLevel1"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmSetTariffLevel2"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmSetTariffLevel3"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmSetTariffLevel4"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmSetTariffLevel5"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmSetTariffLevel6"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmSetTariffLevel7"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmSetTariffLevel8"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmTariffLevel1AcctSwitch"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmTariffLevel2AcctSwitch"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmTariffLevel3AcctSwitch"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmTariffLevel4AcctSwitch"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmTariffLevel5AcctSwitch"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmTariffLevel6AcctSwitch"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmTariffLevel7AcctSwitch"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmTariffLevel8AcctSwitch"))
)
if mibBuilder.loadTexts:
    hwVsmServicePolicyObjectGroup.setStatus("current")

hwVsmValServiceObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 4, 2, 3)
)
hwVsmValServiceObjectGroup.setObjects(
      *(("HUAWEI-BRAS-VSM-MIB", "hwVsmServiceID"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmUserID"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmFlowNum"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmServiceSource"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmServiceSlot"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmValServicePolicy"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmAcctMethod"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmAcctStartTime"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmAcctServerName"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmTwoLevelAcctServerName"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmPhyInfoAcctServerName"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmServiceIdleCutTime"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmServiceIdleCutFlow"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmUpPacketNum"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmUpByteNum"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmDownPacketNum"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmDownByteNum"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmDownloadServerName"),
        ("HUAWEI-BRAS-VSM-MIB", "hwVsmAcctServerType"))
)
if mibBuilder.loadTexts:
    hwVsmValServiceObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwVsmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 9, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hwVsmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BRAS-VSM-MIB",
    **{"hwBRASVsm": hwBRASVsm,
       "hwVsmSetFlowQryTLenTable": hwVsmSetFlowQryTLenTable,
       "hwVsmSetTimeLen": hwVsmSetTimeLen,
       "hwVsmServicePolicyTable": hwVsmServicePolicyTable,
       "hwVsmServicePolicyEntry": hwVsmServicePolicyEntry,
       "hwVsmServicePolicyName": hwVsmServicePolicyName,
       "hwVsmAcctSchemeName": hwVsmAcctSchemeName,
       "hwVsmTrafficPolicyName": hwVsmTrafficPolicyName,
       "hwVsmSetIdleCutTime": hwVsmSetIdleCutTime,
       "hwVsmSetIdleCutFlow": hwVsmSetIdleCutFlow,
       "hwVsmSevicePolicyRowStatus": hwVsmSevicePolicyRowStatus,
       "hwVsmOutTrafficPolicyName": hwVsmOutTrafficPolicyName,
       "hwVsmDaaPolicyFlag": hwVsmDaaPolicyFlag,
       "hwVsmSetTariffLevel1": hwVsmSetTariffLevel1,
       "hwVsmSetTariffLevel2": hwVsmSetTariffLevel2,
       "hwVsmSetTariffLevel3": hwVsmSetTariffLevel3,
       "hwVsmSetTariffLevel4": hwVsmSetTariffLevel4,
       "hwVsmSetTariffLevel5": hwVsmSetTariffLevel5,
       "hwVsmSetTariffLevel6": hwVsmSetTariffLevel6,
       "hwVsmSetTariffLevel7": hwVsmSetTariffLevel7,
       "hwVsmSetTariffLevel8": hwVsmSetTariffLevel8,
       "hwVsmTariffLevel1AcctSwitch": hwVsmTariffLevel1AcctSwitch,
       "hwVsmTariffLevel2AcctSwitch": hwVsmTariffLevel2AcctSwitch,
       "hwVsmTariffLevel3AcctSwitch": hwVsmTariffLevel3AcctSwitch,
       "hwVsmTariffLevel4AcctSwitch": hwVsmTariffLevel4AcctSwitch,
       "hwVsmTariffLevel5AcctSwitch": hwVsmTariffLevel5AcctSwitch,
       "hwVsmTariffLevel6AcctSwitch": hwVsmTariffLevel6AcctSwitch,
       "hwVsmTariffLevel7AcctSwitch": hwVsmTariffLevel7AcctSwitch,
       "hwVsmTariffLevel8AcctSwitch": hwVsmTariffLevel8AcctSwitch,
       "hwVsmValServiceTable": hwVsmValServiceTable,
       "hwVsmValServiceEntry": hwVsmValServiceEntry,
       "hwVsmServiceID": hwVsmServiceID,
       "hwVsmUserID": hwVsmUserID,
       "hwVsmFlowNum": hwVsmFlowNum,
       "hwVsmServiceSource": hwVsmServiceSource,
       "hwVsmServiceSlot": hwVsmServiceSlot,
       "hwVsmValServicePolicy": hwVsmValServicePolicy,
       "hwVsmAcctMethod": hwVsmAcctMethod,
       "hwVsmAcctStartTime": hwVsmAcctStartTime,
       "hwVsmAcctServerName": hwVsmAcctServerName,
       "hwVsmTwoLevelAcctServerName": hwVsmTwoLevelAcctServerName,
       "hwVsmPhyInfoAcctServerName": hwVsmPhyInfoAcctServerName,
       "hwVsmServiceIdleCutTime": hwVsmServiceIdleCutTime,
       "hwVsmServiceIdleCutFlow": hwVsmServiceIdleCutFlow,
       "hwVsmUpPacketNum": hwVsmUpPacketNum,
       "hwVsmUpByteNum": hwVsmUpByteNum,
       "hwVsmDownPacketNum": hwVsmDownPacketNum,
       "hwVsmDownByteNum": hwVsmDownByteNum,
       "hwVsmDownloadServerName": hwVsmDownloadServerName,
       "hwVsmAcctServerType": hwVsmAcctServerType,
       "hwVsmConformance": hwVsmConformance,
       "hwVsmCompliances": hwVsmCompliances,
       "hwVsmCompliance": hwVsmCompliance,
       "hwVsmObjectGroups": hwVsmObjectGroups,
       "hwVsmSetFlowQryTLenObjectGroup": hwVsmSetFlowQryTLenObjectGroup,
       "hwVsmServicePolicyObjectGroup": hwVsmServicePolicyObjectGroup,
       "hwVsmValServiceObjectGroup": hwVsmValServiceObjectGroup,
       "hwVsmAcctServicePolicyEnableTable": hwVsmAcctServicePolicyEnableTable,
       "hwVsmAcctServicePolicyEnable": hwVsmAcctServicePolicyEnable,
       "hwVsmAcctServicePolicyDisable": hwVsmAcctServicePolicyDisable}
)
