# SNMP MIB module (HP-ICF-FTRCO) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-FTRCO
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:09 2024
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

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfFtrCo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46)
)
hpicfFtrCo.setRevisions(
        ("2010-06-01 00:00",
         "2009-08-28 00:02")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VidList(OctetString, TextualConvention):
    status = "current"
    displayHint = "512x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )



class IndexName(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



# MIB Managed Objects in the order of their OIDs

_HpicfFtrcoObjects_ObjectIdentity = ObjectIdentity
hpicfFtrcoObjects = _HpicfFtrcoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1)
)
_HpFtrCoEntityTable_Object = MibTable
hpFtrCoEntityTable = _HpFtrCoEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 1)
)
if mibBuilder.loadTexts:
    hpFtrCoEntityTable.setStatus("current")
_HpFtrCoEntityEntry_Object = MibTableRow
hpFtrCoEntityEntry = _HpFtrCoEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 1, 1)
)
hpFtrCoEntityEntry.setIndexNames(
    (0, "HP-ICF-FTRCO", "hpFtrCoEntityName"),
)
if mibBuilder.loadTexts:
    hpFtrCoEntityEntry.setStatus("current")


class _HpFtrCoEntityName_Type(IndexName):
    """Custom type hpFtrCoEntityName based on IndexName"""
    subtypeSpec = IndexName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpFtrCoEntityName_Type.__name__ = "IndexName"
_HpFtrCoEntityName_Object = MibTableColumn
hpFtrCoEntityName = _HpFtrCoEntityName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 1, 1, 1),
    _HpFtrCoEntityName_Type()
)
hpFtrCoEntityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpFtrCoEntityName.setStatus("current")


class _HpFtrCoRestrictNextIndex_Type(Integer32):
    """Custom type hpFtrCoRestrictNextIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpFtrCoRestrictNextIndex_Type.__name__ = "Integer32"
_HpFtrCoRestrictNextIndex_Object = MibTableColumn
hpFtrCoRestrictNextIndex = _HpFtrCoRestrictNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 1, 1, 2),
    _HpFtrCoRestrictNextIndex_Type()
)
hpFtrCoRestrictNextIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpFtrCoRestrictNextIndex.setStatus("current")
_HpFtrCoEntityDate_Type = DateAndTime
_HpFtrCoEntityDate_Object = MibTableColumn
hpFtrCoEntityDate = _HpFtrCoEntityDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 1, 1, 3),
    _HpFtrCoEntityDate_Type()
)
hpFtrCoEntityDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpFtrCoEntityDate.setStatus("current")
_HpFtrCoEntityStatus_Type = RowStatus
_HpFtrCoEntityStatus_Object = MibTableColumn
hpFtrCoEntityStatus = _HpFtrCoEntityStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 1, 1, 4),
    _HpFtrCoEntityStatus_Type()
)
hpFtrCoEntityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpFtrCoEntityStatus.setStatus("current")
_HpFtrCoRestrictionTable_Object = MibTable
hpFtrCoRestrictionTable = _HpFtrCoRestrictionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2)
)
if mibBuilder.loadTexts:
    hpFtrCoRestrictionTable.setStatus("current")
_HpFtrCoRestrictEntry_Object = MibTableRow
hpFtrCoRestrictEntry = _HpFtrCoRestrictEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1)
)
hpFtrCoRestrictEntry.setIndexNames(
    (0, "HP-ICF-FTRCO", "hpFtrCoEntityName"),
    (0, "HP-ICF-FTRCO", "hpFtrCoRestrictId"),
    (0, "HP-ICF-FTRCO", "hpFtrCoRestrictIndex"),
)
if mibBuilder.loadTexts:
    hpFtrCoRestrictEntry.setStatus("current")


class _HpFtrCoRestrictId_Type(Integer32):
    """Custom type hpFtrCoRestrictId based on Integer32"""
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
        *(("aclPermitLogging", 24),
          ("distributedTrunk", 8),
          ("portAcl", 4),
          ("portBpduPvstGuard", 13),
          ("portDhcpSnoop", 11),
          ("portIgmp", 19),
          ("portIpLockdown", 18),
          ("portKeepalive", 23),
          ("portLacp", 7),
          ("portLinkConfig", 21),
          ("portLldp", 22),
          ("portLoopDetection", 12),
          ("portMeshing", 6),
          ("portMirrorDestination", 20),
          ("portQos", 15),
          ("portRateLimit", 16),
          ("portSecurity", 3),
          ("portSflow", 10),
          ("portSourcePortFilter", 5),
          ("portStaticMac", 17),
          ("portVirusThrottling", 9),
          ("qinq", 14),
          ("vidDelete", 2),
          ("vidIpConfig", 1))
    )


_HpFtrCoRestrictId_Type.__name__ = "Integer32"
_HpFtrCoRestrictId_Object = MibTableColumn
hpFtrCoRestrictId = _HpFtrCoRestrictId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 1),
    _HpFtrCoRestrictId_Type()
)
hpFtrCoRestrictId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpFtrCoRestrictId.setStatus("current")


class _HpFtrCoRestrictIndex_Type(Integer32):
    """Custom type hpFtrCoRestrictIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpFtrCoRestrictIndex_Type.__name__ = "Integer32"
_HpFtrCoRestrictIndex_Object = MibTableColumn
hpFtrCoRestrictIndex = _HpFtrCoRestrictIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 2),
    _HpFtrCoRestrictIndex_Type()
)
hpFtrCoRestrictIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpFtrCoRestrictIndex.setStatus("current")


class _HpFtrCoRestrictIdParm_Type(Integer32):
    """Custom type hpFtrCoRestrictIdParm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpFtrCoRestrictIdParm_Type.__name__ = "Integer32"
_HpFtrCoRestrictIdParm_Object = MibTableColumn
hpFtrCoRestrictIdParm = _HpFtrCoRestrictIdParm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 3),
    _HpFtrCoRestrictIdParm_Type()
)
hpFtrCoRestrictIdParm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpFtrCoRestrictIdParm.setStatus("current")
_HpFtrCoRestrictStatus_Type = RowStatus
_HpFtrCoRestrictStatus_Object = MibTableColumn
hpFtrCoRestrictStatus = _HpFtrCoRestrictStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 4),
    _HpFtrCoRestrictStatus_Type()
)
hpFtrCoRestrictStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpFtrCoRestrictStatus.setStatus("current")


class _HpFtrCoRestrictMessage_Type(SnmpAdminString):
    """Custom type hpFtrCoRestrictMessage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpFtrCoRestrictMessage_Type.__name__ = "SnmpAdminString"
_HpFtrCoRestrictMessage_Object = MibTableColumn
hpFtrCoRestrictMessage = _HpFtrCoRestrictMessage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 5),
    _HpFtrCoRestrictMessage_Type()
)
hpFtrCoRestrictMessage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpFtrCoRestrictMessage.setStatus("current")
_HpFtrCoRestrictPorts_Type = PortList
_HpFtrCoRestrictPorts_Object = MibTableColumn
hpFtrCoRestrictPorts = _HpFtrCoRestrictPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 6),
    _HpFtrCoRestrictPorts_Type()
)
hpFtrCoRestrictPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpFtrCoRestrictPorts.setStatus("current")
_HpFtrCoRestrictVlans_Type = VidList
_HpFtrCoRestrictVlans_Object = MibTableColumn
hpFtrCoRestrictVlans = _HpFtrCoRestrictVlans_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 7),
    _HpFtrCoRestrictVlans_Type()
)
hpFtrCoRestrictVlans.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpFtrCoRestrictVlans.setStatus("current")


class _HpFtrCoExpireSlot_Type(Integer32):
    """Custom type hpFtrCoExpireSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpFtrCoExpireSlot_Type.__name__ = "Integer32"
_HpFtrCoExpireSlot_Object = MibTableColumn
hpFtrCoExpireSlot = _HpFtrCoExpireSlot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 8),
    _HpFtrCoExpireSlot_Type()
)
hpFtrCoExpireSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpFtrCoExpireSlot.setStatus("current")


class _HpFtrCoExpireApplication_Type(IndexName):
    """Custom type hpFtrCoExpireApplication based on IndexName"""
    subtypeSpec = IndexName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HpFtrCoExpireApplication_Type.__name__ = "IndexName"
_HpFtrCoExpireApplication_Object = MibTableColumn
hpFtrCoExpireApplication = _HpFtrCoExpireApplication_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 9),
    _HpFtrCoExpireApplication_Type()
)
hpFtrCoExpireApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpFtrCoExpireApplication.setStatus("current")


class _HpFtrCoExpireVidDelete_Type(Integer32):
    """Custom type hpFtrCoExpireVidDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_HpFtrCoExpireVidDelete_Type.__name__ = "Integer32"
_HpFtrCoExpireVidDelete_Object = MibTableColumn
hpFtrCoExpireVidDelete = _HpFtrCoExpireVidDelete_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 10),
    _HpFtrCoExpireVidDelete_Type()
)
hpFtrCoExpireVidDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpFtrCoExpireVidDelete.setStatus("current")
_HpFtrCoExpireDate_Type = DateAndTime
_HpFtrCoExpireDate_Object = MibTableColumn
hpFtrCoExpireDate = _HpFtrCoExpireDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 11),
    _HpFtrCoExpireDate_Type()
)
hpFtrCoExpireDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpFtrCoExpireDate.setStatus("current")


class _HpFtrCoExpireBoot_Type(TruthValue):
    """Custom type hpFtrCoExpireBoot based on TruthValue"""


_HpFtrCoExpireBoot_Object = MibTableColumn
hpFtrCoExpireBoot = _HpFtrCoExpireBoot_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 1, 2, 1, 12),
    _HpFtrCoExpireBoot_Type()
)
hpFtrCoExpireBoot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpFtrCoExpireBoot.setStatus("current")
_HpicfFtrCoConformance_ObjectIdentity = ObjectIdentity
hpicfFtrCoConformance = _HpicfFtrCoConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 2)
)
_HpicfFtrCoCompliances_ObjectIdentity = ObjectIdentity
hpicfFtrCoCompliances = _HpicfFtrCoCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 2, 1)
)
_HpicfFtrCoGroups_ObjectIdentity = ObjectIdentity
hpicfFtrCoGroups = _HpicfFtrCoGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 2, 2)
)

# Managed Objects groups

hpicfFtrCoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 2, 2, 1)
)
hpicfFtrCoGroup.setObjects(
      *(("HP-ICF-FTRCO", "hpFtrCoRestrictNextIndex"),
        ("HP-ICF-FTRCO", "hpFtrCoEntityDate"),
        ("HP-ICF-FTRCO", "hpFtrCoEntityStatus"),
        ("HP-ICF-FTRCO", "hpFtrCoRestrictIdParm"),
        ("HP-ICF-FTRCO", "hpFtrCoRestrictStatus"),
        ("HP-ICF-FTRCO", "hpFtrCoRestrictMessage"),
        ("HP-ICF-FTRCO", "hpFtrCoRestrictPorts"),
        ("HP-ICF-FTRCO", "hpFtrCoRestrictVlans"),
        ("HP-ICF-FTRCO", "hpFtrCoExpireSlot"),
        ("HP-ICF-FTRCO", "hpFtrCoExpireApplication"),
        ("HP-ICF-FTRCO", "hpFtrCoExpireVidDelete"),
        ("HP-ICF-FTRCO", "hpFtrCoExpireDate"),
        ("HP-ICF-FTRCO", "hpFtrCoExpireBoot"))
)
if mibBuilder.loadTexts:
    hpicfFtrCoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfFtrCoCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 46, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfFtrCoCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-FTRCO",
    **{"VidList": VidList,
       "IndexName": IndexName,
       "hpicfFtrCo": hpicfFtrCo,
       "hpicfFtrcoObjects": hpicfFtrcoObjects,
       "hpFtrCoEntityTable": hpFtrCoEntityTable,
       "hpFtrCoEntityEntry": hpFtrCoEntityEntry,
       "hpFtrCoEntityName": hpFtrCoEntityName,
       "hpFtrCoRestrictNextIndex": hpFtrCoRestrictNextIndex,
       "hpFtrCoEntityDate": hpFtrCoEntityDate,
       "hpFtrCoEntityStatus": hpFtrCoEntityStatus,
       "hpFtrCoRestrictionTable": hpFtrCoRestrictionTable,
       "hpFtrCoRestrictEntry": hpFtrCoRestrictEntry,
       "hpFtrCoRestrictId": hpFtrCoRestrictId,
       "hpFtrCoRestrictIndex": hpFtrCoRestrictIndex,
       "hpFtrCoRestrictIdParm": hpFtrCoRestrictIdParm,
       "hpFtrCoRestrictStatus": hpFtrCoRestrictStatus,
       "hpFtrCoRestrictMessage": hpFtrCoRestrictMessage,
       "hpFtrCoRestrictPorts": hpFtrCoRestrictPorts,
       "hpFtrCoRestrictVlans": hpFtrCoRestrictVlans,
       "hpFtrCoExpireSlot": hpFtrCoExpireSlot,
       "hpFtrCoExpireApplication": hpFtrCoExpireApplication,
       "hpFtrCoExpireVidDelete": hpFtrCoExpireVidDelete,
       "hpFtrCoExpireDate": hpFtrCoExpireDate,
       "hpFtrCoExpireBoot": hpFtrCoExpireBoot,
       "hpicfFtrCoConformance": hpicfFtrCoConformance,
       "hpicfFtrCoCompliances": hpicfFtrCoCompliances,
       "hpicfFtrCoCompliance": hpicfFtrCoCompliance,
       "hpicfFtrCoGroups": hpicfFtrCoGroups,
       "hpicfFtrCoGroup": hpicfFtrCoGroup}
)
