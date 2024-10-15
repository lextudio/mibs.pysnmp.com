# SNMP MIB module (TPLINK-L2BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-L2BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:14 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkl2BridgeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10)
)
tplinkl2BridgeMIB.setRevisions(
        ("2012-12-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanSecEntryStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("createRequest", 3),
          ("destroy", 4),
          ("disable", 0),
          ("drop", 1),
          ("forward", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Tplinkl2BridgeMIBObjects_ObjectIdentity = ObjectIdentity
tplinkl2BridgeMIBObjects = _Tplinkl2BridgeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1)
)
_Tpl2BridgeManageStaticAddrCtrl_ObjectIdentity = ObjectIdentity
tpl2BridgeManageStaticAddrCtrl = _Tpl2BridgeManageStaticAddrCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 1)
)
_Tpl2BridgeManageStaticAddrCtrlTable_Object = MibTable
tpl2BridgeManageStaticAddrCtrlTable = _Tpl2BridgeManageStaticAddrCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tpl2BridgeManageStaticAddrCtrlTable.setStatus("current")
_Tpl2BridgeManageStaticAddrCtrlEntry_Object = MibTableRow
tpl2BridgeManageStaticAddrCtrlEntry = _Tpl2BridgeManageStaticAddrCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 1, 1, 1)
)
tpl2BridgeManageStaticAddrCtrlEntry.setIndexNames(
    (0, "TPLINK-L2BRIDGE-MIB", "tpl2BridgeManageStaticMac"),
    (0, "TPLINK-L2BRIDGE-MIB", "tpl2BridgeManageStaticVlanId"),
)
if mibBuilder.loadTexts:
    tpl2BridgeManageStaticAddrCtrlEntry.setStatus("current")
_Tpl2BridgeManageStaticMac_Type = OctetString
_Tpl2BridgeManageStaticMac_Object = MibTableColumn
tpl2BridgeManageStaticMac = _Tpl2BridgeManageStaticMac_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 1, 1, 1, 1),
    _Tpl2BridgeManageStaticMac_Type()
)
tpl2BridgeManageStaticMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpl2BridgeManageStaticMac.setStatus("current")


class _Tpl2BridgeManageStaticVlanId_Type(Integer32):
    """Custom type tpl2BridgeManageStaticVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Tpl2BridgeManageStaticVlanId_Type.__name__ = "Integer32"
_Tpl2BridgeManageStaticVlanId_Object = MibTableColumn
tpl2BridgeManageStaticVlanId = _Tpl2BridgeManageStaticVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 1, 1, 1, 2),
    _Tpl2BridgeManageStaticVlanId_Type()
)
tpl2BridgeManageStaticVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpl2BridgeManageStaticVlanId.setStatus("current")
_Tpl2BridgeManageStaticPort_Type = OctetString
_Tpl2BridgeManageStaticPort_Object = MibTableColumn
tpl2BridgeManageStaticPort = _Tpl2BridgeManageStaticPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 1, 1, 1, 3),
    _Tpl2BridgeManageStaticPort_Type()
)
tpl2BridgeManageStaticPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpl2BridgeManageStaticPort.setStatus("current")
_Tpl2BridgeManageStaticStatus_Type = TPRowStatus
_Tpl2BridgeManageStaticStatus_Object = MibTableColumn
tpl2BridgeManageStaticStatus = _Tpl2BridgeManageStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 1, 1, 1, 4),
    _Tpl2BridgeManageStaticStatus_Type()
)
tpl2BridgeManageStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpl2BridgeManageStaticStatus.setStatus("current")
_Tpl2BridgeManageDynAddrCtrl_ObjectIdentity = ObjectIdentity
tpl2BridgeManageDynAddrCtrl = _Tpl2BridgeManageDynAddrCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 2)
)


class _Tpl2BridgeManageDynAddrCtrlAgingTime_Type(Integer32):
    """Custom type tpl2BridgeManageDynAddrCtrlAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 630),
    )


_Tpl2BridgeManageDynAddrCtrlAgingTime_Type.__name__ = "Integer32"
_Tpl2BridgeManageDynAddrCtrlAgingTime_Object = MibScalar
tpl2BridgeManageDynAddrCtrlAgingTime = _Tpl2BridgeManageDynAddrCtrlAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 2, 1),
    _Tpl2BridgeManageDynAddrCtrlAgingTime_Type()
)
tpl2BridgeManageDynAddrCtrlAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpl2BridgeManageDynAddrCtrlAgingTime.setStatus("current")
_Tpl2BridgeManageDynAddrCtrlTable_Object = MibTable
tpl2BridgeManageDynAddrCtrlTable = _Tpl2BridgeManageDynAddrCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tpl2BridgeManageDynAddrCtrlTable.setStatus("current")
_Tpl2BridgeManageDynAddrCtrlEntry_Object = MibTableRow
tpl2BridgeManageDynAddrCtrlEntry = _Tpl2BridgeManageDynAddrCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 2, 2, 1)
)
tpl2BridgeManageDynAddrCtrlEntry.setIndexNames(
    (0, "TPLINK-L2BRIDGE-MIB", "tpl2BridgeManageDynMac"),
    (0, "TPLINK-L2BRIDGE-MIB", "tpl2BridgeManageDynVlanId"),
)
if mibBuilder.loadTexts:
    tpl2BridgeManageDynAddrCtrlEntry.setStatus("current")
_Tpl2BridgeManageDynMac_Type = OctetString
_Tpl2BridgeManageDynMac_Object = MibTableColumn
tpl2BridgeManageDynMac = _Tpl2BridgeManageDynMac_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 2, 2, 1, 1),
    _Tpl2BridgeManageDynMac_Type()
)
tpl2BridgeManageDynMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpl2BridgeManageDynMac.setStatus("current")


class _Tpl2BridgeManageDynVlanId_Type(Integer32):
    """Custom type tpl2BridgeManageDynVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Tpl2BridgeManageDynVlanId_Type.__name__ = "Integer32"
_Tpl2BridgeManageDynVlanId_Object = MibTableColumn
tpl2BridgeManageDynVlanId = _Tpl2BridgeManageDynVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 2, 2, 1, 2),
    _Tpl2BridgeManageDynVlanId_Type()
)
tpl2BridgeManageDynVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpl2BridgeManageDynVlanId.setStatus("current")
_Tpl2BridgeManageDynPort_Type = OctetString
_Tpl2BridgeManageDynPort_Object = MibTableColumn
tpl2BridgeManageDynPort = _Tpl2BridgeManageDynPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 2, 2, 1, 3),
    _Tpl2BridgeManageDynPort_Type()
)
tpl2BridgeManageDynPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpl2BridgeManageDynPort.setStatus("current")


class _Tpl2BridgeManageDynAgeStatus_Type(Integer32):
    """Custom type tpl2BridgeManageDynAgeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aging", 1),
          ("noAging", 0))
    )


_Tpl2BridgeManageDynAgeStatus_Type.__name__ = "Integer32"
_Tpl2BridgeManageDynAgeStatus_Object = MibTableColumn
tpl2BridgeManageDynAgeStatus = _Tpl2BridgeManageDynAgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 2, 2, 1, 4),
    _Tpl2BridgeManageDynAgeStatus_Type()
)
tpl2BridgeManageDynAgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpl2BridgeManageDynAgeStatus.setStatus("current")


class _Tpl2BridgeManageDynStatus_Type(Integer32):
    """Custom type tpl2BridgeManageDynStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("bind", 4),
          ("destroy", 6))
    )


_Tpl2BridgeManageDynStatus_Type.__name__ = "Integer32"
_Tpl2BridgeManageDynStatus_Object = MibTableColumn
tpl2BridgeManageDynStatus = _Tpl2BridgeManageDynStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 2, 2, 1, 5),
    _Tpl2BridgeManageDynStatus_Type()
)
tpl2BridgeManageDynStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpl2BridgeManageDynStatus.setStatus("current")
_Tpl2BridgeManageFilterAddrCtrl_ObjectIdentity = ObjectIdentity
tpl2BridgeManageFilterAddrCtrl = _Tpl2BridgeManageFilterAddrCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 3)
)
_Tpl2BridgeManageFilterCtrlTable_Object = MibTable
tpl2BridgeManageFilterCtrlTable = _Tpl2BridgeManageFilterCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tpl2BridgeManageFilterCtrlTable.setStatus("current")
_Tpl2BridgeManageFilterCtrlEntry_Object = MibTableRow
tpl2BridgeManageFilterCtrlEntry = _Tpl2BridgeManageFilterCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 3, 1, 1)
)
tpl2BridgeManageFilterCtrlEntry.setIndexNames(
    (0, "TPLINK-L2BRIDGE-MIB", "tpl2BridgeManageFilterMac"),
    (0, "TPLINK-L2BRIDGE-MIB", "tpl2BridgeManageFilterVlanId"),
)
if mibBuilder.loadTexts:
    tpl2BridgeManageFilterCtrlEntry.setStatus("current")
_Tpl2BridgeManageFilterMac_Type = OctetString
_Tpl2BridgeManageFilterMac_Object = MibTableColumn
tpl2BridgeManageFilterMac = _Tpl2BridgeManageFilterMac_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 3, 1, 1, 1),
    _Tpl2BridgeManageFilterMac_Type()
)
tpl2BridgeManageFilterMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpl2BridgeManageFilterMac.setStatus("current")


class _Tpl2BridgeManageFilterVlanId_Type(Integer32):
    """Custom type tpl2BridgeManageFilterVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Tpl2BridgeManageFilterVlanId_Type.__name__ = "Integer32"
_Tpl2BridgeManageFilterVlanId_Object = MibTableColumn
tpl2BridgeManageFilterVlanId = _Tpl2BridgeManageFilterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 3, 1, 1, 2),
    _Tpl2BridgeManageFilterVlanId_Type()
)
tpl2BridgeManageFilterVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpl2BridgeManageFilterVlanId.setStatus("current")
_Tpl2BridgeManageFilterStatus_Type = TPRowStatus
_Tpl2BridgeManageFilterStatus_Object = MibTableColumn
tpl2BridgeManageFilterStatus = _Tpl2BridgeManageFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 3, 1, 1, 3),
    _Tpl2BridgeManageFilterStatus_Type()
)
tpl2BridgeManageFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpl2BridgeManageFilterStatus.setStatus("current")
_Tpl2BridgeManageVlanSecurityCtrl_ObjectIdentity = ObjectIdentity
tpl2BridgeManageVlanSecurityCtrl = _Tpl2BridgeManageVlanSecurityCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 4)
)
_Tpl2BridgeManagevlanSecurityTable_Object = MibTable
tpl2BridgeManagevlanSecurityTable = _Tpl2BridgeManagevlanSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tpl2BridgeManagevlanSecurityTable.setStatus("current")
_Tpl2BridgeManagevlanSecEntry_Object = MibTableRow
tpl2BridgeManagevlanSecEntry = _Tpl2BridgeManagevlanSecEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 4, 1, 1)
)
tpl2BridgeManagevlanSecEntry.setIndexNames(
    (0, "TPLINK-L2BRIDGE-MIB", "tpFdbVlanSecurityVid"),
)
if mibBuilder.loadTexts:
    tpl2BridgeManagevlanSecEntry.setStatus("current")


class _TpFdbVlanSecurityVid_Type(Integer32):
    """Custom type tpFdbVlanSecurityVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TpFdbVlanSecurityVid_Type.__name__ = "Integer32"
_TpFdbVlanSecurityVid_Object = MibTableColumn
tpFdbVlanSecurityVid = _TpFdbVlanSecurityVid_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 4, 1, 1, 1),
    _TpFdbVlanSecurityVid_Type()
)
tpFdbVlanSecurityVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpFdbVlanSecurityVid.setStatus("current")


class _TpFdbVlanSecurityMaxLearned_Type(Integer32):
    """Custom type tpFdbVlanSecurityMaxLearned based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_TpFdbVlanSecurityMaxLearned_Type.__name__ = "Integer32"
_TpFdbVlanSecurityMaxLearned_Object = MibTableColumn
tpFdbVlanSecurityMaxLearned = _TpFdbVlanSecurityMaxLearned_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 4, 1, 1, 2),
    _TpFdbVlanSecurityMaxLearned_Type()
)
tpFdbVlanSecurityMaxLearned.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpFdbVlanSecurityMaxLearned.setStatus("current")


class _TpFdbVlanSecurityRowStatus_Type(VlanSecEntryStatus):
    """Custom type tpFdbVlanSecurityRowStatus based on VlanSecEntryStatus"""
    defaultValue = 2


_TpFdbVlanSecurityRowStatus_Object = MibTableColumn
tpFdbVlanSecurityRowStatus = _TpFdbVlanSecurityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 4, 1, 1, 3),
    _TpFdbVlanSecurityRowStatus_Type()
)
tpFdbVlanSecurityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpFdbVlanSecurityRowStatus.setStatus("current")
_Tpl2BridgeManageNotificationCtrl_ObjectIdentity = ObjectIdentity
tpl2BridgeManageNotificationCtrl = _Tpl2BridgeManageNotificationCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 5)
)


class _Tpl2BridgeManageNotificationGlobalStatus_Type(Integer32):
    """Custom type tpl2BridgeManageNotificationGlobalStatus based on Integer32"""
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


_Tpl2BridgeManageNotificationGlobalStatus_Type.__name__ = "Integer32"
_Tpl2BridgeManageNotificationGlobalStatus_Object = MibScalar
tpl2BridgeManageNotificationGlobalStatus = _Tpl2BridgeManageNotificationGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 5, 1),
    _Tpl2BridgeManageNotificationGlobalStatus_Type()
)
tpl2BridgeManageNotificationGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpl2BridgeManageNotificationGlobalStatus.setStatus("current")


class _Tpl2BridgeManageNotificationTableFullStatus_Type(Integer32):
    """Custom type tpl2BridgeManageNotificationTableFullStatus based on Integer32"""
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


_Tpl2BridgeManageNotificationTableFullStatus_Type.__name__ = "Integer32"
_Tpl2BridgeManageNotificationTableFullStatus_Object = MibScalar
tpl2BridgeManageNotificationTableFullStatus = _Tpl2BridgeManageNotificationTableFullStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 5, 2),
    _Tpl2BridgeManageNotificationTableFullStatus_Type()
)
tpl2BridgeManageNotificationTableFullStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpl2BridgeManageNotificationTableFullStatus.setStatus("current")


class _Tpl2BridgeManageNotificationInterval_Type(Integer32):
    """Custom type tpl2BridgeManageNotificationInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Tpl2BridgeManageNotificationInterval_Type.__name__ = "Integer32"
_Tpl2BridgeManageNotificationInterval_Object = MibScalar
tpl2BridgeManageNotificationInterval = _Tpl2BridgeManageNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 5, 3),
    _Tpl2BridgeManageNotificationInterval_Type()
)
tpl2BridgeManageNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpl2BridgeManageNotificationInterval.setStatus("current")
_Tpl2BridgeManageNotificationTable_Object = MibTable
tpl2BridgeManageNotificationTable = _Tpl2BridgeManageNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 5, 4)
)
if mibBuilder.loadTexts:
    tpl2BridgeManageNotificationTable.setStatus("current")
_Tpl2BridgeManageNotificationCtrlEntry_Object = MibTableRow
tpl2BridgeManageNotificationCtrlEntry = _Tpl2BridgeManageNotificationCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 5, 4, 1)
)
tpl2BridgeManageNotificationCtrlEntry.setIndexNames(
    (0, "TPLINK-L2BRIDGE-MIB", "tpl2BridgeManagePortIndex"),
)
if mibBuilder.loadTexts:
    tpl2BridgeManageNotificationCtrlEntry.setStatus("current")


class _Tpl2BridgeManagePortIndex_Type(DisplayString):
    """Custom type tpl2BridgeManagePortIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Tpl2BridgeManagePortIndex_Type.__name__ = "DisplayString"
_Tpl2BridgeManagePortIndex_Object = MibTableColumn
tpl2BridgeManagePortIndex = _Tpl2BridgeManagePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 5, 4, 1, 1),
    _Tpl2BridgeManagePortIndex_Type()
)
tpl2BridgeManagePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpl2BridgeManagePortIndex.setStatus("current")


class _Tpl2BridgeManageLrnModeChg_Type(Integer32):
    """Custom type tpl2BridgeManageLrnModeChg based on Integer32"""
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


_Tpl2BridgeManageLrnModeChg_Type.__name__ = "Integer32"
_Tpl2BridgeManageLrnModeChg_Object = MibTableColumn
tpl2BridgeManageLrnModeChg = _Tpl2BridgeManageLrnModeChg_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 5, 4, 1, 2),
    _Tpl2BridgeManageLrnModeChg_Type()
)
tpl2BridgeManageLrnModeChg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpl2BridgeManageLrnModeChg.setStatus("current")


class _Tpl2BridgeManageExceedMaxLrn_Type(Integer32):
    """Custom type tpl2BridgeManageExceedMaxLrn based on Integer32"""
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


_Tpl2BridgeManageExceedMaxLrn_Type.__name__ = "Integer32"
_Tpl2BridgeManageExceedMaxLrn_Object = MibTableColumn
tpl2BridgeManageExceedMaxLrn = _Tpl2BridgeManageExceedMaxLrn_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 5, 4, 1, 3),
    _Tpl2BridgeManageExceedMaxLrn_Type()
)
tpl2BridgeManageExceedMaxLrn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpl2BridgeManageExceedMaxLrn.setStatus("current")


class _Tpl2BridgeManageNewMacLrn_Type(Integer32):
    """Custom type tpl2BridgeManageNewMacLrn based on Integer32"""
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


_Tpl2BridgeManageNewMacLrn_Type.__name__ = "Integer32"
_Tpl2BridgeManageNewMacLrn_Object = MibTableColumn
tpl2BridgeManageNewMacLrn = _Tpl2BridgeManageNewMacLrn_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 1, 5, 4, 1, 4),
    _Tpl2BridgeManageNewMacLrn_Type()
)
tpl2BridgeManageNewMacLrn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpl2BridgeManageNewMacLrn.setStatus("current")
_Tplinkl2BridgeNotifications_ObjectIdentity = ObjectIdentity
tplinkl2BridgeNotifications = _Tplinkl2BridgeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 2)
)

# Managed Objects groups


# Notification objects

fdbDynMacNew = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 2, 1)
)
fdbDynMacNew.setObjects(
    ("TPLINK-L2BRIDGE-MIB", "tpl2BridgeManageDynPort")
)
if mibBuilder.loadTexts:
    fdbDynMacNew.setStatus(
        "current"
    )

fdbStaticMacNew = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 2, 2)
)
fdbStaticMacNew.setObjects(
    ("TPLINK-L2BRIDGE-MIB", "tpl2BridgeManageStaticPort")
)
if mibBuilder.loadTexts:
    fdbStaticMacNew.setStatus(
        "current"
    )

fdbFilterMacNew = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 2, 3)
)
fdbFilterMacNew.setObjects(
    ("TPLINK-L2BRIDGE-MIB", "tpl2BridgeManageFilterVlanId")
)
if mibBuilder.loadTexts:
    fdbFilterMacNew.setStatus(
        "current"
    )

fdbMacTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 2, 4)
)
fdbMacTableFull.setObjects(
    ("TPLINK-L2BRIDGE-MIB", "tpl2BridgeManageStaticPort")
)
if mibBuilder.loadTexts:
    fdbMacTableFull.setStatus(
        "current"
    )

fdbMacMaxLearnedNumExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 2, 5)
)
fdbMacMaxLearnedNumExceed.setObjects(
    ("TPLINK-L2BRIDGE-MIB", "tpl2BridgeManageStaticPort")
)
if mibBuilder.loadTexts:
    fdbMacMaxLearnedNumExceed.setStatus(
        "current"
    )

fdbMacLearnModeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 10, 2, 6)
)
fdbMacLearnModeChange.setObjects(
    ("TPLINK-L2BRIDGE-MIB", "tpl2BridgeManageStaticPort")
)
if mibBuilder.loadTexts:
    fdbMacLearnModeChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-L2BRIDGE-MIB",
    **{"VlanSecEntryStatus": VlanSecEntryStatus,
       "tplinkl2BridgeMIB": tplinkl2BridgeMIB,
       "tplinkl2BridgeMIBObjects": tplinkl2BridgeMIBObjects,
       "tpl2BridgeManageStaticAddrCtrl": tpl2BridgeManageStaticAddrCtrl,
       "tpl2BridgeManageStaticAddrCtrlTable": tpl2BridgeManageStaticAddrCtrlTable,
       "tpl2BridgeManageStaticAddrCtrlEntry": tpl2BridgeManageStaticAddrCtrlEntry,
       "tpl2BridgeManageStaticMac": tpl2BridgeManageStaticMac,
       "tpl2BridgeManageStaticVlanId": tpl2BridgeManageStaticVlanId,
       "tpl2BridgeManageStaticPort": tpl2BridgeManageStaticPort,
       "tpl2BridgeManageStaticStatus": tpl2BridgeManageStaticStatus,
       "tpl2BridgeManageDynAddrCtrl": tpl2BridgeManageDynAddrCtrl,
       "tpl2BridgeManageDynAddrCtrlAgingTime": tpl2BridgeManageDynAddrCtrlAgingTime,
       "tpl2BridgeManageDynAddrCtrlTable": tpl2BridgeManageDynAddrCtrlTable,
       "tpl2BridgeManageDynAddrCtrlEntry": tpl2BridgeManageDynAddrCtrlEntry,
       "tpl2BridgeManageDynMac": tpl2BridgeManageDynMac,
       "tpl2BridgeManageDynVlanId": tpl2BridgeManageDynVlanId,
       "tpl2BridgeManageDynPort": tpl2BridgeManageDynPort,
       "tpl2BridgeManageDynAgeStatus": tpl2BridgeManageDynAgeStatus,
       "tpl2BridgeManageDynStatus": tpl2BridgeManageDynStatus,
       "tpl2BridgeManageFilterAddrCtrl": tpl2BridgeManageFilterAddrCtrl,
       "tpl2BridgeManageFilterCtrlTable": tpl2BridgeManageFilterCtrlTable,
       "tpl2BridgeManageFilterCtrlEntry": tpl2BridgeManageFilterCtrlEntry,
       "tpl2BridgeManageFilterMac": tpl2BridgeManageFilterMac,
       "tpl2BridgeManageFilterVlanId": tpl2BridgeManageFilterVlanId,
       "tpl2BridgeManageFilterStatus": tpl2BridgeManageFilterStatus,
       "tpl2BridgeManageVlanSecurityCtrl": tpl2BridgeManageVlanSecurityCtrl,
       "tpl2BridgeManagevlanSecurityTable": tpl2BridgeManagevlanSecurityTable,
       "tpl2BridgeManagevlanSecEntry": tpl2BridgeManagevlanSecEntry,
       "tpFdbVlanSecurityVid": tpFdbVlanSecurityVid,
       "tpFdbVlanSecurityMaxLearned": tpFdbVlanSecurityMaxLearned,
       "tpFdbVlanSecurityRowStatus": tpFdbVlanSecurityRowStatus,
       "tpl2BridgeManageNotificationCtrl": tpl2BridgeManageNotificationCtrl,
       "tpl2BridgeManageNotificationGlobalStatus": tpl2BridgeManageNotificationGlobalStatus,
       "tpl2BridgeManageNotificationTableFullStatus": tpl2BridgeManageNotificationTableFullStatus,
       "tpl2BridgeManageNotificationInterval": tpl2BridgeManageNotificationInterval,
       "tpl2BridgeManageNotificationTable": tpl2BridgeManageNotificationTable,
       "tpl2BridgeManageNotificationCtrlEntry": tpl2BridgeManageNotificationCtrlEntry,
       "tpl2BridgeManagePortIndex": tpl2BridgeManagePortIndex,
       "tpl2BridgeManageLrnModeChg": tpl2BridgeManageLrnModeChg,
       "tpl2BridgeManageExceedMaxLrn": tpl2BridgeManageExceedMaxLrn,
       "tpl2BridgeManageNewMacLrn": tpl2BridgeManageNewMacLrn,
       "tplinkl2BridgeNotifications": tplinkl2BridgeNotifications,
       "fdbDynMacNew": fdbDynMacNew,
       "fdbStaticMacNew": fdbStaticMacNew,
       "fdbFilterMacNew": fdbFilterMacNew,
       "fdbMacTableFull": fdbMacTableFull,
       "fdbMacMaxLearnedNumExceed": fdbMacMaxLearnedNumExceed,
       "fdbMacLearnModeChange": fdbMacLearnModeChange}
)
