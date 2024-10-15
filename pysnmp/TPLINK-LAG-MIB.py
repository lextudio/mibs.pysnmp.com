# SNMP MIB module (TPLINK-LAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-LAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:16 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkLagMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 9)
)
tplinkLagMIB.setRevisions(
        ("2012-12-13 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkLagMIBObjects_ObjectIdentity = ObjectIdentity
tplinkLagMIBObjects = _TplinkLagMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 9, 1)
)
_TplinkLagMIBGlobalConfig_ObjectIdentity = ObjectIdentity
tplinkLagMIBGlobalConfig = _TplinkLagMIBGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 1)
)
_TpLagMaxEntryNum_Type = Integer32
_TpLagMaxEntryNum_Object = MibScalar
tpLagMaxEntryNum = _TpLagMaxEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 1, 1),
    _TpLagMaxEntryNum_Type()
)
tpLagMaxEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpLagMaxEntryNum.setStatus("current")


class _TpLagLoadBalance_Type(Integer32):
    """Custom type tpLagLoadBalance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ip-dest", 4),
          ("ip-source", 3),
          ("ip-source-dest", 5),
          ("mac-dest", 1),
          ("mac-source", 0),
          ("mac-source-dest", 2))
    )


_TpLagLoadBalance_Type.__name__ = "Integer32"
_TpLagLoadBalance_Object = MibScalar
tpLagLoadBalance = _TpLagLoadBalance_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 1, 2),
    _TpLagLoadBalance_Type()
)
tpLagLoadBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpLagLoadBalance.setStatus("current")
_TplinkLagTable_ObjectIdentity = ObjectIdentity
tplinkLagTable = _TplinkLagTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 2)
)
_TpLagTable_Object = MibTable
tpLagTable = _TpLagTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 2, 3)
)
if mibBuilder.loadTexts:
    tpLagTable.setStatus("current")
_TpLagEntry_Object = MibTableRow
tpLagEntry = _TpLagEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 2, 3, 1)
)
tpLagEntry.setIndexNames(
    (0, "TPLINK-LAG-MIB", "tpLagIndex"),
)
if mibBuilder.loadTexts:
    tpLagEntry.setStatus("current")
_TpLagIndex_Type = Integer32
_TpLagIndex_Object = MibTableColumn
tpLagIndex = _TpLagIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 2, 3, 1, 1),
    _TpLagIndex_Type()
)
tpLagIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpLagIndex.setStatus("current")


class _TpLagType_Type(Integer32):
    """Custom type tpLagType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("on", 1),
          ("passive", 3))
    )


_TpLagType_Type.__name__ = "Integer32"
_TpLagType_Object = MibTableColumn
tpLagType = _TpLagType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 2, 3, 1, 2),
    _TpLagType_Type()
)
tpLagType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpLagType.setStatus("current")


class _TpLagMember_Type(DisplayString):
    """Custom type tpLagMember based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_TpLagMember_Type.__name__ = "DisplayString"
_TpLagMember_Object = MibTableColumn
tpLagMember = _TpLagMember_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 2, 3, 1, 3),
    _TpLagMember_Type()
)
tpLagMember.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpLagMember.setStatus("current")
_TpLagRowStatus_Type = RowStatus
_TpLagRowStatus_Object = MibTableColumn
tpLagRowStatus = _TpLagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 2, 3, 1, 4),
    _TpLagRowStatus_Type()
)
tpLagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpLagRowStatus.setStatus("current")
_TplinkLagLacpManage_ObjectIdentity = ObjectIdentity
tplinkLagLacpManage = _TplinkLagLacpManage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 3)
)


class _TpLacpSystemPriority_Type(Integer32):
    """Custom type tpLacpSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TpLacpSystemPriority_Type.__name__ = "Integer32"
_TpLacpSystemPriority_Object = MibScalar
tpLacpSystemPriority = _TpLacpSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 3, 1),
    _TpLacpSystemPriority_Type()
)
tpLacpSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpLacpSystemPriority.setStatus("current")
_TpLacpTable_Object = MibTable
tpLacpTable = _TpLacpTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tpLacpTable.setStatus("current")
_TpLacpEntry_Object = MibTableRow
tpLacpEntry = _TpLacpEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 3, 2, 1)
)
tpLacpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpLacpEntry.setStatus("current")
_TpLacpPort_Type = DisplayString
_TpLacpPort_Object = MibTableColumn
tpLacpPort = _TpLacpPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 3, 2, 1, 1),
    _TpLacpPort_Type()
)
tpLacpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpLacpPort.setStatus("current")


class _TpLacpAdminKey_Type(Integer32):
    """Custom type tpLacpAdminKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TpLacpAdminKey_Type.__name__ = "Integer32"
_TpLacpAdminKey_Object = MibTableColumn
tpLacpAdminKey = _TpLacpAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 3, 2, 1, 2),
    _TpLacpAdminKey_Type()
)
tpLacpAdminKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpLacpAdminKey.setStatus("current")


class _TpLacpPortPriority_Type(Integer32):
    """Custom type tpLacpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TpLacpPortPriority_Type.__name__ = "Integer32"
_TpLacpPortPriority_Object = MibTableColumn
tpLacpPortPriority = _TpLacpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 3, 2, 1, 3),
    _TpLacpPortPriority_Type()
)
tpLacpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpLacpPortPriority.setStatus("current")


class _TpLacpMode_Type(Integer32):
    """Custom type tpLacpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 0))
    )


_TpLacpMode_Type.__name__ = "Integer32"
_TpLacpMode_Object = MibTableColumn
tpLacpMode = _TpLacpMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 3, 2, 1, 4),
    _TpLacpMode_Type()
)
tpLacpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpLacpMode.setStatus("current")


class _TpLacpChan_Type(DisplayString):
    """Custom type tpLacpChan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TpLacpChan_Type.__name__ = "DisplayString"
_TpLacpChan_Object = MibTableColumn
tpLacpChan = _TpLacpChan_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 9, 1, 3, 2, 1, 5),
    _TpLacpChan_Type()
)
tpLacpChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpLacpChan.setStatus("current")
_TplinkLagNotifications_ObjectIdentity = ObjectIdentity
tplinkLagNotifications = _TplinkLagNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 9, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-LAG-MIB",
    **{"tplinkLagMIB": tplinkLagMIB,
       "tplinkLagMIBObjects": tplinkLagMIBObjects,
       "tplinkLagMIBGlobalConfig": tplinkLagMIBGlobalConfig,
       "tpLagMaxEntryNum": tpLagMaxEntryNum,
       "tpLagLoadBalance": tpLagLoadBalance,
       "tplinkLagTable": tplinkLagTable,
       "tpLagTable": tpLagTable,
       "tpLagEntry": tpLagEntry,
       "tpLagIndex": tpLagIndex,
       "tpLagType": tpLagType,
       "tpLagMember": tpLagMember,
       "tpLagRowStatus": tpLagRowStatus,
       "tplinkLagLacpManage": tplinkLagLacpManage,
       "tpLacpSystemPriority": tpLacpSystemPriority,
       "tpLacpTable": tpLacpTable,
       "tpLacpEntry": tpLacpEntry,
       "tpLacpPort": tpLacpPort,
       "tpLacpAdminKey": tpLacpAdminKey,
       "tpLacpPortPriority": tpLacpPortPriority,
       "tpLacpMode": tpLacpMode,
       "tpLacpChan": tpLacpChan,
       "tplinkLagNotifications": tplinkLagNotifications}
)
