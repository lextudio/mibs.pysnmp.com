# SNMP MIB module (HUAWEI-DHCP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-DHCP-SNOOPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:31 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIdOrNone")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwDhcpSnpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112)
)
hwDhcpSnpMib.setRevisions(
        ("2014-07-18 00:00",
         "2014-01-27 00:00",
         "2013-06-19 18:00",
         "2006-09-16 18:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HWVlanId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )



class HWMatchMode(Integer32, TextualConvention):
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
        *(("all", 3),
          ("cvlan", 2),
          ("pvlan", 1))
    )



class HWTransmitAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("pass", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HwDhcpSnpObjects_ObjectIdentity = ObjectIdentity
hwDhcpSnpObjects = _HwDhcpSnpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1)
)


class _HwDhcpSnpGlobal_Type(Integer32):
    """Custom type hwDhcpSnpGlobal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwDhcpSnpGlobal_Type.__name__ = "Integer32"
_HwDhcpSnpGlobal_Object = MibScalar
hwDhcpSnpGlobal = _HwDhcpSnpGlobal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 1),
    _HwDhcpSnpGlobal_Type()
)
hwDhcpSnpGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpSnpGlobal.setStatus("current")


class _HwDhcpPktRateCheck_Type(Integer32):
    """Custom type hwDhcpPktRateCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwDhcpPktRateCheck_Type.__name__ = "Integer32"
_HwDhcpPktRateCheck_Object = MibScalar
hwDhcpPktRateCheck = _HwDhcpPktRateCheck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 2),
    _HwDhcpPktRateCheck_Type()
)
hwDhcpPktRateCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpPktRateCheck.setStatus("current")


class _HwDhcpPktRate_Type(Integer32):
    """Custom type hwDhcpPktRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwDhcpPktRate_Type.__name__ = "Integer32"
_HwDhcpPktRate_Object = MibScalar
hwDhcpPktRate = _HwDhcpPktRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 3),
    _HwDhcpPktRate_Type()
)
hwDhcpPktRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpPktRate.setStatus("current")


class _HwDhcpPktRateAlarmThreshold_Type(Integer32):
    """Custom type hwDhcpPktRateAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwDhcpPktRateAlarmThreshold_Type.__name__ = "Integer32"
_HwDhcpPktRateAlarmThreshold_Object = MibScalar
hwDhcpPktRateAlarmThreshold = _HwDhcpPktRateAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 4),
    _HwDhcpPktRateAlarmThreshold_Type()
)
hwDhcpPktRateAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpPktRateAlarmThreshold.setStatus("current")


class _HwDhcpPktRateAlarmEnable_Type(Integer32):
    """Custom type hwDhcpPktRateAlarmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwDhcpPktRateAlarmEnable_Type.__name__ = "Integer32"
_HwDhcpPktRateAlarmEnable_Object = MibScalar
hwDhcpPktRateAlarmEnable = _HwDhcpPktRateAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 5),
    _HwDhcpPktRateAlarmEnable_Type()
)
hwDhcpPktRateAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpPktRateAlarmEnable.setStatus("current")


class _HwDhcpSnpBindTblNomatchedArpGlobalAction_Type(Integer32):
    """Custom type hwDhcpSnpBindTblNomatchedArpGlobalAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 0))
    )


_HwDhcpSnpBindTblNomatchedArpGlobalAction_Type.__name__ = "Integer32"
_HwDhcpSnpBindTblNomatchedArpGlobalAction_Object = MibScalar
hwDhcpSnpBindTblNomatchedArpGlobalAction = _HwDhcpSnpBindTblNomatchedArpGlobalAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 6),
    _HwDhcpSnpBindTblNomatchedArpGlobalAction_Type()
)
hwDhcpSnpBindTblNomatchedArpGlobalAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpSnpBindTblNomatchedArpGlobalAction.setStatus("current")


class _HwDhcpSnpBindTblNomatchedIpGlobalAction_Type(Integer32):
    """Custom type hwDhcpSnpBindTblNomatchedIpGlobalAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 0))
    )


_HwDhcpSnpBindTblNomatchedIpGlobalAction_Type.__name__ = "Integer32"
_HwDhcpSnpBindTblNomatchedIpGlobalAction_Object = MibScalar
hwDhcpSnpBindTblNomatchedIpGlobalAction = _HwDhcpSnpBindTblNomatchedIpGlobalAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 7),
    _HwDhcpSnpBindTblNomatchedIpGlobalAction_Type()
)
hwDhcpSnpBindTblNomatchedIpGlobalAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpSnpBindTblNomatchedIpGlobalAction.setStatus("current")


class _HwDhcpSnpBindTblAutosaveFilename_Type(DisplayString):
    """Custom type hwDhcpSnpBindTblAutosaveFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 51),
    )


_HwDhcpSnpBindTblAutosaveFilename_Type.__name__ = "DisplayString"
_HwDhcpSnpBindTblAutosaveFilename_Object = MibScalar
hwDhcpSnpBindTblAutosaveFilename = _HwDhcpSnpBindTblAutosaveFilename_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 8),
    _HwDhcpSnpBindTblAutosaveFilename_Type()
)
hwDhcpSnpBindTblAutosaveFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpSnpBindTblAutosaveFilename.setStatus("current")


class _HwDhcpSnpBindTblAutosave_Type(Integer32):
    """Custom type hwDhcpSnpBindTblAutosave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwDhcpSnpBindTblAutosave_Type.__name__ = "Integer32"
_HwDhcpSnpBindTblAutosave_Object = MibScalar
hwDhcpSnpBindTblAutosave = _HwDhcpSnpBindTblAutosave_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 9),
    _HwDhcpSnpBindTblAutosave_Type()
)
hwDhcpSnpBindTblAutosave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpSnpBindTblAutosave.setStatus("current")


class _HwDhcpSnpGlobalThreshold_Type(Integer32):
    """Custom type hwDhcpSnpGlobalThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwDhcpSnpGlobalThreshold_Type.__name__ = "Integer32"
_HwDhcpSnpGlobalThreshold_Object = MibScalar
hwDhcpSnpGlobalThreshold = _HwDhcpSnpGlobalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 10),
    _HwDhcpSnpGlobalThreshold_Type()
)
hwDhcpSnpGlobalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpSnpGlobalThreshold.setStatus("current")
_HwDhcpPktRateDiscardNum_Type = Counter32
_HwDhcpPktRateDiscardNum_Object = MibScalar
hwDhcpPktRateDiscardNum = _HwDhcpPktRateDiscardNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 11),
    _HwDhcpPktRateDiscardNum_Type()
)
hwDhcpPktRateDiscardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpPktRateDiscardNum.setStatus("current")
_HwDhcpSnpCfgTable_Object = MibTable
hwDhcpSnpCfgTable = _HwDhcpSnpCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13)
)
if mibBuilder.loadTexts:
    hwDhcpSnpCfgTable.setStatus("current")
_HwDhcpSnpCfgEntry_Object = MibTableRow
hwDhcpSnpCfgEntry = _HwDhcpSnpCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1)
)
hwDhcpSnpCfgEntry.setIndexNames(
    (0, "HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpIfIndex"),
    (0, "HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpVlanIndex"),
    (0, "HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpVsiIndex"),
)
if mibBuilder.loadTexts:
    hwDhcpSnpCfgEntry.setStatus("current")
_HwDhcpSnpIfIndex_Type = InterfaceIndexOrZero
_HwDhcpSnpIfIndex_Object = MibTableColumn
hwDhcpSnpIfIndex = _HwDhcpSnpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 1),
    _HwDhcpSnpIfIndex_Type()
)
hwDhcpSnpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDhcpSnpIfIndex.setStatus("current")
_HwDhcpSnpVlanIndex_Type = VlanIdOrNone
_HwDhcpSnpVlanIndex_Object = MibTableColumn
hwDhcpSnpVlanIndex = _HwDhcpSnpVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 2),
    _HwDhcpSnpVlanIndex_Type()
)
hwDhcpSnpVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDhcpSnpVlanIndex.setStatus("current")


class _HwDhcpSnpVsiIndex_Type(Integer32):
    """Custom type hwDhcpSnpVsiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(65535, 65535),
    )


_HwDhcpSnpVsiIndex_Type.__name__ = "Integer32"
_HwDhcpSnpVsiIndex_Object = MibTableColumn
hwDhcpSnpVsiIndex = _HwDhcpSnpVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 3),
    _HwDhcpSnpVsiIndex_Type()
)
hwDhcpSnpVsiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDhcpSnpVsiIndex.setStatus("current")


class _HwDhcpSnpEnable_Type(Integer32):
    """Custom type hwDhcpSnpEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwDhcpSnpEnable_Type.__name__ = "Integer32"
_HwDhcpSnpEnable_Object = MibTableColumn
hwDhcpSnpEnable = _HwDhcpSnpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 5),
    _HwDhcpSnpEnable_Type()
)
hwDhcpSnpEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpSnpEnable.setStatus("current")


class _HwDhcpTrusted_Type(Integer32):
    """Custom type hwDhcpTrusted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("untrusted", 0))
    )


_HwDhcpTrusted_Type.__name__ = "Integer32"
_HwDhcpTrusted_Object = MibTableColumn
hwDhcpTrusted = _HwDhcpTrusted_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 6),
    _HwDhcpTrusted_Type()
)
hwDhcpTrusted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpTrusted.setStatus("current")


class _HwDhcpOption82Insert_Type(Integer32):
    """Custom type hwDhcpOption82Insert based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwDhcpOption82Insert_Type.__name__ = "Integer32"
_HwDhcpOption82Insert_Object = MibTableColumn
hwDhcpOption82Insert = _HwDhcpOption82Insert_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 7),
    _HwDhcpOption82Insert_Type()
)
hwDhcpOption82Insert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpOption82Insert.setStatus("current")


class _HwDhcpOption82Rebuild_Type(Integer32):
    """Custom type hwDhcpOption82Rebuild based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwDhcpOption82Rebuild_Type.__name__ = "Integer32"
_HwDhcpOption82Rebuild_Object = MibTableColumn
hwDhcpOption82Rebuild = _HwDhcpOption82Rebuild_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 8),
    _HwDhcpOption82Rebuild_Type()
)
hwDhcpOption82Rebuild.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpOption82Rebuild.setStatus("current")


class _HwDhcpChaddrCheck_Type(Integer32):
    """Custom type hwDhcpChaddrCheck based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwDhcpChaddrCheck_Type.__name__ = "Integer32"
_HwDhcpChaddrCheck_Object = MibTableColumn
hwDhcpChaddrCheck = _HwDhcpChaddrCheck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 9),
    _HwDhcpChaddrCheck_Type()
)
hwDhcpChaddrCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpChaddrCheck.setStatus("current")


class _HwDhcpChaddrAlarmThreshold_Type(Integer32):
    """Custom type hwDhcpChaddrAlarmThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwDhcpChaddrAlarmThreshold_Type.__name__ = "Integer32"
_HwDhcpChaddrAlarmThreshold_Object = MibTableColumn
hwDhcpChaddrAlarmThreshold = _HwDhcpChaddrAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 10),
    _HwDhcpChaddrAlarmThreshold_Type()
)
hwDhcpChaddrAlarmThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpChaddrAlarmThreshold.setStatus("current")


class _HwDhcpChaddrAlarmEnable_Type(Integer32):
    """Custom type hwDhcpChaddrAlarmEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwDhcpChaddrAlarmEnable_Type.__name__ = "Integer32"
_HwDhcpChaddrAlarmEnable_Object = MibTableColumn
hwDhcpChaddrAlarmEnable = _HwDhcpChaddrAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 11),
    _HwDhcpChaddrAlarmEnable_Type()
)
hwDhcpChaddrAlarmEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpChaddrAlarmEnable.setStatus("current")


class _HwDhcpArpCheck_Type(Integer32):
    """Custom type hwDhcpArpCheck based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwDhcpArpCheck_Type.__name__ = "Integer32"
_HwDhcpArpCheck_Object = MibTableColumn
hwDhcpArpCheck = _HwDhcpArpCheck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 12),
    _HwDhcpArpCheck_Type()
)
hwDhcpArpCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpArpCheck.setStatus("current")


class _HwDhcpSnpBindTblNomatchedArpAction_Type(Integer32):
    """Custom type hwDhcpSnpBindTblNomatchedArpAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 0))
    )


_HwDhcpSnpBindTblNomatchedArpAction_Type.__name__ = "Integer32"
_HwDhcpSnpBindTblNomatchedArpAction_Object = MibTableColumn
hwDhcpSnpBindTblNomatchedArpAction = _HwDhcpSnpBindTblNomatchedArpAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 13),
    _HwDhcpSnpBindTblNomatchedArpAction_Type()
)
hwDhcpSnpBindTblNomatchedArpAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpSnpBindTblNomatchedArpAction.setStatus("current")


class _HwDhcpArpAlarmThreshold_Type(Integer32):
    """Custom type hwDhcpArpAlarmThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwDhcpArpAlarmThreshold_Type.__name__ = "Integer32"
_HwDhcpArpAlarmThreshold_Object = MibTableColumn
hwDhcpArpAlarmThreshold = _HwDhcpArpAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 14),
    _HwDhcpArpAlarmThreshold_Type()
)
hwDhcpArpAlarmThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpArpAlarmThreshold.setStatus("current")


class _HwDhcpArpAlarmEnable_Type(Integer32):
    """Custom type hwDhcpArpAlarmEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwDhcpArpAlarmEnable_Type.__name__ = "Integer32"
_HwDhcpArpAlarmEnable_Object = MibTableColumn
hwDhcpArpAlarmEnable = _HwDhcpArpAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 15),
    _HwDhcpArpAlarmEnable_Type()
)
hwDhcpArpAlarmEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpArpAlarmEnable.setStatus("current")


class _HwDhcpIpCheck_Type(Integer32):
    """Custom type hwDhcpIpCheck based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwDhcpIpCheck_Type.__name__ = "Integer32"
_HwDhcpIpCheck_Object = MibTableColumn
hwDhcpIpCheck = _HwDhcpIpCheck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 16),
    _HwDhcpIpCheck_Type()
)
hwDhcpIpCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpIpCheck.setStatus("current")


class _HwDhcpSnpBindTblNomatchedIpAction_Type(Integer32):
    """Custom type hwDhcpSnpBindTblNomatchedIpAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 0))
    )


_HwDhcpSnpBindTblNomatchedIpAction_Type.__name__ = "Integer32"
_HwDhcpSnpBindTblNomatchedIpAction_Object = MibTableColumn
hwDhcpSnpBindTblNomatchedIpAction = _HwDhcpSnpBindTblNomatchedIpAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 17),
    _HwDhcpSnpBindTblNomatchedIpAction_Type()
)
hwDhcpSnpBindTblNomatchedIpAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpSnpBindTblNomatchedIpAction.setStatus("current")


class _HwDhcpIpAlarmThreshold_Type(Integer32):
    """Custom type hwDhcpIpAlarmThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwDhcpIpAlarmThreshold_Type.__name__ = "Integer32"
_HwDhcpIpAlarmThreshold_Object = MibTableColumn
hwDhcpIpAlarmThreshold = _HwDhcpIpAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 18),
    _HwDhcpIpAlarmThreshold_Type()
)
hwDhcpIpAlarmThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpIpAlarmThreshold.setStatus("current")


class _HwDhcpIpAlarmEnable_Type(Integer32):
    """Custom type hwDhcpIpAlarmEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwDhcpIpAlarmEnable_Type.__name__ = "Integer32"
_HwDhcpIpAlarmEnable_Object = MibTableColumn
hwDhcpIpAlarmEnable = _HwDhcpIpAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 19),
    _HwDhcpIpAlarmEnable_Type()
)
hwDhcpIpAlarmEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpIpAlarmEnable.setStatus("current")


class _HwDhcpUntrustReplyAlarmThreshold_Type(Integer32):
    """Custom type hwDhcpUntrustReplyAlarmThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwDhcpUntrustReplyAlarmThreshold_Type.__name__ = "Integer32"
_HwDhcpUntrustReplyAlarmThreshold_Object = MibTableColumn
hwDhcpUntrustReplyAlarmThreshold = _HwDhcpUntrustReplyAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 20),
    _HwDhcpUntrustReplyAlarmThreshold_Type()
)
hwDhcpUntrustReplyAlarmThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpUntrustReplyAlarmThreshold.setStatus("current")


class _HwDhcpUntrustReplyAlarmEnable_Type(Integer32):
    """Custom type hwDhcpUntrustReplyAlarmEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwDhcpUntrustReplyAlarmEnable_Type.__name__ = "Integer32"
_HwDhcpUntrustReplyAlarmEnable_Object = MibTableColumn
hwDhcpUntrustReplyAlarmEnable = _HwDhcpUntrustReplyAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 21),
    _HwDhcpUntrustReplyAlarmEnable_Type()
)
hwDhcpUntrustReplyAlarmEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpUntrustReplyAlarmEnable.setStatus("current")


class _HwDhcpSnpBindTblCheck_Type(Integer32):
    """Custom type hwDhcpSnpBindTblCheck based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwDhcpSnpBindTblCheck_Type.__name__ = "Integer32"
_HwDhcpSnpBindTblCheck_Object = MibTableColumn
hwDhcpSnpBindTblCheck = _HwDhcpSnpBindTblCheck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 22),
    _HwDhcpSnpBindTblCheck_Type()
)
hwDhcpSnpBindTblCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpSnpBindTblCheck.setStatus("current")


class _HwDhcpSnpBindTblAlarmThreshold_Type(Integer32):
    """Custom type hwDhcpSnpBindTblAlarmThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwDhcpSnpBindTblAlarmThreshold_Type.__name__ = "Integer32"
_HwDhcpSnpBindTblAlarmThreshold_Object = MibTableColumn
hwDhcpSnpBindTblAlarmThreshold = _HwDhcpSnpBindTblAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 23),
    _HwDhcpSnpBindTblAlarmThreshold_Type()
)
hwDhcpSnpBindTblAlarmThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpSnpBindTblAlarmThreshold.setStatus("current")


class _HwDhcpSnpBindTblAlarmEnable_Type(Integer32):
    """Custom type hwDhcpSnpBindTblAlarmEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwDhcpSnpBindTblAlarmEnable_Type.__name__ = "Integer32"
_HwDhcpSnpBindTblAlarmEnable_Object = MibTableColumn
hwDhcpSnpBindTblAlarmEnable = _HwDhcpSnpBindTblAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 24),
    _HwDhcpSnpBindTblAlarmEnable_Type()
)
hwDhcpSnpBindTblAlarmEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpSnpBindTblAlarmEnable.setStatus("current")


class _HwDhcpSnpMatchMode_Type(HWMatchMode):
    """Custom type hwDhcpSnpMatchMode based on HWMatchMode"""
    defaultValue = 1


_HwDhcpSnpMatchMode_Object = MibTableColumn
hwDhcpSnpMatchMode = _HwDhcpSnpMatchMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 25),
    _HwDhcpSnpMatchMode_Type()
)
hwDhcpSnpMatchMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpSnpMatchMode.setStatus("current")


class _HwDhcpSnpDynamicItemCheck_Type(Integer32):
    """Custom type hwDhcpSnpDynamicItemCheck based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("ipInterface", 3),
          ("ipMac", 2),
          ("ipMacInterface", 4),
          ("undo", 0))
    )


_HwDhcpSnpDynamicItemCheck_Type.__name__ = "Integer32"
_HwDhcpSnpDynamicItemCheck_Object = MibTableColumn
hwDhcpSnpDynamicItemCheck = _HwDhcpSnpDynamicItemCheck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 26),
    _HwDhcpSnpDynamicItemCheck_Type()
)
hwDhcpSnpDynamicItemCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpSnpDynamicItemCheck.setStatus("current")


class _HwDhcpSnpMaxUserNum_Type(Integer32):
    """Custom type hwDhcpSnpMaxUserNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_HwDhcpSnpMaxUserNum_Type.__name__ = "Integer32"
_HwDhcpSnpMaxUserNum_Object = MibTableColumn
hwDhcpSnpMaxUserNum = _HwDhcpSnpMaxUserNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 27),
    _HwDhcpSnpMaxUserNum_Type()
)
hwDhcpSnpMaxUserNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpSnpMaxUserNum.setStatus("current")


class _HwDhcpSnpUserLimitAlarmThreshold_Type(Integer32):
    """Custom type hwDhcpSnpUserLimitAlarmThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwDhcpSnpUserLimitAlarmThreshold_Type.__name__ = "Integer32"
_HwDhcpSnpUserLimitAlarmThreshold_Object = MibTableColumn
hwDhcpSnpUserLimitAlarmThreshold = _HwDhcpSnpUserLimitAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 28),
    _HwDhcpSnpUserLimitAlarmThreshold_Type()
)
hwDhcpSnpUserLimitAlarmThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpSnpUserLimitAlarmThreshold.setStatus("current")


class _HwDhcpSnpUserLimitAlarmEnable_Type(Integer32):
    """Custom type hwDhcpSnpUserLimitAlarmEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwDhcpSnpUserLimitAlarmEnable_Type.__name__ = "Integer32"
_HwDhcpSnpUserLimitAlarmEnable_Object = MibTableColumn
hwDhcpSnpUserLimitAlarmEnable = _HwDhcpSnpUserLimitAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 29),
    _HwDhcpSnpUserLimitAlarmEnable_Type()
)
hwDhcpSnpUserLimitAlarmEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpSnpUserLimitAlarmEnable.setStatus("current")
_HwDhcpSnpCfgTblRowStatus_Type = RowStatus
_HwDhcpSnpCfgTblRowStatus_Object = MibTableColumn
hwDhcpSnpCfgTblRowStatus = _HwDhcpSnpCfgTblRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 30),
    _HwDhcpSnpCfgTblRowStatus_Type()
)
hwDhcpSnpCfgTblRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpSnpCfgTblRowStatus.setStatus("current")
_HwDhcpPktIfRateCheck_Type = EnabledStatus
_HwDhcpPktIfRateCheck_Object = MibTableColumn
hwDhcpPktIfRateCheck = _HwDhcpPktIfRateCheck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 31),
    _HwDhcpPktIfRateCheck_Type()
)
hwDhcpPktIfRateCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpPktIfRateCheck.setStatus("current")


class _HwDhcpPktIfRate_Type(Integer32):
    """Custom type hwDhcpPktIfRate based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwDhcpPktIfRate_Type.__name__ = "Integer32"
_HwDhcpPktIfRate_Object = MibTableColumn
hwDhcpPktIfRate = _HwDhcpPktIfRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 32),
    _HwDhcpPktIfRate_Type()
)
hwDhcpPktIfRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpPktIfRate.setStatus("current")


class _HwDhcpPktIfRateAlarmThreshold_Type(Integer32):
    """Custom type hwDhcpPktIfRateAlarmThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HwDhcpPktIfRateAlarmThreshold_Type.__name__ = "Integer32"
_HwDhcpPktIfRateAlarmThreshold_Object = MibTableColumn
hwDhcpPktIfRateAlarmThreshold = _HwDhcpPktIfRateAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 33),
    _HwDhcpPktIfRateAlarmThreshold_Type()
)
hwDhcpPktIfRateAlarmThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpPktIfRateAlarmThreshold.setStatus("current")


class _HwDhcpPktIfRateAlarmEnable_Type(EnabledStatus):
    """Custom type hwDhcpPktIfRateAlarmEnable based on EnabledStatus"""


_HwDhcpPktIfRateAlarmEnable_Object = MibTableColumn
hwDhcpPktIfRateAlarmEnable = _HwDhcpPktIfRateAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 34),
    _HwDhcpPktIfRateAlarmEnable_Type()
)
hwDhcpPktIfRateAlarmEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpPktIfRateAlarmEnable.setStatus("current")


class _HwDhcpSnpIfVlanOption82RemoteId_Type(DisplayString):
    """Custom type hwDhcpSnpIfVlanOption82RemoteId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwDhcpSnpIfVlanOption82RemoteId_Type.__name__ = "DisplayString"
_HwDhcpSnpIfVlanOption82RemoteId_Object = MibTableColumn
hwDhcpSnpIfVlanOption82RemoteId = _HwDhcpSnpIfVlanOption82RemoteId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 35),
    _HwDhcpSnpIfVlanOption82RemoteId_Type()
)
hwDhcpSnpIfVlanOption82RemoteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpSnpIfVlanOption82RemoteId.setStatus("current")


class _HwDhcpSnpIfVlanOption82CircuitId_Type(DisplayString):
    """Custom type hwDhcpSnpIfVlanOption82CircuitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwDhcpSnpIfVlanOption82CircuitId_Type.__name__ = "DisplayString"
_HwDhcpSnpIfVlanOption82CircuitId_Object = MibTableColumn
hwDhcpSnpIfVlanOption82CircuitId = _HwDhcpSnpIfVlanOption82CircuitId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 13, 1, 36),
    _HwDhcpSnpIfVlanOption82CircuitId_Type()
)
hwDhcpSnpIfVlanOption82CircuitId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpSnpIfVlanOption82CircuitId.setStatus("current")
_HwDhcpSnpBindTable_Object = MibTable
hwDhcpSnpBindTable = _HwDhcpSnpBindTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 14)
)
if mibBuilder.loadTexts:
    hwDhcpSnpBindTable.setStatus("current")
_HwDhcpSnpBindEntry_Object = MibTableRow
hwDhcpSnpBindEntry = _HwDhcpSnpBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 14, 1)
)
hwDhcpSnpBindEntry.setIndexNames(
    (0, "HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindIpIndex"),
    (0, "HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindPVlanIndex"),
    (0, "HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindCVlanIndex"),
    (0, "HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindVRFIdIndex"),
    (0, "HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindVsiIndex"),
)
if mibBuilder.loadTexts:
    hwDhcpSnpBindEntry.setStatus("current")
_HwDhcpSnpBindIpIndex_Type = IpAddress
_HwDhcpSnpBindIpIndex_Object = MibTableColumn
hwDhcpSnpBindIpIndex = _HwDhcpSnpBindIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 14, 1, 1),
    _HwDhcpSnpBindIpIndex_Type()
)
hwDhcpSnpBindIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDhcpSnpBindIpIndex.setStatus("current")
_HwDhcpSnpBindPVlanIndex_Type = VlanId
_HwDhcpSnpBindPVlanIndex_Object = MibTableColumn
hwDhcpSnpBindPVlanIndex = _HwDhcpSnpBindPVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 14, 1, 2),
    _HwDhcpSnpBindPVlanIndex_Type()
)
hwDhcpSnpBindPVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDhcpSnpBindPVlanIndex.setStatus("current")
_HwDhcpSnpBindCVlanIndex_Type = VlanId
_HwDhcpSnpBindCVlanIndex_Object = MibTableColumn
hwDhcpSnpBindCVlanIndex = _HwDhcpSnpBindCVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 14, 1, 3),
    _HwDhcpSnpBindCVlanIndex_Type()
)
hwDhcpSnpBindCVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDhcpSnpBindCVlanIndex.setStatus("current")


class _HwDhcpSnpBindVRFIdIndex_Type(Integer32):
    """Custom type hwDhcpSnpBindVRFIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HwDhcpSnpBindVRFIdIndex_Type.__name__ = "Integer32"
_HwDhcpSnpBindVRFIdIndex_Object = MibTableColumn
hwDhcpSnpBindVRFIdIndex = _HwDhcpSnpBindVRFIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 14, 1, 4),
    _HwDhcpSnpBindVRFIdIndex_Type()
)
hwDhcpSnpBindVRFIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDhcpSnpBindVRFIdIndex.setStatus("current")


class _HwDhcpSnpBindVsiIndex_Type(Integer32):
    """Custom type hwDhcpSnpBindVsiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(65535, 65535),
    )


_HwDhcpSnpBindVsiIndex_Type.__name__ = "Integer32"
_HwDhcpSnpBindVsiIndex_Object = MibTableColumn
hwDhcpSnpBindVsiIndex = _HwDhcpSnpBindVsiIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 14, 1, 5),
    _HwDhcpSnpBindVsiIndex_Type()
)
hwDhcpSnpBindVsiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDhcpSnpBindVsiIndex.setStatus("current")


class _HwDhcpSnpBindIfDescr_Type(DisplayString):
    """Custom type hwDhcpSnpBindIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_HwDhcpSnpBindIfDescr_Type.__name__ = "DisplayString"
_HwDhcpSnpBindIfDescr_Object = MibTableColumn
hwDhcpSnpBindIfDescr = _HwDhcpSnpBindIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 14, 1, 6),
    _HwDhcpSnpBindIfDescr_Type()
)
hwDhcpSnpBindIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpSnpBindIfDescr.setStatus("current")
_HwDhcpSnpBindPVlanId_Type = VlanId
_HwDhcpSnpBindPVlanId_Object = MibTableColumn
hwDhcpSnpBindPVlanId = _HwDhcpSnpBindPVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 14, 1, 7),
    _HwDhcpSnpBindPVlanId_Type()
)
hwDhcpSnpBindPVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpSnpBindPVlanId.setStatus("current")
_HwDhcpSnpBindCVlanId_Type = VlanId
_HwDhcpSnpBindCVlanId_Object = MibTableColumn
hwDhcpSnpBindCVlanId = _HwDhcpSnpBindCVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 14, 1, 8),
    _HwDhcpSnpBindCVlanId_Type()
)
hwDhcpSnpBindCVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpSnpBindCVlanId.setStatus("current")


class _HwDhcpSnpBindVRFId_Type(Integer32):
    """Custom type hwDhcpSnpBindVRFId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HwDhcpSnpBindVRFId_Type.__name__ = "Integer32"
_HwDhcpSnpBindVRFId_Object = MibTableColumn
hwDhcpSnpBindVRFId = _HwDhcpSnpBindVRFId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 14, 1, 9),
    _HwDhcpSnpBindVRFId_Type()
)
hwDhcpSnpBindVRFId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpSnpBindVRFId.setStatus("current")


class _HwDhcpSnpBindVsiId_Type(Integer32):
    """Custom type hwDhcpSnpBindVsiId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(65535, 65535),
    )


_HwDhcpSnpBindVsiId_Type.__name__ = "Integer32"
_HwDhcpSnpBindVsiId_Object = MibTableColumn
hwDhcpSnpBindVsiId = _HwDhcpSnpBindVsiId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 14, 1, 10),
    _HwDhcpSnpBindVsiId_Type()
)
hwDhcpSnpBindVsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpSnpBindVsiId.setStatus("current")
_HwDhcpSnpBindMac_Type = MacAddress
_HwDhcpSnpBindMac_Object = MibTableColumn
hwDhcpSnpBindMac = _HwDhcpSnpBindMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 14, 1, 11),
    _HwDhcpSnpBindMac_Type()
)
hwDhcpSnpBindMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpSnpBindMac.setStatus("current")
_HwDhcpSnpBindIp_Type = IpAddress
_HwDhcpSnpBindIp_Object = MibTableColumn
hwDhcpSnpBindIp = _HwDhcpSnpBindIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 14, 1, 12),
    _HwDhcpSnpBindIp_Type()
)
hwDhcpSnpBindIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpSnpBindIp.setStatus("current")


class _HwDhcpSnpBindStatus_Type(Integer32):
    """Custom type hwDhcpSnpBindStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_HwDhcpSnpBindStatus_Type.__name__ = "Integer32"
_HwDhcpSnpBindStatus_Object = MibTableColumn
hwDhcpSnpBindStatus = _HwDhcpSnpBindStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 14, 1, 13),
    _HwDhcpSnpBindStatus_Type()
)
hwDhcpSnpBindStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpSnpBindStatus.setStatus("current")
_HwDhcpSnpBindLease_Type = Integer32
_HwDhcpSnpBindLease_Object = MibTableColumn
hwDhcpSnpBindLease = _HwDhcpSnpBindLease_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 14, 1, 14),
    _HwDhcpSnpBindLease_Type()
)
hwDhcpSnpBindLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpSnpBindLease.setStatus("current")
_HwDhcpSnpBindRowStatus_Type = RowStatus
_HwDhcpSnpBindRowStatus_Object = MibTableColumn
hwDhcpSnpBindRowStatus = _HwDhcpSnpBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 14, 1, 18),
    _HwDhcpSnpBindRowStatus_Type()
)
hwDhcpSnpBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpSnpBindRowStatus.setStatus("current")
_HwDhcpSnpFalsePktStatisticTable_Object = MibTable
hwDhcpSnpFalsePktStatisticTable = _HwDhcpSnpFalsePktStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 15)
)
if mibBuilder.loadTexts:
    hwDhcpSnpFalsePktStatisticTable.setStatus("current")
_HwDhcpSnpFalsePktStatisticEntry_Object = MibTableRow
hwDhcpSnpFalsePktStatisticEntry = _HwDhcpSnpFalsePktStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 15, 1)
)
hwDhcpSnpFalsePktStatisticEntry.setIndexNames(
    (0, "HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpIfIndex"),
    (0, "HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpVlanIndex"),
    (0, "HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpVsiIndex"),
)
if mibBuilder.loadTexts:
    hwDhcpSnpFalsePktStatisticEntry.setStatus("current")


class _HwDhcpSnpStatisticIfDescr_Type(DisplayString):
    """Custom type hwDhcpSnpStatisticIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_HwDhcpSnpStatisticIfDescr_Type.__name__ = "DisplayString"
_HwDhcpSnpStatisticIfDescr_Object = MibTableColumn
hwDhcpSnpStatisticIfDescr = _HwDhcpSnpStatisticIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 15, 1, 1),
    _HwDhcpSnpStatisticIfDescr_Type()
)
hwDhcpSnpStatisticIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpSnpStatisticIfDescr.setStatus("current")
_HwDhcpSnpStatisticVlanId_Type = VlanIdOrNone
_HwDhcpSnpStatisticVlanId_Object = MibTableColumn
hwDhcpSnpStatisticVlanId = _HwDhcpSnpStatisticVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 15, 1, 2),
    _HwDhcpSnpStatisticVlanId_Type()
)
hwDhcpSnpStatisticVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpSnpStatisticVlanId.setStatus("current")
_HwChaddrNomatchSrcMacDhcpPktNum_Type = Counter32
_HwChaddrNomatchSrcMacDhcpPktNum_Object = MibTableColumn
hwChaddrNomatchSrcMacDhcpPktNum = _HwChaddrNomatchSrcMacDhcpPktNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 15, 1, 3),
    _HwChaddrNomatchSrcMacDhcpPktNum_Type()
)
hwChaddrNomatchSrcMacDhcpPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwChaddrNomatchSrcMacDhcpPktNum.setStatus("current")
_HwArpNomatchSnpBindTblPktNum_Type = Counter32
_HwArpNomatchSnpBindTblPktNum_Object = MibTableColumn
hwArpNomatchSnpBindTblPktNum = _HwArpNomatchSnpBindTblPktNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 15, 1, 4),
    _HwArpNomatchSnpBindTblPktNum_Type()
)
hwArpNomatchSnpBindTblPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwArpNomatchSnpBindTblPktNum.setStatus("current")
_HwIpNomatchSnpBindTblPktNum_Type = Counter32
_HwIpNomatchSnpBindTblPktNum_Object = MibTableColumn
hwIpNomatchSnpBindTblPktNum = _HwIpNomatchSnpBindTblPktNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 15, 1, 5),
    _HwIpNomatchSnpBindTblPktNum_Type()
)
hwIpNomatchSnpBindTblPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIpNomatchSnpBindTblPktNum.setStatus("current")
_HwNomatchSnpBindTblDhcpPktNum_Type = Counter32
_HwNomatchSnpBindTblDhcpPktNum_Object = MibTableColumn
hwNomatchSnpBindTblDhcpPktNum = _HwNomatchSnpBindTblDhcpPktNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 15, 1, 6),
    _HwNomatchSnpBindTblDhcpPktNum_Type()
)
hwNomatchSnpBindTblDhcpPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNomatchSnpBindTblDhcpPktNum.setStatus("current")
_HwUntrustedReplyPktNum_Type = Counter32
_HwUntrustedReplyPktNum_Object = MibTableColumn
hwUntrustedReplyPktNum = _HwUntrustedReplyPktNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 15, 1, 7),
    _HwUntrustedReplyPktNum_Type()
)
hwUntrustedReplyPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUntrustedReplyPktNum.setStatus("current")


class _HwDhcpSnpStatisticVsiId_Type(Integer32):
    """Custom type hwDhcpSnpStatisticVsiId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
        ValueRangeConstraint(65535, 65535),
    )


_HwDhcpSnpStatisticVsiId_Type.__name__ = "Integer32"
_HwDhcpSnpStatisticVsiId_Object = MibTableColumn
hwDhcpSnpStatisticVsiId = _HwDhcpSnpStatisticVsiId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 15, 1, 8),
    _HwDhcpSnpStatisticVsiId_Type()
)
hwDhcpSnpStatisticVsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpSnpStatisticVsiId.setStatus("current")
_HwSnpBindingItemNum_Type = Counter32
_HwSnpBindingItemNum_Object = MibTableColumn
hwSnpBindingItemNum = _HwSnpBindingItemNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 15, 1, 9),
    _HwSnpBindingItemNum_Type()
)
hwSnpBindingItemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSnpBindingItemNum.setStatus("current")
_HwSnpCfgMaxUserNum_Type = Counter32
_HwSnpCfgMaxUserNum_Object = MibTableColumn
hwSnpCfgMaxUserNum = _HwSnpCfgMaxUserNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 15, 1, 10),
    _HwSnpCfgMaxUserNum_Type()
)
hwSnpCfgMaxUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSnpCfgMaxUserNum.setStatus("current")
_HwDhcpPktIfRateDiscardNum_Type = Counter32
_HwDhcpPktIfRateDiscardNum_Object = MibTableColumn
hwDhcpPktIfRateDiscardNum = _HwDhcpPktIfRateDiscardNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 15, 1, 11),
    _HwDhcpPktIfRateDiscardNum_Type()
)
hwDhcpPktIfRateDiscardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDhcpPktIfRateDiscardNum.setStatus("current")
_HwDhcpSnpCarCfgTable_Object = MibTable
hwDhcpSnpCarCfgTable = _HwDhcpSnpCarCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 16)
)
if mibBuilder.loadTexts:
    hwDhcpSnpCarCfgTable.setStatus("current")
_HwDhcpSnpCarCfgEntry_Object = MibTableRow
hwDhcpSnpCarCfgEntry = _HwDhcpSnpCarCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 16, 1)
)
hwDhcpSnpCarCfgEntry.setIndexNames(
    (0, "HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpIfIndex"),
    (0, "HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpVlanIndex"),
)
if mibBuilder.loadTexts:
    hwDhcpSnpCarCfgEntry.setStatus("current")


class _HwDhcpSnpCarEnable_Type(EnabledStatus):
    """Custom type hwDhcpSnpCarEnable based on EnabledStatus"""


_HwDhcpSnpCarEnable_Object = MibTableColumn
hwDhcpSnpCarEnable = _HwDhcpSnpCarEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 16, 1, 11),
    _HwDhcpSnpCarEnable_Type()
)
hwDhcpSnpCarEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpSnpCarEnable.setStatus("current")


class _HwDhcpSnpCarCir_Type(Integer32):
    """Custom type hwDhcpSnpCarCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000000),
    )


_HwDhcpSnpCarCir_Type.__name__ = "Integer32"
_HwDhcpSnpCarCir_Object = MibTableColumn
hwDhcpSnpCarCir = _HwDhcpSnpCarCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 16, 1, 12),
    _HwDhcpSnpCarCir_Type()
)
hwDhcpSnpCarCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpSnpCarCir.setStatus("current")


class _HwDhcpSnpCarPir_Type(Integer32):
    """Custom type hwDhcpSnpCarPir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000000),
    )


_HwDhcpSnpCarPir_Type.__name__ = "Integer32"
_HwDhcpSnpCarPir_Object = MibTableColumn
hwDhcpSnpCarPir = _HwDhcpSnpCarPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 16, 1, 13),
    _HwDhcpSnpCarPir_Type()
)
hwDhcpSnpCarPir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpSnpCarPir.setStatus("current")


class _HwDhcpSnpCaCbs_Type(Integer32):
    """Custom type hwDhcpSnpCaCbs based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 39314432),
    )


_HwDhcpSnpCaCbs_Type.__name__ = "Integer32"
_HwDhcpSnpCaCbs_Object = MibTableColumn
hwDhcpSnpCaCbs = _HwDhcpSnpCaCbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 16, 1, 14),
    _HwDhcpSnpCaCbs_Type()
)
hwDhcpSnpCaCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpSnpCaCbs.setStatus("current")


class _HwDhcpSnpCarPbs_Type(Integer32):
    """Custom type hwDhcpSnpCarPbs based on Integer32"""
    defaultValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 39314432),
    )


_HwDhcpSnpCarPbs_Type.__name__ = "Integer32"
_HwDhcpSnpCarPbs_Object = MibTableColumn
hwDhcpSnpCarPbs = _HwDhcpSnpCarPbs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 16, 1, 15),
    _HwDhcpSnpCarPbs_Type()
)
hwDhcpSnpCarPbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpSnpCarPbs.setStatus("current")


class _HwDhcpSnpCarYellow_Type(HWTransmitAction):
    """Custom type hwDhcpSnpCarYellow based on HWTransmitAction"""
    defaultValue = 2


_HwDhcpSnpCarYellow_Object = MibTableColumn
hwDhcpSnpCarYellow = _HwDhcpSnpCarYellow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 16, 1, 16),
    _HwDhcpSnpCarYellow_Type()
)
hwDhcpSnpCarYellow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpSnpCarYellow.setStatus("current")


class _HwDhcpSnpCarRed_Type(HWTransmitAction):
    """Custom type hwDhcpSnpCarRed based on HWTransmitAction"""
    defaultValue = 1


_HwDhcpSnpCarRed_Object = MibTableColumn
hwDhcpSnpCarRed = _HwDhcpSnpCarRed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 16, 1, 17),
    _HwDhcpSnpCarRed_Type()
)
hwDhcpSnpCarRed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpSnpCarRed.setStatus("current")
_HwDhcpSnpCarRowStatus_Type = RowStatus
_HwDhcpSnpCarRowStatus_Object = MibTableColumn
hwDhcpSnpCarRowStatus = _HwDhcpSnpCarRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 16, 1, 50),
    _HwDhcpSnpCarRowStatus_Type()
)
hwDhcpSnpCarRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpSnpCarRowStatus.setStatus("current")


class _HwDhcpSnpGlobalOption82Format_Type(Integer32):
    """Custom type hwDhcpSnpGlobalOption82Format based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 2),
          ("hex", 1))
    )


_HwDhcpSnpGlobalOption82Format_Type.__name__ = "Integer32"
_HwDhcpSnpGlobalOption82Format_Object = MibScalar
hwDhcpSnpGlobalOption82Format = _HwDhcpSnpGlobalOption82Format_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 17),
    _HwDhcpSnpGlobalOption82Format_Type()
)
hwDhcpSnpGlobalOption82Format.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpSnpGlobalOption82Format.setStatus("current")


class _HwDhcpSnpGlobalOption82PacketFormat_Type(Integer32):
    """Custom type hwDhcpSnpGlobalOption82PacketFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extended", 1),
          ("standard", 2))
    )


_HwDhcpSnpGlobalOption82PacketFormat_Type.__name__ = "Integer32"
_HwDhcpSnpGlobalOption82PacketFormat_Object = MibScalar
hwDhcpSnpGlobalOption82PacketFormat = _HwDhcpSnpGlobalOption82PacketFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 18),
    _HwDhcpSnpGlobalOption82PacketFormat_Type()
)
hwDhcpSnpGlobalOption82PacketFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpSnpGlobalOption82PacketFormat.setStatus("current")


class _HwDhcpSnpGlobalOption82RemoteId_Type(DisplayString):
    """Custom type hwDhcpSnpGlobalOption82RemoteId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwDhcpSnpGlobalOption82RemoteId_Type.__name__ = "DisplayString"
_HwDhcpSnpGlobalOption82RemoteId_Object = MibScalar
hwDhcpSnpGlobalOption82RemoteId = _HwDhcpSnpGlobalOption82RemoteId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 19),
    _HwDhcpSnpGlobalOption82RemoteId_Type()
)
hwDhcpSnpGlobalOption82RemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpSnpGlobalOption82RemoteId.setStatus("current")
_HwDhcpSnpGlobalOption82RemoteIdSysName_Type = EnabledStatus
_HwDhcpSnpGlobalOption82RemoteIdSysName_Object = MibScalar
hwDhcpSnpGlobalOption82RemoteIdSysName = _HwDhcpSnpGlobalOption82RemoteIdSysName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 20),
    _HwDhcpSnpGlobalOption82RemoteIdSysName_Type()
)
hwDhcpSnpGlobalOption82RemoteIdSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpSnpGlobalOption82RemoteIdSysName.setStatus("current")


class _HwDhcpSnpGlobalOption82CircuitId_Type(DisplayString):
    """Custom type hwDhcpSnpGlobalOption82CircuitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_HwDhcpSnpGlobalOption82CircuitId_Type.__name__ = "DisplayString"
_HwDhcpSnpGlobalOption82CircuitId_Object = MibScalar
hwDhcpSnpGlobalOption82CircuitId = _HwDhcpSnpGlobalOption82CircuitId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 21),
    _HwDhcpSnpGlobalOption82CircuitId_Type()
)
hwDhcpSnpGlobalOption82CircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpSnpGlobalOption82CircuitId.setStatus("current")
_HwDhcpSnpGlobalOption82PktFormatTable_Object = MibTable
hwDhcpSnpGlobalOption82PktFormatTable = _HwDhcpSnpGlobalOption82PktFormatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 22)
)
if mibBuilder.loadTexts:
    hwDhcpSnpGlobalOption82PktFormatTable.setStatus("current")
_HwDhcpSnpGlobalOption82PktFormatEntry_Object = MibTableRow
hwDhcpSnpGlobalOption82PktFormatEntry = _HwDhcpSnpGlobalOption82PktFormatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 22, 1)
)
hwDhcpSnpGlobalOption82PktFormatEntry.setIndexNames(
    (0, "HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpGlobalOption82Type"),
)
if mibBuilder.loadTexts:
    hwDhcpSnpGlobalOption82PktFormatEntry.setStatus("current")


class _HwDhcpSnpGlobalOption82Type_Type(Integer32):
    """Custom type hwDhcpSnpGlobalOption82Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("circuitid", 1),
          ("remoteid", 2))
    )


_HwDhcpSnpGlobalOption82Type_Type.__name__ = "Integer32"
_HwDhcpSnpGlobalOption82Type_Object = MibTableColumn
hwDhcpSnpGlobalOption82Type = _HwDhcpSnpGlobalOption82Type_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 22, 1, 1),
    _HwDhcpSnpGlobalOption82Type_Type()
)
hwDhcpSnpGlobalOption82Type.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDhcpSnpGlobalOption82Type.setStatus("current")


class _HwDhcpSnpGlobalOption82PktFormat_Type(Integer32):
    """Custom type hwDhcpSnpGlobalOption82PktFormat based on Integer32"""
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
        *(("common", 1),
          ("default", 4),
          ("extend", 2),
          ("userdefined", 3))
    )


_HwDhcpSnpGlobalOption82PktFormat_Type.__name__ = "Integer32"
_HwDhcpSnpGlobalOption82PktFormat_Object = MibTableColumn
hwDhcpSnpGlobalOption82PktFormat = _HwDhcpSnpGlobalOption82PktFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 22, 1, 2),
    _HwDhcpSnpGlobalOption82PktFormat_Type()
)
hwDhcpSnpGlobalOption82PktFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpSnpGlobalOption82PktFormat.setStatus("current")


class _HwDhcpSnpGlobalOption82DefString_Type(DisplayString):
    """Custom type hwDhcpSnpGlobalOption82DefString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwDhcpSnpGlobalOption82DefString_Type.__name__ = "DisplayString"
_HwDhcpSnpGlobalOption82DefString_Object = MibTableColumn
hwDhcpSnpGlobalOption82DefString = _HwDhcpSnpGlobalOption82DefString_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 22, 1, 3),
    _HwDhcpSnpGlobalOption82DefString_Type()
)
hwDhcpSnpGlobalOption82DefString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpSnpGlobalOption82DefString.setStatus("current")
_HwDhcpSnpStaticBindTable_Object = MibTable
hwDhcpSnpStaticBindTable = _HwDhcpSnpStaticBindTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 23)
)
if mibBuilder.loadTexts:
    hwDhcpSnpStaticBindTable.setStatus("current")
_HwDhcpSnpStaticBindEntry_Object = MibTableRow
hwDhcpSnpStaticBindEntry = _HwDhcpSnpStaticBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 23, 1)
)
hwDhcpSnpStaticBindEntry.setIndexNames(
    (0, "HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStaticBindIpIndex"),
    (0, "HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStaticBindMacIndex"),
    (0, "HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStaticBindPVlanIndex"),
    (0, "HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStaticBindCVlanIndex"),
    (0, "HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStaticBindIfIndex"),
)
if mibBuilder.loadTexts:
    hwDhcpSnpStaticBindEntry.setStatus("current")
_HwDhcpSnpStaticBindIpIndex_Type = IpAddress
_HwDhcpSnpStaticBindIpIndex_Object = MibTableColumn
hwDhcpSnpStaticBindIpIndex = _HwDhcpSnpStaticBindIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 23, 1, 1),
    _HwDhcpSnpStaticBindIpIndex_Type()
)
hwDhcpSnpStaticBindIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDhcpSnpStaticBindIpIndex.setStatus("current")
_HwDhcpSnpStaticBindMacIndex_Type = MacAddress
_HwDhcpSnpStaticBindMacIndex_Object = MibTableColumn
hwDhcpSnpStaticBindMacIndex = _HwDhcpSnpStaticBindMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 23, 1, 2),
    _HwDhcpSnpStaticBindMacIndex_Type()
)
hwDhcpSnpStaticBindMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDhcpSnpStaticBindMacIndex.setStatus("current")
_HwDhcpSnpStaticBindPVlanIndex_Type = VlanId
_HwDhcpSnpStaticBindPVlanIndex_Object = MibTableColumn
hwDhcpSnpStaticBindPVlanIndex = _HwDhcpSnpStaticBindPVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 23, 1, 3),
    _HwDhcpSnpStaticBindPVlanIndex_Type()
)
hwDhcpSnpStaticBindPVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDhcpSnpStaticBindPVlanIndex.setStatus("current")
_HwDhcpSnpStaticBindCVlanIndex_Type = VlanId
_HwDhcpSnpStaticBindCVlanIndex_Object = MibTableColumn
hwDhcpSnpStaticBindCVlanIndex = _HwDhcpSnpStaticBindCVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 23, 1, 4),
    _HwDhcpSnpStaticBindCVlanIndex_Type()
)
hwDhcpSnpStaticBindCVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDhcpSnpStaticBindCVlanIndex.setStatus("current")
_HwDhcpSnpStaticBindIfIndex_Type = InterfaceIndexOrZero
_HwDhcpSnpStaticBindIfIndex_Object = MibTableColumn
hwDhcpSnpStaticBindIfIndex = _HwDhcpSnpStaticBindIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 23, 1, 5),
    _HwDhcpSnpStaticBindIfIndex_Type()
)
hwDhcpSnpStaticBindIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDhcpSnpStaticBindIfIndex.setStatus("current")
_HwDhcpSnpStaticBindRowStatus_Type = RowStatus
_HwDhcpSnpStaticBindRowStatus_Object = MibTableColumn
hwDhcpSnpStaticBindRowStatus = _HwDhcpSnpStaticBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 23, 1, 20),
    _HwDhcpSnpStaticBindRowStatus_Type()
)
hwDhcpSnpStaticBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDhcpSnpStaticBindRowStatus.setStatus("current")
_HwDhcpSnpServerDetectStatus_Type = EnabledStatus
_HwDhcpSnpServerDetectStatus_Object = MibScalar
hwDhcpSnpServerDetectStatus = _HwDhcpSnpServerDetectStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 24),
    _HwDhcpSnpServerDetectStatus_Type()
)
hwDhcpSnpServerDetectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDhcpSnpServerDetectStatus.setStatus("current")
_HwDhcpSnpBdFalsePktTable_Object = MibTable
hwDhcpSnpBdFalsePktTable = _HwDhcpSnpBdFalsePktTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 25)
)
if mibBuilder.loadTexts:
    hwDhcpSnpBdFalsePktTable.setStatus("current")
_HwDhcpSnpBdFalsePktEntry_Object = MibTableRow
hwDhcpSnpBdFalsePktEntry = _HwDhcpSnpBdFalsePktEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 25, 1)
)
hwDhcpSnpBdFalsePktEntry.setIndexNames(
    (0, "HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBdIndex"),
)
if mibBuilder.loadTexts:
    hwDhcpSnpBdFalsePktEntry.setStatus("current")


class _HwDhcpSnpBdIndex_Type(Integer32):
    """Custom type hwDhcpSnpBdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_HwDhcpSnpBdIndex_Type.__name__ = "Integer32"
_HwDhcpSnpBdIndex_Object = MibTableColumn
hwDhcpSnpBdIndex = _HwDhcpSnpBdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 25, 1, 1),
    _HwDhcpSnpBdIndex_Type()
)
hwDhcpSnpBdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDhcpSnpBdIndex.setStatus("current")
_HwBdNomatchSnpBindTblDhcpPktNum_Type = Counter32
_HwBdNomatchSnpBindTblDhcpPktNum_Object = MibTableColumn
hwBdNomatchSnpBindTblDhcpPktNum = _HwBdNomatchSnpBindTblDhcpPktNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 25, 1, 2),
    _HwBdNomatchSnpBindTblDhcpPktNum_Type()
)
hwBdNomatchSnpBindTblDhcpPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBdNomatchSnpBindTblDhcpPktNum.setStatus("current")
_HwBdChaddrNomatchSrcMacDhcpPktNum_Type = Counter32
_HwBdChaddrNomatchSrcMacDhcpPktNum_Object = MibTableColumn
hwBdChaddrNomatchSrcMacDhcpPktNum = _HwBdChaddrNomatchSrcMacDhcpPktNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 25, 1, 3),
    _HwBdChaddrNomatchSrcMacDhcpPktNum_Type()
)
hwBdChaddrNomatchSrcMacDhcpPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBdChaddrNomatchSrcMacDhcpPktNum.setStatus("current")
_HwBdArpNomatchSnpBindTblPktNum_Type = Counter32
_HwBdArpNomatchSnpBindTblPktNum_Object = MibTableColumn
hwBdArpNomatchSnpBindTblPktNum = _HwBdArpNomatchSnpBindTblPktNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 25, 1, 4),
    _HwBdArpNomatchSnpBindTblPktNum_Type()
)
hwBdArpNomatchSnpBindTblPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBdArpNomatchSnpBindTblPktNum.setStatus("current")
_HwBdIpNomatchSnpBindTblPktNum_Type = Counter32
_HwBdIpNomatchSnpBindTblPktNum_Object = MibTableColumn
hwBdIpNomatchSnpBindTblPktNum = _HwBdIpNomatchSnpBindTblPktNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 25, 1, 5),
    _HwBdIpNomatchSnpBindTblPktNum_Type()
)
hwBdIpNomatchSnpBindTblPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBdIpNomatchSnpBindTblPktNum.setStatus("current")
_HwBdUntrustedReplyPktNum_Type = Counter32
_HwBdUntrustedReplyPktNum_Object = MibTableColumn
hwBdUntrustedReplyPktNum = _HwBdUntrustedReplyPktNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 25, 1, 6),
    _HwBdUntrustedReplyPktNum_Type()
)
hwBdUntrustedReplyPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBdUntrustedReplyPktNum.setStatus("current")
_HwBdSnpBindingItemNum_Type = Counter32
_HwBdSnpBindingItemNum_Object = MibTableColumn
hwBdSnpBindingItemNum = _HwBdSnpBindingItemNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 25, 1, 7),
    _HwBdSnpBindingItemNum_Type()
)
hwBdSnpBindingItemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBdSnpBindingItemNum.setStatus("current")
_HwBdSnpCfgMaxUserNum_Type = Counter32
_HwBdSnpCfgMaxUserNum_Object = MibTableColumn
hwBdSnpCfgMaxUserNum = _HwBdSnpCfgMaxUserNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 1, 25, 1, 8),
    _HwBdSnpCfgMaxUserNum_Type()
)
hwBdSnpCfgMaxUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBdSnpCfgMaxUserNum.setStatus("current")
_HwDhcpSnpTraps_ObjectIdentity = ObjectIdentity
hwDhcpSnpTraps = _HwDhcpSnpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2)
)
_HwDhcpSnpCompliance_ObjectIdentity = ObjectIdentity
hwDhcpSnpCompliance = _HwDhcpSnpCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 3)
)

# Managed Objects groups

hwDhcpSnpCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 3, 1, 1)
)
hwDhcpSnpCfgGroup.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpGlobal"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpPktRateCheck"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpPktRate"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpPktRateAlarmThreshold"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpPktRateAlarmEnable"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindTblNomatchedArpGlobalAction"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindTblNomatchedIpGlobalAction"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindTblAutosaveFilename"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindTblAutosave"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpGlobalThreshold"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpEnable"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpTrusted"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpOption82Insert"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpOption82Rebuild"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpChaddrCheck"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpChaddrAlarmThreshold"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpChaddrAlarmEnable"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpArpCheck"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindTblNomatchedArpAction"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpArpAlarmThreshold"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpArpAlarmEnable"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpIpCheck"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindTblNomatchedIpAction"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpIpAlarmThreshold"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpIpAlarmEnable"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpUntrustReplyAlarmThreshold"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpUntrustReplyAlarmEnable"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindTblCheck"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindTblAlarmThreshold"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindTblAlarmEnable"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpMatchMode"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpDynamicItemCheck"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpMaxUserNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpUserLimitAlarmThreshold"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpUserLimitAlarmEnable"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpCfgTblRowStatus"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpPktIfRateCheck"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpPktIfRate"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpPktIfRateAlarmThreshold"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpPktIfRateAlarmEnable"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpIfVlanOption82RemoteId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpIfVlanOption82CircuitId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpCarEnable"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpCarCir"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpCarPir"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpCaCbs"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpCarPbs"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpCarYellow"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpCarRed"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpGlobalOption82Format"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpGlobalOption82PacketFormat"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpGlobalOption82RemoteId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpGlobalOption82RemoteIdSysName"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpGlobalOption82CircuitId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpGlobalOption82PktFormat"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpGlobalOption82DefString"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpCarRowStatus"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpServerDetectStatus"))
)
if mibBuilder.loadTexts:
    hwDhcpSnpCfgGroup.setStatus("current")

hwDhcpSnpBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 3, 1, 2)
)
hwDhcpSnpBindGroup.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindIfDescr"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindPVlanId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindCVlanId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindVRFId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindMac"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindVsiId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindIp"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindStatus"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindLease"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBindRowStatus"))
)
if mibBuilder.loadTexts:
    hwDhcpSnpBindGroup.setStatus("current")

hwDhcpSnpStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 3, 1, 3)
)
hwDhcpSnpStatisticGroup.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticIfDescr"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticVlanId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwChaddrNomatchSrcMacDhcpPktNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwArpNomatchSnpBindTblPktNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwIpNomatchSnpBindTblPktNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwNomatchSnpBindTblDhcpPktNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwUntrustedReplyPktNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpPktRateDiscardNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticVsiId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpBindingItemNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpCfgMaxUserNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpPktIfRateDiscardNum"))
)
if mibBuilder.loadTexts:
    hwDhcpSnpStatisticGroup.setStatus("current")

hwDhcpSnpBdStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 3, 1, 5)
)
hwDhcpSnpBdStatisticGroup.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpBdIndex"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwBdNomatchSnpBindTblDhcpPktNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwBdChaddrNomatchSrcMacDhcpPktNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwBdArpNomatchSnpBindTblPktNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwBdIpNomatchSnpBindTblPktNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwBdUntrustedReplyPktNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwBdSnpBindingItemNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwBdSnpCfgMaxUserNum"))
)
if mibBuilder.loadTexts:
    hwDhcpSnpBdStatisticGroup.setStatus("current")


# Notification objects

hwDhcpSnpChaddrAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 1)
)
hwDhcpSnpChaddrAlarm.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticIfDescr"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticVlanId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwChaddrNomatchSrcMacDhcpPktNum"))
)
if mibBuilder.loadTexts:
    hwDhcpSnpChaddrAlarm.setStatus(
        "current"
    )

hwArpNomatchSnpBindTblPktAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 2)
)
hwArpNomatchSnpBindTblPktAlarm.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticIfDescr"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticVlanId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwArpNomatchSnpBindTblPktNum"))
)
if mibBuilder.loadTexts:
    hwArpNomatchSnpBindTblPktAlarm.setStatus(
        "current"
    )

hwIpNomatchSnpBindTblPktAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 3)
)
hwIpNomatchSnpBindTblPktAlarm.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticIfDescr"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticVlanId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwIpNomatchSnpBindTblPktNum"))
)
if mibBuilder.loadTexts:
    hwIpNomatchSnpBindTblPktAlarm.setStatus(
        "current"
    )

hwUntrustedReplyPktAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 4)
)
hwUntrustedReplyPktAlarm.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticIfDescr"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticVlanId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwUntrustedReplyPktNum"))
)
if mibBuilder.loadTexts:
    hwUntrustedReplyPktAlarm.setStatus(
        "current"
    )

hwNomatchSnpBindTblDhcpPktAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 5)
)
hwNomatchSnpBindTblDhcpPktAlarm.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticIfDescr"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticVlanId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwNomatchSnpBindTblDhcpPktNum"))
)
if mibBuilder.loadTexts:
    hwNomatchSnpBindTblDhcpPktAlarm.setStatus(
        "current"
    )

hwDhcpPktRateAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 6)
)
hwDhcpPktRateAlarm.setObjects(
    ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpPktRateDiscardNum")
)
if mibBuilder.loadTexts:
    hwDhcpPktRateAlarm.setStatus(
        "current"
    )

hwSnpUserNumberAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 7)
)
hwSnpUserNumberAlarm.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticIfDescr"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticVlanId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpBindingItemNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpCfgMaxUserNum"))
)
if mibBuilder.loadTexts:
    hwSnpUserNumberAlarm.setStatus(
        "current"
    )

hwSnpUserNumberAlarmIf = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 8)
)
hwSnpUserNumberAlarmIf.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticIfDescr"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpBindingItemNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpCfgMaxUserNum"))
)
if mibBuilder.loadTexts:
    hwSnpUserNumberAlarmIf.setStatus(
        "current"
    )

hwSnpUserNumberAlarmIfResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 9)
)
hwSnpUserNumberAlarmIfResume.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticIfDescr"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpBindingItemNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpCfgMaxUserNum"))
)
if mibBuilder.loadTexts:
    hwSnpUserNumberAlarmIfResume.setStatus(
        "current"
    )

hwSnpUserNumberAlarmVlan = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 10)
)
hwSnpUserNumberAlarmVlan.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticVlanId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpBindingItemNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpCfgMaxUserNum"))
)
if mibBuilder.loadTexts:
    hwSnpUserNumberAlarmVlan.setStatus(
        "current"
    )

hwSnpUserNumberAlarmVlanResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 11)
)
hwSnpUserNumberAlarmVlanResume.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticVlanId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpBindingItemNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpCfgMaxUserNum"))
)
if mibBuilder.loadTexts:
    hwSnpUserNumberAlarmVlanResume.setStatus(
        "current"
    )

hwSnpUserNumberAlarmGlobal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 12)
)
hwSnpUserNumberAlarmGlobal.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpBindingItemNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpCfgMaxUserNum"))
)
if mibBuilder.loadTexts:
    hwSnpUserNumberAlarmGlobal.setStatus(
        "current"
    )

hwSnpUserNumberAlarmGlobalResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 13)
)
hwSnpUserNumberAlarmGlobalResume.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpBindingItemNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpCfgMaxUserNum"))
)
if mibBuilder.loadTexts:
    hwSnpUserNumberAlarmGlobalResume.setStatus(
        "current"
    )

hwNdSnpUserNumberAlarmIf = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 14)
)
hwNdSnpUserNumberAlarmIf.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticIfDescr"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpBindingItemNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpCfgMaxUserNum"))
)
if mibBuilder.loadTexts:
    hwNdSnpUserNumberAlarmIf.setStatus(
        "current"
    )

hwNdSnpUserNumberAlarmIfResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 15)
)
hwNdSnpUserNumberAlarmIfResume.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticIfDescr"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpBindingItemNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpCfgMaxUserNum"))
)
if mibBuilder.loadTexts:
    hwNdSnpUserNumberAlarmIfResume.setStatus(
        "current"
    )

hwNdSnpUserNumberAlarmGlobal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 16)
)
hwNdSnpUserNumberAlarmGlobal.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpBindingItemNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpCfgMaxUserNum"))
)
if mibBuilder.loadTexts:
    hwNdSnpUserNumberAlarmGlobal.setStatus(
        "current"
    )

hwNdSnpUserNumberAlarmGlobalResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 17)
)
hwNdSnpUserNumberAlarmGlobalResume.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpBindingItemNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpCfgMaxUserNum"))
)
if mibBuilder.loadTexts:
    hwNdSnpUserNumberAlarmGlobalResume.setStatus(
        "current"
    )

hwBdNomatchSnpBindTblDhcpPktAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 18)
)
hwBdNomatchSnpBindTblDhcpPktAlarm.setObjects(
    ("HUAWEI-DHCP-SNOOPING-MIB", "hwBdNomatchSnpBindTblDhcpPktNum")
)
if mibBuilder.loadTexts:
    hwBdNomatchSnpBindTblDhcpPktAlarm.setStatus(
        "current"
    )

hwBdDhcpSnpChaddrAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 19)
)
hwBdDhcpSnpChaddrAlarm.setObjects(
    ("HUAWEI-DHCP-SNOOPING-MIB", "hwBdChaddrNomatchSrcMacDhcpPktNum")
)
if mibBuilder.loadTexts:
    hwBdDhcpSnpChaddrAlarm.setStatus(
        "current"
    )

hwBdArpNomatchSnpBindTblPktAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 20)
)
hwBdArpNomatchSnpBindTblPktAlarm.setObjects(
    ("HUAWEI-DHCP-SNOOPING-MIB", "hwBdArpNomatchSnpBindTblPktNum")
)
if mibBuilder.loadTexts:
    hwBdArpNomatchSnpBindTblPktAlarm.setStatus(
        "current"
    )

hwBdIpNomatchSnpBindTblPktAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 21)
)
hwBdIpNomatchSnpBindTblPktAlarm.setObjects(
    ("HUAWEI-DHCP-SNOOPING-MIB", "hwBdIpNomatchSnpBindTblPktNum")
)
if mibBuilder.loadTexts:
    hwBdIpNomatchSnpBindTblPktAlarm.setStatus(
        "current"
    )

hwBdUntrustedReplyPktAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 22)
)
hwBdUntrustedReplyPktAlarm.setObjects(
    ("HUAWEI-DHCP-SNOOPING-MIB", "hwBdUntrustedReplyPktNum")
)
if mibBuilder.loadTexts:
    hwBdUntrustedReplyPktAlarm.setStatus(
        "current"
    )

hwBdSnpUserNumberAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 23)
)
hwBdSnpUserNumberAlarm.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwBdSnpBindingItemNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwBdSnpCfgMaxUserNum"))
)
if mibBuilder.loadTexts:
    hwBdSnpUserNumberAlarm.setStatus(
        "current"
    )

hwDhcpSnpChaddrAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 24)
)
hwDhcpSnpChaddrAlarmResume.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticIfDescr"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticVlanId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwChaddrNomatchSrcMacDhcpPktNum"))
)
if mibBuilder.loadTexts:
    hwDhcpSnpChaddrAlarmResume.setStatus(
        "current"
    )

hwArpNomatchSnpBindTblPktAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 25)
)
hwArpNomatchSnpBindTblPktAlarmResume.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticIfDescr"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticVlanId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwArpNomatchSnpBindTblPktNum"))
)
if mibBuilder.loadTexts:
    hwArpNomatchSnpBindTblPktAlarmResume.setStatus(
        "current"
    )

hwIpNomatchSnpBindTblPktAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 26)
)
hwIpNomatchSnpBindTblPktAlarmResume.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticIfDescr"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticVlanId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwIpNomatchSnpBindTblPktNum"))
)
if mibBuilder.loadTexts:
    hwIpNomatchSnpBindTblPktAlarmResume.setStatus(
        "current"
    )

hwUntrustedReplyPktAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 27)
)
hwUntrustedReplyPktAlarmResume.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticIfDescr"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticVlanId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwUntrustedReplyPktNum"))
)
if mibBuilder.loadTexts:
    hwUntrustedReplyPktAlarmResume.setStatus(
        "current"
    )

hwNomatchSnpBindTblDhcpPktAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 28)
)
hwNomatchSnpBindTblDhcpPktAlarmResume.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticIfDescr"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticVlanId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwNomatchSnpBindTblDhcpPktNum"))
)
if mibBuilder.loadTexts:
    hwNomatchSnpBindTblDhcpPktAlarmResume.setStatus(
        "current"
    )

hwSnpUserNumberAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 2, 29)
)
hwSnpUserNumberAlarmResume.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticIfDescr"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpStatisticVlanId"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpBindingItemNum"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpCfgMaxUserNum"))
)
if mibBuilder.loadTexts:
    hwSnpUserNumberAlarmResume.setStatus(
        "current"
    )


# Notifications groups

hwDhcpSnpTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 3, 1, 4)
)
hwDhcpSnpTrapGroup.setObjects(
      *(("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpChaddrAlarm"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwArpNomatchSnpBindTblPktAlarm"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwIpNomatchSnpBindTblPktAlarm"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwUntrustedReplyPktAlarm"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwNomatchSnpBindTblDhcpPktAlarm"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpPktRateAlarm"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpUserNumberAlarm"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpUserNumberAlarmIf"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpUserNumberAlarmIfResume"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpUserNumberAlarmVlan"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpUserNumberAlarmVlanResume"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpUserNumberAlarmGlobal"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpUserNumberAlarmGlobalResume"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwNdSnpUserNumberAlarmIf"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwNdSnpUserNumberAlarmIfResume"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwNdSnpUserNumberAlarmGlobal"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwNdSnpUserNumberAlarmGlobalResume"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwBdNomatchSnpBindTblDhcpPktAlarm"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwBdDhcpSnpChaddrAlarm"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwBdArpNomatchSnpBindTblPktAlarm"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwBdIpNomatchSnpBindTblPktAlarm"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwBdUntrustedReplyPktAlarm"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwBdSnpUserNumberAlarm"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwDhcpSnpChaddrAlarmResume"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwArpNomatchSnpBindTblPktAlarmResume"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwIpNomatchSnpBindTblPktAlarmResume"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwUntrustedReplyPktAlarmResume"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwNomatchSnpBindTblDhcpPktAlarmResume"),
        ("HUAWEI-DHCP-SNOOPING-MIB", "hwSnpUserNumberAlarmResume"))
)
if mibBuilder.loadTexts:
    hwDhcpSnpTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwDhcpSnpMibGroups = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 112, 3, 1)
)
if mibBuilder.loadTexts:
    hwDhcpSnpMibGroups.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-DHCP-SNOOPING-MIB",
    **{"HWVlanId": HWVlanId,
       "HWMatchMode": HWMatchMode,
       "HWTransmitAction": HWTransmitAction,
       "hwDhcpSnpMib": hwDhcpSnpMib,
       "hwDhcpSnpObjects": hwDhcpSnpObjects,
       "hwDhcpSnpGlobal": hwDhcpSnpGlobal,
       "hwDhcpPktRateCheck": hwDhcpPktRateCheck,
       "hwDhcpPktRate": hwDhcpPktRate,
       "hwDhcpPktRateAlarmThreshold": hwDhcpPktRateAlarmThreshold,
       "hwDhcpPktRateAlarmEnable": hwDhcpPktRateAlarmEnable,
       "hwDhcpSnpBindTblNomatchedArpGlobalAction": hwDhcpSnpBindTblNomatchedArpGlobalAction,
       "hwDhcpSnpBindTblNomatchedIpGlobalAction": hwDhcpSnpBindTblNomatchedIpGlobalAction,
       "hwDhcpSnpBindTblAutosaveFilename": hwDhcpSnpBindTblAutosaveFilename,
       "hwDhcpSnpBindTblAutosave": hwDhcpSnpBindTblAutosave,
       "hwDhcpSnpGlobalThreshold": hwDhcpSnpGlobalThreshold,
       "hwDhcpPktRateDiscardNum": hwDhcpPktRateDiscardNum,
       "hwDhcpSnpCfgTable": hwDhcpSnpCfgTable,
       "hwDhcpSnpCfgEntry": hwDhcpSnpCfgEntry,
       "hwDhcpSnpIfIndex": hwDhcpSnpIfIndex,
       "hwDhcpSnpVlanIndex": hwDhcpSnpVlanIndex,
       "hwDhcpSnpVsiIndex": hwDhcpSnpVsiIndex,
       "hwDhcpSnpEnable": hwDhcpSnpEnable,
       "hwDhcpTrusted": hwDhcpTrusted,
       "hwDhcpOption82Insert": hwDhcpOption82Insert,
       "hwDhcpOption82Rebuild": hwDhcpOption82Rebuild,
       "hwDhcpChaddrCheck": hwDhcpChaddrCheck,
       "hwDhcpChaddrAlarmThreshold": hwDhcpChaddrAlarmThreshold,
       "hwDhcpChaddrAlarmEnable": hwDhcpChaddrAlarmEnable,
       "hwDhcpArpCheck": hwDhcpArpCheck,
       "hwDhcpSnpBindTblNomatchedArpAction": hwDhcpSnpBindTblNomatchedArpAction,
       "hwDhcpArpAlarmThreshold": hwDhcpArpAlarmThreshold,
       "hwDhcpArpAlarmEnable": hwDhcpArpAlarmEnable,
       "hwDhcpIpCheck": hwDhcpIpCheck,
       "hwDhcpSnpBindTblNomatchedIpAction": hwDhcpSnpBindTblNomatchedIpAction,
       "hwDhcpIpAlarmThreshold": hwDhcpIpAlarmThreshold,
       "hwDhcpIpAlarmEnable": hwDhcpIpAlarmEnable,
       "hwDhcpUntrustReplyAlarmThreshold": hwDhcpUntrustReplyAlarmThreshold,
       "hwDhcpUntrustReplyAlarmEnable": hwDhcpUntrustReplyAlarmEnable,
       "hwDhcpSnpBindTblCheck": hwDhcpSnpBindTblCheck,
       "hwDhcpSnpBindTblAlarmThreshold": hwDhcpSnpBindTblAlarmThreshold,
       "hwDhcpSnpBindTblAlarmEnable": hwDhcpSnpBindTblAlarmEnable,
       "hwDhcpSnpMatchMode": hwDhcpSnpMatchMode,
       "hwDhcpSnpDynamicItemCheck": hwDhcpSnpDynamicItemCheck,
       "hwDhcpSnpMaxUserNum": hwDhcpSnpMaxUserNum,
       "hwDhcpSnpUserLimitAlarmThreshold": hwDhcpSnpUserLimitAlarmThreshold,
       "hwDhcpSnpUserLimitAlarmEnable": hwDhcpSnpUserLimitAlarmEnable,
       "hwDhcpSnpCfgTblRowStatus": hwDhcpSnpCfgTblRowStatus,
       "hwDhcpPktIfRateCheck": hwDhcpPktIfRateCheck,
       "hwDhcpPktIfRate": hwDhcpPktIfRate,
       "hwDhcpPktIfRateAlarmThreshold": hwDhcpPktIfRateAlarmThreshold,
       "hwDhcpPktIfRateAlarmEnable": hwDhcpPktIfRateAlarmEnable,
       "hwDhcpSnpIfVlanOption82RemoteId": hwDhcpSnpIfVlanOption82RemoteId,
       "hwDhcpSnpIfVlanOption82CircuitId": hwDhcpSnpIfVlanOption82CircuitId,
       "hwDhcpSnpBindTable": hwDhcpSnpBindTable,
       "hwDhcpSnpBindEntry": hwDhcpSnpBindEntry,
       "hwDhcpSnpBindIpIndex": hwDhcpSnpBindIpIndex,
       "hwDhcpSnpBindPVlanIndex": hwDhcpSnpBindPVlanIndex,
       "hwDhcpSnpBindCVlanIndex": hwDhcpSnpBindCVlanIndex,
       "hwDhcpSnpBindVRFIdIndex": hwDhcpSnpBindVRFIdIndex,
       "hwDhcpSnpBindVsiIndex": hwDhcpSnpBindVsiIndex,
       "hwDhcpSnpBindIfDescr": hwDhcpSnpBindIfDescr,
       "hwDhcpSnpBindPVlanId": hwDhcpSnpBindPVlanId,
       "hwDhcpSnpBindCVlanId": hwDhcpSnpBindCVlanId,
       "hwDhcpSnpBindVRFId": hwDhcpSnpBindVRFId,
       "hwDhcpSnpBindVsiId": hwDhcpSnpBindVsiId,
       "hwDhcpSnpBindMac": hwDhcpSnpBindMac,
       "hwDhcpSnpBindIp": hwDhcpSnpBindIp,
       "hwDhcpSnpBindStatus": hwDhcpSnpBindStatus,
       "hwDhcpSnpBindLease": hwDhcpSnpBindLease,
       "hwDhcpSnpBindRowStatus": hwDhcpSnpBindRowStatus,
       "hwDhcpSnpFalsePktStatisticTable": hwDhcpSnpFalsePktStatisticTable,
       "hwDhcpSnpFalsePktStatisticEntry": hwDhcpSnpFalsePktStatisticEntry,
       "hwDhcpSnpStatisticIfDescr": hwDhcpSnpStatisticIfDescr,
       "hwDhcpSnpStatisticVlanId": hwDhcpSnpStatisticVlanId,
       "hwChaddrNomatchSrcMacDhcpPktNum": hwChaddrNomatchSrcMacDhcpPktNum,
       "hwArpNomatchSnpBindTblPktNum": hwArpNomatchSnpBindTblPktNum,
       "hwIpNomatchSnpBindTblPktNum": hwIpNomatchSnpBindTblPktNum,
       "hwNomatchSnpBindTblDhcpPktNum": hwNomatchSnpBindTblDhcpPktNum,
       "hwUntrustedReplyPktNum": hwUntrustedReplyPktNum,
       "hwDhcpSnpStatisticVsiId": hwDhcpSnpStatisticVsiId,
       "hwSnpBindingItemNum": hwSnpBindingItemNum,
       "hwSnpCfgMaxUserNum": hwSnpCfgMaxUserNum,
       "hwDhcpPktIfRateDiscardNum": hwDhcpPktIfRateDiscardNum,
       "hwDhcpSnpCarCfgTable": hwDhcpSnpCarCfgTable,
       "hwDhcpSnpCarCfgEntry": hwDhcpSnpCarCfgEntry,
       "hwDhcpSnpCarEnable": hwDhcpSnpCarEnable,
       "hwDhcpSnpCarCir": hwDhcpSnpCarCir,
       "hwDhcpSnpCarPir": hwDhcpSnpCarPir,
       "hwDhcpSnpCaCbs": hwDhcpSnpCaCbs,
       "hwDhcpSnpCarPbs": hwDhcpSnpCarPbs,
       "hwDhcpSnpCarYellow": hwDhcpSnpCarYellow,
       "hwDhcpSnpCarRed": hwDhcpSnpCarRed,
       "hwDhcpSnpCarRowStatus": hwDhcpSnpCarRowStatus,
       "hwDhcpSnpGlobalOption82Format": hwDhcpSnpGlobalOption82Format,
       "hwDhcpSnpGlobalOption82PacketFormat": hwDhcpSnpGlobalOption82PacketFormat,
       "hwDhcpSnpGlobalOption82RemoteId": hwDhcpSnpGlobalOption82RemoteId,
       "hwDhcpSnpGlobalOption82RemoteIdSysName": hwDhcpSnpGlobalOption82RemoteIdSysName,
       "hwDhcpSnpGlobalOption82CircuitId": hwDhcpSnpGlobalOption82CircuitId,
       "hwDhcpSnpGlobalOption82PktFormatTable": hwDhcpSnpGlobalOption82PktFormatTable,
       "hwDhcpSnpGlobalOption82PktFormatEntry": hwDhcpSnpGlobalOption82PktFormatEntry,
       "hwDhcpSnpGlobalOption82Type": hwDhcpSnpGlobalOption82Type,
       "hwDhcpSnpGlobalOption82PktFormat": hwDhcpSnpGlobalOption82PktFormat,
       "hwDhcpSnpGlobalOption82DefString": hwDhcpSnpGlobalOption82DefString,
       "hwDhcpSnpStaticBindTable": hwDhcpSnpStaticBindTable,
       "hwDhcpSnpStaticBindEntry": hwDhcpSnpStaticBindEntry,
       "hwDhcpSnpStaticBindIpIndex": hwDhcpSnpStaticBindIpIndex,
       "hwDhcpSnpStaticBindMacIndex": hwDhcpSnpStaticBindMacIndex,
       "hwDhcpSnpStaticBindPVlanIndex": hwDhcpSnpStaticBindPVlanIndex,
       "hwDhcpSnpStaticBindCVlanIndex": hwDhcpSnpStaticBindCVlanIndex,
       "hwDhcpSnpStaticBindIfIndex": hwDhcpSnpStaticBindIfIndex,
       "hwDhcpSnpStaticBindRowStatus": hwDhcpSnpStaticBindRowStatus,
       "hwDhcpSnpServerDetectStatus": hwDhcpSnpServerDetectStatus,
       "hwDhcpSnpBdFalsePktTable": hwDhcpSnpBdFalsePktTable,
       "hwDhcpSnpBdFalsePktEntry": hwDhcpSnpBdFalsePktEntry,
       "hwDhcpSnpBdIndex": hwDhcpSnpBdIndex,
       "hwBdNomatchSnpBindTblDhcpPktNum": hwBdNomatchSnpBindTblDhcpPktNum,
       "hwBdChaddrNomatchSrcMacDhcpPktNum": hwBdChaddrNomatchSrcMacDhcpPktNum,
       "hwBdArpNomatchSnpBindTblPktNum": hwBdArpNomatchSnpBindTblPktNum,
       "hwBdIpNomatchSnpBindTblPktNum": hwBdIpNomatchSnpBindTblPktNum,
       "hwBdUntrustedReplyPktNum": hwBdUntrustedReplyPktNum,
       "hwBdSnpBindingItemNum": hwBdSnpBindingItemNum,
       "hwBdSnpCfgMaxUserNum": hwBdSnpCfgMaxUserNum,
       "hwDhcpSnpTraps": hwDhcpSnpTraps,
       "hwDhcpSnpChaddrAlarm": hwDhcpSnpChaddrAlarm,
       "hwArpNomatchSnpBindTblPktAlarm": hwArpNomatchSnpBindTblPktAlarm,
       "hwIpNomatchSnpBindTblPktAlarm": hwIpNomatchSnpBindTblPktAlarm,
       "hwUntrustedReplyPktAlarm": hwUntrustedReplyPktAlarm,
       "hwNomatchSnpBindTblDhcpPktAlarm": hwNomatchSnpBindTblDhcpPktAlarm,
       "hwDhcpPktRateAlarm": hwDhcpPktRateAlarm,
       "hwSnpUserNumberAlarm": hwSnpUserNumberAlarm,
       "hwSnpUserNumberAlarmIf": hwSnpUserNumberAlarmIf,
       "hwSnpUserNumberAlarmIfResume": hwSnpUserNumberAlarmIfResume,
       "hwSnpUserNumberAlarmVlan": hwSnpUserNumberAlarmVlan,
       "hwSnpUserNumberAlarmVlanResume": hwSnpUserNumberAlarmVlanResume,
       "hwSnpUserNumberAlarmGlobal": hwSnpUserNumberAlarmGlobal,
       "hwSnpUserNumberAlarmGlobalResume": hwSnpUserNumberAlarmGlobalResume,
       "hwNdSnpUserNumberAlarmIf": hwNdSnpUserNumberAlarmIf,
       "hwNdSnpUserNumberAlarmIfResume": hwNdSnpUserNumberAlarmIfResume,
       "hwNdSnpUserNumberAlarmGlobal": hwNdSnpUserNumberAlarmGlobal,
       "hwNdSnpUserNumberAlarmGlobalResume": hwNdSnpUserNumberAlarmGlobalResume,
       "hwBdNomatchSnpBindTblDhcpPktAlarm": hwBdNomatchSnpBindTblDhcpPktAlarm,
       "hwBdDhcpSnpChaddrAlarm": hwBdDhcpSnpChaddrAlarm,
       "hwBdArpNomatchSnpBindTblPktAlarm": hwBdArpNomatchSnpBindTblPktAlarm,
       "hwBdIpNomatchSnpBindTblPktAlarm": hwBdIpNomatchSnpBindTblPktAlarm,
       "hwBdUntrustedReplyPktAlarm": hwBdUntrustedReplyPktAlarm,
       "hwBdSnpUserNumberAlarm": hwBdSnpUserNumberAlarm,
       "hwDhcpSnpChaddrAlarmResume": hwDhcpSnpChaddrAlarmResume,
       "hwArpNomatchSnpBindTblPktAlarmResume": hwArpNomatchSnpBindTblPktAlarmResume,
       "hwIpNomatchSnpBindTblPktAlarmResume": hwIpNomatchSnpBindTblPktAlarmResume,
       "hwUntrustedReplyPktAlarmResume": hwUntrustedReplyPktAlarmResume,
       "hwNomatchSnpBindTblDhcpPktAlarmResume": hwNomatchSnpBindTblDhcpPktAlarmResume,
       "hwSnpUserNumberAlarmResume": hwSnpUserNumberAlarmResume,
       "hwDhcpSnpCompliance": hwDhcpSnpCompliance,
       "hwDhcpSnpMibGroups": hwDhcpSnpMibGroups,
       "hwDhcpSnpCfgGroup": hwDhcpSnpCfgGroup,
       "hwDhcpSnpBindGroup": hwDhcpSnpBindGroup,
       "hwDhcpSnpStatisticGroup": hwDhcpSnpStatisticGroup,
       "hwDhcpSnpTrapGroup": hwDhcpSnpTrapGroup,
       "hwDhcpSnpBdStatisticGroup": hwDhcpSnpBdStatisticGroup}
)
