# SNMP MIB module (ISLVLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ISLVLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:55 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

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

islVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4)
)
_IslVlanMIBObjects_ObjectIdentity = ObjectIdentity
islVlanMIBObjects = _IslVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 9, 1)
)
_IslVlanControlTable_Object = MibTable
islVlanControlTable = _IslVlanControlTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 9, 1, 1)
)
if mibBuilder.loadTexts:
    islVlanControlTable.setStatus("current")
_IslVlanControlEntry_Object = MibTableRow
islVlanControlEntry = _IslVlanControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 9, 1, 1, 1)
)
islVlanControlEntry.setIndexNames(
    (0, "ISLVLAN-MIB", "islVlanControlIndex"),
)
if mibBuilder.loadTexts:
    islVlanControlEntry.setStatus("current")


class _IslVlanControlIndex_Type(Integer32):
    """Custom type islVlanControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IslVlanControlIndex_Type.__name__ = "Integer32"
_IslVlanControlIndex_Object = MibTableColumn
islVlanControlIndex = _IslVlanControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 9, 1, 1, 1, 1),
    _IslVlanControlIndex_Type()
)
islVlanControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    islVlanControlIndex.setStatus("current")
_IslVlanControlDataSource_Type = ObjectIdentifier
_IslVlanControlDataSource_Object = MibTableColumn
islVlanControlDataSource = _IslVlanControlDataSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 9, 1, 1, 1, 2),
    _IslVlanControlDataSource_Type()
)
islVlanControlDataSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    islVlanControlDataSource.setStatus("current")
_IslVlanControlVtpDomain_Type = IpAddress
_IslVlanControlVtpDomain_Object = MibTableColumn
islVlanControlVtpDomain = _IslVlanControlVtpDomain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 9, 1, 1, 1, 3),
    _IslVlanControlVtpDomain_Type()
)
islVlanControlVtpDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    islVlanControlVtpDomain.setStatus("current")
_IslVlanControlVtpCommunity_Type = DisplayString
_IslVlanControlVtpCommunity_Object = MibTableColumn
islVlanControlVtpCommunity = _IslVlanControlVtpCommunity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 9, 1, 1, 1, 4),
    _IslVlanControlVtpCommunity_Type()
)
islVlanControlVtpCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    islVlanControlVtpCommunity.setStatus("current")


class _IslVlanControlEnable_Type(Integer32):
    """Custom type islVlanControlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("explicitOnly", 2),
          ("implicitCreate", 3))
    )


_IslVlanControlEnable_Type.__name__ = "Integer32"
_IslVlanControlEnable_Object = MibTableColumn
islVlanControlEnable = _IslVlanControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 9, 1, 1, 1, 5),
    _IslVlanControlEnable_Type()
)
islVlanControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    islVlanControlEnable.setStatus("current")
_IslVlanTable_Object = MibTable
islVlanTable = _IslVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 9, 1, 2)
)
if mibBuilder.loadTexts:
    islVlanTable.setStatus("current")
_IslVlanEntry_Object = MibTableRow
islVlanEntry = _IslVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 9, 1, 2, 1)
)
islVlanEntry.setIndexNames(
    (0, "ISLVLAN-MIB", "islVlanIndex"),
)
if mibBuilder.loadTexts:
    islVlanEntry.setStatus("current")


class _IslVlanIndex_Type(Integer32):
    """Custom type islVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IslVlanIndex_Type.__name__ = "Integer32"
_IslVlanIndex_Object = MibTableColumn
islVlanIndex = _IslVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 9, 1, 2, 1, 1),
    _IslVlanIndex_Type()
)
islVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    islVlanIndex.setStatus("current")


class _IslVlanControlEntryIndex_Type(Integer32):
    """Custom type islVlanControlEntryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IslVlanControlEntryIndex_Type.__name__ = "Integer32"
_IslVlanControlEntryIndex_Object = MibTableColumn
islVlanControlEntryIndex = _IslVlanControlEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 9, 1, 2, 1, 2),
    _IslVlanControlEntryIndex_Type()
)
islVlanControlEntryIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    islVlanControlEntryIndex.setStatus("current")


class _IslVlanId_Type(Integer32):
    """Custom type islVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_IslVlanId_Type.__name__ = "Integer32"
_IslVlanId_Object = MibTableColumn
islVlanId = _IslVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 9, 1, 2, 1, 3),
    _IslVlanId_Type()
)
islVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    islVlanId.setStatus("current")
_IslVlanIfIndex_Type = InterfaceIndex
_IslVlanIfIndex_Object = MibTableColumn
islVlanIfIndex = _IslVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 9, 1, 2, 1, 4),
    _IslVlanIfIndex_Type()
)
islVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    islVlanIfIndex.setStatus("current")


class _IslVlanName_Type(DisplayString):
    """Custom type islVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_IslVlanName_Type.__name__ = "DisplayString"
_IslVlanName_Object = MibTableColumn
islVlanName = _IslVlanName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 9, 1, 2, 1, 5),
    _IslVlanName_Type()
)
islVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    islVlanName.setStatus("current")
_IslVlanMtu_Type = Integer32
_IslVlanMtu_Object = MibTableColumn
islVlanMtu = _IslVlanMtu_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 9, 1, 2, 1, 6),
    _IslVlanMtu_Type()
)
islVlanMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    islVlanMtu.setStatus("current")
_IslVlanOwner_Type = OwnerString
_IslVlanOwner_Object = MibTableColumn
islVlanOwner = _IslVlanOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 9, 1, 2, 1, 7),
    _IslVlanOwner_Type()
)
islVlanOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    islVlanOwner.setStatus("current")
_IslVlanStatus_Type = RowStatus
_IslVlanStatus_Object = MibTableColumn
islVlanStatus = _IslVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 4, 9, 1, 2, 1, 8),
    _IslVlanStatus_Type()
)
islVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    islVlanStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ISLVLAN-MIB",
    **{"hp": hp,
       "nm": nm,
       "interface": interface,
       "islVlanMIB": islVlanMIB,
       "islVlanMIBObjects": islVlanMIBObjects,
       "islVlanControlTable": islVlanControlTable,
       "islVlanControlEntry": islVlanControlEntry,
       "islVlanControlIndex": islVlanControlIndex,
       "islVlanControlDataSource": islVlanControlDataSource,
       "islVlanControlVtpDomain": islVlanControlVtpDomain,
       "islVlanControlVtpCommunity": islVlanControlVtpCommunity,
       "islVlanControlEnable": islVlanControlEnable,
       "islVlanTable": islVlanTable,
       "islVlanEntry": islVlanEntry,
       "islVlanIndex": islVlanIndex,
       "islVlanControlEntryIndex": islVlanControlEntryIndex,
       "islVlanId": islVlanId,
       "islVlanIfIndex": islVlanIfIndex,
       "islVlanName": islVlanName,
       "islVlanMtu": islVlanMtu,
       "islVlanOwner": islVlanOwner,
       "islVlanStatus": islVlanStatus}
)
