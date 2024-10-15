# SNMP MIB module (EQLIPADDR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQLIPADDR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:05 2024
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

(UTFString,
 eqlGroupId) = mibBuilder.importSymbols(
    "EQLGROUP-MIB",
    "UTFString",
    "eqlGroupId")

(eqlMemberIndex,) = mibBuilder.importSymbols(
    "EQLMEMBER-MIB",
    "eqlMemberIndex")

(equalLogic,) = mibBuilder.importSymbols(
    "EQUALLOGIC-SMI",
    "equalLogic")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

eqlipaddrModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 9)
)
eqlipaddrModule.setRevisions(
        ("2002-09-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EqlipAddrTable_Object = MibTable
eqlipAddrTable = _EqlipAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 1)
)
if mibBuilder.loadTexts:
    eqlipAddrTable.setStatus("deprecated")
_EqlipAddrEntry_Object = MibTableRow
eqlipAddrEntry = _EqlipAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 1, 1)
)
eqlipAddrEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLIPADDR-MIB", "eqlIpAdEntAddr"),
)
if mibBuilder.loadTexts:
    eqlipAddrEntry.setStatus("current")
_EqlIpAdEntAddr_Type = IpAddress
_EqlIpAdEntAddr_Object = MibTableColumn
eqlIpAdEntAddr = _EqlIpAdEntAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 1, 1, 1),
    _EqlIpAdEntAddr_Type()
)
eqlIpAdEntAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlIpAdEntAddr.setStatus("current")


class _EqlIpAdEntIfName_Type(DisplayString):
    """Custom type eqlIpAdEntIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_EqlIpAdEntIfName_Type.__name__ = "DisplayString"
_EqlIpAdEntIfName_Object = MibTableColumn
eqlIpAdEntIfName = _EqlIpAdEntIfName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 1, 1, 2),
    _EqlIpAdEntIfName_Type()
)
eqlIpAdEntIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpAdEntIfName.setStatus("current")
_EqlIpAdEntNetMask_Type = IpAddress
_EqlIpAdEntNetMask_Object = MibTableColumn
eqlIpAdEntNetMask = _EqlIpAdEntNetMask_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 1, 1, 3),
    _EqlIpAdEntNetMask_Type()
)
eqlIpAdEntNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpAdEntNetMask.setStatus("current")
_EqlIpAdEntIfIndex_Type = Integer32
_EqlIpAdEntIfIndex_Object = MibTableColumn
eqlIpAdEntIfIndex = _EqlIpAdEntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 1, 1, 4),
    _EqlIpAdEntIfIndex_Type()
)
eqlIpAdEntIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpAdEntIfIndex.setStatus("current")
_EqlIpAdEntRowStatus_Type = RowStatus
_EqlIpAdEntRowStatus_Object = MibTableColumn
eqlIpAdEntRowStatus = _EqlIpAdEntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 1, 1, 5),
    _EqlIpAdEntRowStatus_Type()
)
eqlIpAdEntRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlIpAdEntRowStatus.setStatus("current")
_EqlifTable_Object = MibTable
eqlifTable = _EqlifTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 2)
)
if mibBuilder.loadTexts:
    eqlifTable.setStatus("current")
_EqlifEntry_Object = MibTableRow
eqlifEntry = _EqlifEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 2, 1)
)
eqlifEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eqlifEntry.setStatus("current")


class _EqlifDescr_Type(DisplayString):
    """Custom type eqlifDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_EqlifDescr_Type.__name__ = "DisplayString"
_EqlifDescr_Object = MibTableColumn
eqlifDescr = _EqlifDescr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 2, 1, 1),
    _EqlifDescr_Type()
)
eqlifDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlifDescr.setStatus("current")


class _EqlifPortAttr_Type(Integer32):
    """Custom type eqlifPortAttr based on Integer32"""
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
        *(("attr-any", 3),
          ("attr-initiator-only", 2),
          ("attr-pss-only", 1))
    )


_EqlifPortAttr_Type.__name__ = "Integer32"
_EqlifPortAttr_Object = MibTableColumn
eqlifPortAttr = _EqlifPortAttr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 2, 1, 2),
    _EqlifPortAttr_Type()
)
eqlifPortAttr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlifPortAttr.setStatus("current")


class _EqlifAdminStatus_Type(Integer32):
    """Custom type eqlifAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_EqlifAdminStatus_Type.__name__ = "Integer32"
_EqlifAdminStatus_Object = MibTableColumn
eqlifAdminStatus = _EqlifAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 2, 1, 3),
    _EqlifAdminStatus_Type()
)
eqlifAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlifAdminStatus.setStatus("current")


class _EqlifRole_Type(Integer32):
    """Custom type eqlifRole based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("iscsi-only", 0),
          ("mgmt-only", 1))
    )


_EqlifRole_Type.__name__ = "Integer32"
_EqlifRole_Object = MibTableColumn
eqlifRole = _EqlifRole_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 2, 1, 4),
    _EqlifRole_Type()
)
eqlifRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlifRole.setStatus("current")
_EqlWKATable_Object = MibTable
eqlWKATable = _EqlWKATable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 3)
)
if mibBuilder.loadTexts:
    eqlWKATable.setStatus("current")
_EqlWKAEntry_Object = MibTableRow
eqlWKAEntry = _EqlWKAEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 3, 1)
)
eqlWKAEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLIPADDR-MIB", "eqlInetAddrEntAddrType"),
    (0, "EQLIPADDR-MIB", "eqlInetAddrEntAddr"),
)
if mibBuilder.loadTexts:
    eqlWKAEntry.setStatus("current")
_EqlWKARowStatus_Type = RowStatus
_EqlWKARowStatus_Object = MibTableColumn
eqlWKARowStatus = _EqlWKARowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 3, 1, 1),
    _EqlWKARowStatus_Type()
)
eqlWKARowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlWKARowStatus.setStatus("current")


class _EqlWKARole_Type(Integer32):
    """Custom type eqlWKARole based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("management", 1),
          ("secondary", 2))
    )


_EqlWKARole_Type.__name__ = "Integer32"
_EqlWKARole_Object = MibTableColumn
eqlWKARole = _EqlWKARole_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 3, 1, 2),
    _EqlWKARole_Type()
)
eqlWKARole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlWKARole.setStatus("current")
_EqlifStatusTable_Object = MibTable
eqlifStatusTable = _EqlifStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 4)
)
if mibBuilder.loadTexts:
    eqlifStatusTable.setStatus("current")
_EqlifStatusEntry_Object = MibTableRow
eqlifStatusEntry = _EqlifStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 4, 1)
)
if mibBuilder.loadTexts:
    eqlifStatusEntry.setStatus("current")


class _EqlifStatusMgmtRolePolicy_Type(Integer32):
    """Custom type eqlifStatusMgmtRolePolicy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configurable", 1),
          ("fixed", 2),
          ("non-configurable", 0))
    )


_EqlifStatusMgmtRolePolicy_Type.__name__ = "Integer32"
_EqlifStatusMgmtRolePolicy_Object = MibTableColumn
eqlifStatusMgmtRolePolicy = _EqlifStatusMgmtRolePolicy_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 4, 1, 1),
    _EqlifStatusMgmtRolePolicy_Type()
)
eqlifStatusMgmtRolePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlifStatusMgmtRolePolicy.setStatus("current")


class _EqlifStatusConfigurationFlags_Type(Bits):
    """Custom type eqlifStatusConfigurationFlags based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("flag1", 1),
          ("flag10", 10),
          ("flag11", 11),
          ("flag12", 12),
          ("flag13", 13),
          ("flag14", 14),
          ("flag15", 15),
          ("flag16", 16),
          ("flag17", 17),
          ("flag18", 18),
          ("flag19", 19),
          ("flag2", 2),
          ("flag20", 20),
          ("flag21", 21),
          ("flag22", 22),
          ("flag23", 23),
          ("flag24", 24),
          ("flag25", 25),
          ("flag26", 26),
          ("flag27", 27),
          ("flag28", 28),
          ("flag29", 29),
          ("flag3", 3),
          ("flag30", 30),
          ("flag31", 31),
          ("flag4", 4),
          ("flag5", 5),
          ("flag6", 6),
          ("flag7", 7),
          ("flag8", 8),
          ("flag9", 9),
          ("isDcbCapable", 0))
    )

_EqlifStatusConfigurationFlags_Type.__name__ = "Bits"
_EqlifStatusConfigurationFlags_Object = MibTableColumn
eqlifStatusConfigurationFlags = _EqlifStatusConfigurationFlags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 4, 1, 2),
    _EqlifStatusConfigurationFlags_Type()
)
eqlifStatusConfigurationFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlifStatusConfigurationFlags.setStatus("current")


class _EqlifOperStatus_Type(Integer32):
    """Custom type eqlifOperStatus based on Integer32"""
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
        *(("dormant", 5),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_EqlifOperStatus_Type.__name__ = "Integer32"
_EqlifOperStatus_Object = MibTableColumn
eqlifOperStatus = _EqlifOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 4, 1, 3),
    _EqlifOperStatus_Type()
)
eqlifOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlifOperStatus.setStatus("current")
_EqlinetAddrTable_Object = MibTable
eqlinetAddrTable = _EqlinetAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 5)
)
if mibBuilder.loadTexts:
    eqlinetAddrTable.setStatus("current")
_EqlinetAddrEntry_Object = MibTableRow
eqlinetAddrEntry = _EqlinetAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 5, 1)
)
eqlinetAddrEntry.setIndexNames(
    (0, "EQLGROUP-MIB", "eqlGroupId"),
    (0, "EQLMEMBER-MIB", "eqlMemberIndex"),
    (0, "EQLIPADDR-MIB", "eqlInetAddrEntAddrType"),
    (0, "EQLIPADDR-MIB", "eqlInetAddrEntAddr"),
)
if mibBuilder.loadTexts:
    eqlinetAddrEntry.setStatus("current")
_EqlInetAddrEntAddrType_Type = InetAddressType
_EqlInetAddrEntAddrType_Object = MibTableColumn
eqlInetAddrEntAddrType = _EqlInetAddrEntAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 5, 1, 1),
    _EqlInetAddrEntAddrType_Type()
)
eqlInetAddrEntAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlInetAddrEntAddrType.setStatus("current")
_EqlInetAddrEntAddr_Type = InetAddress
_EqlInetAddrEntAddr_Object = MibTableColumn
eqlInetAddrEntAddr = _EqlInetAddrEntAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 5, 1, 2),
    _EqlInetAddrEntAddr_Type()
)
eqlInetAddrEntAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlInetAddrEntAddr.setStatus("current")


class _EqlInetAddrEntIfName_Type(DisplayString):
    """Custom type eqlInetAddrEntIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_EqlInetAddrEntIfName_Type.__name__ = "DisplayString"
_EqlInetAddrEntIfName_Object = MibTableColumn
eqlInetAddrEntIfName = _EqlInetAddrEntIfName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 5, 1, 3),
    _EqlInetAddrEntIfName_Type()
)
eqlInetAddrEntIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlInetAddrEntIfName.setStatus("current")
_EqlInetAddrEntNetMaskType_Type = InetAddressType
_EqlInetAddrEntNetMaskType_Object = MibTableColumn
eqlInetAddrEntNetMaskType = _EqlInetAddrEntNetMaskType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 5, 1, 4),
    _EqlInetAddrEntNetMaskType_Type()
)
eqlInetAddrEntNetMaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlInetAddrEntNetMaskType.setStatus("current")
_EqlInetAddrEntNetMask_Type = InetAddress
_EqlInetAddrEntNetMask_Object = MibTableColumn
eqlInetAddrEntNetMask = _EqlInetAddrEntNetMask_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 5, 1, 5),
    _EqlInetAddrEntNetMask_Type()
)
eqlInetAddrEntNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlInetAddrEntNetMask.setStatus("current")
_EqlInetAddrEntIfIndex_Type = Integer32
_EqlInetAddrEntIfIndex_Object = MibTableColumn
eqlInetAddrEntIfIndex = _EqlInetAddrEntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 5, 1, 6),
    _EqlInetAddrEntIfIndex_Type()
)
eqlInetAddrEntIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlInetAddrEntIfIndex.setStatus("current")


class _EqlInetAddrEntFlags_Type(Integer32):
    """Custom type eqlInetAddrEntFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no-options", 0),
          ("static", 1))
    )


_EqlInetAddrEntFlags_Type.__name__ = "Integer32"
_EqlInetAddrEntFlags_Object = MibTableColumn
eqlInetAddrEntFlags = _EqlInetAddrEntFlags_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 5, 1, 7),
    _EqlInetAddrEntFlags_Type()
)
eqlInetAddrEntFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlInetAddrEntFlags.setStatus("current")
_EqlInetAddrEntRowStatus_Type = RowStatus
_EqlInetAddrEntRowStatus_Object = MibTableColumn
eqlInetAddrEntRowStatus = _EqlInetAddrEntRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 9, 5, 1, 8),
    _EqlInetAddrEntRowStatus_Type()
)
eqlInetAddrEntRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlInetAddrEntRowStatus.setStatus("current")
eqlifEntry.registerAugmentions(
    ("EQLIPADDR-MIB",
     "eqlifStatusEntry")
)
eqlifStatusEntry.setIndexNames(*eqlifEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQLIPADDR-MIB",
    **{"eqlipaddrModule": eqlipaddrModule,
       "eqlipAddrTable": eqlipAddrTable,
       "eqlipAddrEntry": eqlipAddrEntry,
       "eqlIpAdEntAddr": eqlIpAdEntAddr,
       "eqlIpAdEntIfName": eqlIpAdEntIfName,
       "eqlIpAdEntNetMask": eqlIpAdEntNetMask,
       "eqlIpAdEntIfIndex": eqlIpAdEntIfIndex,
       "eqlIpAdEntRowStatus": eqlIpAdEntRowStatus,
       "eqlifTable": eqlifTable,
       "eqlifEntry": eqlifEntry,
       "eqlifDescr": eqlifDescr,
       "eqlifPortAttr": eqlifPortAttr,
       "eqlifAdminStatus": eqlifAdminStatus,
       "eqlifRole": eqlifRole,
       "eqlWKATable": eqlWKATable,
       "eqlWKAEntry": eqlWKAEntry,
       "eqlWKARowStatus": eqlWKARowStatus,
       "eqlWKARole": eqlWKARole,
       "eqlifStatusTable": eqlifStatusTable,
       "eqlifStatusEntry": eqlifStatusEntry,
       "eqlifStatusMgmtRolePolicy": eqlifStatusMgmtRolePolicy,
       "eqlifStatusConfigurationFlags": eqlifStatusConfigurationFlags,
       "eqlifOperStatus": eqlifOperStatus,
       "eqlinetAddrTable": eqlinetAddrTable,
       "eqlinetAddrEntry": eqlinetAddrEntry,
       "eqlInetAddrEntAddrType": eqlInetAddrEntAddrType,
       "eqlInetAddrEntAddr": eqlInetAddrEntAddr,
       "eqlInetAddrEntIfName": eqlInetAddrEntIfName,
       "eqlInetAddrEntNetMaskType": eqlInetAddrEntNetMaskType,
       "eqlInetAddrEntNetMask": eqlInetAddrEntNetMask,
       "eqlInetAddrEntIfIndex": eqlInetAddrEntIfIndex,
       "eqlInetAddrEntFlags": eqlInetAddrEntFlags,
       "eqlInetAddrEntRowStatus": eqlInetAddrEntRowStatus}
)
