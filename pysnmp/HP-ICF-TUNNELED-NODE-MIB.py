# SNMP MIB module (HP-ICF-TUNNELED-NODE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-TUNNELED-NODE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:19 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfTunneledNode = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128)
)
hpicfTunneledNode.setRevisions(
        ("2016-12-06 00:00",
         "2016-08-05 00:00",
         "2016-02-11 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfTunneledNodeObjects_ObjectIdentity = ObjectIdentity
hpicfTunneledNodeObjects = _HpicfTunneledNodeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1)
)
_HpicfTunneledNodeConfig_ObjectIdentity = ObjectIdentity
hpicfTunneledNodeConfig = _HpicfTunneledNodeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1)
)
_HpicfTunneledNodeTable_Object = MibTable
hpicfTunneledNodeTable = _HpicfTunneledNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfTunneledNodeTable.setStatus("current")
_HpicfTunneledNodeEntry_Object = MibTableRow
hpicfTunneledNodeEntry = _HpicfTunneledNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1)
)
hpicfTunneledNodeEntry.setIndexNames(
    (0, "HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeIndex"),
)
if mibBuilder.loadTexts:
    hpicfTunneledNodeEntry.setStatus("current")
_HpicfTunneledNodeIndex_Type = Unsigned32
_HpicfTunneledNodeIndex_Object = MibTableColumn
hpicfTunneledNodeIndex = _HpicfTunneledNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1, 1),
    _HpicfTunneledNodeIndex_Type()
)
hpicfTunneledNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfTunneledNodeIndex.setStatus("current")
_HpicfTunneledNodeEnable_Type = TruthValue
_HpicfTunneledNodeEnable_Object = MibTableColumn
hpicfTunneledNodeEnable = _HpicfTunneledNodeEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1, 2),
    _HpicfTunneledNodeEnable_Type()
)
hpicfTunneledNodeEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodeEnable.setStatus("current")
_HpicfTunneledNodePrimaryAddrType_Type = InetAddressType
_HpicfTunneledNodePrimaryAddrType_Object = MibTableColumn
hpicfTunneledNodePrimaryAddrType = _HpicfTunneledNodePrimaryAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1, 3),
    _HpicfTunneledNodePrimaryAddrType_Type()
)
hpicfTunneledNodePrimaryAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodePrimaryAddrType.setStatus("current")
_HpicfTunneledNodePrimaryAddr_Type = InetAddress
_HpicfTunneledNodePrimaryAddr_Object = MibTableColumn
hpicfTunneledNodePrimaryAddr = _HpicfTunneledNodePrimaryAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1, 4),
    _HpicfTunneledNodePrimaryAddr_Type()
)
hpicfTunneledNodePrimaryAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodePrimaryAddr.setStatus("current")
_HpicfTunneledNodeBackupAddrType_Type = InetAddressType
_HpicfTunneledNodeBackupAddrType_Object = MibTableColumn
hpicfTunneledNodeBackupAddrType = _HpicfTunneledNodeBackupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1, 5),
    _HpicfTunneledNodeBackupAddrType_Type()
)
hpicfTunneledNodeBackupAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodeBackupAddrType.setStatus("current")
_HpicfTunneledNodeBackupAddr_Type = InetAddress
_HpicfTunneledNodeBackupAddr_Object = MibTableColumn
hpicfTunneledNodeBackupAddr = _HpicfTunneledNodeBackupAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1, 6),
    _HpicfTunneledNodeBackupAddr_Type()
)
hpicfTunneledNodeBackupAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodeBackupAddr.setStatus("current")


class _HpicfTunneledNodeTimeout_Type(Unsigned32):
    """Custom type hpicfTunneledNodeTimeout based on Unsigned32"""
    defaultValue = 8


_HpicfTunneledNodeTimeout_Object = MibTableColumn
hpicfTunneledNodeTimeout = _HpicfTunneledNodeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1, 7),
    _HpicfTunneledNodeTimeout_Type()
)
hpicfTunneledNodeTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodeTimeout.setStatus("current")
_HpicfTunneledNodeRowStatus_Type = RowStatus
_HpicfTunneledNodeRowStatus_Object = MibTableColumn
hpicfTunneledNodeRowStatus = _HpicfTunneledNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1, 8),
    _HpicfTunneledNodeRowStatus_Type()
)
hpicfTunneledNodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodeRowStatus.setStatus("current")


class _HpicfTunneledNodeMode_Type(Integer32):
    """Custom type hpicfTunneledNodeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portbased", 1),
          ("rolebased", 2))
    )


_HpicfTunneledNodeMode_Type.__name__ = "Integer32"
_HpicfTunneledNodeMode_Object = MibTableColumn
hpicfTunneledNodeMode = _HpicfTunneledNodeMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1, 9),
    _HpicfTunneledNodeMode_Type()
)
hpicfTunneledNodeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodeMode.setStatus("current")
_HpicfTunneledNodePortConfigTable_Object = MibTable
hpicfTunneledNodePortConfigTable = _HpicfTunneledNodePortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfTunneledNodePortConfigTable.setStatus("current")
_HpicfTunneledNodePortConfigEntry_Object = MibTableRow
hpicfTunneledNodePortConfigEntry = _HpicfTunneledNodePortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 2, 1)
)
hpicfTunneledNodePortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfTunneledNodePortConfigEntry.setStatus("current")
_HpicfTunneledNodePortRowStatus_Type = RowStatus
_HpicfTunneledNodePortRowStatus_Object = MibTableColumn
hpicfTunneledNodePortRowStatus = _HpicfTunneledNodePortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 2, 1, 1),
    _HpicfTunneledNodePortRowStatus_Type()
)
hpicfTunneledNodePortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodePortRowStatus.setStatus("current")
_HpicfTunneledNodeFallbackLclSw_Type = TruthValue
_HpicfTunneledNodeFallbackLclSw_Object = MibTableColumn
hpicfTunneledNodeFallbackLclSw = _HpicfTunneledNodeFallbackLclSw_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 2, 1, 2),
    _HpicfTunneledNodeFallbackLclSw_Type()
)
hpicfTunneledNodeFallbackLclSw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodeFallbackLclSw.setStatus("current")


class _HpicfTunneledNodeClearStats_Type(TruthValue):
    """Custom type hpicfTunneledNodeClearStats based on TruthValue"""


_HpicfTunneledNodeClearStats_Object = MibScalar
hpicfTunneledNodeClearStats = _HpicfTunneledNodeClearStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 3),
    _HpicfTunneledNodeClearStats_Type()
)
hpicfTunneledNodeClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfTunneledNodeClearStats.setStatus("current")
_HpicfTunneledNodePapiTable_Object = MibTable
hpicfTunneledNodePapiTable = _HpicfTunneledNodePapiTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfTunneledNodePapiTable.setStatus("current")
_HpicfTunneledNodePapiEntry_Object = MibTableRow
hpicfTunneledNodePapiEntry = _HpicfTunneledNodePapiEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 4, 1)
)
hpicfTunneledNodePapiEntry.setIndexNames(
    (0, "HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePapiAuthMode"),
)
if mibBuilder.loadTexts:
    hpicfTunneledNodePapiEntry.setStatus("current")


class _HpicfTunneledNodePapiAuthMode_Type(Integer32):
    """Custom type hpicfTunneledNodePapiAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("none", 1))
    )


_HpicfTunneledNodePapiAuthMode_Type.__name__ = "Integer32"
_HpicfTunneledNodePapiAuthMode_Object = MibTableColumn
hpicfTunneledNodePapiAuthMode = _HpicfTunneledNodePapiAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 4, 1, 1),
    _HpicfTunneledNodePapiAuthMode_Type()
)
hpicfTunneledNodePapiAuthMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfTunneledNodePapiAuthMode.setStatus("current")


class _HpicfTunneledNodePapiKeyValue_Type(OctetString):
    """Custom type hpicfTunneledNodePapiKeyValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpicfTunneledNodePapiKeyValue_Type.__name__ = "OctetString"
_HpicfTunneledNodePapiKeyValue_Object = MibTableColumn
hpicfTunneledNodePapiKeyValue = _HpicfTunneledNodePapiKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 4, 1, 2),
    _HpicfTunneledNodePapiKeyValue_Type()
)
hpicfTunneledNodePapiKeyValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodePapiKeyValue.setStatus("current")


class _HpicfTunneledNodePapiKeyEncr_Type(OctetString):
    """Custom type hpicfTunneledNodePapiKeyEncr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpicfTunneledNodePapiKeyEncr_Type.__name__ = "OctetString"
_HpicfTunneledNodePapiKeyEncr_Object = MibTableColumn
hpicfTunneledNodePapiKeyEncr = _HpicfTunneledNodePapiKeyEncr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 4, 1, 3),
    _HpicfTunneledNodePapiKeyEncr_Type()
)
hpicfTunneledNodePapiKeyEncr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodePapiKeyEncr.setStatus("current")
_HpicfTunneledNodePapiRowStatus_Type = RowStatus
_HpicfTunneledNodePapiRowStatus_Object = MibTableColumn
hpicfTunneledNodePapiRowStatus = _HpicfTunneledNodePapiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 4, 1, 4),
    _HpicfTunneledNodePapiRowStatus_Type()
)
hpicfTunneledNodePapiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodePapiRowStatus.setStatus("current")
_HpicfTunneledNodeConformance_ObjectIdentity = ObjectIdentity
hpicfTunneledNodeConformance = _HpicfTunneledNodeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2)
)
_HpicfTunneledNodeCompliances_ObjectIdentity = ObjectIdentity
hpicfTunneledNodeCompliances = _HpicfTunneledNodeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2, 1)
)
_HpicfTunneledNodeGroups_ObjectIdentity = ObjectIdentity
hpicfTunneledNodeGroups = _HpicfTunneledNodeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2, 2)
)

# Managed Objects groups

hpicfTunneledNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2, 2, 1)
)
hpicfTunneledNodeGroup.setObjects(
      *(("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeEnable"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePrimaryAddrType"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePrimaryAddr"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeBackupAddrType"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeBackupAddr"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeTimeout"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeRowStatus"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeClearStats"))
)
if mibBuilder.loadTexts:
    hpicfTunneledNodeGroup.setStatus("deprecated")

hpicfTunneledNodePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2, 2, 2)
)
hpicfTunneledNodePortGroup.setObjects(
      *(("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePortRowStatus"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeFallbackLclSw"))
)
if mibBuilder.loadTexts:
    hpicfTunneledNodePortGroup.setStatus("current")

hpicfTunneledNodePapiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2, 2, 3)
)
hpicfTunneledNodePapiGroup.setObjects(
      *(("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePapiKeyValue"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePapiKeyEncr"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePapiRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfTunneledNodePapiGroup.setStatus("current")

hpicfTunneledNodeGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2, 2, 4)
)
hpicfTunneledNodeGroup1.setObjects(
      *(("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeEnable"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePrimaryAddrType"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePrimaryAddr"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeBackupAddrType"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeBackupAddr"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeTimeout"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeRowStatus"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeClearStats"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeMode"))
)
if mibBuilder.loadTexts:
    hpicfTunneledNodeGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfTunneledNodeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfTunneledNodeCompliance.setStatus(
        "deprecated"
    )

hpicfTunneledNodeCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfTunneledNodeCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-TUNNELED-NODE-MIB",
    **{"hpicfTunneledNode": hpicfTunneledNode,
       "hpicfTunneledNodeObjects": hpicfTunneledNodeObjects,
       "hpicfTunneledNodeConfig": hpicfTunneledNodeConfig,
       "hpicfTunneledNodeTable": hpicfTunneledNodeTable,
       "hpicfTunneledNodeEntry": hpicfTunneledNodeEntry,
       "hpicfTunneledNodeIndex": hpicfTunneledNodeIndex,
       "hpicfTunneledNodeEnable": hpicfTunneledNodeEnable,
       "hpicfTunneledNodePrimaryAddrType": hpicfTunneledNodePrimaryAddrType,
       "hpicfTunneledNodePrimaryAddr": hpicfTunneledNodePrimaryAddr,
       "hpicfTunneledNodeBackupAddrType": hpicfTunneledNodeBackupAddrType,
       "hpicfTunneledNodeBackupAddr": hpicfTunneledNodeBackupAddr,
       "hpicfTunneledNodeTimeout": hpicfTunneledNodeTimeout,
       "hpicfTunneledNodeRowStatus": hpicfTunneledNodeRowStatus,
       "hpicfTunneledNodeMode": hpicfTunneledNodeMode,
       "hpicfTunneledNodePortConfigTable": hpicfTunneledNodePortConfigTable,
       "hpicfTunneledNodePortConfigEntry": hpicfTunneledNodePortConfigEntry,
       "hpicfTunneledNodePortRowStatus": hpicfTunneledNodePortRowStatus,
       "hpicfTunneledNodeFallbackLclSw": hpicfTunneledNodeFallbackLclSw,
       "hpicfTunneledNodeClearStats": hpicfTunneledNodeClearStats,
       "hpicfTunneledNodePapiTable": hpicfTunneledNodePapiTable,
       "hpicfTunneledNodePapiEntry": hpicfTunneledNodePapiEntry,
       "hpicfTunneledNodePapiAuthMode": hpicfTunneledNodePapiAuthMode,
       "hpicfTunneledNodePapiKeyValue": hpicfTunneledNodePapiKeyValue,
       "hpicfTunneledNodePapiKeyEncr": hpicfTunneledNodePapiKeyEncr,
       "hpicfTunneledNodePapiRowStatus": hpicfTunneledNodePapiRowStatus,
       "hpicfTunneledNodeConformance": hpicfTunneledNodeConformance,
       "hpicfTunneledNodeCompliances": hpicfTunneledNodeCompliances,
       "hpicfTunneledNodeCompliance": hpicfTunneledNodeCompliance,
       "hpicfTunneledNodeCompliance1": hpicfTunneledNodeCompliance1,
       "hpicfTunneledNodeGroups": hpicfTunneledNodeGroups,
       "hpicfTunneledNodeGroup": hpicfTunneledNodeGroup,
       "hpicfTunneledNodePortGroup": hpicfTunneledNodePortGroup,
       "hpicfTunneledNodePapiGroup": hpicfTunneledNodePapiGroup,
       "hpicfTunneledNodeGroup1": hpicfTunneledNodeGroup1}
)
