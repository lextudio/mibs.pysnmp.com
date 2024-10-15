# SNMP MIB module (HUAWEI-ATK-EUDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-ATK-EUDM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:48 2024
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

(mplsVpnVrfName,) = mibBuilder.importSymbols(
    "MPLS-VPN-MIB",
    "mplsVpnVrfName")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwATKEudm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwATK_ObjectIdentity = ObjectIdentity
hwATK = _HwATK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10)
)
_HwAtkZoneMibObjects_ObjectIdentity = ObjectIdentity
hwAtkZoneMibObjects = _HwAtkZoneMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 1)
)
_HwAtkSynFloodZoneTable_Object = MibTable
hwAtkSynFloodZoneTable = _HwAtkSynFloodZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwAtkSynFloodZoneTable.setStatus("current")
_HwAtkSynFloodZoneEntry_Object = MibTableRow
hwAtkSynFloodZoneEntry = _HwAtkSynFloodZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 1, 1, 1)
)
hwAtkSynFloodZoneEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-ATK-EUDM-MIB", "hwAtkSynFloodZoneID"),
)
if mibBuilder.loadTexts:
    hwAtkSynFloodZoneEntry.setStatus("current")


class _HwAtkSynFloodZoneID_Type(Integer32):
    """Custom type hwAtkSynFloodZoneID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwAtkSynFloodZoneID_Type.__name__ = "Integer32"
_HwAtkSynFloodZoneID_Object = MibTableColumn
hwAtkSynFloodZoneID = _HwAtkSynFloodZoneID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 1, 1, 1, 1),
    _HwAtkSynFloodZoneID_Type()
)
hwAtkSynFloodZoneID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAtkSynFloodZoneID.setStatus("current")


class _HwAtkZoneSynFloodSynSpeed_Type(Integer32):
    """Custom type hwAtkZoneSynFloodSynSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_HwAtkZoneSynFloodSynSpeed_Type.__name__ = "Integer32"
_HwAtkZoneSynFloodSynSpeed_Object = MibTableColumn
hwAtkZoneSynFloodSynSpeed = _HwAtkZoneSynFloodSynSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 1, 1, 1, 2),
    _HwAtkZoneSynFloodSynSpeed_Type()
)
hwAtkZoneSynFloodSynSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtkZoneSynFloodSynSpeed.setStatus("current")


class _HwAtkZoneSynFloodHalfMax_Type(Integer32):
    """Custom type hwAtkZoneSynFloodHalfMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000000),
    )


_HwAtkZoneSynFloodHalfMax_Type.__name__ = "Integer32"
_HwAtkZoneSynFloodHalfMax_Object = MibTableColumn
hwAtkZoneSynFloodHalfMax = _HwAtkZoneSynFloodHalfMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 1, 1, 1, 3),
    _HwAtkZoneSynFloodHalfMax_Type()
)
hwAtkZoneSynFloodHalfMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtkZoneSynFloodHalfMax.setStatus("current")


class _HwAtkZoneSynFloodHalfAge_Type(Integer32):
    """Custom type hwAtkZoneSynFloodHalfAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwAtkZoneSynFloodHalfAge_Type.__name__ = "Integer32"
_HwAtkZoneSynFloodHalfAge_Object = MibTableColumn
hwAtkZoneSynFloodHalfAge = _HwAtkZoneSynFloodHalfAge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 1, 1, 1, 4),
    _HwAtkZoneSynFloodHalfAge_Type()
)
hwAtkZoneSynFloodHalfAge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtkZoneSynFloodHalfAge.setStatus("current")


class _HwAtkZoneSynFloodProxy_Type(Integer32):
    """Custom type hwAtkZoneSynFloodProxy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("off", 3),
          ("on", 2))
    )


_HwAtkZoneSynFloodProxy_Type.__name__ = "Integer32"
_HwAtkZoneSynFloodProxy_Object = MibTableColumn
hwAtkZoneSynFloodProxy = _HwAtkZoneSynFloodProxy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 1, 1, 1, 5),
    _HwAtkZoneSynFloodProxy_Type()
)
hwAtkZoneSynFloodProxy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtkZoneSynFloodProxy.setStatus("current")
_HwAtkZoneSynFloodStatus_Type = RowStatus
_HwAtkZoneSynFloodStatus_Object = MibTableColumn
hwAtkZoneSynFloodStatus = _HwAtkZoneSynFloodStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 1, 1, 1, 6),
    _HwAtkZoneSynFloodStatus_Type()
)
hwAtkZoneSynFloodStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtkZoneSynFloodStatus.setStatus("current")
_HwAtkUdpFloodZoneTable_Object = MibTable
hwAtkUdpFloodZoneTable = _HwAtkUdpFloodZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hwAtkUdpFloodZoneTable.setStatus("current")
_HwAtkUdpFloodZoneEntry_Object = MibTableRow
hwAtkUdpFloodZoneEntry = _HwAtkUdpFloodZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 1, 2, 1)
)
hwAtkUdpFloodZoneEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-ATK-EUDM-MIB", "hwAtkUdpFloodZoneID"),
)
if mibBuilder.loadTexts:
    hwAtkUdpFloodZoneEntry.setStatus("current")


class _HwAtkUdpFloodZoneID_Type(Integer32):
    """Custom type hwAtkUdpFloodZoneID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwAtkUdpFloodZoneID_Type.__name__ = "Integer32"
_HwAtkUdpFloodZoneID_Object = MibTableColumn
hwAtkUdpFloodZoneID = _HwAtkUdpFloodZoneID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 1, 2, 1, 1),
    _HwAtkUdpFloodZoneID_Type()
)
hwAtkUdpFloodZoneID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAtkUdpFloodZoneID.setStatus("current")


class _HwAtkZoneUdpFloodSpeed_Type(Integer32):
    """Custom type hwAtkZoneUdpFloodSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_HwAtkZoneUdpFloodSpeed_Type.__name__ = "Integer32"
_HwAtkZoneUdpFloodSpeed_Object = MibTableColumn
hwAtkZoneUdpFloodSpeed = _HwAtkZoneUdpFloodSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 1, 2, 1, 2),
    _HwAtkZoneUdpFloodSpeed_Type()
)
hwAtkZoneUdpFloodSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtkZoneUdpFloodSpeed.setStatus("current")
_HwAtkZoneUdpFloodStatus_Type = RowStatus
_HwAtkZoneUdpFloodStatus_Object = MibTableColumn
hwAtkZoneUdpFloodStatus = _HwAtkZoneUdpFloodStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 1, 2, 1, 3),
    _HwAtkZoneUdpFloodStatus_Type()
)
hwAtkZoneUdpFloodStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtkZoneUdpFloodStatus.setStatus("current")
_HwAtkIcmpFloodZoneTable_Object = MibTable
hwAtkIcmpFloodZoneTable = _HwAtkIcmpFloodZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hwAtkIcmpFloodZoneTable.setStatus("current")
_HwAtkIcmpFloodZoneEntry_Object = MibTableRow
hwAtkIcmpFloodZoneEntry = _HwAtkIcmpFloodZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 1, 3, 1)
)
hwAtkIcmpFloodZoneEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-ATK-EUDM-MIB", "hwAtkIcmpFloodZoneID"),
)
if mibBuilder.loadTexts:
    hwAtkIcmpFloodZoneEntry.setStatus("current")


class _HwAtkIcmpFloodZoneID_Type(Integer32):
    """Custom type hwAtkIcmpFloodZoneID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_HwAtkIcmpFloodZoneID_Type.__name__ = "Integer32"
_HwAtkIcmpFloodZoneID_Object = MibTableColumn
hwAtkIcmpFloodZoneID = _HwAtkIcmpFloodZoneID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 1, 3, 1, 1),
    _HwAtkIcmpFloodZoneID_Type()
)
hwAtkIcmpFloodZoneID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAtkIcmpFloodZoneID.setStatus("current")


class _HwAtkZoneIcmpFloodSpeed_Type(Integer32):
    """Custom type hwAtkZoneIcmpFloodSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_HwAtkZoneIcmpFloodSpeed_Type.__name__ = "Integer32"
_HwAtkZoneIcmpFloodSpeed_Object = MibTableColumn
hwAtkZoneIcmpFloodSpeed = _HwAtkZoneIcmpFloodSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 1, 3, 1, 2),
    _HwAtkZoneIcmpFloodSpeed_Type()
)
hwAtkZoneIcmpFloodSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtkZoneIcmpFloodSpeed.setStatus("current")
_HwAtkZoneIcmpFloodStatus_Type = RowStatus
_HwAtkZoneIcmpFloodStatus_Object = MibTableColumn
hwAtkZoneIcmpFloodStatus = _HwAtkZoneIcmpFloodStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 1, 3, 1, 3),
    _HwAtkZoneIcmpFloodStatus_Type()
)
hwAtkZoneIcmpFloodStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAtkZoneIcmpFloodStatus.setStatus("current")
_HwAtkEudmConformance_ObjectIdentity = ObjectIdentity
hwAtkEudmConformance = _HwAtkEudmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 2)
)
_HwAtkEudmCompliance_ObjectIdentity = ObjectIdentity
hwAtkEudmCompliance = _HwAtkEudmCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 2, 1)
)
_HwAtkEudmMibGroups_ObjectIdentity = ObjectIdentity
hwAtkEudmMibGroups = _HwAtkEudmMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 2, 2)
)

# Managed Objects groups

hwAtkEudmSynFloodGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 2, 2, 1)
)
hwAtkEudmSynFloodGroup.setObjects(
      *(("HUAWEI-ATK-EUDM-MIB", "hwAtkZoneSynFloodSynSpeed"),
        ("HUAWEI-ATK-EUDM-MIB", "hwAtkZoneSynFloodHalfMax"),
        ("HUAWEI-ATK-EUDM-MIB", "hwAtkZoneSynFloodHalfAge"),
        ("HUAWEI-ATK-EUDM-MIB", "hwAtkZoneSynFloodProxy"),
        ("HUAWEI-ATK-EUDM-MIB", "hwAtkZoneSynFloodStatus"))
)
if mibBuilder.loadTexts:
    hwAtkEudmSynFloodGroup.setStatus("current")

hwAtkEudmUdpFloodGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 2, 2, 2)
)
hwAtkEudmUdpFloodGroup.setObjects(
      *(("HUAWEI-ATK-EUDM-MIB", "hwAtkZoneUdpFloodSpeed"),
        ("HUAWEI-ATK-EUDM-MIB", "hwAtkZoneUdpFloodStatus"))
)
if mibBuilder.loadTexts:
    hwAtkEudmUdpFloodGroup.setStatus("current")

hwAtkEudmIcmpFloodGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 10, 2, 2, 2, 3)
)
hwAtkEudmIcmpFloodGroup.setObjects(
      *(("HUAWEI-ATK-EUDM-MIB", "hwAtkZoneIcmpFloodSpeed"),
        ("HUAWEI-ATK-EUDM-MIB", "hwAtkZoneIcmpFloodStatus"))
)
if mibBuilder.loadTexts:
    hwAtkEudmIcmpFloodGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-ATK-EUDM-MIB",
    **{"hwATK": hwATK,
       "hwATKEudm": hwATKEudm,
       "hwAtkZoneMibObjects": hwAtkZoneMibObjects,
       "hwAtkSynFloodZoneTable": hwAtkSynFloodZoneTable,
       "hwAtkSynFloodZoneEntry": hwAtkSynFloodZoneEntry,
       "hwAtkSynFloodZoneID": hwAtkSynFloodZoneID,
       "hwAtkZoneSynFloodSynSpeed": hwAtkZoneSynFloodSynSpeed,
       "hwAtkZoneSynFloodHalfMax": hwAtkZoneSynFloodHalfMax,
       "hwAtkZoneSynFloodHalfAge": hwAtkZoneSynFloodHalfAge,
       "hwAtkZoneSynFloodProxy": hwAtkZoneSynFloodProxy,
       "hwAtkZoneSynFloodStatus": hwAtkZoneSynFloodStatus,
       "hwAtkUdpFloodZoneTable": hwAtkUdpFloodZoneTable,
       "hwAtkUdpFloodZoneEntry": hwAtkUdpFloodZoneEntry,
       "hwAtkUdpFloodZoneID": hwAtkUdpFloodZoneID,
       "hwAtkZoneUdpFloodSpeed": hwAtkZoneUdpFloodSpeed,
       "hwAtkZoneUdpFloodStatus": hwAtkZoneUdpFloodStatus,
       "hwAtkIcmpFloodZoneTable": hwAtkIcmpFloodZoneTable,
       "hwAtkIcmpFloodZoneEntry": hwAtkIcmpFloodZoneEntry,
       "hwAtkIcmpFloodZoneID": hwAtkIcmpFloodZoneID,
       "hwAtkZoneIcmpFloodSpeed": hwAtkZoneIcmpFloodSpeed,
       "hwAtkZoneIcmpFloodStatus": hwAtkZoneIcmpFloodStatus,
       "hwAtkEudmConformance": hwAtkEudmConformance,
       "hwAtkEudmCompliance": hwAtkEudmCompliance,
       "hwAtkEudmMibGroups": hwAtkEudmMibGroups,
       "hwAtkEudmSynFloodGroup": hwAtkEudmSynFloodGroup,
       "hwAtkEudmUdpFloodGroup": hwAtkEudmUdpFloodGroup,
       "hwAtkEudmIcmpFloodGroup": hwAtkEudmIcmpFloodGroup}
)
