# SNMP MIB module (HUAWEI-L2MAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-L2MAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:20 2024
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

(PhysicalIndex,
 entPhysicalIndex,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex",
    "entPhysicalName")

(hwBaseTrapEventType,
 hwBaseTrapProbableCause,
 hwBaseTrapSeverity) = mibBuilder.importSymbols(
    "HUAWEI-BASE-TRAP-MIB",
    "hwBaseTrapEventType",
    "hwBaseTrapProbableCause",
    "hwBaseTrapSeverity")

(hwL2IfPortName,) = mibBuilder.importSymbols(
    "HUAWEI-L2IF-MIB",
    "hwL2IfPortName")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(hwVplsVsiName,) = mibBuilder.importSymbols(
    "HUAWEI-VPLS-EXT-MIB",
    "hwVplsVsiName")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifDescr) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifDescr")

(EnableValue,) = mibBuilder.importSymbols(
    "NQA-MIB",
    "EnableValue")

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

hwL2MAM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2)
)
hwL2MAM.setRevisions(
        ("2015-08-25 00:00",
         "2015-08-06 00:00",
         "2015-07-23 00:00",
         "2014-12-19 23:43",
         "2014-07-25 09:45",
         "2014-06-16 09:45",
         "2014-06-06 09:45",
         "2014-01-21 00:00",
         "2014-05-10 00:00",
         "2014-03-13 00:00",
         "2013-09-07 00:00",
         "2013-05-24 00:00",
         "2013-05-14 00:00",
         "2004-06-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanIndex(Unsigned32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_HwL2Mgmt_ObjectIdentity = ObjectIdentity
hwL2Mgmt = _HwL2Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42)
)
_HwL2MAMObjects_ObjectIdentity = ObjectIdentity
hwL2MAMObjects = _HwL2MAMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1)
)
_HwL2MaxMacLimit_Type = Integer32
_HwL2MaxMacLimit_Object = MibScalar
hwL2MaxMacLimit = _HwL2MaxMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 1),
    _HwL2MaxMacLimit_Type()
)
hwL2MaxMacLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2MaxMacLimit.setStatus("current")
_HwdbCfgFdbTable_Object = MibTable
hwdbCfgFdbTable = _HwdbCfgFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hwdbCfgFdbTable.setStatus("current")
_HwdbCfgFdbEntry_Object = MibTableRow
hwdbCfgFdbEntry = _HwdbCfgFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 2, 1)
)
hwdbCfgFdbEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwCfgFdbMac"),
    (0, "HUAWEI-L2MAM-MIB", "hwCfgFdbVlanId"),
    (0, "HUAWEI-L2MAM-MIB", "hwCfgFdbVsiName"),
)
if mibBuilder.loadTexts:
    hwdbCfgFdbEntry.setStatus("current")
_HwCfgFdbMac_Type = MacAddress
_HwCfgFdbMac_Object = MibTableColumn
hwCfgFdbMac = _HwCfgFdbMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 2, 1, 1),
    _HwCfgFdbMac_Type()
)
hwCfgFdbMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCfgFdbMac.setStatus("current")


class _HwCfgFdbVlanId_Type(VlanIndex):
    """Custom type hwCfgFdbVlanId based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwCfgFdbVlanId_Type.__name__ = "VlanIndex"
_HwCfgFdbVlanId_Object = MibTableColumn
hwCfgFdbVlanId = _HwCfgFdbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 2, 1, 2),
    _HwCfgFdbVlanId_Type()
)
hwCfgFdbVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCfgFdbVlanId.setStatus("current")


class _HwCfgFdbVsiName_Type(OctetString):
    """Custom type hwCfgFdbVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwCfgFdbVsiName_Type.__name__ = "OctetString"
_HwCfgFdbVsiName_Object = MibTableColumn
hwCfgFdbVsiName = _HwCfgFdbVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 2, 1, 3),
    _HwCfgFdbVsiName_Type()
)
hwCfgFdbVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCfgFdbVsiName.setStatus("current")
_HwCfgFdbPort_Type = InterfaceIndexOrZero
_HwCfgFdbPort_Object = MibTableColumn
hwCfgFdbPort = _HwCfgFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 2, 1, 4),
    _HwCfgFdbPort_Type()
)
hwCfgFdbPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgFdbPort.setStatus("current")


class _HwCfgFdbType_Type(Integer32):
    """Custom type hwCfgFdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blackhole", 3),
          ("static", 2))
    )


_HwCfgFdbType_Type.__name__ = "Integer32"
_HwCfgFdbType_Object = MibTableColumn
hwCfgFdbType = _HwCfgFdbType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 2, 1, 5),
    _HwCfgFdbType_Type()
)
hwCfgFdbType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgFdbType.setStatus("current")
_HwCfgFdbRowstatus_Type = RowStatus
_HwCfgFdbRowstatus_Object = MibTableColumn
hwCfgFdbRowstatus = _HwCfgFdbRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 2, 1, 6),
    _HwCfgFdbRowstatus_Type()
)
hwCfgFdbRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgFdbRowstatus.setStatus("current")
_HwCfgFdbAtmPort_Type = InterfaceIndexOrZero
_HwCfgFdbAtmPort_Object = MibTableColumn
hwCfgFdbAtmPort = _HwCfgFdbAtmPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 2, 1, 7),
    _HwCfgFdbAtmPort_Type()
)
hwCfgFdbAtmPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgFdbAtmPort.setStatus("current")


class _HwCfgFdbVpi_Type(Integer32):
    """Custom type hwCfgFdbVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HwCfgFdbVpi_Type.__name__ = "Integer32"
_HwCfgFdbVpi_Object = MibTableColumn
hwCfgFdbVpi = _HwCfgFdbVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 2, 1, 8),
    _HwCfgFdbVpi_Type()
)
hwCfgFdbVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgFdbVpi.setStatus("current")


class _HwCfgFdbVci_Type(Integer32):
    """Custom type hwCfgFdbVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
        ValueRangeConstraint(65535, 65535),
    )


_HwCfgFdbVci_Type.__name__ = "Integer32"
_HwCfgFdbVci_Object = MibTableColumn
hwCfgFdbVci = _HwCfgFdbVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 2, 1, 9),
    _HwCfgFdbVci_Type()
)
hwCfgFdbVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgFdbVci.setStatus("current")


class _HwCfgFdbCeDefault_Type(Integer32):
    """Custom type hwCfgFdbCeDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ceDefault", 1),
          ("noCeDefault", 0))
    )


_HwCfgFdbCeDefault_Type.__name__ = "Integer32"
_HwCfgFdbCeDefault_Object = MibTableColumn
hwCfgFdbCeDefault = _HwCfgFdbCeDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 2, 1, 10),
    _HwCfgFdbCeDefault_Type()
)
hwCfgFdbCeDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwCfgFdbCeDefault.setStatus("current")
_HwdbDynFdbTable_Object = MibTable
hwdbDynFdbTable = _HwdbDynFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hwdbDynFdbTable.setStatus("current")
_HwdbDynFdbEntry_Object = MibTableRow
hwdbDynFdbEntry = _HwdbDynFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 3, 1)
)
hwdbDynFdbEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwDynFdbMac"),
    (0, "HUAWEI-L2MAM-MIB", "hwDynFdbVlanId"),
    (0, "HUAWEI-L2MAM-MIB", "hwDynFdbVsiName"),
)
if mibBuilder.loadTexts:
    hwdbDynFdbEntry.setStatus("current")
_HwDynFdbMac_Type = MacAddress
_HwDynFdbMac_Object = MibTableColumn
hwDynFdbMac = _HwDynFdbMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 3, 1, 1),
    _HwDynFdbMac_Type()
)
hwDynFdbMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDynFdbMac.setStatus("current")


class _HwDynFdbVlanId_Type(VlanIndex):
    """Custom type hwDynFdbVlanId based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwDynFdbVlanId_Type.__name__ = "VlanIndex"
_HwDynFdbVlanId_Object = MibTableColumn
hwDynFdbVlanId = _HwDynFdbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 3, 1, 2),
    _HwDynFdbVlanId_Type()
)
hwDynFdbVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDynFdbVlanId.setStatus("current")


class _HwDynFdbVsiName_Type(OctetString):
    """Custom type hwDynFdbVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwDynFdbVsiName_Type.__name__ = "OctetString"
_HwDynFdbVsiName_Object = MibTableColumn
hwDynFdbVsiName = _HwDynFdbVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 3, 1, 3),
    _HwDynFdbVsiName_Type()
)
hwDynFdbVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDynFdbVsiName.setStatus("current")
_HwDynFdbPort_Type = InterfaceIndexOrZero
_HwDynFdbPort_Object = MibTableColumn
hwDynFdbPort = _HwDynFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 3, 1, 4),
    _HwDynFdbPort_Type()
)
hwDynFdbPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDynFdbPort.setStatus("current")
_HwDynFdbAtmPort_Type = InterfaceIndexOrZero
_HwDynFdbAtmPort_Object = MibTableColumn
hwDynFdbAtmPort = _HwDynFdbAtmPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 3, 1, 5),
    _HwDynFdbAtmPort_Type()
)
hwDynFdbAtmPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDynFdbAtmPort.setStatus("current")


class _HwDynFdbVpi_Type(Integer32):
    """Custom type hwDynFdbVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
        ValueRangeConstraint(65535, 65535),
    )


_HwDynFdbVpi_Type.__name__ = "Integer32"
_HwDynFdbVpi_Object = MibTableColumn
hwDynFdbVpi = _HwDynFdbVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 3, 1, 6),
    _HwDynFdbVpi_Type()
)
hwDynFdbVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDynFdbVpi.setStatus("current")


class _HwDynFdbVci_Type(Integer32):
    """Custom type hwDynFdbVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
        ValueRangeConstraint(65535, 65535),
    )


_HwDynFdbVci_Type.__name__ = "Integer32"
_HwDynFdbVci_Object = MibTableColumn
hwDynFdbVci = _HwDynFdbVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 3, 1, 7),
    _HwDynFdbVci_Type()
)
hwDynFdbVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDynFdbVci.setStatus("current")
_HwDynFdbRowstatus_Type = RowStatus
_HwDynFdbRowstatus_Object = MibTableColumn
hwDynFdbRowstatus = _HwDynFdbRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 3, 1, 8),
    _HwDynFdbRowstatus_Type()
)
hwDynFdbRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDynFdbRowstatus.setStatus("current")
_HwDynSecurityFdbToStaticEnable_Type = EnableValue
_HwDynSecurityFdbToStaticEnable_Object = MibTableColumn
hwDynSecurityFdbToStaticEnable = _HwDynSecurityFdbToStaticEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 3, 1, 9),
    _HwDynSecurityFdbToStaticEnable_Type()
)
hwDynSecurityFdbToStaticEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDynSecurityFdbToStaticEnable.setStatus("current")
_HwMacLimitTable_Object = MibTable
hwMacLimitTable = _HwMacLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hwMacLimitTable.setStatus("current")
_HwMacLimitEntry_Object = MibTableRow
hwMacLimitEntry = _HwMacLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 4, 1)
)
hwMacLimitEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwMacLimitPort"),
    (0, "HUAWEI-L2MAM-MIB", "hwMacLimitVlanId"),
    (0, "HUAWEI-L2MAM-MIB", "hwMacLimitVsiName"),
)
if mibBuilder.loadTexts:
    hwMacLimitEntry.setStatus("current")
_HwMacLimitPort_Type = InterfaceIndexOrZero
_HwMacLimitPort_Object = MibTableColumn
hwMacLimitPort = _HwMacLimitPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 4, 1, 1),
    _HwMacLimitPort_Type()
)
hwMacLimitPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacLimitPort.setStatus("current")


class _HwMacLimitVlanId_Type(Integer32):
    """Custom type hwMacLimitVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwMacLimitVlanId_Type.__name__ = "Integer32"
_HwMacLimitVlanId_Object = MibTableColumn
hwMacLimitVlanId = _HwMacLimitVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 4, 1, 2),
    _HwMacLimitVlanId_Type()
)
hwMacLimitVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMacLimitVlanId.setStatus("current")


class _HwMacLimitVsiName_Type(OctetString):
    """Custom type hwMacLimitVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwMacLimitVsiName_Type.__name__ = "OctetString"
_HwMacLimitVsiName_Object = MibTableColumn
hwMacLimitVsiName = _HwMacLimitVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 4, 1, 3),
    _HwMacLimitVsiName_Type()
)
hwMacLimitVsiName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMacLimitVsiName.setStatus("current")


class _HwMacLimitMaxMac_Type(Integer32):
    """Custom type hwMacLimitMaxMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131072),
    )


_HwMacLimitMaxMac_Type.__name__ = "Integer32"
_HwMacLimitMaxMac_Object = MibTableColumn
hwMacLimitMaxMac = _HwMacLimitMaxMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 4, 1, 4),
    _HwMacLimitMaxMac_Type()
)
hwMacLimitMaxMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacLimitMaxMac.setStatus("current")


class _HwMacLimitMaxRate_Type(Integer32):
    """Custom type hwMacLimitMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HwMacLimitMaxRate_Type.__name__ = "Integer32"
_HwMacLimitMaxRate_Object = MibTableColumn
hwMacLimitMaxRate = _HwMacLimitMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 4, 1, 5),
    _HwMacLimitMaxRate_Type()
)
hwMacLimitMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacLimitMaxRate.setStatus("current")


class _HwMacLimitAction_Type(Integer32):
    """Custom type hwMacLimitAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 2))
    )


_HwMacLimitAction_Type.__name__ = "Integer32"
_HwMacLimitAction_Object = MibTableColumn
hwMacLimitAction = _HwMacLimitAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 4, 1, 6),
    _HwMacLimitAction_Type()
)
hwMacLimitAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacLimitAction.setStatus("current")


class _HwMacLimitAlarm_Type(Integer32):
    """Custom type hwMacLimitAlarm based on Integer32"""
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


_HwMacLimitAlarm_Type.__name__ = "Integer32"
_HwMacLimitAlarm_Object = MibTableColumn
hwMacLimitAlarm = _HwMacLimitAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 4, 1, 7),
    _HwMacLimitAlarm_Type()
)
hwMacLimitAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacLimitAlarm.setStatus("current")
_HwMacLimitRowstatus_Type = RowStatus
_HwMacLimitRowstatus_Object = MibTableColumn
hwMacLimitRowstatus = _HwMacLimitRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 4, 1, 8),
    _HwMacLimitRowstatus_Type()
)
hwMacLimitRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacLimitRowstatus.setStatus("current")


class _HwMacAddressLearn_Type(Integer32):
    """Custom type hwMacAddressLearn based on Integer32"""
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


_HwMacAddressLearn_Type.__name__ = "Integer32"
_HwMacAddressLearn_Object = MibTableColumn
hwMacAddressLearn = _HwMacAddressLearn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 4, 1, 9),
    _HwMacAddressLearn_Type()
)
hwMacAddressLearn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacAddressLearn.setStatus("current")


class _HwMacDynAddressLearnNum_Type(Integer32):
    """Custom type hwMacDynAddressLearnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131072),
    )


_HwMacDynAddressLearnNum_Type.__name__ = "Integer32"
_HwMacDynAddressLearnNum_Object = MibTableColumn
hwMacDynAddressLearnNum = _HwMacDynAddressLearnNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 4, 1, 10),
    _HwMacDynAddressLearnNum_Type()
)
hwMacDynAddressLearnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacDynAddressLearnNum.setStatus("current")


class _HwMacSecureAddressLearnNum_Type(Integer32):
    """Custom type hwMacSecureAddressLearnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131072),
    )


_HwMacSecureAddressLearnNum_Type.__name__ = "Integer32"
_HwMacSecureAddressLearnNum_Object = MibTableColumn
hwMacSecureAddressLearnNum = _HwMacSecureAddressLearnNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 4, 1, 11),
    _HwMacSecureAddressLearnNum_Type()
)
hwMacSecureAddressLearnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacSecureAddressLearnNum.setStatus("current")
_HwMacUsageTable_Object = MibTable
hwMacUsageTable = _HwMacUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hwMacUsageTable.setStatus("current")
_HwMacUsageEntry_Object = MibTableRow
hwMacUsageEntry = _HwMacUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 5, 1)
)
hwMacUsageEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hwMacUsageEntry.setStatus("current")


class _HwMacEntityUsage_Type(Integer32):
    """Custom type hwMacEntityUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwMacEntityUsage_Type.__name__ = "Integer32"
_HwMacEntityUsage_Object = MibTableColumn
hwMacEntityUsage = _HwMacEntityUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 5, 1, 1),
    _HwMacEntityUsage_Type()
)
hwMacEntityUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacEntityUsage.setStatus("current")


class _HwMacEntityUsageThreshold_Type(Integer32):
    """Custom type hwMacEntityUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwMacEntityUsageThreshold_Type.__name__ = "Integer32"
_HwMacEntityUsageThreshold_Object = MibTableColumn
hwMacEntityUsageThreshold = _HwMacEntityUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 5, 1, 2),
    _HwMacEntityUsageThreshold_Type()
)
hwMacEntityUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacEntityUsageThreshold.setStatus("current")
_HwdbCfg3tupleFdbTable_Object = MibTable
hwdbCfg3tupleFdbTable = _HwdbCfg3tupleFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 6)
)
if mibBuilder.loadTexts:
    hwdbCfg3tupleFdbTable.setStatus("current")
_HwdbCfg3tupleFdbEntry_Object = MibTableRow
hwdbCfg3tupleFdbEntry = _HwdbCfg3tupleFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 6, 1)
)
hwdbCfg3tupleFdbEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwdbCfg3tupleFdbMac"),
    (0, "HUAWEI-L2MAM-MIB", "hwdbCfg3tupleFdbVlanId"),
    (0, "HUAWEI-L2MAM-MIB", "hwdbCfg3tupleFdbInPort"),
)
if mibBuilder.loadTexts:
    hwdbCfg3tupleFdbEntry.setStatus("current")
_HwdbCfg3tupleFdbMac_Type = MacAddress
_HwdbCfg3tupleFdbMac_Object = MibTableColumn
hwdbCfg3tupleFdbMac = _HwdbCfg3tupleFdbMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 6, 1, 1),
    _HwdbCfg3tupleFdbMac_Type()
)
hwdbCfg3tupleFdbMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwdbCfg3tupleFdbMac.setStatus("current")


class _HwdbCfg3tupleFdbVlanId_Type(Integer32):
    """Custom type hwdbCfg3tupleFdbVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwdbCfg3tupleFdbVlanId_Type.__name__ = "Integer32"
_HwdbCfg3tupleFdbVlanId_Object = MibTableColumn
hwdbCfg3tupleFdbVlanId = _HwdbCfg3tupleFdbVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 6, 1, 2),
    _HwdbCfg3tupleFdbVlanId_Type()
)
hwdbCfg3tupleFdbVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwdbCfg3tupleFdbVlanId.setStatus("current")
_HwdbCfg3tupleFdbInPort_Type = InterfaceIndex
_HwdbCfg3tupleFdbInPort_Object = MibTableColumn
hwdbCfg3tupleFdbInPort = _HwdbCfg3tupleFdbInPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 6, 1, 3),
    _HwdbCfg3tupleFdbInPort_Type()
)
hwdbCfg3tupleFdbInPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwdbCfg3tupleFdbInPort.setStatus("current")
_HwdbCfg3tupleFdbOutPort_Type = InterfaceIndex
_HwdbCfg3tupleFdbOutPort_Object = MibTableColumn
hwdbCfg3tupleFdbOutPort = _HwdbCfg3tupleFdbOutPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 6, 1, 4),
    _HwdbCfg3tupleFdbOutPort_Type()
)
hwdbCfg3tupleFdbOutPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwdbCfg3tupleFdbOutPort.setStatus("current")
_HwdbCfg3tupleFdbRowStatus_Type = RowStatus
_HwdbCfg3tupleFdbRowStatus_Object = MibTableColumn
hwdbCfg3tupleFdbRowStatus = _HwdbCfg3tupleFdbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 6, 1, 5),
    _HwdbCfg3tupleFdbRowStatus_Type()
)
hwdbCfg3tupleFdbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwdbCfg3tupleFdbRowStatus.setStatus("current")
_HwL2MacTraps_ObjectIdentity = ObjectIdentity
hwL2MacTraps = _HwL2MacTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7)
)
_HwUntargetMacNum_Type = Counter64
_HwUntargetMacNum_Object = MibScalar
hwUntargetMacNum = _HwUntargetMacNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 8),
    _HwUntargetMacNum_Type()
)
hwUntargetMacNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUntargetMacNum.setStatus("current")


class _HwMacAgingTime_Type(Integer32):
    """Custom type hwMacAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
        ValueRangeConstraint(0, 0),
    )


_HwMacAgingTime_Type.__name__ = "Integer32"
_HwMacAgingTime_Object = MibScalar
hwMacAgingTime = _HwMacAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 9),
    _HwMacAgingTime_Type()
)
hwMacAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacAgingTime.setStatus("current")
_HwMacRestrict_Type = EnabledStatus
_HwMacRestrict_Object = MibScalar
hwMacRestrict = _HwMacRestrict_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 10),
    _HwMacRestrict_Type()
)
hwMacRestrict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacRestrict.setStatus("current")
_HwPortSecurityTable_Object = MibTable
hwPortSecurityTable = _HwPortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 11)
)
if mibBuilder.loadTexts:
    hwPortSecurityTable.setStatus("current")
_HwPortSecurityEntry_Object = MibTableRow
hwPortSecurityEntry = _HwPortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 11, 1)
)
hwPortSecurityEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwPortSecurityPort"),
)
if mibBuilder.loadTexts:
    hwPortSecurityEntry.setStatus("current")
_HwPortSecurityPort_Type = InterfaceIndexOrZero
_HwPortSecurityPort_Object = MibTableColumn
hwPortSecurityPort = _HwPortSecurityPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 11, 1, 1),
    _HwPortSecurityPort_Type()
)
hwPortSecurityPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPortSecurityPort.setStatus("current")
_HwPortSecurityEnabled_Type = EnabledStatus
_HwPortSecurityEnabled_Object = MibTableColumn
hwPortSecurityEnabled = _HwPortSecurityEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 11, 1, 2),
    _HwPortSecurityEnabled_Type()
)
hwPortSecurityEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortSecurityEnabled.setStatus("current")


class _HwPortSecurityProtectAction_Type(Integer32):
    """Custom type hwPortSecurityProtectAction based on Integer32"""
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
        *(("noaction", 4),
          ("protect", 2),
          ("restrict", 1),
          ("shutdown", 3))
    )


_HwPortSecurityProtectAction_Type.__name__ = "Integer32"
_HwPortSecurityProtectAction_Object = MibTableColumn
hwPortSecurityProtectAction = _HwPortSecurityProtectAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 11, 1, 3),
    _HwPortSecurityProtectAction_Type()
)
hwPortSecurityProtectAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortSecurityProtectAction.setStatus("current")
_HwPortSecurityAllDynToStaticEnable_Type = EnableValue
_HwPortSecurityAllDynToStaticEnable_Object = MibTableColumn
hwPortSecurityAllDynToStaticEnable = _HwPortSecurityAllDynToStaticEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 11, 1, 4),
    _HwPortSecurityAllDynToStaticEnable_Type()
)
hwPortSecurityAllDynToStaticEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortSecurityAllDynToStaticEnable.setStatus("current")
_HwPortSecurityAllDynToStickyEnable_Type = EnableValue
_HwPortSecurityAllDynToStickyEnable_Object = MibTableColumn
hwPortSecurityAllDynToStickyEnable = _HwPortSecurityAllDynToStickyEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 11, 1, 5),
    _HwPortSecurityAllDynToStickyEnable_Type()
)
hwPortSecurityAllDynToStickyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortSecurityAllDynToStickyEnable.setStatus("current")


class _HwPortSecurityMaxMacNum_Type(Integer32):
    """Custom type hwPortSecurityMaxMacNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_HwPortSecurityMaxMacNum_Type.__name__ = "Integer32"
_HwPortSecurityMaxMacNum_Object = MibTableColumn
hwPortSecurityMaxMacNum = _HwPortSecurityMaxMacNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 11, 1, 6),
    _HwPortSecurityMaxMacNum_Type()
)
hwPortSecurityMaxMacNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPortSecurityMaxMacNum.setStatus("current")
_HwMacLimitGlobalRuleTable_Object = MibTable
hwMacLimitGlobalRuleTable = _HwMacLimitGlobalRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 12)
)
if mibBuilder.loadTexts:
    hwMacLimitGlobalRuleTable.setStatus("current")
_HwMacLimitGlobalRuleEntry_Object = MibTableRow
hwMacLimitGlobalRuleEntry = _HwMacLimitGlobalRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 12, 1)
)
hwMacLimitGlobalRuleEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwMacLimitGlobalRuleName"),
)
if mibBuilder.loadTexts:
    hwMacLimitGlobalRuleEntry.setStatus("current")


class _HwMacLimitGlobalRuleName_Type(OctetString):
    """Custom type hwMacLimitGlobalRuleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwMacLimitGlobalRuleName_Type.__name__ = "OctetString"
_HwMacLimitGlobalRuleName_Object = MibTableColumn
hwMacLimitGlobalRuleName = _HwMacLimitGlobalRuleName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 12, 1, 1),
    _HwMacLimitGlobalRuleName_Type()
)
hwMacLimitGlobalRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacLimitGlobalRuleName.setStatus("current")


class _HwMacLimitRuleMaxMac_Type(Integer32):
    """Custom type hwMacLimitRuleMaxMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131072),
    )


_HwMacLimitRuleMaxMac_Type.__name__ = "Integer32"
_HwMacLimitRuleMaxMac_Object = MibTableColumn
hwMacLimitRuleMaxMac = _HwMacLimitRuleMaxMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 12, 1, 11),
    _HwMacLimitRuleMaxMac_Type()
)
hwMacLimitRuleMaxMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacLimitRuleMaxMac.setStatus("current")


class _HwMacLimitRuleMaxRate_Type(Integer32):
    """Custom type hwMacLimitRuleMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HwMacLimitRuleMaxRate_Type.__name__ = "Integer32"
_HwMacLimitRuleMaxRate_Object = MibTableColumn
hwMacLimitRuleMaxRate = _HwMacLimitRuleMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 12, 1, 12),
    _HwMacLimitRuleMaxRate_Type()
)
hwMacLimitRuleMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacLimitRuleMaxRate.setStatus("current")


class _HwMacLimitRuleAction_Type(Integer32):
    """Custom type hwMacLimitRuleAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 2))
    )


_HwMacLimitRuleAction_Type.__name__ = "Integer32"
_HwMacLimitRuleAction_Object = MibTableColumn
hwMacLimitRuleAction = _HwMacLimitRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 12, 1, 13),
    _HwMacLimitRuleAction_Type()
)
hwMacLimitRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacLimitRuleAction.setStatus("current")


class _HwMacLimitRuleAlarm_Type(Integer32):
    """Custom type hwMacLimitRuleAlarm based on Integer32"""
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


_HwMacLimitRuleAlarm_Type.__name__ = "Integer32"
_HwMacLimitRuleAlarm_Object = MibTableColumn
hwMacLimitRuleAlarm = _HwMacLimitRuleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 12, 1, 14),
    _HwMacLimitRuleAlarm_Type()
)
hwMacLimitRuleAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacLimitRuleAlarm.setStatus("current")
_HwMacLimitRuleRowstatus_Type = RowStatus
_HwMacLimitRuleRowstatus_Object = MibTableColumn
hwMacLimitRuleRowstatus = _HwMacLimitRuleRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 12, 1, 51),
    _HwMacLimitRuleRowstatus_Type()
)
hwMacLimitRuleRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacLimitRuleRowstatus.setStatus("current")


class _HwMacRuleDynAddressLearnNum_Type(Integer32):
    """Custom type hwMacRuleDynAddressLearnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131072),
    )


_HwMacRuleDynAddressLearnNum_Type.__name__ = "Integer32"
_HwMacRuleDynAddressLearnNum_Object = MibTableColumn
hwMacRuleDynAddressLearnNum = _HwMacRuleDynAddressLearnNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 12, 1, 52),
    _HwMacRuleDynAddressLearnNum_Type()
)
hwMacRuleDynAddressLearnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRuleDynAddressLearnNum.setStatus("current")
_HwMacLimitApplyRuleTable_Object = MibTable
hwMacLimitApplyRuleTable = _HwMacLimitApplyRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 13)
)
if mibBuilder.loadTexts:
    hwMacLimitApplyRuleTable.setStatus("current")
_HwMacLimitApplyRuleEntry_Object = MibTableRow
hwMacLimitApplyRuleEntry = _HwMacLimitApplyRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 13, 1)
)
hwMacLimitApplyRuleEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwMacLimitApplyPort"),
    (0, "HUAWEI-L2MAM-MIB", "hwMacLimitApplyVlanId"),
)
if mibBuilder.loadTexts:
    hwMacLimitApplyRuleEntry.setStatus("current")
_HwMacLimitApplyPort_Type = InterfaceIndexOrZero
_HwMacLimitApplyPort_Object = MibTableColumn
hwMacLimitApplyPort = _HwMacLimitApplyPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 13, 1, 1),
    _HwMacLimitApplyPort_Type()
)
hwMacLimitApplyPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacLimitApplyPort.setStatus("current")


class _HwMacLimitApplyVlanId_Type(Integer32):
    """Custom type hwMacLimitApplyVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwMacLimitApplyVlanId_Type.__name__ = "Integer32"
_HwMacLimitApplyVlanId_Object = MibTableColumn
hwMacLimitApplyVlanId = _HwMacLimitApplyVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 13, 1, 2),
    _HwMacLimitApplyVlanId_Type()
)
hwMacLimitApplyVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacLimitApplyVlanId.setStatus("current")


class _HwMacLimitApplyRuleName_Type(OctetString):
    """Custom type hwMacLimitApplyRuleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwMacLimitApplyRuleName_Type.__name__ = "OctetString"
_HwMacLimitApplyRuleName_Object = MibTableColumn
hwMacLimitApplyRuleName = _HwMacLimitApplyRuleName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 13, 1, 11),
    _HwMacLimitApplyRuleName_Type()
)
hwMacLimitApplyRuleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacLimitApplyRuleName.setStatus("current")
_HwMacLimitApplyRowstatus_Type = RowStatus
_HwMacLimitApplyRowstatus_Object = MibTableColumn
hwMacLimitApplyRowstatus = _HwMacLimitApplyRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 13, 1, 51),
    _HwMacLimitApplyRowstatus_Type()
)
hwMacLimitApplyRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacLimitApplyRowstatus.setStatus("current")
_HwMacGlobalStatistics_Type = Integer32
_HwMacGlobalStatistics_Object = MibScalar
hwMacGlobalStatistics = _HwMacGlobalStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 14),
    _HwMacGlobalStatistics_Type()
)
hwMacGlobalStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacGlobalStatistics.setStatus("current")
_HwMacIfStatisticsTable_Object = MibTable
hwMacIfStatisticsTable = _HwMacIfStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 15)
)
if mibBuilder.loadTexts:
    hwMacIfStatisticsTable.setStatus("current")
_HwMacIfStatisticsEntry_Object = MibTableRow
hwMacIfStatisticsEntry = _HwMacIfStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 15, 1)
)
hwMacIfStatisticsEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwMacIfStatisticsIfIndex"),
)
if mibBuilder.loadTexts:
    hwMacIfStatisticsEntry.setStatus("current")
_HwMacIfStatisticsIfIndex_Type = InterfaceIndex
_HwMacIfStatisticsIfIndex_Object = MibTableColumn
hwMacIfStatisticsIfIndex = _HwMacIfStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 15, 1, 1),
    _HwMacIfStatisticsIfIndex_Type()
)
hwMacIfStatisticsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacIfStatisticsIfIndex.setStatus("current")
_HwMacIfStatistics_Type = Integer32
_HwMacIfStatistics_Object = MibTableColumn
hwMacIfStatistics = _HwMacIfStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 15, 1, 2),
    _HwMacIfStatistics_Type()
)
hwMacIfStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacIfStatistics.setStatus("current")
_HwMacSlotStatisticsTable_Object = MibTable
hwMacSlotStatisticsTable = _HwMacSlotStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 16)
)
if mibBuilder.loadTexts:
    hwMacSlotStatisticsTable.setStatus("current")
_HwMacSlotStatisticsEntry_Object = MibTableRow
hwMacSlotStatisticsEntry = _HwMacSlotStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 16, 1)
)
hwMacSlotStatisticsEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwMacSlotStatisticsSlotId"),
)
if mibBuilder.loadTexts:
    hwMacSlotStatisticsEntry.setStatus("current")


class _HwMacSlotStatisticsSlotId_Type(Integer32):
    """Custom type hwMacSlotStatisticsSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwMacSlotStatisticsSlotId_Type.__name__ = "Integer32"
_HwMacSlotStatisticsSlotId_Object = MibTableColumn
hwMacSlotStatisticsSlotId = _HwMacSlotStatisticsSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 16, 1, 1),
    _HwMacSlotStatisticsSlotId_Type()
)
hwMacSlotStatisticsSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacSlotStatisticsSlotId.setStatus("current")
_HwMacSlotStatistics_Type = Integer32
_HwMacSlotStatistics_Object = MibTableColumn
hwMacSlotStatistics = _HwMacSlotStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 16, 1, 2),
    _HwMacSlotStatistics_Type()
)
hwMacSlotStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacSlotStatistics.setStatus("current")
_HwMacSlotStatisticsSpecify_Type = Integer32
_HwMacSlotStatisticsSpecify_Object = MibTableColumn
hwMacSlotStatisticsSpecify = _HwMacSlotStatisticsSpecify_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 16, 1, 3),
    _HwMacSlotStatisticsSpecify_Type()
)
hwMacSlotStatisticsSpecify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacSlotStatisticsSpecify.setStatus("current")
_HwMacVlanStatisticsTable_Object = MibTable
hwMacVlanStatisticsTable = _HwMacVlanStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 17)
)
if mibBuilder.loadTexts:
    hwMacVlanStatisticsTable.setStatus("current")
_HwMacVlanStatisticsEntry_Object = MibTableRow
hwMacVlanStatisticsEntry = _HwMacVlanStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 17, 1)
)
hwMacVlanStatisticsEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwMacVlanStatisticsVlanId"),
)
if mibBuilder.loadTexts:
    hwMacVlanStatisticsEntry.setStatus("current")
_HwMacVlanStatisticsVlanId_Type = VlanId
_HwMacVlanStatisticsVlanId_Object = MibTableColumn
hwMacVlanStatisticsVlanId = _HwMacVlanStatisticsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 17, 1, 1),
    _HwMacVlanStatisticsVlanId_Type()
)
hwMacVlanStatisticsVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacVlanStatisticsVlanId.setStatus("current")
_HwMacVlanStatistics_Type = Integer32
_HwMacVlanStatistics_Object = MibTableColumn
hwMacVlanStatistics = _HwMacVlanStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 17, 1, 2),
    _HwMacVlanStatistics_Type()
)
hwMacVlanStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacVlanStatistics.setStatus("current")
_HwMacVsiStatisticsTable_Object = MibTable
hwMacVsiStatisticsTable = _HwMacVsiStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 18)
)
if mibBuilder.loadTexts:
    hwMacVsiStatisticsTable.setStatus("current")
_HwMacVsiStatisticsEntry_Object = MibTableRow
hwMacVsiStatisticsEntry = _HwMacVsiStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 18, 1)
)
hwMacVsiStatisticsEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwMacVsiStatisticsVsiName"),
)
if mibBuilder.loadTexts:
    hwMacVsiStatisticsEntry.setStatus("current")


class _HwMacVsiStatisticsVsiName_Type(OctetString):
    """Custom type hwMacVsiStatisticsVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwMacVsiStatisticsVsiName_Type.__name__ = "OctetString"
_HwMacVsiStatisticsVsiName_Object = MibTableColumn
hwMacVsiStatisticsVsiName = _HwMacVsiStatisticsVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 18, 1, 1),
    _HwMacVsiStatisticsVsiName_Type()
)
hwMacVsiStatisticsVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacVsiStatisticsVsiName.setStatus("current")
_HwMacVsiStatistics_Type = Integer32
_HwMacVsiStatistics_Object = MibTableColumn
hwMacVsiStatistics = _HwMacVsiStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 18, 1, 2),
    _HwMacVsiStatistics_Type()
)
hwMacVsiStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacVsiStatistics.setStatus("current")
_HwPwMacLimitTable_Object = MibTable
hwPwMacLimitTable = _HwPwMacLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 19)
)
if mibBuilder.loadTexts:
    hwPwMacLimitTable.setStatus("current")
_HwPwMacLimitEntry_Object = MibTableRow
hwPwMacLimitEntry = _HwPwMacLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 19, 1)
)
hwPwMacLimitEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwPwMacLimitVsiName"),
    (0, "HUAWEI-L2MAM-MIB", "hwPwMacLimitPwName"),
)
if mibBuilder.loadTexts:
    hwPwMacLimitEntry.setStatus("current")


class _HwPwMacLimitVsiName_Type(OctetString):
    """Custom type hwPwMacLimitVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwPwMacLimitVsiName_Type.__name__ = "OctetString"
_HwPwMacLimitVsiName_Object = MibTableColumn
hwPwMacLimitVsiName = _HwPwMacLimitVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 19, 1, 1),
    _HwPwMacLimitVsiName_Type()
)
hwPwMacLimitVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPwMacLimitVsiName.setStatus("current")


class _HwPwMacLimitPwName_Type(OctetString):
    """Custom type hwPwMacLimitPwName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwPwMacLimitPwName_Type.__name__ = "OctetString"
_HwPwMacLimitPwName_Object = MibTableColumn
hwPwMacLimitPwName = _HwPwMacLimitPwName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 19, 1, 2),
    _HwPwMacLimitPwName_Type()
)
hwPwMacLimitPwName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPwMacLimitPwName.setStatus("current")


class _HwPwMacLimitMaxMac_Type(Integer32):
    """Custom type hwPwMacLimitMaxMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131072),
    )


_HwPwMacLimitMaxMac_Type.__name__ = "Integer32"
_HwPwMacLimitMaxMac_Object = MibTableColumn
hwPwMacLimitMaxMac = _HwPwMacLimitMaxMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 19, 1, 3),
    _HwPwMacLimitMaxMac_Type()
)
hwPwMacLimitMaxMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPwMacLimitMaxMac.setStatus("current")


class _HwPwMacLimitMaxRate_Type(Integer32):
    """Custom type hwPwMacLimitMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HwPwMacLimitMaxRate_Type.__name__ = "Integer32"
_HwPwMacLimitMaxRate_Object = MibTableColumn
hwPwMacLimitMaxRate = _HwPwMacLimitMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 19, 1, 4),
    _HwPwMacLimitMaxRate_Type()
)
hwPwMacLimitMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPwMacLimitMaxRate.setStatus("current")


class _HwPwMacLimitAction_Type(Integer32):
    """Custom type hwPwMacLimitAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 2))
    )


_HwPwMacLimitAction_Type.__name__ = "Integer32"
_HwPwMacLimitAction_Object = MibTableColumn
hwPwMacLimitAction = _HwPwMacLimitAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 19, 1, 5),
    _HwPwMacLimitAction_Type()
)
hwPwMacLimitAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPwMacLimitAction.setStatus("current")
_HwPwMacLimitAlarm_Type = EnabledStatus
_HwPwMacLimitAlarm_Object = MibTableColumn
hwPwMacLimitAlarm = _HwPwMacLimitAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 19, 1, 6),
    _HwPwMacLimitAlarm_Type()
)
hwPwMacLimitAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPwMacLimitAlarm.setStatus("current")
_HwPwMacLimitRowstatus_Type = RowStatus
_HwPwMacLimitRowstatus_Object = MibTableColumn
hwPwMacLimitRowstatus = _HwPwMacLimitRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 19, 1, 7),
    _HwPwMacLimitRowstatus_Type()
)
hwPwMacLimitRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPwMacLimitRowstatus.setStatus("current")
_HwPwMacAddressLearn_Type = EnabledStatus
_HwPwMacAddressLearn_Object = MibTableColumn
hwPwMacAddressLearn = _HwPwMacAddressLearn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 19, 1, 8),
    _HwPwMacAddressLearn_Type()
)
hwPwMacAddressLearn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwPwMacAddressLearn.setStatus("current")


class _HwPwMacDynAddressLearnNum_Type(Integer32):
    """Custom type hwPwMacDynAddressLearnNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131072),
    )


_HwPwMacDynAddressLearnNum_Type.__name__ = "Integer32"
_HwPwMacDynAddressLearnNum_Object = MibTableColumn
hwPwMacDynAddressLearnNum = _HwPwMacDynAddressLearnNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 19, 1, 9),
    _HwPwMacDynAddressLearnNum_Type()
)
hwPwMacDynAddressLearnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPwMacDynAddressLearnNum.setStatus("current")
_HwMacSpoofingDefendTable_Object = MibTable
hwMacSpoofingDefendTable = _HwMacSpoofingDefendTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 20)
)
if mibBuilder.loadTexts:
    hwMacSpoofingDefendTable.setStatus("current")
_HwMacSpoofingDefendEntry_Object = MibTableRow
hwMacSpoofingDefendEntry = _HwMacSpoofingDefendEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 20, 1)
)
hwMacSpoofingDefendEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwMacSpoofingDefendPort"),
)
if mibBuilder.loadTexts:
    hwMacSpoofingDefendEntry.setStatus("current")
_HwMacSpoofingDefendPort_Type = InterfaceIndexOrZero
_HwMacSpoofingDefendPort_Object = MibTableColumn
hwMacSpoofingDefendPort = _HwMacSpoofingDefendPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 20, 1, 1),
    _HwMacSpoofingDefendPort_Type()
)
hwMacSpoofingDefendPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacSpoofingDefendPort.setStatus("current")
_HwMacSpoofingDefendEnabled_Type = EnabledStatus
_HwMacSpoofingDefendEnabled_Object = MibTableColumn
hwMacSpoofingDefendEnabled = _HwMacSpoofingDefendEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 20, 1, 2),
    _HwMacSpoofingDefendEnabled_Type()
)
hwMacSpoofingDefendEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacSpoofingDefendEnabled.setStatus("current")
_HwDiscardIllegalMacEnable_Type = EnabledStatus
_HwDiscardIllegalMacEnable_Object = MibScalar
hwDiscardIllegalMacEnable = _HwDiscardIllegalMacEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 21),
    _HwDiscardIllegalMacEnable_Type()
)
hwDiscardIllegalMacEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDiscardIllegalMacEnable.setStatus("current")
_HwDiscardIllegalMacAlarm_Type = EnabledStatus
_HwDiscardIllegalMacAlarm_Object = MibScalar
hwDiscardIllegalMacAlarm = _HwDiscardIllegalMacAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 22),
    _HwDiscardIllegalMacAlarm_Type()
)
hwDiscardIllegalMacAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDiscardIllegalMacAlarm.setStatus("current")
_HwMacSpoofingDefend_Type = EnabledStatus
_HwMacSpoofingDefend_Object = MibScalar
hwMacSpoofingDefend = _HwMacSpoofingDefend_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 23),
    _HwMacSpoofingDefend_Type()
)
hwMacSpoofingDefend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacSpoofingDefend.setStatus("current")
_HwL2MacFlappingTrapObjects_ObjectIdentity = ObjectIdentity
hwL2MacFlappingTrapObjects = _HwL2MacFlappingTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 24)
)
_HwMacflappingMac_Type = OctetString
_HwMacflappingMac_Object = MibScalar
hwMacflappingMac = _HwMacflappingMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 24, 1),
    _HwMacflappingMac_Type()
)
hwMacflappingMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMacflappingMac.setStatus("current")


class _HwMacFlappingVlan_Type(Integer32):
    """Custom type hwMacFlappingVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwMacFlappingVlan_Type.__name__ = "Integer32"
_HwMacFlappingVlan_Object = MibScalar
hwMacFlappingVlan = _HwMacFlappingVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 24, 2),
    _HwMacFlappingVlan_Type()
)
hwMacFlappingVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMacFlappingVlan.setStatus("current")
_HwSlotMacLimitTable_Object = MibTable
hwSlotMacLimitTable = _HwSlotMacLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 25)
)
if mibBuilder.loadTexts:
    hwSlotMacLimitTable.setStatus("current")
_HwSlotMacLimitEntry_Object = MibTableRow
hwSlotMacLimitEntry = _HwSlotMacLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 25, 1)
)
hwSlotMacLimitEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwSlotMacLimitId"),
)
if mibBuilder.loadTexts:
    hwSlotMacLimitEntry.setStatus("current")
_HwSlotMacLimitId_Type = Integer32
_HwSlotMacLimitId_Object = MibTableColumn
hwSlotMacLimitId = _HwSlotMacLimitId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 25, 1, 1),
    _HwSlotMacLimitId_Type()
)
hwSlotMacLimitId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSlotMacLimitId.setStatus("current")
_HwSlotMacLimitMaxMac_Type = Integer32
_HwSlotMacLimitMaxMac_Object = MibTableColumn
hwSlotMacLimitMaxMac = _HwSlotMacLimitMaxMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 25, 1, 2),
    _HwSlotMacLimitMaxMac_Type()
)
hwSlotMacLimitMaxMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSlotMacLimitMaxMac.setStatus("current")
_HwSlotMacLimitMaxRate_Type = Integer32
_HwSlotMacLimitMaxRate_Object = MibTableColumn
hwSlotMacLimitMaxRate = _HwSlotMacLimitMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 25, 1, 3),
    _HwSlotMacLimitMaxRate_Type()
)
hwSlotMacLimitMaxRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSlotMacLimitMaxRate.setStatus("current")


class _HwSlotMacLimitAction_Type(Integer32):
    """Custom type hwSlotMacLimitAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("forward", 2))
    )


_HwSlotMacLimitAction_Type.__name__ = "Integer32"
_HwSlotMacLimitAction_Object = MibTableColumn
hwSlotMacLimitAction = _HwSlotMacLimitAction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 25, 1, 4),
    _HwSlotMacLimitAction_Type()
)
hwSlotMacLimitAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSlotMacLimitAction.setStatus("current")


class _HwSlotMacLimitAlarm_Type(Integer32):
    """Custom type hwSlotMacLimitAlarm based on Integer32"""
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


_HwSlotMacLimitAlarm_Type.__name__ = "Integer32"
_HwSlotMacLimitAlarm_Object = MibTableColumn
hwSlotMacLimitAlarm = _HwSlotMacLimitAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 25, 1, 5),
    _HwSlotMacLimitAlarm_Type()
)
hwSlotMacLimitAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSlotMacLimitAlarm.setStatus("current")
_HwSlotMacLimitRowstatus_Type = RowStatus
_HwSlotMacLimitRowstatus_Object = MibTableColumn
hwSlotMacLimitRowstatus = _HwSlotMacLimitRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 25, 1, 6),
    _HwSlotMacLimitRowstatus_Type()
)
hwSlotMacLimitRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwSlotMacLimitRowstatus.setStatus("current")
_HwL2ProtocolTunnelTrapObjects_ObjectIdentity = ObjectIdentity
hwL2ProtocolTunnelTrapObjects = _HwL2ProtocolTunnelTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 26)
)
_HwL2ProtocolTunnelTrapPortName_Type = OctetString
_HwL2ProtocolTunnelTrapPortName_Object = MibScalar
hwL2ProtocolTunnelTrapPortName = _HwL2ProtocolTunnelTrapPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 26, 1),
    _HwL2ProtocolTunnelTrapPortName_Type()
)
hwL2ProtocolTunnelTrapPortName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2ProtocolTunnelTrapPortName.setStatus("current")
_HwL2ProtocolTunnelTrapProtocolName_Type = OctetString
_HwL2ProtocolTunnelTrapProtocolName_Object = MibScalar
hwL2ProtocolTunnelTrapProtocolName = _HwL2ProtocolTunnelTrapProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 26, 2),
    _HwL2ProtocolTunnelTrapProtocolName_Type()
)
hwL2ProtocolTunnelTrapProtocolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2ProtocolTunnelTrapProtocolName.setStatus("current")


class _HwL2ProtocolTunnelTrapDropThreshold_Type(Integer32):
    """Custom type hwL2ProtocolTunnelTrapDropThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_HwL2ProtocolTunnelTrapDropThreshold_Type.__name__ = "Integer32"
_HwL2ProtocolTunnelTrapDropThreshold_Object = MibScalar
hwL2ProtocolTunnelTrapDropThreshold = _HwL2ProtocolTunnelTrapDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 26, 3),
    _HwL2ProtocolTunnelTrapDropThreshold_Type()
)
hwL2ProtocolTunnelTrapDropThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwL2ProtocolTunnelTrapDropThreshold.setStatus("current")
_HwL2ProtclTnlStdTable_Object = MibTable
hwL2ProtclTnlStdTable = _HwL2ProtclTnlStdTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 27)
)
if mibBuilder.loadTexts:
    hwL2ProtclTnlStdTable.setStatus("current")
_HwL2ProtclTnlStdEntry_Object = MibTableRow
hwL2ProtclTnlStdEntry = _HwL2ProtclTnlStdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 27, 1)
)
hwL2ProtclTnlStdEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwL2ProtclTnlStdProtclName"),
)
if mibBuilder.loadTexts:
    hwL2ProtclTnlStdEntry.setStatus("current")


class _HwL2ProtclTnlStdProtclName_Type(OctetString):
    """Custom type hwL2ProtclTnlStdProtclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwL2ProtclTnlStdProtclName_Type.__name__ = "OctetString"
_HwL2ProtclTnlStdProtclName_Object = MibTableColumn
hwL2ProtclTnlStdProtclName = _HwL2ProtclTnlStdProtclName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 27, 1, 1),
    _HwL2ProtclTnlStdProtclName_Type()
)
hwL2ProtclTnlStdProtclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2ProtclTnlStdProtclName.setStatus("current")
_HwL2ProtclTnlStdProtclMacAddr_Type = MacAddress
_HwL2ProtclTnlStdProtclMacAddr_Object = MibTableColumn
hwL2ProtclTnlStdProtclMacAddr = _HwL2ProtclTnlStdProtclMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 27, 1, 2),
    _HwL2ProtclTnlStdProtclMacAddr_Type()
)
hwL2ProtclTnlStdProtclMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2ProtclTnlStdProtclMacAddr.setStatus("current")


class _HwL2ProtclTnlStdEncapType_Type(Integer32):
    """Custom type hwL2ProtclTnlStdEncapType based on Integer32"""
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
        *(("ethernetii", 1),
          ("llc", 3),
          ("others", 4),
          ("snap", 2))
    )


_HwL2ProtclTnlStdEncapType_Type.__name__ = "Integer32"
_HwL2ProtclTnlStdEncapType_Object = MibTableColumn
hwL2ProtclTnlStdEncapType = _HwL2ProtclTnlStdEncapType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 27, 1, 3),
    _HwL2ProtclTnlStdEncapType_Type()
)
hwL2ProtclTnlStdEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2ProtclTnlStdEncapType.setStatus("current")
_HwL2ProtclTnlStdProtclType_Type = Integer32
_HwL2ProtclTnlStdProtclType_Object = MibTableColumn
hwL2ProtclTnlStdProtclType = _HwL2ProtclTnlStdProtclType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 27, 1, 4),
    _HwL2ProtclTnlStdProtclType_Type()
)
hwL2ProtclTnlStdProtclType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2ProtclTnlStdProtclType.setStatus("current")
_HwL2ProtclTnlStdGroupMacAddr_Type = MacAddress
_HwL2ProtclTnlStdGroupMacAddr_Object = MibTableColumn
hwL2ProtclTnlStdGroupMacAddr = _HwL2ProtclTnlStdGroupMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 27, 1, 5),
    _HwL2ProtclTnlStdGroupMacAddr_Type()
)
hwL2ProtclTnlStdGroupMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2ProtclTnlStdGroupMacAddr.setStatus("current")
_HwL2ProtclTnlStdGroupDefault_Type = MacAddress
_HwL2ProtclTnlStdGroupDefault_Object = MibTableColumn
hwL2ProtclTnlStdGroupDefault = _HwL2ProtclTnlStdGroupDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 27, 1, 6),
    _HwL2ProtclTnlStdGroupDefault_Type()
)
hwL2ProtclTnlStdGroupDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2ProtclTnlStdGroupDefault.setStatus("current")


class _HwL2ProtclTnlStdPriority_Type(Integer32):
    """Custom type hwL2ProtclTnlStdPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwL2ProtclTnlStdPriority_Type.__name__ = "Integer32"
_HwL2ProtclTnlStdPriority_Object = MibTableColumn
hwL2ProtclTnlStdPriority = _HwL2ProtclTnlStdPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 27, 1, 7),
    _HwL2ProtclTnlStdPriority_Type()
)
hwL2ProtclTnlStdPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2ProtclTnlStdPriority.setStatus("current")
_HwL2ProtclTnlCusTable_Object = MibTable
hwL2ProtclTnlCusTable = _HwL2ProtclTnlCusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 28)
)
if mibBuilder.loadTexts:
    hwL2ProtclTnlCusTable.setStatus("current")
_HwL2ProtclTnlCusEntry_Object = MibTableRow
hwL2ProtclTnlCusEntry = _HwL2ProtclTnlCusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 28, 1)
)
hwL2ProtclTnlCusEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwL2ProtclTnlCusProtclName"),
)
if mibBuilder.loadTexts:
    hwL2ProtclTnlCusEntry.setStatus("current")


class _HwL2ProtclTnlCusProtclName_Type(OctetString):
    """Custom type hwL2ProtclTnlCusProtclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwL2ProtclTnlCusProtclName_Type.__name__ = "OctetString"
_HwL2ProtclTnlCusProtclName_Object = MibTableColumn
hwL2ProtclTnlCusProtclName = _HwL2ProtclTnlCusProtclName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 28, 1, 1),
    _HwL2ProtclTnlCusProtclName_Type()
)
hwL2ProtclTnlCusProtclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2ProtclTnlCusProtclName.setStatus("current")
_HwL2ProtclTnlCusProtclMacAddr_Type = MacAddress
_HwL2ProtclTnlCusProtclMacAddr_Object = MibTableColumn
hwL2ProtclTnlCusProtclMacAddr = _HwL2ProtclTnlCusProtclMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 28, 1, 2),
    _HwL2ProtclTnlCusProtclMacAddr_Type()
)
hwL2ProtclTnlCusProtclMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2ProtclTnlCusProtclMacAddr.setStatus("current")


class _HwL2ProtclTnlCusEncapType_Type(Integer32):
    """Custom type hwL2ProtclTnlCusEncapType based on Integer32"""
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
        *(("ethernetii", 1),
          ("llc", 3),
          ("others", 4),
          ("snap", 2))
    )


_HwL2ProtclTnlCusEncapType_Type.__name__ = "Integer32"
_HwL2ProtclTnlCusEncapType_Object = MibTableColumn
hwL2ProtclTnlCusEncapType = _HwL2ProtclTnlCusEncapType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 28, 1, 3),
    _HwL2ProtclTnlCusEncapType_Type()
)
hwL2ProtclTnlCusEncapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2ProtclTnlCusEncapType.setStatus("current")
_HwL2ProtclTnlCusProtclType_Type = Integer32
_HwL2ProtclTnlCusProtclType_Object = MibTableColumn
hwL2ProtclTnlCusProtclType = _HwL2ProtclTnlCusProtclType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 28, 1, 4),
    _HwL2ProtclTnlCusProtclType_Type()
)
hwL2ProtclTnlCusProtclType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2ProtclTnlCusProtclType.setStatus("current")
_HwL2ProtclTnlCusGroupMacAddr_Type = MacAddress
_HwL2ProtclTnlCusGroupMacAddr_Object = MibTableColumn
hwL2ProtclTnlCusGroupMacAddr = _HwL2ProtclTnlCusGroupMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 28, 1, 5),
    _HwL2ProtclTnlCusGroupMacAddr_Type()
)
hwL2ProtclTnlCusGroupMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2ProtclTnlCusGroupMacAddr.setStatus("current")
_HwL2ProtclTnlCusGroupDefault_Type = MacAddress
_HwL2ProtclTnlCusGroupDefault_Object = MibTableColumn
hwL2ProtclTnlCusGroupDefault = _HwL2ProtclTnlCusGroupDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 28, 1, 6),
    _HwL2ProtclTnlCusGroupDefault_Type()
)
hwL2ProtclTnlCusGroupDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2ProtclTnlCusGroupDefault.setStatus("current")


class _HwL2ProtclTnlCusPriority_Type(Integer32):
    """Custom type hwL2ProtclTnlCusPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_HwL2ProtclTnlCusPriority_Type.__name__ = "Integer32"
_HwL2ProtclTnlCusPriority_Object = MibTableColumn
hwL2ProtclTnlCusPriority = _HwL2ProtclTnlCusPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 28, 1, 7),
    _HwL2ProtclTnlCusPriority_Type()
)
hwL2ProtclTnlCusPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2ProtclTnlCusPriority.setStatus("current")
_HwL2ProtclTnlCusRowStatus_Type = RowStatus
_HwL2ProtclTnlCusRowStatus_Object = MibTableColumn
hwL2ProtclTnlCusRowStatus = _HwL2ProtclTnlCusRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 28, 1, 8),
    _HwL2ProtclTnlCusRowStatus_Type()
)
hwL2ProtclTnlCusRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2ProtclTnlCusRowStatus.setStatus("current")
_HwL2ProtclTnlEnableTable_Object = MibTable
hwL2ProtclTnlEnableTable = _HwL2ProtclTnlEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 29)
)
if mibBuilder.loadTexts:
    hwL2ProtclTnlEnableTable.setStatus("current")
_HwL2ProtclTnlEnableEntry_Object = MibTableRow
hwL2ProtclTnlEnableEntry = _HwL2ProtclTnlEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 29, 1)
)
hwL2ProtclTnlEnableEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwL2ProtclTnlEnableIfIndex"),
    (0, "HUAWEI-L2MAM-MIB", "hwL2ProtclTnlEnableProtclName"),
)
if mibBuilder.loadTexts:
    hwL2ProtclTnlEnableEntry.setStatus("current")
_HwL2ProtclTnlEnableIfIndex_Type = InterfaceIndex
_HwL2ProtclTnlEnableIfIndex_Object = MibTableColumn
hwL2ProtclTnlEnableIfIndex = _HwL2ProtclTnlEnableIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 29, 1, 1),
    _HwL2ProtclTnlEnableIfIndex_Type()
)
hwL2ProtclTnlEnableIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2ProtclTnlEnableIfIndex.setStatus("current")


class _HwL2ProtclTnlEnableProtclName_Type(OctetString):
    """Custom type hwL2ProtclTnlEnableProtclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwL2ProtclTnlEnableProtclName_Type.__name__ = "OctetString"
_HwL2ProtclTnlEnableProtclName_Object = MibTableColumn
hwL2ProtclTnlEnableProtclName = _HwL2ProtclTnlEnableProtclName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 29, 1, 2),
    _HwL2ProtclTnlEnableProtclName_Type()
)
hwL2ProtclTnlEnableProtclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2ProtclTnlEnableProtclName.setStatus("current")


class _HwL2ProtclTnlEnableTransMode_Type(Integer32):
    """Custom type hwL2ProtclTnlEnableTransMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 1),
          ("untagged", 2))
    )


_HwL2ProtclTnlEnableTransMode_Type.__name__ = "Integer32"
_HwL2ProtclTnlEnableTransMode_Object = MibTableColumn
hwL2ProtclTnlEnableTransMode = _HwL2ProtclTnlEnableTransMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 29, 1, 3),
    _HwL2ProtclTnlEnableTransMode_Type()
)
hwL2ProtclTnlEnableTransMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2ProtclTnlEnableTransMode.setStatus("current")


class _HwL2ProtclTnlEnableTagListLow_Type(OctetString):
    """Custom type hwL2ProtclTnlEnableTagListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2ProtclTnlEnableTagListLow_Type.__name__ = "OctetString"
_HwL2ProtclTnlEnableTagListLow_Object = MibTableColumn
hwL2ProtclTnlEnableTagListLow = _HwL2ProtclTnlEnableTagListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 29, 1, 4),
    _HwL2ProtclTnlEnableTagListLow_Type()
)
hwL2ProtclTnlEnableTagListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2ProtclTnlEnableTagListLow.setStatus("current")


class _HwL2ProtclTnlEnableTagListHigh_Type(OctetString):
    """Custom type hwL2ProtclTnlEnableTagListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(256, 256),
    )


_HwL2ProtclTnlEnableTagListHigh_Type.__name__ = "OctetString"
_HwL2ProtclTnlEnableTagListHigh_Object = MibTableColumn
hwL2ProtclTnlEnableTagListHigh = _HwL2ProtclTnlEnableTagListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 29, 1, 5),
    _HwL2ProtclTnlEnableTagListHigh_Type()
)
hwL2ProtclTnlEnableTagListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2ProtclTnlEnableTagListHigh.setStatus("current")


class _HwL2ProtclTnlEnableDropthresholdRate_Type(Integer32):
    """Custom type hwL2ProtclTnlEnableDropthresholdRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_HwL2ProtclTnlEnableDropthresholdRate_Type.__name__ = "Integer32"
_HwL2ProtclTnlEnableDropthresholdRate_Object = MibTableColumn
hwL2ProtclTnlEnableDropthresholdRate = _HwL2ProtclTnlEnableDropthresholdRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 29, 1, 6),
    _HwL2ProtclTnlEnableDropthresholdRate_Type()
)
hwL2ProtclTnlEnableDropthresholdRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwL2ProtclTnlEnableDropthresholdRate.setStatus("current")
_HwL2ProtclTnlEnableRowStatus_Type = RowStatus
_HwL2ProtclTnlEnableRowStatus_Object = MibTableColumn
hwL2ProtclTnlEnableRowStatus = _HwL2ProtclTnlEnableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 29, 1, 7),
    _HwL2ProtclTnlEnableRowStatus_Type()
)
hwL2ProtclTnlEnableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwL2ProtclTnlEnableRowStatus.setStatus("current")
_HwL2ProtclTnlStatisticsTable_Object = MibTable
hwL2ProtclTnlStatisticsTable = _HwL2ProtclTnlStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 30)
)
if mibBuilder.loadTexts:
    hwL2ProtclTnlStatisticsTable.setStatus("current")
_HwL2ProtclTnlStatisticsEntry_Object = MibTableRow
hwL2ProtclTnlStatisticsEntry = _HwL2ProtclTnlStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 30, 1)
)
hwL2ProtclTnlStatisticsEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwL2ProtclTnlStatisticsIfIndex"),
    (0, "HUAWEI-L2MAM-MIB", "hwL2ProtclTnlStatisticsProtclName"),
)
if mibBuilder.loadTexts:
    hwL2ProtclTnlStatisticsEntry.setStatus("current")
_HwL2ProtclTnlStatisticsIfIndex_Type = InterfaceIndex
_HwL2ProtclTnlStatisticsIfIndex_Object = MibTableColumn
hwL2ProtclTnlStatisticsIfIndex = _HwL2ProtclTnlStatisticsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 30, 1, 1),
    _HwL2ProtclTnlStatisticsIfIndex_Type()
)
hwL2ProtclTnlStatisticsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2ProtclTnlStatisticsIfIndex.setStatus("current")


class _HwL2ProtclTnlStatisticsProtclName_Type(OctetString):
    """Custom type hwL2ProtclTnlStatisticsProtclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwL2ProtclTnlStatisticsProtclName_Type.__name__ = "OctetString"
_HwL2ProtclTnlStatisticsProtclName_Object = MibTableColumn
hwL2ProtclTnlStatisticsProtclName = _HwL2ProtclTnlStatisticsProtclName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 30, 1, 2),
    _HwL2ProtclTnlStatisticsProtclName_Type()
)
hwL2ProtclTnlStatisticsProtclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwL2ProtclTnlStatisticsProtclName.setStatus("current")
_HwL2ProtclTnlStatisticsDropthrhldRate_Type = Integer32
_HwL2ProtclTnlStatisticsDropthrhldRate_Object = MibTableColumn
hwL2ProtclTnlStatisticsDropthrhldRate = _HwL2ProtclTnlStatisticsDropthrhldRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 30, 1, 3),
    _HwL2ProtclTnlStatisticsDropthrhldRate_Type()
)
hwL2ProtclTnlStatisticsDropthrhldRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2ProtclTnlStatisticsDropthrhldRate.setStatus("current")
_HwL2ProtclTnlStatisticsInputPkts_Type = Integer32
_HwL2ProtclTnlStatisticsInputPkts_Object = MibTableColumn
hwL2ProtclTnlStatisticsInputPkts = _HwL2ProtclTnlStatisticsInputPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 30, 1, 4),
    _HwL2ProtclTnlStatisticsInputPkts_Type()
)
hwL2ProtclTnlStatisticsInputPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2ProtclTnlStatisticsInputPkts.setStatus("current")
_HwL2ProtclTnlStatisticsOutputPkts_Type = Integer32
_HwL2ProtclTnlStatisticsOutputPkts_Object = MibTableColumn
hwL2ProtclTnlStatisticsOutputPkts = _HwL2ProtclTnlStatisticsOutputPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 30, 1, 5),
    _HwL2ProtclTnlStatisticsOutputPkts_Type()
)
hwL2ProtclTnlStatisticsOutputPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2ProtclTnlStatisticsOutputPkts.setStatus("current")
_HwL2ProtclTnlStatisticsDropPkts_Type = Integer32
_HwL2ProtclTnlStatisticsDropPkts_Object = MibTableColumn
hwL2ProtclTnlStatisticsDropPkts = _HwL2ProtclTnlStatisticsDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 30, 1, 6),
    _HwL2ProtclTnlStatisticsDropPkts_Type()
)
hwL2ProtclTnlStatisticsDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL2ProtclTnlStatisticsDropPkts.setStatus("current")


class _HwBridgeMacAgingTime_Type(Integer32):
    """Custom type hwBridgeMacAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1000000),
        ValueRangeConstraint(0, 0),
    )


_HwBridgeMacAgingTime_Type.__name__ = "Integer32"
_HwBridgeMacAgingTime_Object = MibScalar
hwBridgeMacAgingTime = _HwBridgeMacAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 31),
    _HwBridgeMacAgingTime_Type()
)
hwBridgeMacAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBridgeMacAgingTime.setStatus("current")
_HwCfgMacAddrQueryTable_Object = MibTable
hwCfgMacAddrQueryTable = _HwCfgMacAddrQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 32)
)
if mibBuilder.loadTexts:
    hwCfgMacAddrQueryTable.setStatus("current")
_HwCfgMacAddrQueryEntry_Object = MibTableRow
hwCfgMacAddrQueryEntry = _HwCfgMacAddrQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 32, 1)
)
hwCfgMacAddrQueryEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwCfgMacAddrQueryVlanId"),
    (0, "HUAWEI-L2MAM-MIB", "hwCfgMacAddrQueryVsiName"),
    (0, "HUAWEI-L2MAM-MIB", "hwCfgMacAddrQuerySiName"),
    (0, "HUAWEI-L2MAM-MIB", "hwCfgMacAddrQueryBridgeId"),
    (0, "HUAWEI-L2MAM-MIB", "hwCfgMacAddrQueryMacAddr"),
    (0, "HUAWEI-L2MAM-MIB", "hwCfgMacAddrQueryConditionMode"),
    (0, "HUAWEI-L2MAM-MIB", "hwCfgMacAddrQueryConditionStringA"),
    (0, "HUAWEI-L2MAM-MIB", "hwCfgMacAddrQueryConditionStringB"),
    (0, "HUAWEI-L2MAM-MIB", "hwCfgMacAddrQueryConditionDigitA"),
    (0, "HUAWEI-L2MAM-MIB", "hwCfgMacAddrQueryConditionDigitB"),
    (0, "HUAWEI-L2MAM-MIB", "hwCfgMacAddrQueryConditionDigitC"),
)
if mibBuilder.loadTexts:
    hwCfgMacAddrQueryEntry.setStatus("current")
_HwCfgMacAddrQueryVlanId_Type = VlanIdOrNone
_HwCfgMacAddrQueryVlanId_Object = MibTableColumn
hwCfgMacAddrQueryVlanId = _HwCfgMacAddrQueryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 32, 1, 1),
    _HwCfgMacAddrQueryVlanId_Type()
)
hwCfgMacAddrQueryVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCfgMacAddrQueryVlanId.setStatus("current")


class _HwCfgMacAddrQueryVsiName_Type(OctetString):
    """Custom type hwCfgMacAddrQueryVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwCfgMacAddrQueryVsiName_Type.__name__ = "OctetString"
_HwCfgMacAddrQueryVsiName_Object = MibTableColumn
hwCfgMacAddrQueryVsiName = _HwCfgMacAddrQueryVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 32, 1, 2),
    _HwCfgMacAddrQueryVsiName_Type()
)
hwCfgMacAddrQueryVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCfgMacAddrQueryVsiName.setStatus("current")


class _HwCfgMacAddrQuerySiName_Type(OctetString):
    """Custom type hwCfgMacAddrQuerySiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwCfgMacAddrQuerySiName_Type.__name__ = "OctetString"
_HwCfgMacAddrQuerySiName_Object = MibTableColumn
hwCfgMacAddrQuerySiName = _HwCfgMacAddrQuerySiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 32, 1, 3),
    _HwCfgMacAddrQuerySiName_Type()
)
hwCfgMacAddrQuerySiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCfgMacAddrQuerySiName.setStatus("current")


class _HwCfgMacAddrQueryBridgeId_Type(Integer32):
    """Custom type hwCfgMacAddrQueryBridgeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwCfgMacAddrQueryBridgeId_Type.__name__ = "Integer32"
_HwCfgMacAddrQueryBridgeId_Object = MibTableColumn
hwCfgMacAddrQueryBridgeId = _HwCfgMacAddrQueryBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 32, 1, 4),
    _HwCfgMacAddrQueryBridgeId_Type()
)
hwCfgMacAddrQueryBridgeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCfgMacAddrQueryBridgeId.setStatus("current")
_HwCfgMacAddrQueryMacAddr_Type = MacAddress
_HwCfgMacAddrQueryMacAddr_Object = MibTableColumn
hwCfgMacAddrQueryMacAddr = _HwCfgMacAddrQueryMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 32, 1, 5),
    _HwCfgMacAddrQueryMacAddr_Type()
)
hwCfgMacAddrQueryMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCfgMacAddrQueryMacAddr.setStatus("current")


class _HwCfgMacAddrQueryConditionMode_Type(Integer32):
    """Custom type hwCfgMacAddrQueryConditionMode based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("showall", 1),
          ("showbymac", 2),
          ("showbymacvlan", 3),
          ("showbymacvsi", 11),
          ("showbyport", 9),
          ("showbyportvlan", 10),
          ("showbyportvsi", 15),
          ("showbytype", 4),
          ("showbytypeport", 6),
          ("showbytypeportvlan", 7),
          ("showbytypeportvsi", 13),
          ("showbytypevlan", 5),
          ("showbytypevsi", 12),
          ("showbyvlan", 8),
          ("showbyvsi", 14))
    )


_HwCfgMacAddrQueryConditionMode_Type.__name__ = "Integer32"
_HwCfgMacAddrQueryConditionMode_Object = MibTableColumn
hwCfgMacAddrQueryConditionMode = _HwCfgMacAddrQueryConditionMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 32, 1, 6),
    _HwCfgMacAddrQueryConditionMode_Type()
)
hwCfgMacAddrQueryConditionMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCfgMacAddrQueryConditionMode.setStatus("current")


class _HwCfgMacAddrQueryConditionStringA_Type(OctetString):
    """Custom type hwCfgMacAddrQueryConditionStringA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwCfgMacAddrQueryConditionStringA_Type.__name__ = "OctetString"
_HwCfgMacAddrQueryConditionStringA_Object = MibTableColumn
hwCfgMacAddrQueryConditionStringA = _HwCfgMacAddrQueryConditionStringA_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 32, 1, 7),
    _HwCfgMacAddrQueryConditionStringA_Type()
)
hwCfgMacAddrQueryConditionStringA.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCfgMacAddrQueryConditionStringA.setStatus("current")


class _HwCfgMacAddrQueryConditionStringB_Type(OctetString):
    """Custom type hwCfgMacAddrQueryConditionStringB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwCfgMacAddrQueryConditionStringB_Type.__name__ = "OctetString"
_HwCfgMacAddrQueryConditionStringB_Object = MibTableColumn
hwCfgMacAddrQueryConditionStringB = _HwCfgMacAddrQueryConditionStringB_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 32, 1, 8),
    _HwCfgMacAddrQueryConditionStringB_Type()
)
hwCfgMacAddrQueryConditionStringB.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCfgMacAddrQueryConditionStringB.setStatus("current")
_HwCfgMacAddrQueryConditionDigitA_Type = Unsigned32
_HwCfgMacAddrQueryConditionDigitA_Object = MibTableColumn
hwCfgMacAddrQueryConditionDigitA = _HwCfgMacAddrQueryConditionDigitA_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 32, 1, 9),
    _HwCfgMacAddrQueryConditionDigitA_Type()
)
hwCfgMacAddrQueryConditionDigitA.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCfgMacAddrQueryConditionDigitA.setStatus("current")
_HwCfgMacAddrQueryConditionDigitB_Type = Unsigned32
_HwCfgMacAddrQueryConditionDigitB_Object = MibTableColumn
hwCfgMacAddrQueryConditionDigitB = _HwCfgMacAddrQueryConditionDigitB_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 32, 1, 10),
    _HwCfgMacAddrQueryConditionDigitB_Type()
)
hwCfgMacAddrQueryConditionDigitB.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCfgMacAddrQueryConditionDigitB.setStatus("current")
_HwCfgMacAddrQueryConditionDigitC_Type = Unsigned32
_HwCfgMacAddrQueryConditionDigitC_Object = MibTableColumn
hwCfgMacAddrQueryConditionDigitC = _HwCfgMacAddrQueryConditionDigitC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 32, 1, 11),
    _HwCfgMacAddrQueryConditionDigitC_Type()
)
hwCfgMacAddrQueryConditionDigitC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCfgMacAddrQueryConditionDigitC.setStatus("current")


class _HwCfgMacAddrQueryType_Type(OctetString):
    """Custom type hwCfgMacAddrQueryType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwCfgMacAddrQueryType_Type.__name__ = "OctetString"
_HwCfgMacAddrQueryType_Object = MibTableColumn
hwCfgMacAddrQueryType = _HwCfgMacAddrQueryType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 32, 1, 12),
    _HwCfgMacAddrQueryType_Type()
)
hwCfgMacAddrQueryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgMacAddrQueryType.setStatus("current")
_HwCfgMacAddrQueryIfIndex_Type = InterfaceIndexOrZero
_HwCfgMacAddrQueryIfIndex_Object = MibTableColumn
hwCfgMacAddrQueryIfIndex = _HwCfgMacAddrQueryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 32, 1, 13),
    _HwCfgMacAddrQueryIfIndex_Type()
)
hwCfgMacAddrQueryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgMacAddrQueryIfIndex.setStatus("current")
_HwCfgMacAddrQueryPeVlanId_Type = VlanIdOrNone
_HwCfgMacAddrQueryPeVlanId_Object = MibTableColumn
hwCfgMacAddrQueryPeVlanId = _HwCfgMacAddrQueryPeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 32, 1, 14),
    _HwCfgMacAddrQueryPeVlanId_Type()
)
hwCfgMacAddrQueryPeVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgMacAddrQueryPeVlanId.setStatus("current")
_HwCfgMacAddrQueryCeVlanId_Type = VlanIdOrNone
_HwCfgMacAddrQueryCeVlanId_Object = MibTableColumn
hwCfgMacAddrQueryCeVlanId = _HwCfgMacAddrQueryCeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 32, 1, 15),
    _HwCfgMacAddrQueryCeVlanId_Type()
)
hwCfgMacAddrQueryCeVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgMacAddrQueryCeVlanId.setStatus("current")


class _HwCfgMacAddrQueryCedefaultFlag_Type(Integer32):
    """Custom type hwCfgMacAddrQueryCedefaultFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cedefault", 1),
          ("nocedefault", 0))
    )


_HwCfgMacAddrQueryCedefaultFlag_Type.__name__ = "Integer32"
_HwCfgMacAddrQueryCedefaultFlag_Object = MibTableColumn
hwCfgMacAddrQueryCedefaultFlag = _HwCfgMacAddrQueryCedefaultFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 32, 1, 16),
    _HwCfgMacAddrQueryCedefaultFlag_Type()
)
hwCfgMacAddrQueryCedefaultFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgMacAddrQueryCedefaultFlag.setStatus("current")
_HwCfgMacAddrQueryAtmIfIndex_Type = InterfaceIndexOrZero
_HwCfgMacAddrQueryAtmIfIndex_Object = MibTableColumn
hwCfgMacAddrQueryAtmIfIndex = _HwCfgMacAddrQueryAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 32, 1, 17),
    _HwCfgMacAddrQueryAtmIfIndex_Type()
)
hwCfgMacAddrQueryAtmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgMacAddrQueryAtmIfIndex.setStatus("current")


class _HwCfgMacAddrQueryVpi_Type(Integer32):
    """Custom type hwCfgMacAddrQueryVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwCfgMacAddrQueryVpi_Type.__name__ = "Integer32"
_HwCfgMacAddrQueryVpi_Object = MibTableColumn
hwCfgMacAddrQueryVpi = _HwCfgMacAddrQueryVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 32, 1, 18),
    _HwCfgMacAddrQueryVpi_Type()
)
hwCfgMacAddrQueryVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgMacAddrQueryVpi.setStatus("current")


class _HwCfgMacAddrQueryVci_Type(Integer32):
    """Custom type hwCfgMacAddrQueryVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwCfgMacAddrQueryVci_Type.__name__ = "Integer32"
_HwCfgMacAddrQueryVci_Object = MibTableColumn
hwCfgMacAddrQueryVci = _HwCfgMacAddrQueryVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 32, 1, 19),
    _HwCfgMacAddrQueryVci_Type()
)
hwCfgMacAddrQueryVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgMacAddrQueryVci.setStatus("current")


class _HwCfgMacAddrQueryMacTunnel_Type(OctetString):
    """Custom type hwCfgMacAddrQueryMacTunnel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwCfgMacAddrQueryMacTunnel_Type.__name__ = "OctetString"
_HwCfgMacAddrQueryMacTunnel_Object = MibTableColumn
hwCfgMacAddrQueryMacTunnel = _HwCfgMacAddrQueryMacTunnel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 32, 1, 20),
    _HwCfgMacAddrQueryMacTunnel_Type()
)
hwCfgMacAddrQueryMacTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCfgMacAddrQueryMacTunnel.setStatus("current")
_HwDynMacAddrQueryTable_Object = MibTable
hwDynMacAddrQueryTable = _HwDynMacAddrQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33)
)
if mibBuilder.loadTexts:
    hwDynMacAddrQueryTable.setStatus("current")
_HwDynMacAddrQueryEntry_Object = MibTableRow
hwDynMacAddrQueryEntry = _HwDynMacAddrQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33, 1)
)
hwDynMacAddrQueryEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwDynMacAddrQueryVlanId"),
    (0, "HUAWEI-L2MAM-MIB", "hwDynMacAddrQueryVsiName"),
    (0, "HUAWEI-L2MAM-MIB", "hwDynMacAddrQuerySiName"),
    (0, "HUAWEI-L2MAM-MIB", "hwDynMacAddrQueryBridgeId"),
    (0, "HUAWEI-L2MAM-MIB", "hwDynMacAddrQueryMacAddr"),
    (0, "HUAWEI-L2MAM-MIB", "hwDynMacAddrQueryConditionMode"),
    (0, "HUAWEI-L2MAM-MIB", "hwDynMacAddrQueryConditionStringA"),
    (0, "HUAWEI-L2MAM-MIB", "hwDynMacAddrQueryConditionStringB"),
    (0, "HUAWEI-L2MAM-MIB", "hwDynMacAddrQueryConditionDigitA"),
    (0, "HUAWEI-L2MAM-MIB", "hwDynMacAddrQueryConditionDigitB"),
    (0, "HUAWEI-L2MAM-MIB", "hwDynMacAddrQueryConditionDigitC"),
)
if mibBuilder.loadTexts:
    hwDynMacAddrQueryEntry.setStatus("current")
_HwDynMacAddrQueryVlanId_Type = VlanIdOrNone
_HwDynMacAddrQueryVlanId_Object = MibTableColumn
hwDynMacAddrQueryVlanId = _HwDynMacAddrQueryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33, 1, 1),
    _HwDynMacAddrQueryVlanId_Type()
)
hwDynMacAddrQueryVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDynMacAddrQueryVlanId.setStatus("current")


class _HwDynMacAddrQueryVsiName_Type(OctetString):
    """Custom type hwDynMacAddrQueryVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwDynMacAddrQueryVsiName_Type.__name__ = "OctetString"
_HwDynMacAddrQueryVsiName_Object = MibTableColumn
hwDynMacAddrQueryVsiName = _HwDynMacAddrQueryVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33, 1, 2),
    _HwDynMacAddrQueryVsiName_Type()
)
hwDynMacAddrQueryVsiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDynMacAddrQueryVsiName.setStatus("current")


class _HwDynMacAddrQuerySiName_Type(OctetString):
    """Custom type hwDynMacAddrQuerySiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwDynMacAddrQuerySiName_Type.__name__ = "OctetString"
_HwDynMacAddrQuerySiName_Object = MibTableColumn
hwDynMacAddrQuerySiName = _HwDynMacAddrQuerySiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33, 1, 3),
    _HwDynMacAddrQuerySiName_Type()
)
hwDynMacAddrQuerySiName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDynMacAddrQuerySiName.setStatus("current")


class _HwDynMacAddrQueryBridgeId_Type(Integer32):
    """Custom type hwDynMacAddrQueryBridgeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwDynMacAddrQueryBridgeId_Type.__name__ = "Integer32"
_HwDynMacAddrQueryBridgeId_Object = MibTableColumn
hwDynMacAddrQueryBridgeId = _HwDynMacAddrQueryBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33, 1, 4),
    _HwDynMacAddrQueryBridgeId_Type()
)
hwDynMacAddrQueryBridgeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDynMacAddrQueryBridgeId.setStatus("current")
_HwDynMacAddrQueryMacAddr_Type = MacAddress
_HwDynMacAddrQueryMacAddr_Object = MibTableColumn
hwDynMacAddrQueryMacAddr = _HwDynMacAddrQueryMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33, 1, 5),
    _HwDynMacAddrQueryMacAddr_Type()
)
hwDynMacAddrQueryMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDynMacAddrQueryMacAddr.setStatus("current")


class _HwDynMacAddrQueryConditionMode_Type(Integer32):
    """Custom type hwDynMacAddrQueryConditionMode based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("showall", 1),
          ("showbymac", 2),
          ("showbymacvlan", 3),
          ("showbymacvsi", 11),
          ("showbyport", 9),
          ("showbyportvlan", 10),
          ("showbyportvsi", 15),
          ("showbytype", 4),
          ("showbytypeport", 6),
          ("showbytypeportvlan", 7),
          ("showbytypeportvsi", 13),
          ("showbytypeslot", 17),
          ("showbytypeslotport", 20),
          ("showbytypeslotportvlan", 21),
          ("showbytypeslotportvsi", 23),
          ("showbytypeslotsourceslot", 18),
          ("showbytypeslotvlan", 19),
          ("showbytypeslotvsi", 22),
          ("showbytypeslotvsipw", 24),
          ("showbytypevlan", 5),
          ("showbytypevsi", 12),
          ("showbyvlan", 8),
          ("showbyvsi", 14),
          ("showbyvsipw", 16))
    )


_HwDynMacAddrQueryConditionMode_Type.__name__ = "Integer32"
_HwDynMacAddrQueryConditionMode_Object = MibTableColumn
hwDynMacAddrQueryConditionMode = _HwDynMacAddrQueryConditionMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33, 1, 6),
    _HwDynMacAddrQueryConditionMode_Type()
)
hwDynMacAddrQueryConditionMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDynMacAddrQueryConditionMode.setStatus("current")


class _HwDynMacAddrQueryConditionStringA_Type(OctetString):
    """Custom type hwDynMacAddrQueryConditionStringA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwDynMacAddrQueryConditionStringA_Type.__name__ = "OctetString"
_HwDynMacAddrQueryConditionStringA_Object = MibTableColumn
hwDynMacAddrQueryConditionStringA = _HwDynMacAddrQueryConditionStringA_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33, 1, 7),
    _HwDynMacAddrQueryConditionStringA_Type()
)
hwDynMacAddrQueryConditionStringA.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDynMacAddrQueryConditionStringA.setStatus("current")


class _HwDynMacAddrQueryConditionStringB_Type(OctetString):
    """Custom type hwDynMacAddrQueryConditionStringB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwDynMacAddrQueryConditionStringB_Type.__name__ = "OctetString"
_HwDynMacAddrQueryConditionStringB_Object = MibTableColumn
hwDynMacAddrQueryConditionStringB = _HwDynMacAddrQueryConditionStringB_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33, 1, 8),
    _HwDynMacAddrQueryConditionStringB_Type()
)
hwDynMacAddrQueryConditionStringB.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDynMacAddrQueryConditionStringB.setStatus("current")
_HwDynMacAddrQueryConditionDigitA_Type = Unsigned32
_HwDynMacAddrQueryConditionDigitA_Object = MibTableColumn
hwDynMacAddrQueryConditionDigitA = _HwDynMacAddrQueryConditionDigitA_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33, 1, 9),
    _HwDynMacAddrQueryConditionDigitA_Type()
)
hwDynMacAddrQueryConditionDigitA.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDynMacAddrQueryConditionDigitA.setStatus("current")
_HwDynMacAddrQueryConditionDigitB_Type = Unsigned32
_HwDynMacAddrQueryConditionDigitB_Object = MibTableColumn
hwDynMacAddrQueryConditionDigitB = _HwDynMacAddrQueryConditionDigitB_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33, 1, 10),
    _HwDynMacAddrQueryConditionDigitB_Type()
)
hwDynMacAddrQueryConditionDigitB.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDynMacAddrQueryConditionDigitB.setStatus("current")
_HwDynMacAddrQueryConditionDigitC_Type = Unsigned32
_HwDynMacAddrQueryConditionDigitC_Object = MibTableColumn
hwDynMacAddrQueryConditionDigitC = _HwDynMacAddrQueryConditionDigitC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33, 1, 11),
    _HwDynMacAddrQueryConditionDigitC_Type()
)
hwDynMacAddrQueryConditionDigitC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDynMacAddrQueryConditionDigitC.setStatus("current")


class _HwDynMacAddrQueryType_Type(OctetString):
    """Custom type hwDynMacAddrQueryType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwDynMacAddrQueryType_Type.__name__ = "OctetString"
_HwDynMacAddrQueryType_Object = MibTableColumn
hwDynMacAddrQueryType = _HwDynMacAddrQueryType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33, 1, 12),
    _HwDynMacAddrQueryType_Type()
)
hwDynMacAddrQueryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDynMacAddrQueryType.setStatus("current")
_HwDynMacAddrQueryIfIndex_Type = InterfaceIndexOrZero
_HwDynMacAddrQueryIfIndex_Object = MibTableColumn
hwDynMacAddrQueryIfIndex = _HwDynMacAddrQueryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33, 1, 13),
    _HwDynMacAddrQueryIfIndex_Type()
)
hwDynMacAddrQueryIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDynMacAddrQueryIfIndex.setStatus("current")
_HwDynMacAddrQueryPeVlanId_Type = VlanIdOrNone
_HwDynMacAddrQueryPeVlanId_Object = MibTableColumn
hwDynMacAddrQueryPeVlanId = _HwDynMacAddrQueryPeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33, 1, 14),
    _HwDynMacAddrQueryPeVlanId_Type()
)
hwDynMacAddrQueryPeVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDynMacAddrQueryPeVlanId.setStatus("current")
_HwDynMacAddrQueryCeVlanId_Type = VlanIdOrNone
_HwDynMacAddrQueryCeVlanId_Object = MibTableColumn
hwDynMacAddrQueryCeVlanId = _HwDynMacAddrQueryCeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33, 1, 15),
    _HwDynMacAddrQueryCeVlanId_Type()
)
hwDynMacAddrQueryCeVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDynMacAddrQueryCeVlanId.setStatus("current")
_HwDynMacAddrQueryAtmIfIndex_Type = InterfaceIndexOrZero
_HwDynMacAddrQueryAtmIfIndex_Object = MibTableColumn
hwDynMacAddrQueryAtmIfIndex = _HwDynMacAddrQueryAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33, 1, 16),
    _HwDynMacAddrQueryAtmIfIndex_Type()
)
hwDynMacAddrQueryAtmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDynMacAddrQueryAtmIfIndex.setStatus("current")


class _HwDynMacAddrQueryVpi_Type(Integer32):
    """Custom type hwDynMacAddrQueryVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwDynMacAddrQueryVpi_Type.__name__ = "Integer32"
_HwDynMacAddrQueryVpi_Object = MibTableColumn
hwDynMacAddrQueryVpi = _HwDynMacAddrQueryVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33, 1, 17),
    _HwDynMacAddrQueryVpi_Type()
)
hwDynMacAddrQueryVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDynMacAddrQueryVpi.setStatus("current")


class _HwDynMacAddrQueryVci_Type(Integer32):
    """Custom type hwDynMacAddrQueryVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwDynMacAddrQueryVci_Type.__name__ = "Integer32"
_HwDynMacAddrQueryVci_Object = MibTableColumn
hwDynMacAddrQueryVci = _HwDynMacAddrQueryVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33, 1, 18),
    _HwDynMacAddrQueryVci_Type()
)
hwDynMacAddrQueryVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDynMacAddrQueryVci.setStatus("current")
_HwDynMacAddrQueryPeerIp_Type = IpAddress
_HwDynMacAddrQueryPeerIp_Object = MibTableColumn
hwDynMacAddrQueryPeerIp = _HwDynMacAddrQueryPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33, 1, 19),
    _HwDynMacAddrQueryPeerIp_Type()
)
hwDynMacAddrQueryPeerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDynMacAddrQueryPeerIp.setStatus("current")
_HwDynMacAddrQueryPwId_Type = Unsigned32
_HwDynMacAddrQueryPwId_Object = MibTableColumn
hwDynMacAddrQueryPwId = _HwDynMacAddrQueryPwId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33, 1, 20),
    _HwDynMacAddrQueryPwId_Type()
)
hwDynMacAddrQueryPwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDynMacAddrQueryPwId.setStatus("current")


class _HwDynMacAddrQueryMacTunnel_Type(OctetString):
    """Custom type hwDynMacAddrQueryMacTunnel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwDynMacAddrQueryMacTunnel_Type.__name__ = "OctetString"
_HwDynMacAddrQueryMacTunnel_Object = MibTableColumn
hwDynMacAddrQueryMacTunnel = _HwDynMacAddrQueryMacTunnel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33, 1, 21),
    _HwDynMacAddrQueryMacTunnel_Type()
)
hwDynMacAddrQueryMacTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDynMacAddrQueryMacTunnel.setStatus("current")


class _HwDynMacAddrQueryAgingTime_Type(Integer32):
    """Custom type hwDynMacAddrQueryAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_HwDynMacAddrQueryAgingTime_Type.__name__ = "Integer32"
_HwDynMacAddrQueryAgingTime_Object = MibTableColumn
hwDynMacAddrQueryAgingTime = _HwDynMacAddrQueryAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 33, 1, 22),
    _HwDynMacAddrQueryAgingTime_Type()
)
hwDynMacAddrQueryAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDynMacAddrQueryAgingTime.setStatus("current")
_HwMacInfoQueryTable_Object = MibTable
hwMacInfoQueryTable = _HwMacInfoQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 34)
)
if mibBuilder.loadTexts:
    hwMacInfoQueryTable.setStatus("current")
_HwMacInfoQueryEntry_Object = MibTableRow
hwMacInfoQueryEntry = _HwMacInfoQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 34, 1)
)
hwMacInfoQueryEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwMacInfoQueryConditionMode"),
    (0, "HUAWEI-L2MAM-MIB", "hwMacInfoQueryConditionStringA"),
    (0, "HUAWEI-L2MAM-MIB", "hwMacInfoQueryConditionStringB"),
    (0, "HUAWEI-L2MAM-MIB", "hwMacInfoQueryConditionStringC"),
    (0, "HUAWEI-L2MAM-MIB", "hwMacInfoQueryConditionDigitA"),
    (0, "HUAWEI-L2MAM-MIB", "hwMacInfoQueryConditionDigitB"),
    (0, "HUAWEI-L2MAM-MIB", "hwMacInfoQueryConditionDigitC"),
)
if mibBuilder.loadTexts:
    hwMacInfoQueryEntry.setStatus("current")


class _HwMacInfoQueryConditionMode_Type(Integer32):
    """Custom type hwMacInfoQueryConditionMode based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("showcapacity", 21),
          ("showtotalnumberbyall", 1),
          ("showtotalnumberbyport", 7),
          ("showtotalnumberbyportvlan", 8),
          ("showtotalnumberbyportvsi", 12),
          ("showtotalnumberbytype", 2),
          ("showtotalnumberbytypeport", 4),
          ("showtotalnumberbytypeportvlan", 5),
          ("showtotalnumberbytypeportvsi", 10),
          ("showtotalnumberbytypeslot", 14),
          ("showtotalnumberbytypeslotport", 16),
          ("showtotalnumberbytypeslotportvlan", 17),
          ("showtotalnumberbytypeslotportvsi", 19),
          ("showtotalnumberbytypeslotvlan", 15),
          ("showtotalnumberbytypeslotvsi", 18),
          ("showtotalnumberbytypeslotvsipw", 20),
          ("showtotalnumberbytypevlan", 3),
          ("showtotalnumberbytypevsi", 9),
          ("showtotalnumberbyvlan", 6),
          ("showtotalnumberbyvsi", 11),
          ("showtotalnumberbyvsipw", 13))
    )


_HwMacInfoQueryConditionMode_Type.__name__ = "Integer32"
_HwMacInfoQueryConditionMode_Object = MibTableColumn
hwMacInfoQueryConditionMode = _HwMacInfoQueryConditionMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 34, 1, 1),
    _HwMacInfoQueryConditionMode_Type()
)
hwMacInfoQueryConditionMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacInfoQueryConditionMode.setStatus("current")


class _HwMacInfoQueryConditionStringA_Type(OctetString):
    """Custom type hwMacInfoQueryConditionStringA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwMacInfoQueryConditionStringA_Type.__name__ = "OctetString"
_HwMacInfoQueryConditionStringA_Object = MibTableColumn
hwMacInfoQueryConditionStringA = _HwMacInfoQueryConditionStringA_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 34, 1, 2),
    _HwMacInfoQueryConditionStringA_Type()
)
hwMacInfoQueryConditionStringA.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacInfoQueryConditionStringA.setStatus("current")


class _HwMacInfoQueryConditionStringB_Type(OctetString):
    """Custom type hwMacInfoQueryConditionStringB based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HwMacInfoQueryConditionStringB_Type.__name__ = "OctetString"
_HwMacInfoQueryConditionStringB_Object = MibTableColumn
hwMacInfoQueryConditionStringB = _HwMacInfoQueryConditionStringB_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 34, 1, 3),
    _HwMacInfoQueryConditionStringB_Type()
)
hwMacInfoQueryConditionStringB.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacInfoQueryConditionStringB.setStatus("current")


class _HwMacInfoQueryConditionStringC_Type(OctetString):
    """Custom type hwMacInfoQueryConditionStringC based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwMacInfoQueryConditionStringC_Type.__name__ = "OctetString"
_HwMacInfoQueryConditionStringC_Object = MibTableColumn
hwMacInfoQueryConditionStringC = _HwMacInfoQueryConditionStringC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 34, 1, 4),
    _HwMacInfoQueryConditionStringC_Type()
)
hwMacInfoQueryConditionStringC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacInfoQueryConditionStringC.setStatus("current")
_HwMacInfoQueryConditionDigitA_Type = Unsigned32
_HwMacInfoQueryConditionDigitA_Object = MibTableColumn
hwMacInfoQueryConditionDigitA = _HwMacInfoQueryConditionDigitA_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 34, 1, 5),
    _HwMacInfoQueryConditionDigitA_Type()
)
hwMacInfoQueryConditionDigitA.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacInfoQueryConditionDigitA.setStatus("current")
_HwMacInfoQueryConditionDigitB_Type = Unsigned32
_HwMacInfoQueryConditionDigitB_Object = MibTableColumn
hwMacInfoQueryConditionDigitB = _HwMacInfoQueryConditionDigitB_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 34, 1, 6),
    _HwMacInfoQueryConditionDigitB_Type()
)
hwMacInfoQueryConditionDigitB.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacInfoQueryConditionDigitB.setStatus("current")
_HwMacInfoQueryConditionDigitC_Type = Unsigned32
_HwMacInfoQueryConditionDigitC_Object = MibTableColumn
hwMacInfoQueryConditionDigitC = _HwMacInfoQueryConditionDigitC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 34, 1, 7),
    _HwMacInfoQueryConditionDigitC_Type()
)
hwMacInfoQueryConditionDigitC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacInfoQueryConditionDigitC.setStatus("current")
_HwMacInfoQueryTotalNumber_Type = Unsigned32
_HwMacInfoQueryTotalNumber_Object = MibTableColumn
hwMacInfoQueryTotalNumber = _HwMacInfoQueryTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 34, 1, 8),
    _HwMacInfoQueryTotalNumber_Type()
)
hwMacInfoQueryTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacInfoQueryTotalNumber.setStatus("current")
_HwMacInfoQueryTotalLocalNumber_Type = Unsigned32
_HwMacInfoQueryTotalLocalNumber_Object = MibTableColumn
hwMacInfoQueryTotalLocalNumber = _HwMacInfoQueryTotalLocalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 34, 1, 9),
    _HwMacInfoQueryTotalLocalNumber_Type()
)
hwMacInfoQueryTotalLocalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacInfoQueryTotalLocalNumber.setStatus("current")
_HwMacInfoQueryTotalRemoteNumber_Type = Unsigned32
_HwMacInfoQueryTotalRemoteNumber_Object = MibTableColumn
hwMacInfoQueryTotalRemoteNumber = _HwMacInfoQueryTotalRemoteNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 34, 1, 10),
    _HwMacInfoQueryTotalRemoteNumber_Type()
)
hwMacInfoQueryTotalRemoteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacInfoQueryTotalRemoteNumber.setStatus("current")
_HwMacInfoQueryCapacity_Type = Unsigned32
_HwMacInfoQueryCapacity_Object = MibTableColumn
hwMacInfoQueryCapacity = _HwMacInfoQueryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 34, 1, 11),
    _HwMacInfoQueryCapacity_Type()
)
hwMacInfoQueryCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacInfoQueryCapacity.setStatus("current")
_HwVplsOverGreTable_Object = MibTable
hwVplsOverGreTable = _HwVplsOverGreTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 35)
)
if mibBuilder.loadTexts:
    hwVplsOverGreTable.setStatus("current")
_HwVplsOverGreEntry_Object = MibTableRow
hwVplsOverGreEntry = _HwVplsOverGreEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 35, 1)
)
hwVplsOverGreEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwVplsOverGrePwId"),
)
if mibBuilder.loadTexts:
    hwVplsOverGreEntry.setStatus("current")
_HwVplsOverGrePwId_Type = Integer32
_HwVplsOverGrePwId_Object = MibTableColumn
hwVplsOverGrePwId = _HwVplsOverGrePwId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 35, 1, 1),
    _HwVplsOverGrePwId_Type()
)
hwVplsOverGrePwId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVplsOverGrePwId.setStatus("current")
_HwRemoteIp_Type = IpAddress
_HwRemoteIp_Object = MibTableColumn
hwRemoteIp = _HwRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 35, 1, 2),
    _HwRemoteIp_Type()
)
hwRemoteIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwRemoteIp.setStatus("current")


class _HwVplsOverGreVsiName_Type(OctetString):
    """Custom type hwVplsOverGreVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwVplsOverGreVsiName_Type.__name__ = "OctetString"
_HwVplsOverGreVsiName_Object = MibTableColumn
hwVplsOverGreVsiName = _HwVplsOverGreVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 35, 1, 3),
    _HwVplsOverGreVsiName_Type()
)
hwVplsOverGreVsiName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwVplsOverGreVsiName.setStatus("current")
_HwVllByPassOverGreTable_Object = MibTable
hwVllByPassOverGreTable = _HwVllByPassOverGreTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 36)
)
if mibBuilder.loadTexts:
    hwVllByPassOverGreTable.setStatus("current")
_HwVllByPassOverGreEntry_Object = MibTableRow
hwVllByPassOverGreEntry = _HwVllByPassOverGreEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 36, 1)
)
hwVllByPassOverGreEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwVLLACPortIndex"),
)
if mibBuilder.loadTexts:
    hwVllByPassOverGreEntry.setStatus("current")
_HwVLLACPortIndex_Type = Integer32
_HwVLLACPortIndex_Object = MibTableColumn
hwVLLACPortIndex = _HwVLLACPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 36, 1, 1),
    _HwVLLACPortIndex_Type()
)
hwVLLACPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVLLACPortIndex.setStatus("current")


class _HwVLLACPortName_Type(OctetString):
    """Custom type hwVLLACPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwVLLACPortName_Type.__name__ = "OctetString"
_HwVLLACPortName_Object = MibTableColumn
hwVLLACPortName = _HwVLLACPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 36, 1, 2),
    _HwVLLACPortName_Type()
)
hwVLLACPortName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwVLLACPortName.setStatus("current")
_HwUnucFlowAlarmTable_Object = MibTable
hwUnucFlowAlarmTable = _HwUnucFlowAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 37)
)
if mibBuilder.loadTexts:
    hwUnucFlowAlarmTable.setStatus("current")
_HwUnucFlowAlarmEntry_Object = MibTableRow
hwUnucFlowAlarmEntry = _HwUnucFlowAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 37, 1)
)
hwUnucFlowAlarmEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwUNUCPortIndex"),
)
if mibBuilder.loadTexts:
    hwUnucFlowAlarmEntry.setStatus("current")
_HwUNUCPortIndex_Type = Integer32
_HwUNUCPortIndex_Object = MibTableColumn
hwUNUCPortIndex = _HwUNUCPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 37, 1, 1),
    _HwUNUCPortIndex_Type()
)
hwUNUCPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwUNUCPortIndex.setStatus("current")


class _HwUNUCPortName_Type(OctetString):
    """Custom type hwUNUCPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwUNUCPortName_Type.__name__ = "OctetString"
_HwUNUCPortName_Object = MibTableColumn
hwUNUCPortName = _HwUNUCPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 37, 1, 2),
    _HwUNUCPortName_Type()
)
hwUNUCPortName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUNUCPortName.setStatus("current")
_HwUNUCPortAlarmThreshold_Type = Integer32
_HwUNUCPortAlarmThreshold_Object = MibTableColumn
hwUNUCPortAlarmThreshold = _HwUNUCPortAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 37, 1, 3),
    _HwUNUCPortAlarmThreshold_Type()
)
hwUNUCPortAlarmThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUNUCPortAlarmThreshold.setStatus("current")
_HwUNUCPortRealFlow_Type = Integer32
_HwUNUCPortRealFlow_Object = MibTableColumn
hwUNUCPortRealFlow = _HwUNUCPortRealFlow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 37, 1, 4),
    _HwUNUCPortRealFlow_Type()
)
hwUNUCPortRealFlow.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUNUCPortRealFlow.setStatus("current")
_HwMacHopAlarmTable_Object = MibTable
hwMacHopAlarmTable = _HwMacHopAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 38)
)
if mibBuilder.loadTexts:
    hwMacHopAlarmTable.setStatus("current")
_HwMacHopAlarmEntry_Object = MibTableRow
hwMacHopAlarmEntry = _HwMacHopAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 38, 1)
)
hwMacHopAlarmEntry.setIndexNames(
    (0, "HUAWEI-L2MAM-MIB", "hwMacHopVlan"),
    (0, "HUAWEI-L2MAM-MIB", "hwMacHopVsiName"),
    (0, "HUAWEI-L2MAM-MIB", "hwMacHopBdID"),
)
if mibBuilder.loadTexts:
    hwMacHopAlarmEntry.setStatus("current")


class _HwMacHopVlan_Type(Unsigned32):
    """Custom type hwMacHopVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwMacHopVlan_Type.__name__ = "Unsigned32"
_HwMacHopVlan_Object = MibTableColumn
hwMacHopVlan = _HwMacHopVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 38, 1, 1),
    _HwMacHopVlan_Type()
)
hwMacHopVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMacHopVlan.setStatus("current")


class _HwMacHopVsiName_Type(OctetString):
    """Custom type hwMacHopVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwMacHopVsiName_Type.__name__ = "OctetString"
_HwMacHopVsiName_Object = MibTableColumn
hwMacHopVsiName = _HwMacHopVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 38, 1, 2),
    _HwMacHopVsiName_Type()
)
hwMacHopVsiName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMacHopVsiName.setStatus("current")


class _HwMacHopBdID_Type(Unsigned32):
    """Custom type hwMacHopBdID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_HwMacHopBdID_Type.__name__ = "Unsigned32"
_HwMacHopBdID_Object = MibTableColumn
hwMacHopBdID = _HwMacHopBdID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 38, 1, 3),
    _HwMacHopBdID_Type()
)
hwMacHopBdID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMacHopBdID.setStatus("current")


class _HwMacHopPortName1_Type(OctetString):
    """Custom type hwMacHopPortName1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwMacHopPortName1_Type.__name__ = "OctetString"
_HwMacHopPortName1_Object = MibTableColumn
hwMacHopPortName1 = _HwMacHopPortName1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 38, 1, 4),
    _HwMacHopPortName1_Type()
)
hwMacHopPortName1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMacHopPortName1.setStatus("current")


class _HwMacHopPortName2_Type(OctetString):
    """Custom type hwMacHopPortName2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwMacHopPortName2_Type.__name__ = "OctetString"
_HwMacHopPortName2_Object = MibTableColumn
hwMacHopPortName2 = _HwMacHopPortName2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 38, 1, 5),
    _HwMacHopPortName2_Type()
)
hwMacHopPortName2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMacHopPortName2.setStatus("current")


class _HwMacHopPortName3_Type(OctetString):
    """Custom type hwMacHopPortName3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwMacHopPortName3_Type.__name__ = "OctetString"
_HwMacHopPortName3_Object = MibTableColumn
hwMacHopPortName3 = _HwMacHopPortName3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 38, 1, 6),
    _HwMacHopPortName3_Type()
)
hwMacHopPortName3.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMacHopPortName3.setStatus("current")


class _HwMacHopPortName4_Type(OctetString):
    """Custom type hwMacHopPortName4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwMacHopPortName4_Type.__name__ = "OctetString"
_HwMacHopPortName4_Object = MibTableColumn
hwMacHopPortName4 = _HwMacHopPortName4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 38, 1, 7),
    _HwMacHopPortName4_Type()
)
hwMacHopPortName4.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMacHopPortName4.setStatus("current")


class _HwMacHopPWInfo_Type(OctetString):
    """Custom type hwMacHopPWInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_HwMacHopPWInfo_Type.__name__ = "OctetString"
_HwMacHopPWInfo_Object = MibTableColumn
hwMacHopPWInfo = _HwMacHopPWInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 38, 1, 8),
    _HwMacHopPWInfo_Type()
)
hwMacHopPWInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMacHopPWInfo.setStatus("current")
_HwPwMacSpoofingAttackMacAddr_Type = MacAddress
_HwPwMacSpoofingAttackMacAddr_Object = MibScalar
hwPwMacSpoofingAttackMacAddr = _HwPwMacSpoofingAttackMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 39),
    _HwPwMacSpoofingAttackMacAddr_Type()
)
hwPwMacSpoofingAttackMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPwMacSpoofingAttackMacAddr.setStatus("current")
_HwBdMacLimitBdId_Type = Integer32
_HwBdMacLimitBdId_Object = MibScalar
hwBdMacLimitBdId = _HwBdMacLimitBdId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 40),
    _HwBdMacLimitBdId_Type()
)
hwBdMacLimitBdId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBdMacLimitBdId.setStatus("current")
_HwBdMacLimitMaxMac_Type = MacAddress
_HwBdMacLimitMaxMac_Object = MibScalar
hwBdMacLimitMaxMac = _HwBdMacLimitMaxMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 41),
    _HwBdMacLimitMaxMac_Type()
)
hwBdMacLimitMaxMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBdMacLimitMaxMac.setStatus("current")
_HwL2MAMConformance_ObjectIdentity = ObjectIdentity
hwL2MAMConformance = _HwL2MAMConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2)
)
_HwL2MAMGroups_ObjectIdentity = ObjectIdentity
hwL2MAMGroups = _HwL2MAMGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 1)
)
_HwL2MAMCompliances_ObjectIdentity = ObjectIdentity
hwL2MAMCompliances = _HwL2MAMCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 2)
)
_HwL2MACTrapGroups_ObjectIdentity = ObjectIdentity
hwL2MACTrapGroups = _HwL2MACTrapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 3)
)

# Managed Objects groups

hwL2MAMCfgFdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 1, 1)
)
hwL2MAMCfgFdbGroup.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwCfgFdbPort"),
        ("HUAWEI-L2MAM-MIB", "hwCfgFdbType"),
        ("HUAWEI-L2MAM-MIB", "hwCfgFdbAtmPort"),
        ("HUAWEI-L2MAM-MIB", "hwCfgFdbVpi"),
        ("HUAWEI-L2MAM-MIB", "hwCfgFdbVci"),
        ("HUAWEI-L2MAM-MIB", "hwCfgFdbRowstatus"),
        ("HUAWEI-L2MAM-MIB", "hwCfgFdbCeDefault"),
        ("HUAWEI-L2MAM-MIB", "hwUntargetMacNum"))
)
if mibBuilder.loadTexts:
    hwL2MAMCfgFdbGroup.setStatus("current")

hwL2MAMDynFdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 1, 2)
)
hwL2MAMDynFdbGroup.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwDynFdbPort"),
        ("HUAWEI-L2MAM-MIB", "hwDynFdbAtmPort"),
        ("HUAWEI-L2MAM-MIB", "hwDynFdbVpi"),
        ("HUAWEI-L2MAM-MIB", "hwDynFdbVci"),
        ("HUAWEI-L2MAM-MIB", "hwDynFdbRowstatus"),
        ("HUAWEI-L2MAM-MIB", "hwDynSecurityFdbToStaticEnable"))
)
if mibBuilder.loadTexts:
    hwL2MAMDynFdbGroup.setStatus("current")

hwL2MAMMacLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 1, 3)
)
hwL2MAMMacLimitGroup.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwMacLimitMaxMac"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitMaxRate"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitAction"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitAlarm"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitRowstatus"),
        ("HUAWEI-L2MAM-MIB", "hwL2MaxMacLimit"),
        ("HUAWEI-L2MAM-MIB", "hwMacAddressLearn"),
        ("HUAWEI-L2MAM-MIB", "hwMacDynAddressLearnNum"),
        ("HUAWEI-L2MAM-MIB", "hwMacSecureAddressLearnNum"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitRuleMaxMac"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitRuleMaxRate"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitRuleAction"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitRuleAlarm"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitRuleRowstatus"),
        ("HUAWEI-L2MAM-MIB", "hwMacRuleDynAddressLearnNum"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitApplyRuleName"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitApplyRowstatus"),
        ("HUAWEI-L2MAM-MIB", "hwPwMacLimitMaxMac"),
        ("HUAWEI-L2MAM-MIB", "hwPwMacLimitMaxRate"),
        ("HUAWEI-L2MAM-MIB", "hwPwMacLimitAction"),
        ("HUAWEI-L2MAM-MIB", "hwPwMacLimitAlarm"),
        ("HUAWEI-L2MAM-MIB", "hwPwMacLimitRowstatus"),
        ("HUAWEI-L2MAM-MIB", "hwPwMacAddressLearn"),
        ("HUAWEI-L2MAM-MIB", "hwPwMacDynAddressLearnNum"),
        ("HUAWEI-L2MAM-MIB", "hwSlotMacLimitMaxMac"),
        ("HUAWEI-L2MAM-MIB", "hwSlotMacLimitMaxRate"),
        ("HUAWEI-L2MAM-MIB", "hwSlotMacLimitAction"),
        ("HUAWEI-L2MAM-MIB", "hwSlotMacLimitAlarm"),
        ("HUAWEI-L2MAM-MIB", "hwSlotMacLimitRowstatus"),
        ("HUAWEI-L2MAM-MIB", "hwBridgeMacAgingTime"))
)
if mibBuilder.loadTexts:
    hwL2MAMMacLimitGroup.setStatus("current")

hwL2MAMMacUsageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 1, 4)
)
hwL2MAMMacUsageGroup.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwMacEntityUsage"),
        ("HUAWEI-L2MAM-MIB", "hwMacEntityUsageThreshold"))
)
if mibBuilder.loadTexts:
    hwL2MAMMacUsageGroup.setStatus("current")

hwdbCfg3tupleFdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 1, 5)
)
hwdbCfg3tupleFdbGroup.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwdbCfg3tupleFdbOutPort"),
        ("HUAWEI-L2MAM-MIB", "hwdbCfg3tupleFdbRowStatus"))
)
if mibBuilder.loadTexts:
    hwdbCfg3tupleFdbGroup.setStatus("current")

hwL2MAMObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 1, 6)
)
hwL2MAMObjectsGroup.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwMacAgingTime"),
        ("HUAWEI-L2MAM-MIB", "hwMacRestrict"),
        ("HUAWEI-L2MAM-MIB", "hwMacGlobalStatistics"),
        ("HUAWEI-L2MAM-MIB", "hwDiscardIllegalMacEnable"),
        ("HUAWEI-L2MAM-MIB", "hwDiscardIllegalMacAlarm"),
        ("HUAWEI-L2MAM-MIB", "hwMacSpoofingDefend"),
        ("HUAWEI-L2MAM-MIB", "hwMacflappingMac"),
        ("HUAWEI-L2MAM-MIB", "hwMacFlappingVlan"))
)
if mibBuilder.loadTexts:
    hwL2MAMObjectsGroup.setStatus("current")

hwPortSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 1, 7)
)
hwPortSecurityGroup.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwPortSecurityEnabled"),
        ("HUAWEI-L2MAM-MIB", "hwPortSecurityProtectAction"),
        ("HUAWEI-L2MAM-MIB", "hwPortSecurityAllDynToStaticEnable"),
        ("HUAWEI-L2MAM-MIB", "hwPortSecurityAllDynToStickyEnable"),
        ("HUAWEI-L2MAM-MIB", "hwPortSecurityMaxMacNum"))
)
if mibBuilder.loadTexts:
    hwPortSecurityGroup.setStatus("current")

hwMacIfStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 1, 8)
)
hwMacIfStatisticsGroup.setObjects(
    ("HUAWEI-L2MAM-MIB", "hwMacIfStatistics")
)
if mibBuilder.loadTexts:
    hwMacIfStatisticsGroup.setStatus("current")

hwMacSlotStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 1, 9)
)
hwMacSlotStatisticsGroup.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwMacSlotStatistics"),
        ("HUAWEI-L2MAM-MIB", "hwMacSlotStatisticsSpecify"))
)
if mibBuilder.loadTexts:
    hwMacSlotStatisticsGroup.setStatus("current")

hwMacVlanStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 1, 10)
)
hwMacVlanStatisticsGroup.setObjects(
    ("HUAWEI-L2MAM-MIB", "hwMacVlanStatistics")
)
if mibBuilder.loadTexts:
    hwMacVlanStatisticsGroup.setStatus("current")

hwMacVsiStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 1, 11)
)
hwMacVsiStatisticsGroup.setObjects(
    ("HUAWEI-L2MAM-MIB", "hwMacVsiStatistics")
)
if mibBuilder.loadTexts:
    hwMacVsiStatisticsGroup.setStatus("current")

hwMacSpoofingDefendGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 1, 12)
)
hwMacSpoofingDefendGroup.setObjects(
    ("HUAWEI-L2MAM-MIB", "hwMacSpoofingDefendEnabled")
)
if mibBuilder.loadTexts:
    hwMacSpoofingDefendGroup.setStatus("current")

hwL2ProtocolTunnelTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 1, 13)
)
hwL2ProtocolTunnelTrapGroup.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwL2ProtocolTunnelTrapPortName"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtocolTunnelTrapProtocolName"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtocolTunnelTrapDropThreshold"))
)
if mibBuilder.loadTexts:
    hwL2ProtocolTunnelTrapGroup.setStatus("current")

hwL2ProtclTnlStdProtclGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 1, 14)
)
hwL2ProtclTnlStdProtclGroup.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwL2ProtclTnlStdProtclMacAddr"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtclTnlStdEncapType"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtclTnlStdProtclType"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtclTnlStdGroupMacAddr"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtclTnlStdGroupDefault"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtclTnlStdPriority"))
)
if mibBuilder.loadTexts:
    hwL2ProtclTnlStdProtclGroup.setStatus("current")

hwL2ProtclTnlCusProtclGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 1, 15)
)
hwL2ProtclTnlCusProtclGroup.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwL2ProtclTnlCusProtclMacAddr"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtclTnlCusEncapType"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtclTnlCusProtclType"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtclTnlCusGroupMacAddr"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtclTnlCusGroupDefault"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtclTnlCusPriority"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtclTnlCusRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2ProtclTnlCusProtclGroup.setStatus("current")

hwL2ProtclTnlEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 1, 16)
)
hwL2ProtclTnlEnableGroup.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwL2ProtclTnlEnableTransMode"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtclTnlEnableTagListLow"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtclTnlEnableTagListHigh"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtclTnlEnableDropthresholdRate"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtclTnlEnableRowStatus"))
)
if mibBuilder.loadTexts:
    hwL2ProtclTnlEnableGroup.setStatus("current")

hwL2ProtclTnlStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 1, 17)
)
hwL2ProtclTnlStatisticsGroup.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwL2ProtclTnlStatisticsDropthrhldRate"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtclTnlStatisticsInputPkts"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtclTnlStatisticsOutputPkts"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtclTnlStatisticsDropPkts"))
)
if mibBuilder.loadTexts:
    hwL2ProtclTnlStatisticsGroup.setStatus("current")

hwCfgMacAddrQueryTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 1, 18)
)
hwCfgMacAddrQueryTableGroup.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwCfgMacAddrQueryType"),
        ("HUAWEI-L2MAM-MIB", "hwCfgMacAddrQueryIfIndex"),
        ("HUAWEI-L2MAM-MIB", "hwCfgMacAddrQueryPeVlanId"),
        ("HUAWEI-L2MAM-MIB", "hwCfgMacAddrQueryCeVlanId"),
        ("HUAWEI-L2MAM-MIB", "hwCfgMacAddrQueryCedefaultFlag"),
        ("HUAWEI-L2MAM-MIB", "hwCfgMacAddrQueryAtmIfIndex"),
        ("HUAWEI-L2MAM-MIB", "hwCfgMacAddrQueryVpi"),
        ("HUAWEI-L2MAM-MIB", "hwCfgMacAddrQueryVci"),
        ("HUAWEI-L2MAM-MIB", "hwCfgMacAddrQueryMacTunnel"))
)
if mibBuilder.loadTexts:
    hwCfgMacAddrQueryTableGroup.setStatus("current")

hwDynMacAddrQueryTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 1, 19)
)
hwDynMacAddrQueryTableGroup.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwDynMacAddrQueryType"),
        ("HUAWEI-L2MAM-MIB", "hwDynMacAddrQueryIfIndex"),
        ("HUAWEI-L2MAM-MIB", "hwDynMacAddrQueryPeVlanId"),
        ("HUAWEI-L2MAM-MIB", "hwDynMacAddrQueryCeVlanId"),
        ("HUAWEI-L2MAM-MIB", "hwDynMacAddrQueryAtmIfIndex"),
        ("HUAWEI-L2MAM-MIB", "hwDynMacAddrQueryVpi"),
        ("HUAWEI-L2MAM-MIB", "hwDynMacAddrQueryVci"),
        ("HUAWEI-L2MAM-MIB", "hwDynMacAddrQueryPeerIp"),
        ("HUAWEI-L2MAM-MIB", "hwDynMacAddrQueryPwId"),
        ("HUAWEI-L2MAM-MIB", "hwDynMacAddrQueryMacTunnel"),
        ("HUAWEI-L2MAM-MIB", "hwDynMacAddrQueryAgingTime"))
)
if mibBuilder.loadTexts:
    hwDynMacAddrQueryTableGroup.setStatus("current")

hwMacInfoQueryTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 1, 20)
)
hwMacInfoQueryTableGroup.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwMacInfoQueryTotalNumber"),
        ("HUAWEI-L2MAM-MIB", "hwMacInfoQueryTotalLocalNumber"),
        ("HUAWEI-L2MAM-MIB", "hwMacInfoQueryTotalRemoteNumber"),
        ("HUAWEI-L2MAM-MIB", "hwMacInfoQueryCapacity"))
)
if mibBuilder.loadTexts:
    hwMacInfoQueryTableGroup.setStatus("current")


# Notification objects

hwMacUsageRaisingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 1)
)
hwMacUsageRaisingThreshold.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-L2MAM-MIB", "hwMacEntityUsage"),
        ("HUAWEI-L2MAM-MIB", "hwMacEntityUsageThreshold"))
)
if mibBuilder.loadTexts:
    hwMacUsageRaisingThreshold.setStatus(
        "current"
    )

hwMacUsageFallingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 2)
)
hwMacUsageFallingThreshold.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-L2MAM-MIB", "hwMacEntityUsage"),
        ("HUAWEI-L2MAM-MIB", "hwMacEntityUsageThreshold"))
)
if mibBuilder.loadTexts:
    hwMacUsageFallingThreshold.setStatus(
        "current"
    )

hwMacLimitNumRaisingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 3)
)
hwMacLimitNumRaisingThreshold.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("HUAWEI-L2MAM-MIB", "hwMacDynAddressLearnNum"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitMaxMac"),
        ("HUAWEI-L2IF-MIB", "hwL2IfPortName"))
)
if mibBuilder.loadTexts:
    hwMacLimitNumRaisingThreshold.setStatus(
        "current"
    )

hwMacLimitNumFallingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 4)
)
hwMacLimitNumFallingThreshold.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("HUAWEI-L2MAM-MIB", "hwMacDynAddressLearnNum"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitMaxMac"),
        ("HUAWEI-L2IF-MIB", "hwL2IfPortName"))
)
if mibBuilder.loadTexts:
    hwMacLimitNumFallingThreshold.setStatus(
        "current"
    )

hwUntargetMacNumAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 5)
)
hwUntargetMacNumAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("HUAWEI-L2MAM-MIB", "hwUntargetMacNum"))
)
if mibBuilder.loadTexts:
    hwUntargetMacNumAlarm.setStatus(
        "current"
    )

hwPortSecRcvInsecurePktAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 6)
)
hwPortSecRcvInsecurePktAlarm.setObjects(
      *(("IF-MIB", "ifDescr"),
        ("HUAWEI-L2MAM-MIB", "hwPortSecurityProtectAction"))
)
if mibBuilder.loadTexts:
    hwPortSecRcvInsecurePktAlarm.setStatus(
        "current"
    )

hwPwMacLimitNumRaisingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 7)
)
hwPwMacLimitNumRaisingThreshold.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("HUAWEI-L2MAM-MIB", "hwPwMacDynAddressLearnNum"),
        ("HUAWEI-L2MAM-MIB", "hwPwMacLimitMaxMac"))
)
if mibBuilder.loadTexts:
    hwPwMacLimitNumRaisingThreshold.setStatus(
        "current"
    )

hwPwMacLimitNumFallingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 8)
)
hwPwMacLimitNumFallingThreshold.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("HUAWEI-L2MAM-MIB", "hwPwMacDynAddressLearnNum"),
        ("HUAWEI-L2MAM-MIB", "hwPwMacLimitMaxMac"))
)
if mibBuilder.loadTexts:
    hwPwMacLimitNumFallingThreshold.setStatus(
        "current"
    )

hwPortStickyReachMaxAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 9)
)
if mibBuilder.loadTexts:
    hwPortStickyReachMaxAlarm.setStatus(
        "current"
    )

hwRecIllegalMacPktAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 10)
)
if mibBuilder.loadTexts:
    hwRecIllegalMacPktAlarm.setStatus(
        "current"
    )

hwMacLimitOverThresholdAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 11)
)
hwMacLimitOverThresholdAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("HUAWEI-L2MAM-MIB", "hwMacDynAddressLearnNum"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitMaxMac"),
        ("HUAWEI-L2IF-MIB", "hwL2IfPortName"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitVlanId"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitVsiName"))
)
if mibBuilder.loadTexts:
    hwMacLimitOverThresholdAlarm.setStatus(
        "current"
    )

hwMacFlappingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 12)
)
hwMacFlappingAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("HUAWEI-L2MAM-MIB", "hwMacflappingMac"),
        ("HUAWEI-L2MAM-MIB", "hwMacFlappingVlan"),
        ("HUAWEI-L2IF-MIB", "hwL2IfPortName"),
        ("HUAWEI-L2IF-MIB", "hwL2IfPortName"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwMacFlappingAlarm.setStatus(
        "current"
    )

hwSlotMacLimitNumRaisingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 13)
)
hwSlotMacLimitNumRaisingThreshold.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("HUAWEI-L2MAM-MIB", "hwMacDynAddressLearnNum"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitMaxMac"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwSlotMacLimitNumRaisingThreshold.setStatus(
        "current"
    )

hwSlotMacLimitNumFallingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 14)
)
hwSlotMacLimitNumFallingThreshold.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("HUAWEI-L2MAM-MIB", "hwMacDynAddressLearnNum"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitMaxMac"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwSlotMacLimitNumFallingThreshold.setStatus(
        "current"
    )

hwL2ProtocolTunnelDropThresholdRaising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 15)
)
hwL2ProtocolTunnelDropThresholdRaising.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwL2ProtocolTunnelTrapPortName"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtocolTunnelTrapProtocolName"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtocolTunnelTrapDropThreshold"))
)
if mibBuilder.loadTexts:
    hwL2ProtocolTunnelDropThresholdRaising.setStatus(
        "current"
    )

hwL2ProtocolTunnelDropThresholdFalling = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 16)
)
hwL2ProtocolTunnelDropThresholdFalling.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwL2ProtocolTunnelTrapPortName"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtocolTunnelTrapProtocolName"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtocolTunnelTrapDropThreshold"))
)
if mibBuilder.loadTexts:
    hwL2ProtocolTunnelDropThresholdFalling.setStatus(
        "current"
    )

hwVsiMacLimitNumRaisingThresholdAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 17)
)
hwVsiMacLimitNumRaisingThresholdAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitVsiName"))
)
if mibBuilder.loadTexts:
    hwVsiMacLimitNumRaisingThresholdAlarm.setStatus(
        "current"
    )

hwVsiMacLimitNumRaisingThresholdAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 18)
)
hwVsiMacLimitNumRaisingThresholdAlarmClear.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitVsiName"))
)
if mibBuilder.loadTexts:
    hwVsiMacLimitNumRaisingThresholdAlarmClear.setStatus(
        "current"
    )

hwMacLimitOverThresholdAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 19)
)
hwMacLimitOverThresholdAlarmResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("HUAWEI-L2MAM-MIB", "hwMacDynAddressLearnNum"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitMaxMac"),
        ("HUAWEI-L2IF-MIB", "hwL2IfPortName"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitVlanId"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitVsiName"))
)
if mibBuilder.loadTexts:
    hwMacLimitOverThresholdAlarmResume.setStatus(
        "current"
    )

hwSlotMacNumRaisingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 20)
)
hwSlotMacNumRaisingThreshold.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwMacSlotStatistics"),
        ("HUAWEI-L2MAM-MIB", "hwMacSlotStatisticsSpecify"))
)
if mibBuilder.loadTexts:
    hwSlotMacNumRaisingThreshold.setStatus(
        "current"
    )

hwSlotMacNumFallingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 21)
)
hwSlotMacNumFallingThreshold.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwMacSlotStatistics"),
        ("HUAWEI-L2MAM-MIB", "hwMacSlotStatisticsSpecify"))
)
if mibBuilder.loadTexts:
    hwSlotMacNumFallingThreshold.setStatus(
        "current"
    )

hwMacLimitRuleNumRaisingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 22)
)
hwMacLimitRuleNumRaisingThreshold.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-L2MAM-MIB", "hwMacRuleDynAddressLearnNum"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitRuleMaxMac"))
)
if mibBuilder.loadTexts:
    hwMacLimitRuleNumRaisingThreshold.setStatus(
        "current"
    )

hwMacLimitRuleNumFallingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 23)
)
hwMacLimitRuleNumFallingThreshold.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-L2MAM-MIB", "hwMacRuleDynAddressLearnNum"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitRuleMaxMac"))
)
if mibBuilder.loadTexts:
    hwMacLimitRuleNumFallingThreshold.setStatus(
        "current"
    )

hwVplsOverGRENotSupportForwardRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 24)
)
hwVplsOverGRENotSupportForwardRising.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwVplsOverGreVsiName"),
        ("HUAWEI-L2MAM-MIB", "hwRemoteIp"))
)
if mibBuilder.loadTexts:
    hwVplsOverGRENotSupportForwardRising.setStatus(
        "current"
    )

hwVplsOverGRENotSupportForwardRisingResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 25)
)
hwVplsOverGRENotSupportForwardRisingResume.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwVplsOverGreVsiName"),
        ("HUAWEI-L2MAM-MIB", "hwRemoteIp"))
)
if mibBuilder.loadTexts:
    hwVplsOverGRENotSupportForwardRisingResume.setStatus(
        "current"
    )

hwIfInputUnucFlowRisingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 28)
)
hwIfInputUnucFlowRisingThreshold.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwUNUCPortName"),
        ("HUAWEI-L2MAM-MIB", "hwUNUCPortAlarmThreshold"),
        ("HUAWEI-L2MAM-MIB", "hwUNUCPortRealFlow"))
)
if mibBuilder.loadTexts:
    hwIfInputUnucFlowRisingThreshold.setStatus(
        "current"
    )

hwIfInputUnucFlowFallingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 29)
)
hwIfInputUnucFlowFallingThreshold.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwUNUCPortName"),
        ("HUAWEI-L2MAM-MIB", "hwUNUCPortAlarmThreshold"),
        ("HUAWEI-L2MAM-MIB", "hwUNUCPortRealFlow"))
)
if mibBuilder.loadTexts:
    hwIfInputUnucFlowFallingThreshold.setStatus(
        "current"
    )

hwMacHopAlarmRisingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 30)
)
hwMacHopAlarmRisingThreshold.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwMacHopVlan"),
        ("HUAWEI-L2MAM-MIB", "hwMacHopVsiName"),
        ("HUAWEI-L2MAM-MIB", "hwMacHopBdID"),
        ("HUAWEI-L2MAM-MIB", "hwMacHopPortName1"),
        ("HUAWEI-L2MAM-MIB", "hwMacHopPortName2"),
        ("HUAWEI-L2MAM-MIB", "hwMacHopPortName3"),
        ("HUAWEI-L2MAM-MIB", "hwMacHopPortName4"),
        ("HUAWEI-L2MAM-MIB", "hwMacHopPWInfo"))
)
if mibBuilder.loadTexts:
    hwMacHopAlarmRisingThreshold.setStatus(
        "current"
    )

hwMacHopAlarmFallingThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 31)
)
hwMacHopAlarmFallingThreshold.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwMacHopVlan"),
        ("HUAWEI-L2MAM-MIB", "hwMacHopVsiName"),
        ("HUAWEI-L2MAM-MIB", "hwMacHopBdID"))
)
if mibBuilder.loadTexts:
    hwMacHopAlarmFallingThreshold.setStatus(
        "current"
    )

hwPstBroadcastLostAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 32)
)
hwPstBroadcastLostAlarm.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwPstBroadcastLostAlarm.setStatus(
        "current"
    )

hwPstBroadcastLostResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 33)
)
hwPstBroadcastLostResume.setObjects(
      *(("ENTITY-MIB", "entPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwPstBroadcastLostResume.setStatus(
        "current"
    )

hwPwMacSpoofingAttackAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 34)
)
hwPwMacSpoofingAttackAlarm.setObjects(
      *(("HUAWEI-VPLS-EXT-MIB", "hwVplsVsiName"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-L2MAM-MIB", "hwPwMacSpoofingAttackMacAddr"))
)
if mibBuilder.loadTexts:
    hwPwMacSpoofingAttackAlarm.setStatus(
        "current"
    )

hwPwMacSpoofingAttackAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 35)
)
hwPwMacSpoofingAttackAlarmClear.setObjects(
      *(("HUAWEI-VPLS-EXT-MIB", "hwVplsVsiName"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwPwMacSpoofingAttackAlarmClear.setStatus(
        "current"
    )

hwBdMacLimitOverThresholdAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 36)
)
hwBdMacLimitOverThresholdAlarm.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwBdMacLimitBdId"),
        ("HUAWEI-L2MAM-MIB", "hwBdMacLimitMaxMac"))
)
if mibBuilder.loadTexts:
    hwBdMacLimitOverThresholdAlarm.setStatus(
        "current"
    )

hwBdMacLimitOverThresholdAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 1, 7, 37)
)
hwBdMacLimitOverThresholdAlarmResume.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwBdMacLimitBdId"),
        ("HUAWEI-L2MAM-MIB", "hwBdMacLimitMaxMac"))
)
if mibBuilder.loadTexts:
    hwBdMacLimitOverThresholdAlarmResume.setStatus(
        "current"
    )


# Notifications groups

hwBaseTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 3, 2)
)
hwBaseTrapGroup.setObjects(
      *(("HUAWEI-L2MAM-MIB", "hwMacUsageRaisingThreshold"),
        ("HUAWEI-L2MAM-MIB", "hwMacUsageFallingThreshold"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitNumRaisingThreshold"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitNumFallingThreshold"),
        ("HUAWEI-L2MAM-MIB", "hwUntargetMacNumAlarm"),
        ("HUAWEI-L2MAM-MIB", "hwPortSecRcvInsecurePktAlarm"),
        ("HUAWEI-L2MAM-MIB", "hwPwMacLimitNumRaisingThreshold"),
        ("HUAWEI-L2MAM-MIB", "hwPwMacLimitNumFallingThreshold"),
        ("HUAWEI-L2MAM-MIB", "hwPortStickyReachMaxAlarm"),
        ("HUAWEI-L2MAM-MIB", "hwRecIllegalMacPktAlarm"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitOverThresholdAlarm"),
        ("HUAWEI-L2MAM-MIB", "hwMacFlappingAlarm"),
        ("HUAWEI-L2MAM-MIB", "hwSlotMacLimitNumRaisingThreshold"),
        ("HUAWEI-L2MAM-MIB", "hwSlotMacLimitNumFallingThreshold"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtocolTunnelDropThresholdRaising"),
        ("HUAWEI-L2MAM-MIB", "hwL2ProtocolTunnelDropThresholdFalling"),
        ("HUAWEI-L2MAM-MIB", "hwVsiMacLimitNumRaisingThresholdAlarm"),
        ("HUAWEI-L2MAM-MIB", "hwVsiMacLimitNumRaisingThresholdAlarmClear"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitOverThresholdAlarmResume"),
        ("HUAWEI-L2MAM-MIB", "hwSlotMacNumRaisingThreshold"),
        ("HUAWEI-L2MAM-MIB", "hwSlotMacNumFallingThreshold"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitRuleNumRaisingThreshold"),
        ("HUAWEI-L2MAM-MIB", "hwMacLimitRuleNumFallingThreshold"),
        ("HUAWEI-L2MAM-MIB", "hwVplsOverGRENotSupportForwardRising"),
        ("HUAWEI-L2MAM-MIB", "hwVplsOverGRENotSupportForwardRisingResume"),
        ("HUAWEI-L2MAM-MIB", "hwIfInputUnucFlowRisingThreshold"),
        ("HUAWEI-L2MAM-MIB", "hwIfInputUnucFlowFallingThreshold"),
        ("HUAWEI-L2MAM-MIB", "hwMacHopAlarmRisingThreshold"),
        ("HUAWEI-L2MAM-MIB", "hwMacHopAlarmFallingThreshold"),
        ("HUAWEI-L2MAM-MIB", "hwPstBroadcastLostAlarm"),
        ("HUAWEI-L2MAM-MIB", "hwPstBroadcastLostResume"),
        ("HUAWEI-L2MAM-MIB", "hwBdMacLimitOverThresholdAlarm"),
        ("HUAWEI-L2MAM-MIB", "hwBdMacLimitOverThresholdAlarmResume"))
)
if mibBuilder.loadTexts:
    hwBaseTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwL2MAMCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hwL2MAMCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-L2MAM-MIB",
    **{"VlanIndex": VlanIndex,
       "hwL2Mgmt": hwL2Mgmt,
       "hwL2MAM": hwL2MAM,
       "hwL2MAMObjects": hwL2MAMObjects,
       "hwL2MaxMacLimit": hwL2MaxMacLimit,
       "hwdbCfgFdbTable": hwdbCfgFdbTable,
       "hwdbCfgFdbEntry": hwdbCfgFdbEntry,
       "hwCfgFdbMac": hwCfgFdbMac,
       "hwCfgFdbVlanId": hwCfgFdbVlanId,
       "hwCfgFdbVsiName": hwCfgFdbVsiName,
       "hwCfgFdbPort": hwCfgFdbPort,
       "hwCfgFdbType": hwCfgFdbType,
       "hwCfgFdbRowstatus": hwCfgFdbRowstatus,
       "hwCfgFdbAtmPort": hwCfgFdbAtmPort,
       "hwCfgFdbVpi": hwCfgFdbVpi,
       "hwCfgFdbVci": hwCfgFdbVci,
       "hwCfgFdbCeDefault": hwCfgFdbCeDefault,
       "hwdbDynFdbTable": hwdbDynFdbTable,
       "hwdbDynFdbEntry": hwdbDynFdbEntry,
       "hwDynFdbMac": hwDynFdbMac,
       "hwDynFdbVlanId": hwDynFdbVlanId,
       "hwDynFdbVsiName": hwDynFdbVsiName,
       "hwDynFdbPort": hwDynFdbPort,
       "hwDynFdbAtmPort": hwDynFdbAtmPort,
       "hwDynFdbVpi": hwDynFdbVpi,
       "hwDynFdbVci": hwDynFdbVci,
       "hwDynFdbRowstatus": hwDynFdbRowstatus,
       "hwDynSecurityFdbToStaticEnable": hwDynSecurityFdbToStaticEnable,
       "hwMacLimitTable": hwMacLimitTable,
       "hwMacLimitEntry": hwMacLimitEntry,
       "hwMacLimitPort": hwMacLimitPort,
       "hwMacLimitVlanId": hwMacLimitVlanId,
       "hwMacLimitVsiName": hwMacLimitVsiName,
       "hwMacLimitMaxMac": hwMacLimitMaxMac,
       "hwMacLimitMaxRate": hwMacLimitMaxRate,
       "hwMacLimitAction": hwMacLimitAction,
       "hwMacLimitAlarm": hwMacLimitAlarm,
       "hwMacLimitRowstatus": hwMacLimitRowstatus,
       "hwMacAddressLearn": hwMacAddressLearn,
       "hwMacDynAddressLearnNum": hwMacDynAddressLearnNum,
       "hwMacSecureAddressLearnNum": hwMacSecureAddressLearnNum,
       "hwMacUsageTable": hwMacUsageTable,
       "hwMacUsageEntry": hwMacUsageEntry,
       "hwMacEntityUsage": hwMacEntityUsage,
       "hwMacEntityUsageThreshold": hwMacEntityUsageThreshold,
       "hwdbCfg3tupleFdbTable": hwdbCfg3tupleFdbTable,
       "hwdbCfg3tupleFdbEntry": hwdbCfg3tupleFdbEntry,
       "hwdbCfg3tupleFdbMac": hwdbCfg3tupleFdbMac,
       "hwdbCfg3tupleFdbVlanId": hwdbCfg3tupleFdbVlanId,
       "hwdbCfg3tupleFdbInPort": hwdbCfg3tupleFdbInPort,
       "hwdbCfg3tupleFdbOutPort": hwdbCfg3tupleFdbOutPort,
       "hwdbCfg3tupleFdbRowStatus": hwdbCfg3tupleFdbRowStatus,
       "hwL2MacTraps": hwL2MacTraps,
       "hwMacUsageRaisingThreshold": hwMacUsageRaisingThreshold,
       "hwMacUsageFallingThreshold": hwMacUsageFallingThreshold,
       "hwMacLimitNumRaisingThreshold": hwMacLimitNumRaisingThreshold,
       "hwMacLimitNumFallingThreshold": hwMacLimitNumFallingThreshold,
       "hwUntargetMacNumAlarm": hwUntargetMacNumAlarm,
       "hwPortSecRcvInsecurePktAlarm": hwPortSecRcvInsecurePktAlarm,
       "hwPwMacLimitNumRaisingThreshold": hwPwMacLimitNumRaisingThreshold,
       "hwPwMacLimitNumFallingThreshold": hwPwMacLimitNumFallingThreshold,
       "hwPortStickyReachMaxAlarm": hwPortStickyReachMaxAlarm,
       "hwRecIllegalMacPktAlarm": hwRecIllegalMacPktAlarm,
       "hwMacLimitOverThresholdAlarm": hwMacLimitOverThresholdAlarm,
       "hwMacFlappingAlarm": hwMacFlappingAlarm,
       "hwSlotMacLimitNumRaisingThreshold": hwSlotMacLimitNumRaisingThreshold,
       "hwSlotMacLimitNumFallingThreshold": hwSlotMacLimitNumFallingThreshold,
       "hwL2ProtocolTunnelDropThresholdRaising": hwL2ProtocolTunnelDropThresholdRaising,
       "hwL2ProtocolTunnelDropThresholdFalling": hwL2ProtocolTunnelDropThresholdFalling,
       "hwVsiMacLimitNumRaisingThresholdAlarm": hwVsiMacLimitNumRaisingThresholdAlarm,
       "hwVsiMacLimitNumRaisingThresholdAlarmClear": hwVsiMacLimitNumRaisingThresholdAlarmClear,
       "hwMacLimitOverThresholdAlarmResume": hwMacLimitOverThresholdAlarmResume,
       "hwSlotMacNumRaisingThreshold": hwSlotMacNumRaisingThreshold,
       "hwSlotMacNumFallingThreshold": hwSlotMacNumFallingThreshold,
       "hwMacLimitRuleNumRaisingThreshold": hwMacLimitRuleNumRaisingThreshold,
       "hwMacLimitRuleNumFallingThreshold": hwMacLimitRuleNumFallingThreshold,
       "hwVplsOverGRENotSupportForwardRising": hwVplsOverGRENotSupportForwardRising,
       "hwVplsOverGRENotSupportForwardRisingResume": hwVplsOverGRENotSupportForwardRisingResume,
       "hwIfInputUnucFlowRisingThreshold": hwIfInputUnucFlowRisingThreshold,
       "hwIfInputUnucFlowFallingThreshold": hwIfInputUnucFlowFallingThreshold,
       "hwMacHopAlarmRisingThreshold": hwMacHopAlarmRisingThreshold,
       "hwMacHopAlarmFallingThreshold": hwMacHopAlarmFallingThreshold,
       "hwPstBroadcastLostAlarm": hwPstBroadcastLostAlarm,
       "hwPstBroadcastLostResume": hwPstBroadcastLostResume,
       "hwPwMacSpoofingAttackAlarm": hwPwMacSpoofingAttackAlarm,
       "hwPwMacSpoofingAttackAlarmClear": hwPwMacSpoofingAttackAlarmClear,
       "hwBdMacLimitOverThresholdAlarm": hwBdMacLimitOverThresholdAlarm,
       "hwBdMacLimitOverThresholdAlarmResume": hwBdMacLimitOverThresholdAlarmResume,
       "hwUntargetMacNum": hwUntargetMacNum,
       "hwMacAgingTime": hwMacAgingTime,
       "hwMacRestrict": hwMacRestrict,
       "hwPortSecurityTable": hwPortSecurityTable,
       "hwPortSecurityEntry": hwPortSecurityEntry,
       "hwPortSecurityPort": hwPortSecurityPort,
       "hwPortSecurityEnabled": hwPortSecurityEnabled,
       "hwPortSecurityProtectAction": hwPortSecurityProtectAction,
       "hwPortSecurityAllDynToStaticEnable": hwPortSecurityAllDynToStaticEnable,
       "hwPortSecurityAllDynToStickyEnable": hwPortSecurityAllDynToStickyEnable,
       "hwPortSecurityMaxMacNum": hwPortSecurityMaxMacNum,
       "hwMacLimitGlobalRuleTable": hwMacLimitGlobalRuleTable,
       "hwMacLimitGlobalRuleEntry": hwMacLimitGlobalRuleEntry,
       "hwMacLimitGlobalRuleName": hwMacLimitGlobalRuleName,
       "hwMacLimitRuleMaxMac": hwMacLimitRuleMaxMac,
       "hwMacLimitRuleMaxRate": hwMacLimitRuleMaxRate,
       "hwMacLimitRuleAction": hwMacLimitRuleAction,
       "hwMacLimitRuleAlarm": hwMacLimitRuleAlarm,
       "hwMacLimitRuleRowstatus": hwMacLimitRuleRowstatus,
       "hwMacRuleDynAddressLearnNum": hwMacRuleDynAddressLearnNum,
       "hwMacLimitApplyRuleTable": hwMacLimitApplyRuleTable,
       "hwMacLimitApplyRuleEntry": hwMacLimitApplyRuleEntry,
       "hwMacLimitApplyPort": hwMacLimitApplyPort,
       "hwMacLimitApplyVlanId": hwMacLimitApplyVlanId,
       "hwMacLimitApplyRuleName": hwMacLimitApplyRuleName,
       "hwMacLimitApplyRowstatus": hwMacLimitApplyRowstatus,
       "hwMacGlobalStatistics": hwMacGlobalStatistics,
       "hwMacIfStatisticsTable": hwMacIfStatisticsTable,
       "hwMacIfStatisticsEntry": hwMacIfStatisticsEntry,
       "hwMacIfStatisticsIfIndex": hwMacIfStatisticsIfIndex,
       "hwMacIfStatistics": hwMacIfStatistics,
       "hwMacSlotStatisticsTable": hwMacSlotStatisticsTable,
       "hwMacSlotStatisticsEntry": hwMacSlotStatisticsEntry,
       "hwMacSlotStatisticsSlotId": hwMacSlotStatisticsSlotId,
       "hwMacSlotStatistics": hwMacSlotStatistics,
       "hwMacSlotStatisticsSpecify": hwMacSlotStatisticsSpecify,
       "hwMacVlanStatisticsTable": hwMacVlanStatisticsTable,
       "hwMacVlanStatisticsEntry": hwMacVlanStatisticsEntry,
       "hwMacVlanStatisticsVlanId": hwMacVlanStatisticsVlanId,
       "hwMacVlanStatistics": hwMacVlanStatistics,
       "hwMacVsiStatisticsTable": hwMacVsiStatisticsTable,
       "hwMacVsiStatisticsEntry": hwMacVsiStatisticsEntry,
       "hwMacVsiStatisticsVsiName": hwMacVsiStatisticsVsiName,
       "hwMacVsiStatistics": hwMacVsiStatistics,
       "hwPwMacLimitTable": hwPwMacLimitTable,
       "hwPwMacLimitEntry": hwPwMacLimitEntry,
       "hwPwMacLimitVsiName": hwPwMacLimitVsiName,
       "hwPwMacLimitPwName": hwPwMacLimitPwName,
       "hwPwMacLimitMaxMac": hwPwMacLimitMaxMac,
       "hwPwMacLimitMaxRate": hwPwMacLimitMaxRate,
       "hwPwMacLimitAction": hwPwMacLimitAction,
       "hwPwMacLimitAlarm": hwPwMacLimitAlarm,
       "hwPwMacLimitRowstatus": hwPwMacLimitRowstatus,
       "hwPwMacAddressLearn": hwPwMacAddressLearn,
       "hwPwMacDynAddressLearnNum": hwPwMacDynAddressLearnNum,
       "hwMacSpoofingDefendTable": hwMacSpoofingDefendTable,
       "hwMacSpoofingDefendEntry": hwMacSpoofingDefendEntry,
       "hwMacSpoofingDefendPort": hwMacSpoofingDefendPort,
       "hwMacSpoofingDefendEnabled": hwMacSpoofingDefendEnabled,
       "hwDiscardIllegalMacEnable": hwDiscardIllegalMacEnable,
       "hwDiscardIllegalMacAlarm": hwDiscardIllegalMacAlarm,
       "hwMacSpoofingDefend": hwMacSpoofingDefend,
       "hwL2MacFlappingTrapObjects": hwL2MacFlappingTrapObjects,
       "hwMacflappingMac": hwMacflappingMac,
       "hwMacFlappingVlan": hwMacFlappingVlan,
       "hwSlotMacLimitTable": hwSlotMacLimitTable,
       "hwSlotMacLimitEntry": hwSlotMacLimitEntry,
       "hwSlotMacLimitId": hwSlotMacLimitId,
       "hwSlotMacLimitMaxMac": hwSlotMacLimitMaxMac,
       "hwSlotMacLimitMaxRate": hwSlotMacLimitMaxRate,
       "hwSlotMacLimitAction": hwSlotMacLimitAction,
       "hwSlotMacLimitAlarm": hwSlotMacLimitAlarm,
       "hwSlotMacLimitRowstatus": hwSlotMacLimitRowstatus,
       "hwL2ProtocolTunnelTrapObjects": hwL2ProtocolTunnelTrapObjects,
       "hwL2ProtocolTunnelTrapPortName": hwL2ProtocolTunnelTrapPortName,
       "hwL2ProtocolTunnelTrapProtocolName": hwL2ProtocolTunnelTrapProtocolName,
       "hwL2ProtocolTunnelTrapDropThreshold": hwL2ProtocolTunnelTrapDropThreshold,
       "hwL2ProtclTnlStdTable": hwL2ProtclTnlStdTable,
       "hwL2ProtclTnlStdEntry": hwL2ProtclTnlStdEntry,
       "hwL2ProtclTnlStdProtclName": hwL2ProtclTnlStdProtclName,
       "hwL2ProtclTnlStdProtclMacAddr": hwL2ProtclTnlStdProtclMacAddr,
       "hwL2ProtclTnlStdEncapType": hwL2ProtclTnlStdEncapType,
       "hwL2ProtclTnlStdProtclType": hwL2ProtclTnlStdProtclType,
       "hwL2ProtclTnlStdGroupMacAddr": hwL2ProtclTnlStdGroupMacAddr,
       "hwL2ProtclTnlStdGroupDefault": hwL2ProtclTnlStdGroupDefault,
       "hwL2ProtclTnlStdPriority": hwL2ProtclTnlStdPriority,
       "hwL2ProtclTnlCusTable": hwL2ProtclTnlCusTable,
       "hwL2ProtclTnlCusEntry": hwL2ProtclTnlCusEntry,
       "hwL2ProtclTnlCusProtclName": hwL2ProtclTnlCusProtclName,
       "hwL2ProtclTnlCusProtclMacAddr": hwL2ProtclTnlCusProtclMacAddr,
       "hwL2ProtclTnlCusEncapType": hwL2ProtclTnlCusEncapType,
       "hwL2ProtclTnlCusProtclType": hwL2ProtclTnlCusProtclType,
       "hwL2ProtclTnlCusGroupMacAddr": hwL2ProtclTnlCusGroupMacAddr,
       "hwL2ProtclTnlCusGroupDefault": hwL2ProtclTnlCusGroupDefault,
       "hwL2ProtclTnlCusPriority": hwL2ProtclTnlCusPriority,
       "hwL2ProtclTnlCusRowStatus": hwL2ProtclTnlCusRowStatus,
       "hwL2ProtclTnlEnableTable": hwL2ProtclTnlEnableTable,
       "hwL2ProtclTnlEnableEntry": hwL2ProtclTnlEnableEntry,
       "hwL2ProtclTnlEnableIfIndex": hwL2ProtclTnlEnableIfIndex,
       "hwL2ProtclTnlEnableProtclName": hwL2ProtclTnlEnableProtclName,
       "hwL2ProtclTnlEnableTransMode": hwL2ProtclTnlEnableTransMode,
       "hwL2ProtclTnlEnableTagListLow": hwL2ProtclTnlEnableTagListLow,
       "hwL2ProtclTnlEnableTagListHigh": hwL2ProtclTnlEnableTagListHigh,
       "hwL2ProtclTnlEnableDropthresholdRate": hwL2ProtclTnlEnableDropthresholdRate,
       "hwL2ProtclTnlEnableRowStatus": hwL2ProtclTnlEnableRowStatus,
       "hwL2ProtclTnlStatisticsTable": hwL2ProtclTnlStatisticsTable,
       "hwL2ProtclTnlStatisticsEntry": hwL2ProtclTnlStatisticsEntry,
       "hwL2ProtclTnlStatisticsIfIndex": hwL2ProtclTnlStatisticsIfIndex,
       "hwL2ProtclTnlStatisticsProtclName": hwL2ProtclTnlStatisticsProtclName,
       "hwL2ProtclTnlStatisticsDropthrhldRate": hwL2ProtclTnlStatisticsDropthrhldRate,
       "hwL2ProtclTnlStatisticsInputPkts": hwL2ProtclTnlStatisticsInputPkts,
       "hwL2ProtclTnlStatisticsOutputPkts": hwL2ProtclTnlStatisticsOutputPkts,
       "hwL2ProtclTnlStatisticsDropPkts": hwL2ProtclTnlStatisticsDropPkts,
       "hwBridgeMacAgingTime": hwBridgeMacAgingTime,
       "hwCfgMacAddrQueryTable": hwCfgMacAddrQueryTable,
       "hwCfgMacAddrQueryEntry": hwCfgMacAddrQueryEntry,
       "hwCfgMacAddrQueryVlanId": hwCfgMacAddrQueryVlanId,
       "hwCfgMacAddrQueryVsiName": hwCfgMacAddrQueryVsiName,
       "hwCfgMacAddrQuerySiName": hwCfgMacAddrQuerySiName,
       "hwCfgMacAddrQueryBridgeId": hwCfgMacAddrQueryBridgeId,
       "hwCfgMacAddrQueryMacAddr": hwCfgMacAddrQueryMacAddr,
       "hwCfgMacAddrQueryConditionMode": hwCfgMacAddrQueryConditionMode,
       "hwCfgMacAddrQueryConditionStringA": hwCfgMacAddrQueryConditionStringA,
       "hwCfgMacAddrQueryConditionStringB": hwCfgMacAddrQueryConditionStringB,
       "hwCfgMacAddrQueryConditionDigitA": hwCfgMacAddrQueryConditionDigitA,
       "hwCfgMacAddrQueryConditionDigitB": hwCfgMacAddrQueryConditionDigitB,
       "hwCfgMacAddrQueryConditionDigitC": hwCfgMacAddrQueryConditionDigitC,
       "hwCfgMacAddrQueryType": hwCfgMacAddrQueryType,
       "hwCfgMacAddrQueryIfIndex": hwCfgMacAddrQueryIfIndex,
       "hwCfgMacAddrQueryPeVlanId": hwCfgMacAddrQueryPeVlanId,
       "hwCfgMacAddrQueryCeVlanId": hwCfgMacAddrQueryCeVlanId,
       "hwCfgMacAddrQueryCedefaultFlag": hwCfgMacAddrQueryCedefaultFlag,
       "hwCfgMacAddrQueryAtmIfIndex": hwCfgMacAddrQueryAtmIfIndex,
       "hwCfgMacAddrQueryVpi": hwCfgMacAddrQueryVpi,
       "hwCfgMacAddrQueryVci": hwCfgMacAddrQueryVci,
       "hwCfgMacAddrQueryMacTunnel": hwCfgMacAddrQueryMacTunnel,
       "hwDynMacAddrQueryTable": hwDynMacAddrQueryTable,
       "hwDynMacAddrQueryEntry": hwDynMacAddrQueryEntry,
       "hwDynMacAddrQueryVlanId": hwDynMacAddrQueryVlanId,
       "hwDynMacAddrQueryVsiName": hwDynMacAddrQueryVsiName,
       "hwDynMacAddrQuerySiName": hwDynMacAddrQuerySiName,
       "hwDynMacAddrQueryBridgeId": hwDynMacAddrQueryBridgeId,
       "hwDynMacAddrQueryMacAddr": hwDynMacAddrQueryMacAddr,
       "hwDynMacAddrQueryConditionMode": hwDynMacAddrQueryConditionMode,
       "hwDynMacAddrQueryConditionStringA": hwDynMacAddrQueryConditionStringA,
       "hwDynMacAddrQueryConditionStringB": hwDynMacAddrQueryConditionStringB,
       "hwDynMacAddrQueryConditionDigitA": hwDynMacAddrQueryConditionDigitA,
       "hwDynMacAddrQueryConditionDigitB": hwDynMacAddrQueryConditionDigitB,
       "hwDynMacAddrQueryConditionDigitC": hwDynMacAddrQueryConditionDigitC,
       "hwDynMacAddrQueryType": hwDynMacAddrQueryType,
       "hwDynMacAddrQueryIfIndex": hwDynMacAddrQueryIfIndex,
       "hwDynMacAddrQueryPeVlanId": hwDynMacAddrQueryPeVlanId,
       "hwDynMacAddrQueryCeVlanId": hwDynMacAddrQueryCeVlanId,
       "hwDynMacAddrQueryAtmIfIndex": hwDynMacAddrQueryAtmIfIndex,
       "hwDynMacAddrQueryVpi": hwDynMacAddrQueryVpi,
       "hwDynMacAddrQueryVci": hwDynMacAddrQueryVci,
       "hwDynMacAddrQueryPeerIp": hwDynMacAddrQueryPeerIp,
       "hwDynMacAddrQueryPwId": hwDynMacAddrQueryPwId,
       "hwDynMacAddrQueryMacTunnel": hwDynMacAddrQueryMacTunnel,
       "hwDynMacAddrQueryAgingTime": hwDynMacAddrQueryAgingTime,
       "hwMacInfoQueryTable": hwMacInfoQueryTable,
       "hwMacInfoQueryEntry": hwMacInfoQueryEntry,
       "hwMacInfoQueryConditionMode": hwMacInfoQueryConditionMode,
       "hwMacInfoQueryConditionStringA": hwMacInfoQueryConditionStringA,
       "hwMacInfoQueryConditionStringB": hwMacInfoQueryConditionStringB,
       "hwMacInfoQueryConditionStringC": hwMacInfoQueryConditionStringC,
       "hwMacInfoQueryConditionDigitA": hwMacInfoQueryConditionDigitA,
       "hwMacInfoQueryConditionDigitB": hwMacInfoQueryConditionDigitB,
       "hwMacInfoQueryConditionDigitC": hwMacInfoQueryConditionDigitC,
       "hwMacInfoQueryTotalNumber": hwMacInfoQueryTotalNumber,
       "hwMacInfoQueryTotalLocalNumber": hwMacInfoQueryTotalLocalNumber,
       "hwMacInfoQueryTotalRemoteNumber": hwMacInfoQueryTotalRemoteNumber,
       "hwMacInfoQueryCapacity": hwMacInfoQueryCapacity,
       "hwVplsOverGreTable": hwVplsOverGreTable,
       "hwVplsOverGreEntry": hwVplsOverGreEntry,
       "hwVplsOverGrePwId": hwVplsOverGrePwId,
       "hwRemoteIp": hwRemoteIp,
       "hwVplsOverGreVsiName": hwVplsOverGreVsiName,
       "hwVllByPassOverGreTable": hwVllByPassOverGreTable,
       "hwVllByPassOverGreEntry": hwVllByPassOverGreEntry,
       "hwVLLACPortIndex": hwVLLACPortIndex,
       "hwVLLACPortName": hwVLLACPortName,
       "hwUnucFlowAlarmTable": hwUnucFlowAlarmTable,
       "hwUnucFlowAlarmEntry": hwUnucFlowAlarmEntry,
       "hwUNUCPortIndex": hwUNUCPortIndex,
       "hwUNUCPortName": hwUNUCPortName,
       "hwUNUCPortAlarmThreshold": hwUNUCPortAlarmThreshold,
       "hwUNUCPortRealFlow": hwUNUCPortRealFlow,
       "hwMacHopAlarmTable": hwMacHopAlarmTable,
       "hwMacHopAlarmEntry": hwMacHopAlarmEntry,
       "hwMacHopVlan": hwMacHopVlan,
       "hwMacHopVsiName": hwMacHopVsiName,
       "hwMacHopBdID": hwMacHopBdID,
       "hwMacHopPortName1": hwMacHopPortName1,
       "hwMacHopPortName2": hwMacHopPortName2,
       "hwMacHopPortName3": hwMacHopPortName3,
       "hwMacHopPortName4": hwMacHopPortName4,
       "hwMacHopPWInfo": hwMacHopPWInfo,
       "hwPwMacSpoofingAttackMacAddr": hwPwMacSpoofingAttackMacAddr,
       "hwBdMacLimitBdId": hwBdMacLimitBdId,
       "hwBdMacLimitMaxMac": hwBdMacLimitMaxMac,
       "hwL2MAMConformance": hwL2MAMConformance,
       "hwL2MAMGroups": hwL2MAMGroups,
       "hwL2MAMCfgFdbGroup": hwL2MAMCfgFdbGroup,
       "hwL2MAMDynFdbGroup": hwL2MAMDynFdbGroup,
       "hwL2MAMMacLimitGroup": hwL2MAMMacLimitGroup,
       "hwL2MAMMacUsageGroup": hwL2MAMMacUsageGroup,
       "hwdbCfg3tupleFdbGroup": hwdbCfg3tupleFdbGroup,
       "hwL2MAMObjectsGroup": hwL2MAMObjectsGroup,
       "hwPortSecurityGroup": hwPortSecurityGroup,
       "hwMacIfStatisticsGroup": hwMacIfStatisticsGroup,
       "hwMacSlotStatisticsGroup": hwMacSlotStatisticsGroup,
       "hwMacVlanStatisticsGroup": hwMacVlanStatisticsGroup,
       "hwMacVsiStatisticsGroup": hwMacVsiStatisticsGroup,
       "hwMacSpoofingDefendGroup": hwMacSpoofingDefendGroup,
       "hwL2ProtocolTunnelTrapGroup": hwL2ProtocolTunnelTrapGroup,
       "hwL2ProtclTnlStdProtclGroup": hwL2ProtclTnlStdProtclGroup,
       "hwL2ProtclTnlCusProtclGroup": hwL2ProtclTnlCusProtclGroup,
       "hwL2ProtclTnlEnableGroup": hwL2ProtclTnlEnableGroup,
       "hwL2ProtclTnlStatisticsGroup": hwL2ProtclTnlStatisticsGroup,
       "hwCfgMacAddrQueryTableGroup": hwCfgMacAddrQueryTableGroup,
       "hwDynMacAddrQueryTableGroup": hwDynMacAddrQueryTableGroup,
       "hwMacInfoQueryTableGroup": hwMacInfoQueryTableGroup,
       "hwL2MAMCompliances": hwL2MAMCompliances,
       "hwL2MAMCompliance": hwL2MAMCompliance,
       "hwL2MACTrapGroups": hwL2MACTrapGroups,
       "hwBaseTrapGroup": hwBaseTrapGroup}
)
